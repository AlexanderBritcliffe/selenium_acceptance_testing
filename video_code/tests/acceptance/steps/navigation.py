
from tests.acceptance.page_model.home_page import HomePage


use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
   context.browser = webdriver.Chrome()
   page = HomePage(context.driver)
   context.browser.get(page.url)

@given('I am on the blogpage')
def step_impl(context):
   context.browser = webdriver.Chrome()
   page = BlogPage(context.driver)
   context.browser.get(page.url)

@then('I am on the blogpage')
def step_impl(context):
   expected_url = BlogPage(context.driver).url
   assert context.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
   expected_url = HomePage(context.driver).url
   assert context.current_url == expected_url

