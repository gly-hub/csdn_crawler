# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text

Base = declarative_base()



class ArticleContent(Base):
    __tablename__ = 'article_content'

    Aid = Column(Integer, primary_key = True, autoincrement=True)
    Atitle = Column(String, nullable = False)
    Aabstract = Column(Text, nullable = True)
    Tid = Column(Integer)

class ArticleType(Base):
    __tablename__ = 'article_type'

    Tid = Column(Integer, primary_key = True, autoincrement=True)
    Tname = Column(String, nullable = False)
    Tdescribe = Column(String, nullable = False)

class ArticleHtml(Base):
    __tablename__ = 'article_html'

    Hid = Column(Integer, primary_key = True, autoincrement=True)
    Aid = Column(Integer)
    Ahtml = Column(Text, nullable = False)

class ArticleWord(Base):
    __tablename__ = "article_word"

    Wid = Column(Integer, primary_key = True, autoincrement=True)
    Aid = Column(Integer)
    Wtype = Column(String, nullable = False)
    Wword = Column(String, nullable = False)