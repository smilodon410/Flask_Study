from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcd\x02\x08\xda\x04r\x16\x91Q\xb8\xa7\x89\x15^\xa3\xda'
