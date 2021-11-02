from behave import *

use_step_matcher('re')

@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    context.browser.find_element_by_id('blog-link')
    link.click()