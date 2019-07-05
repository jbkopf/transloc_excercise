from behave import step
from nose.tools import assert_in,assert_equal,assert_not_in
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string

@step('I click the New Feed button')
def click_new_feed(context):
    context.driver.find_element_by_css_selector('a[data-id="new-button"]').click()

@step('I fill in all required fields')
def fill_required_new_feed_fields(context):
    salt = random_generator()
    context.driver.find_element_by_name('name').send_keys('new' + salt)
    context.driver.find_element_by_name('publisher_name').send_keys('new_publisher' + salt)
    context.driver.find_element_by_name('publisher_url').send_keys('new_url' + salt)
    context.driver.find_element_by_name('language').send_keys('new_language' + salt)
    context.execute_steps("""
        Given I click the agency-info-tab
    """)
    context.driver.find_element_by_name('gtfs_agency_url').send_keys('new_agency_url' + salt)
    assert_not_in('Field may not be empty.', context.driver.page_source, 'unexpected error found')

@step('I clear the (.*?) field')
def clear_field_by_name(context, name):
    while context.driver.find_element_by_name(name).get_attribute('value') != '':
        context.driver.find_element_by_name(name).send_keys(Keys.BACK_SPACE)

    assert_equal(context.driver.find_element_by_name(name).get_attribute('value'), '',
                 'Field {} not cleared'.format(name))

@step('I click (save|cancel)')
def click_save(context, button):
    context.driver.find_element_by_css_selector('button[data-id="{}-button"]'.format(button)).click()
    sleep(1)

@step('I see an error that a required field is missing')
def required_field_missing_error(context):
    assert_in('Field may not be empty.',context.driver.page_source,  'expected error not present')

@step('I click the (feed-info-tab|agency-info-tab)')
def click_agency_info_tab(context, tab):
    context.driver.find_element_by_css_selector('button[data-id="{}"]'.format(tab)).click()

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))