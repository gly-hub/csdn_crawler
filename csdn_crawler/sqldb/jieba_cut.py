import pandas as pd
import jieba
from textrank4zh import TextRank4Keyword, TextRank4Sentence


def stripword(seg):
    try:
        wordlist = []
        stop = open('csdn_crawler\sqldb\stopword.txt', 'r+', encoding='utf-8')
        stopword = stop.read().split("\n")
        stop.close()
        for key in seg.split(','):
            if not (key.strip() in stopword) and (len(key.strip()) > 1) and not(key.strip() in wordlist) :
                wordlist.append(key)
        return ','.join(wordlist)
    except Exception as e:
        print(str(e))

def jieba_cut(text):
    try:
        seg_list = jieba.cut(text,cut_all = False)
        res = stripword(','.join(seg_list))
        if res != text:
            return res
        else:
            return ''
    except Exception as e:
        print(str(e))

def jieba_cut_forsearch(text):
    try:
        seg_list = jieba.cut_for_search(text)
        res = stripword(','.join(seg_list))
        if res != text:
            return res
        else:
            return ''
    except Exception as e:
        print(str(e))

def get_summary(text, num=3):
    """提取摘要"""
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    return [item.sentence for item in tr4s.get_key_sentences(num)]


if __name__ == "__main__":
    text = '''

                
                                                
                
                
                    
            
                版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。            
               
                    本文链接：https://blog.csdn.net/ytusdc/article/details/78878995
                
            
                    
                                                    
                                        
                
                                            


package imge;import java.awt.Color;import java.awt.Font;import java.awt.Graphics2D;import java.awt.Image;import java.awt.image.BufferedImage;import java.io.FileOutputStream;import javax.swing.ImageIcon;import com.sun.image.codec.jpeg.JPEGCodec;import com.sun.image.codec.jpeg.JPEGEncodeParam;import com.sun.image.codec.jpeg.JPEGImageEncoder; public class ImageEdit {		public static void main(String[] a) {  		ImageEdit.createStringMark("D://A.jpg", "测试文字","d://B.jpg");		}        /**	     * @param filePath 源图片路径	     * @param markContent 图片中添加内容	     * @param outPath  输出图片路径	     * 字体颜色等在函数内部实现的       */		//给jpg添加文字		public static boolean createStringMark(String filePath,String markContent,String outPath) 		{ 		ImageIcon imgIcon=new ImageIcon(filePath); 		Image theImg =imgIcon.getImage(); 		int width=theImg.getWidth(null)==-1?200:theImg.getWidth(null); 		int height= theImg.getHeight(null)==-1?200:theImg.getHeight(null); 		System.out.println(width);		System.out.println(height);		System.out.println(theImg);		BufferedImage bimage = new BufferedImage(width,height, BufferedImage.TYPE_INT_RGB); 		Graphics2D g=bimage.createGraphics(); 				Color mycolor = Color.red;         g.setColor(mycolor); 		g.setBackground(Color.red); 		g.drawImage(theImg, 0, 0, null ); 		g.setFont(new Font("宋体",Font.PLAIN,50)); //字体、字型、字号 		g.drawString(markContent,width/2,height/2); //画文字 		g.dispose(); 		try 		{ 		FileOutputStream out=new FileOutputStream(outPath); //先用一个特定的输出文件名 		JPEGImageEncoder encoder =JPEGCodec.createJPEGEncoder(out); 		JPEGEncodeParam param = encoder.getDefaultJPEGEncodeParam(bimage); 		param.setQuality(100, true);  //		encoder.encode(bimage, param); 		out.close(); 		} 		catch(Exception e) 		{ return false; } 		return true; 		}  }


  下图是测试结果
 


                                    
                    
    
    '''
    seg_list = jieba.cut_for_search(text)
    res = stripword(','.join(seg_list))
    print(res)
    # data = pd.read_excel('E:\\python\\test\\web_crawler\\jieba分词\\h1.xlsx', sheet_name = 'Sheet1')
    # values = data.iloc[:,0:1].values
    # values = values.tolist()
    # for value in values:
    #     value.append(jieba_cut(value[0]))
    #     value.append(jieba_cut_forsearch(value[0]))
    # print(values)
    # data1 = pd.DataFrame(values)
    # data1.to_excel('data2.xlsx', encoding="utf_8_sig", index = False)


