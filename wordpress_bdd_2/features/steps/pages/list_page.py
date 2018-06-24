from .base_page import BasePage 
from .dashboard_page import DashBoardPage
from selenium.webdriver.common.action_chains import ActionChains


class PostListPage(BasePage):

	@property
	def first_post(self):
		return self.by_css('.row-title')

	def delete_post_by_id(self, post_id):
		row_id = 'post-' + post_id
		the_row = self.by_id(row_id)
		
		ActionChains(self.driver).move_to_element(the_row).perform()
		the_row.find_element_by_css_selector('.submitdelete').click()