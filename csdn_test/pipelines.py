# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .sqldb.model import ArticleContent,ArticleType,ArticleHtml,ArticleWord
from .sqldb.sqloperat import SqlOperat
import re
from .sqldb.jieba_cut import *
from sqlalchemy import and_
from csdn_test.download.building_html import create_html

class CsdnTestPipeline(object):
    def process_item(self, article, spider):
        try:
            session = SqlOperat().getSession()
            articletype = session.query(ArticleType).filter_by(Tname=article['Atype']).first()
            print('数据库操作')
            title = article['title'][0]
            content = re.sub(r'<div class="article-copyright">[\s\S]*?<div .*?id="content_views".*?>', '',
                             article['content'][0])
            content = re.sub(r'<[\s\S]*?>', '', content)
            articlecontent = session.query(ArticleContent).filter_by(Atitle=title).first()
            if articlecontent:
                articlecontent.Tid = articletype.Tid
                articlecontent.Aabstract = ''.join(get_summary(content))
                session.add(articlecontent)
                session.commit()
            else:
                articlecontent = ArticleContent()
                articlecontent.Tid = articletype.Tid
                articlecontent.Aabstract = ''.join(get_summary(content))
                articlecontent.Atitle = title
                session.add(articlecontent)
                session.commit()

            articlecontent = session.query(ArticleContent).filter_by(Atitle=title).first()

            titleseg_list = jieba_cut_forsearch(title).split(',')
            for titleseg in titleseg_list:
                filters = and_(
                    ArticleWord.Aid == articlecontent.Aid,
                    ArticleWord.Wtype == 'title',
                    ArticleWord.Wword == titleseg
                )
                articleword = session.query(ArticleWord).filter(filters).first()
                if not articleword:
                    articleword = ArticleWord()
                    articleword.Aid = articlecontent.Aid
                    articleword.Wtype = 'title'
                    articleword.Wword = titleseg
                    session.add(articleword)
                    session.commit()

            seg_list = jieba_cut_forsearch(content).split(',')
            for seg in seg_list:
                filters = and_(
                    ArticleWord.Aid == articlecontent.Aid,
                    ArticleWord.Wtype == 'content',
                    ArticleWord.Wword == seg
                )
                articleword = session.query(ArticleWord).filter(filters).first()
                if not articleword:
                    articleword = ArticleWord()
                    articleword.Aid = articlecontent.Aid
                    articleword.Wtype = 'content'
                    articleword.Wword = seg
                    session.add(articleword)
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
            html = create_html(article['content'][0], title)
            articlecontent = session.query(ArticleContent).filter_by(Atitle=title).first()
            if articlecontent:
                print('cunzai')
                articlehtml = session.query(ArticleHtml).filter_by(Aid=articlecontent.Aid).first()
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

            return article
        except Exception as e:
            print(str(e))
