from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title.is_displayed()

@step('The title tag has content  "(.*)"')
def step_impl(context):
    assert title_tag.text == content

