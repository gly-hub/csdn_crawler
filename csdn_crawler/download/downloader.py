"""
    下载器
    @developer: gao_liangyong
    @date: 2019/09/17
"""
import os

class Downloader:
    download_path = ''

    def __init__(self, download_path):
        self.download_path = download_path

    def download_File(self, filename, url, path):
        """
        下载文件
        """
        try:
            import requests
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
            response = requests.get(url, headers = header, timeout=5)
            if response.status_code == requests.codes.ok:
                text = response.content
                postfix = '.pdf'
                if url[-4:] == '.doc':
                    postfix = '.doc'
                elif url[-4:] == '.xls':
                    postfix = '.xls'
                elif url[-5:] == '.docx':
                    postfix = '.docx'
                elif url[-4:] == '.wps':
                    postfix = '.wps'
                else:
                    postfix = '.pdf'
                with open(path + filename,'wb') as file:
                    file.write(text)
                print(filename + "下载成功！")
            else:
                print(filename + "下载失败！")
        except:
            pass

    def download_Html(self, html, filename, path):
        """
        用于下载html
        """
        with open('%s%s%s' % (path,filename,'.html'),'w', encoding='utf-8') as file:
            file.write(html)
        print('html文件写入成功>>>>>>>>%s%s%s' % (path,filename,'.html'))

    def detection_Folder(self, path):
        """
        用于检测指定下载路径下的文件夹是否存在
        """
        try:
            isExists=os.path.exists(path)
            return isExists
        except Exception as e:
            print('detection_Folder：' + str(e))

    def delete_Folder(self, path):
        """
        用于删除文件夹
        """
        try:
            import shutil
            shutil.rmtree(path)
        except Exception as e:
            print(e)

    def create_Folder(self, filename):
        """
        用于创建文件夹
        """
        try:
            path = self.download_path + str(filename)
            if self.detection_Folder(path) == True:
                self.delete_Folder(path)
                os.makedirs(path)
                print("创建文件夹成功" + path)
            else:
                os.makedirs(path)
                print("创建文件夹成功" + path)
            return path
        except Exception as e:
            print(e)