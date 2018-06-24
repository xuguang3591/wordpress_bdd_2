from selenium import webdriver


def before_feature(context, feature):
	context.dr = webdriver.Firefox()

def after_feature(context, feature):
	context.dr.close()
