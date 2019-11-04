from model import ArticleContent
from sqloperat import SqlOperat

if __name__ == "__main__":
    articlecontent = ArticleContent()
    session = SqlOperat().getSession()

    # articlecontent.Acontent = '123456'
    # articlecontent.Atitle ='123'
    # session.add(articlecontent)
    # session.commit()

    a = session.query(ArticleContent).filter_by(Atitle = '123').first()
    if a:
        print(a.Aid)
    else:
        print('em')
