from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class SqlOperat:
    __session_obj = None


    def __init__(self):
        __url="mysql+pymysql://root:gaoliangyong@203.195.239.94:3306/graduationprojectdb?charset=utf8"
        __engine=create_engine(__url,echo=False,encoding="utf-8")
        __SessionClass = scoped_session(sessionmaker(bind=__engine))
        self.__session_obj = __SessionClass()

    def getSession(self):
        return self.__session_obj

