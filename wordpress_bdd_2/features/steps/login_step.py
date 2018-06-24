from behave import * 
import time
from selenium.webdriver.common.action_chains import ActionChains
from steps.pages.login_page import LoginPage


@given('go to login page')
def step_impl(context):
	context.login_page = LoginPage(context.dr)
	context.login_page.url = 'http://localhost/wp-login.php'
	context.login_page.navigate()

@when('login with {username} {password}')
def step_impl(context, username, password):
	context.dashboard_page = context.login_page.login(username, password)


@then('redirect to dashboard page')
def step_impl(context):
	assert 'wp-admin' in context.dr.current_url


@then('display hello {username}')
def step_impl(context, username):
	greeking_link = context.dr.find_element_by_css_selector('#wp-admin-bar-my-account .ab-item')
	assert username in greeking_link.text


@when(u'let us login with incorrect {username} and incorrect {password}')
def step_impl(context, username, password):
	if username == 'empty': username = ''
	if password == 'empty': password = ''
	context.login_page.login_and_clear_username(username, password)

@then('should display error {message}')
def step_impl(context, message):
	assert context.login_page.error_message == message
