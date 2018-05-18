import os

class Config:
	SECRET_KEY = "mysososossecretkey"
	SQLALCHEMY_TRACK_MODIFICATIONS=True
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/blog2"
	UPLOADED_PHOTOS_DEST = "app/static/photos"

	# email configurations
	MAIL_SERVER = 'smtp.google.cpm'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get("MAIL.PASSWORD")


	# simple mde configurations
	
	SIMPLEMDE_JS_IIFE = True
	SIMPLEMDE_USE_CDN = True
	
class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True

class TestConfig(Config):
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/blog2_test"


config_options = {
	'development':DevConfig,
	'production':ProdConfig,
	'test': TestConfig,
	'default':ProdConfig
}