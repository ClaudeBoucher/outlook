import outlook
import creds
import re

mail = outlook.Outlook()
mail.login(creds.USERNAME, creds.PASSWORD)
mail.inbox()

def extract_code(email_text):
    pattern = 'BOBBY'
    code = re.search(pattern, email_text)
    if code:
        return code.group(0)
    else:
        return None

# Assuming email_text contains the text content of the unread email
email_message = mail.unread()
email_text = mail.mailbody(email_message)

# Call the extract_code function
code = extract_code(email_text)

if code:
    print("Code found:", code)
else:
    print("No code found in the email")

