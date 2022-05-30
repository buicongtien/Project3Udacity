import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="postgresql-server-project3.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="tienbc@postgresql-server-project3" #TODO: Update value
    POSTGRES_PW="abcde12345-"   #TODO: Update value
    POSTGRES_DB="patient"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://servicebus-namespace-project3.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=BezBM5uLLS7caQvhzxn9kk8TGcOEPiVpkvTPEy5SatA=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='queue-project3'
    ADMIN_EMAIL_ADDRESS: 'buicongtien12@gmai.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False