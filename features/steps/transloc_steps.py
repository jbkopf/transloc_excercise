from behave import step
from nose.tools import assert_in,assert_equal,assert_true,assert_false
from selenium.common.exceptions import NoSuchElementException

@step('I go to transloc')
def go_to_transloc(context):
    context.driver.get(context.env['url'])
    current_url = context.driver.current_url
    assert_in('login.stage.transloc.com', current_url)

@step('I enter an? (valid|invalid) user and password')
def enter_valid_login(context, valid):
    if valid == 'valid':
        user = context.env['user']
        password = context.env['password']
    else:
        user = 'bad_user'
        password = 'bad_password'


    context.driver.find_element_by_id('username').send_keys(user)
    context.driver.find_element_by_id('password').send_keys(password)

@step('I click login')
def click_login_button(context):
    context.driver.find_element_by_css_selector('input[value="Log in"]').click()

@step('I see I am logged in')
def confirm_login(context):
    logged_in = context.driver.find_element_by_link_text('logout').is_displayed()
    assert_true(logged_in, 'Log out link not found, user not logged in')

@step('I see I am not logged in')
def confirm_not_login(context):
    try:
        logged_in = context.driver.find_element_by_link_text('logout').is_displayed()
    except NoSuchElementException:
        assert_true(True)
    else:
        assert_false(logged_in, 'Log out link found, user is logged in')

@step('I see invalid credentials error')
def invalid_credentials_error(context):
    error = context.driver.find_element_by_class_name('alert-warning').text
    assert_equal(error, 'Incorrect username/email or password.', 'Incorrect error text found')
