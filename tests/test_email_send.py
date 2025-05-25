import pytest
import time
from pytest_bdd import scenarios, given, when, then
from pages.email_page import EmailPage
from dotenv import load_dotenv

load_dotenv()

scenarios("../features/email_send.feature")

@pytest.fixture
def email_page(page):
    return EmailPage(page)

@given("the user is logged into the email inbox")
def user_logs_in(email_page):
    email_page.navigate()
    email_page.login()

@when("the user composes a new message")
def compose_message(email_page):
    email_page.write_new_message()

@when("adds a contact to the message")
def add_contact(email_page):
    email_page.add_contact()

@when("attaches a file to the email")
def attach_file(email_page):
    email_page.attach_file()

@when('fills in the subject "SergejTest" and body "test Sergej"')
def fill_subject_and_body(email_page):
    email_page.fill_subject_and_body("SergejTest", "test Sergej")

@then("the email was sent and logout")
def send_email_and_logout(email_page):
    email_page.send_email()
    time.sleep(5)  # wait 5 seconds before logout
    email_page.logout()
