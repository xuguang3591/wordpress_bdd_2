Feature: Create Post 

	@create_post
	Scenario: Success Create Post
		Given go to login page
		When login with guang safe3600
		When create a post with title and content
		Then the new created post should be existed
