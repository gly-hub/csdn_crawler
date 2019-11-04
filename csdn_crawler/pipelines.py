# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from csdn_crawler.download.downloader import Downloader
from csdn_crawler.download.building_html import create_html

class CsdnCrawlerPipeline(object):
    def process_item(self, article, spider):
        # html = create_html(article['content'][0], article['title'][0])
        # filepath = 'D:\\webCrawler_bishe\\test\\'+ article['Atype'] +'\\'
        # downloader = Downloader(filepath)
        # path = downloader.create_Folder(article['title'][0]) + '\\'
        # downloader.download_Html(html, article['title'][0], path)
        return article

from .sqldb.model import ArticleContent,ArticleType,ArticleHtml
from .sqldb.sqloperat import SqlOperat
import re

class MysqlPipeline(object):
    def process_item(self, article, spider):
        try:
            session = SqlOperat().getSession()
            articletype = session.query(ArticleType).filter_by(Tname = article['Atype']).first()
            print('数据库操作')
            title = article['title'][0]
            content = re.sub(r'<[\s\S]*?>','',article['content'][0])
            articlecontent = session.query(ArticleContent).filter_by(Atitle = title).first()
            if articlecontent:
                articlecontent.Tid = articletype.Tid
                articlecontent.Acontent = content
                session.add(articlecontent)
                session.commit()
            else:
                articlecontent = ArticleContent()
                articlecontent.Tid = articletype.Tid
                articlecontent.Atitle = title
                articlecontent.Acontent = content
                session.add(articlecontent)
                session.commit()
            return article
        except Exception as e:
            print(str(e))

class HtmlSqlPipeline(object):
    def process_item(self, article, spider):
        try:
            print('html操作')
            session = SqlOperat().getSession()
            title = article['title'][0]
            html = create_html(article['content'][0],title)
            articlecontent = session.query(ArticleContent).filter_by(Atitle = title).first()
            if articlecontent:
                print('cunzai')
                articlehtml = session.query(ArticleHtml).filter_by(Aid = articlecontent.Aid).first()
                if articlehtml:
                    articlehtml.Ahtml = html
                    session.add(articlehtml)
                    session.commit()
                else:
                    articlehtml = ArticleHtml()
                    articlehtml.Aid = articlecontent.Aid
                    articlehtml.Ahtml = html
                    session.add(articlehtml)
                    session.commit()
            else:
                print('bucunzai ')
        except Exception as e:
            print(str(e))
        
