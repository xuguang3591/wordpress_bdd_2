	Feature: Delete Post 

	@delete_post
	Scenario: Success Delete Post
		Given go to login page
		When login with guang safe3600
		when we create a post and return its id
		When delete the new created post
		Then the new created post should not exist