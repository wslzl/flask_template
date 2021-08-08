class Config:
    DEBUG = True
    port = 8080
    # SQL
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://liang:1994@192.168.3.2:3306/python'


class Development(Config):
    SQLALCHEMY_ECHO = True


class Production(Config):
    pass


config = {
    'development': Development,
    'production': Production
}