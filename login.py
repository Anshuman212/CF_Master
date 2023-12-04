import getpass
import mechanicalsoup
import os
from dotenv import load_dotenv, set_key

load_dotenv()

def set_login(handle, password):
    browser = mechanicalsoup.StatefulBrowser()

    if not handle:
        handle = os.getenv("CODEFORCES_USERNAME", "")

    if not password:
        password = os.getenv("CODEFORCES_PASSWORD", "")

    browser.open('https://codeforces.com/enter')


    login_form = browser.select_form('form#enterForm')

    if not login_form:
        print('Login form not found.')
        return False

    login_form['handleOrEmail'] = handle
    login_form['password'] = password

    browser.submit_selected()

    # Check if login was successful by verifying the handle in the header
    header_text = browser.get_current_page().find('div', id='header').get_text()

    if handle not in header_text:
        print('Login Failed.')
        return False
    else:
        # Save credentials to environment variables
        os.environ["CODEFORCES_USERNAME"] = handle
        os.environ["CODEFORCES_PASSWORD"] = password

        # Save credentials to .env file
        set_key('.env', 'CODEFORCES_USERNAME', handle)
        set_key('.env', 'CODEFORCES_PASSWORD', password)

        print('Successfully logged in as ' + handle)
        return browser

def login():
    handle = os.getenv("CODEFORCES_USERNAME", "")
    password = os.getenv("CODEFORCES_PASSWORD", "")

    if not handle:
        handle = input('Enter your Codeforces handle or email: ')
    
    if not password:
        password = getpass.getpass('Enter your Codeforces password: ')

    set_login(handle, password)


if __name__ == "__main__":
    login()
