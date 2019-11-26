# The 'email' module allows you to:
#   - Create the email text for letting a Santa know who they will be giving
#     a gift to
#   - Send an email to a Santa with instructions

from email.mime.text import MIMEText
import smtplib

#####################
# Week 2, or after learning about string methods
#####################

# Given a string representing a name, change it to follow the standard format
# for names.
# The standard format for names is:
#   - All words start with a capital letter
#   - There are no extra spaces at the beginning or the end
#
# >>> standardize_name("shevek")
# 'Shevek'
# >>> standardize_name("  ana MAria   ")
# 'Ana Maria'
def standardize_name(name):
    remove_space = name.strip().title()
    return remove_space

#####################
# Week 3, or after learning about string templates
#####################

santa_email_body_template = '''TODO: Complete template here'''

# Given the names of the Santa (person giving the gift) and the Santee (person
# receiving the gift), builds the text of the email message with instructions.
#
# The email should:
#   - Use standardized names (we wrote a function for this!)
#   - Greet the Santa by their name
#   - Include the name of the Santee (so that the Santa knows who to give the
#     present to :))
#
# Optionally, the email may also include additional instructions, like:
#   - Tips for choosing a good gift
#   - The price range
#   - The day when the gifts will be given
def build_email_text(santa, santee, cost):
    message = """ Hi {santa},
    You are {santee}'s secret santa.
    Remember the rules: think of something they can really enjoy, and don't spend more than £{cost}.

    Happy giving!

    Your secret santa bot"""
    return message.format(santa = santa, santee = santee, cost = cost )


#####################
# Week 6, or after learning about sending emails
#####################

email_from = 'wtw.secret.santa@hotmail.com'
# In real life, never write your actual password in plain text in a code file.
# If you're not sure why this is a bad idea, ask one of the TAs!
email_password = 'no_deers_just_pythons'
email_user_name = 'wtw.secret.santa@hotmail.com'
smtp_host = "smtp.live.com"
smtp_port = 587

# Given the names of the Santa and the Santee, and the Santa's email address,
# send an email to the Santa to let them know who they will be giving a present
# to.
#
# To build the email text, use the function implemented previously!
def send_santa_email(santa_name, santa_email, santee_name):
    pass
