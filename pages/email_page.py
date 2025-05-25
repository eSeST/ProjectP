# pages/email_page.py
import os
import time

class EmailPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(os.getenv("EMAIL_URL"))

    def login(self):
        self.page.fill('input[name="_user"]', os.getenv("EMAIL_USER"))
        self.page.fill('input[name="_pass"]', os.getenv("EMAIL_PASS"))
        self.page.click('button[type="submit"]')

    def write_new_message(self):
        self.page.click("#rcmbtn104")

    def add_contact(self):
        self.page.click("a.input-group-text.icon.add.recipient")
        self.page.click("#rcmliMA a")
        self.page.click('#l\\:rcmrow0-1140011-0 a')
        self.page.click('button:has-text("Vložiť")')

    def attach_file(self):
        file_path = os.path.abspath("tajomnemiesta.html")
        with self.page.expect_file_chooser() as fc_info:
            self.page.click('button:has-text("Priložiť súbor")')
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        time.sleep(5)

    def fill_subject_and_body(self, subject, body):
        self.page.fill('input#compose-subject', subject)
        self.page.click('input#compose-subject')
        self.page.fill('textarea#composebody', body)

    def send_email(self):
        self.page.click('#rcmbtn111')
        time.sleep(60)
        
    def logout(self):
        self.page.click('a.logout#rcmbtn110')

    
