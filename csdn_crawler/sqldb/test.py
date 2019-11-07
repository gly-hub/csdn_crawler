from model import ArticleContent,ArticleType
from sqloperat import SqlOperat

if __name__ == "__main__":
    # articlecontent = ArticleContent()
    articletype = ArticleType()
    session = SqlOperat().getSession()

    # articlecontent.Acontent = '123456'
    # articlecontent.Atitle ='123'
    # session.add(articlecontent)
    # session.commit()

    # a = session.query(ArticleContent).filter_by(Atitle = '123').first()
    # if a:
    #     print(a.Aid)
    # else:
    #     print('em')

    articletype.Tname = 'java'
    articletype.Tdescribe = 'Java是一门面向对象编程语言，不仅吸收了C++语言的各种优点，还摒弃了C++里难以理解的多继承、指针等概念，因此Java语言具有功能强大和简单易用两个特征。Java语言作为静态面向对象编程语言的代表，极好地实现了面向对象理论，允许程序员以优雅的思维方式进行复杂的编程。'
    session.add(articletype)
    session.commit()

