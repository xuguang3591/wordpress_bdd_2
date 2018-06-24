class BasePage(object):
	url = None
	driver = None
	domain = None

	def __init__(self, driver):
		
		self.driver = driver
		self.domain = 'http://localhost/'

	def title(self):
		return self.driver.get_title()

	def url(self):
		return self.url
	
	def fill_form_by_css(self, from_css, value):
		elem = self.driver.find_element_by_css_selector(form_css)
		elem.send_keys(value)
	
	def find_form_by_id(self, from_element_id, value):
		return self.find_form_by_css('#%s' % from_element_id, value)

	def navigate(self):
		self.driver.get(self.url)

	def by_id(self, the_id):
		return self.driver.find_element_by_id(the_id)

	def by_name(self, the_name):
		return self.driver.find_element_by_name(the_name)

	def by_css(self, the_css):
		return self.driver.find_element_by_css_selector(the_css)
	
	def js(self, js_text):
		return self.driver.execute_script(js_text)
		