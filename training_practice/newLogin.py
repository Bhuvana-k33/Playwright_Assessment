def test_login(page):
	page.goto("https://www.google.com")
	print(page.title())
	print('Hello')