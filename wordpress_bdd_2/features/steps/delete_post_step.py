from behave import * 
import time
from selenium.webdriver.common.action_chains import ActionChains
from steps.pages.create_post_page import CreatePostPage 
from steps.pages.list_page import PostListPage

@when('we create a post and return its id')
def step_impl(context):
	create_page = CreatePostPage(context.dr)
	create_page.url = 'http://localhost/wp-admin/post-new.php' 
	create_page.navigate()

	title = 'Post title %s' % (time.time())
	content = 'Post content %s' %(time.time())
	context.post_id = create_page.create_post_and_return_its_id(title,content)
	context.post_title = title


@when('delete the new created post')
def step_impl(context):
    list_page = PostListPage(context.dr)
    list_page.url = 'http://localhost/wp-admin/edit.php'
    list_page.navigate()

    list_page.delete_post_by_id(context.post_id)
    context.list_page = list_page


@then('the new created post should not exist')
def step_impl(context):
    time.sleep(3)    
    assert context.list_page.first_post.text != context.post_title
