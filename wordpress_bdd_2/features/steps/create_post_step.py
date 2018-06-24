from behave import * 
import time
from steps.pages.create_post_page import CreatePostPage
from steps.pages.list_page import PostListPage


@when('create a post with title and content')
def step_impl(context):
	create_page = CreatePostPage(context.dr)
	create_page.url = 'http://localhost/wp-admin/post-new.php' 
	create_page.navigate()

	title = 'Post title %s' % (time.time())
	content = 'Post content %s' %(time.time())
	create_page.create_post(title, content)
	context.title = title


@then('the new created post should be existed')
def step_impl(context):
	list_page = PostListPage(context.dr)
	list_page.url = 'http://localhost/wp-admin/edit.php' 
	list_page.navigate()

	assert list_page.first_post.text == context.title
