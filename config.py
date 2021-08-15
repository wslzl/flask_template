class Config:
    DEBUG = True
    PORT = 8080
    SECRET_KEY = '123'
    # DATABASE
    DB_USERNAME = 'liang'
    DB_PASSWORD = '1994'
    DB_HOST = '192.168.3.2'
    DB_PORT = '3306'
    DB_NAME = 'python'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?chart=utf8mb4'.format(
        username=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NAME,
    )
    # JOBS
    SCHEDULER_API_ENABLED = True


class Development(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class Production(Config):
    pass


config = {
    'development': Development,
    'production': Production
}