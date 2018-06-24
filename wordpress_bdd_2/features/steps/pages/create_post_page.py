from .base_page import BasePage 
from .dashboard_page import DashBoardPage
from time import sleep


class CreatePostPage(BasePage):

	@property
	def post_title(self):
		return self.by_name('post_title')

	@property
	def publish_btn(self):
		return self.by_id('publish')

	@property
	def permalink(self):
		return self.by_id('sample-permalink')

	def post_content(self, content):
		js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'"%(content)
		self.js(js) 

	def create_post(self, title, content):
		self.post_title.send_keys(title)
		self.post_content(content)
		sleep(1)
		self.publish_btn.click()

	def create_post_and_return_its_id(self, title, content):
		self.create_post(title, content)
		link_test = self.permalink.text
		tokens = link_test.split('=')
		return tokens[-1]