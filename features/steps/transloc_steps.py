from behave import step
from nose.tools import assert_in,assert_not_in

@step('I go to transloc')
def go_to_transloc(context):
    context.driver.get(context.env['url'])
    current_url = context.driver.current_url
    assert_in('login.stage.transloc.com', current_url)

@step('I enter a valid user and password')
def enter_valid_login(context):
    context.driver.find_element_by_id('username').send_keys(context.env['user'])
    context.driver.find_element_by_id('password').send_keys(context.env['password'])

@step('I click login')
def click_login_button(context):
    context.driver.find_element_by_css('input[value="Log in"]').click()

@step('I see I am logged in')
def confirm_login(context):
