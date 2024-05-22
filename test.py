import outlook
import creds
import re

mail = outlook.Outlook()
mail.login(creds.USERNAME, creds.PASSWORD)
mail.inbox()
sender_email = 'bobby.w@cyberpowerpc.com'
latest_email = mail.get_last_email_from(sender_email)


if latest_email:
    print("From:", latest_email.sender)
    print("Subject:", latest_email.subject)
    print("Date:", latest_email.date)
    print("Body:", latest_email.body)
else:
    print("No emails from", sender_email)
# def extract_code(email_text):
#     pattern = 'BOBBY'
#     code = re.search(pattern, email_text)
#     if code:
#         return code.group(0)
#     else:
#         return None

# Assuming email_text contains the text content of the unread email
# email_message = mail.unread()
# email_text = mail.mailbody(email_message)

# Call the extract_code function
# code = extract_code(email_text)

# if code:
#     print("Code found:", code)
# else:
#     print("No code found in the email")



