import os
import time
from dotenv import load_dotenv

load_dotenv()  # Načíta moje hodnoty z .env

def test_login(page):
    page.goto(os.getenv("EMAIL_URL"))

    # Vyplnenie prihlasovacích údajov
    page.fill('input[name="_user"]', os.getenv("EMAIL_USER"))
    page.fill('input[name="_pass"]', os.getenv("EMAIL_PASS"))

    # Klik na tlačidlo prihlásiť
    page.click('button[type="submit"]')

    # Klik na "Napísať správu"
    page.click("#rcmbtn104")

    # Pridať kontakt
    page.click("a.input-group-text.icon.add.recipient")
    page.click("#rcmliMA a")
    page.click('#l\\:rcmrow0-1140011-0 a')
    page.click('button:has-text("Vložiť")')

    # Vybrať súbor – očakávam file chooser
    file_path = os.path.abspath("tajomnemiesta.html")
    with page.expect_file_chooser() as fc_info:
        page.click('button:has-text("Priložiť súbor")')  # klik na tlačidlo
    file_chooser = fc_info.value
    file_chooser.set_files(file_path)

    # **Pozastaviť tu, kým súbor nahrá**
    time.sleep(5)

    # Predmet
    page.fill('input#compose-subject', 'SergejTest')
    page.click('input#compose-subject')  # kliknutie 

    # Textarea
    page.fill('textarea#composebody', 'test Sergej')

    # Klik na Odoslať
    page.click('#rcmbtn111')


    time.sleep(60)
