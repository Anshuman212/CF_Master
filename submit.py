import os
from mechanicalsoup import StatefulBrowser
from login import set_login

def submit_problem(browser, contest, problem, lang, source_code_path):
    # Navigate to the submit page
    browser.open(f"https://codeforces.com/problemset/submit/{contest}/{problem}")

    # Check if the form is present
    form = browser.select_form('form.submit-form')
    if not form:
        print("Submit form not found. Exiting.")
        os._exit(1)


    form['submittedProblemIndex'] = problem
    form['programTypeId'] = lang


    with open(source_code_path, "r") as file:
        source_code = file.read()
    browser["source"] = source_code


    browser.submit_selected()

    print("Code submitted successfully!")

if __name__ == "__main__":
    # Create a StatefulBrowser instance
    browser = StatefulBrowser()

    # Default values
    default_contest_id = input("Enter the contest ID (default is 1): ") or "1"
    default_problem_id = input("Enter the problem ID (e.g., A): ")
    default_lang_id = input("Enter the language ID (default is 73 for C++): ") or "73"
    default_source_code_file = "chuckCodes.cpp"  # Assuming the file is in the same folder


    browser = set_login("", "")

    if not browser:
        print("Exiting due to login failure.")
        os._exit(1)

    submit_problem(browser, default_contest_id, default_problem_id, default_lang_id, default_source_code_file)
