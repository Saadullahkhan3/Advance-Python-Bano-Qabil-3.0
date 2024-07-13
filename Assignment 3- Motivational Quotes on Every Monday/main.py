from datetime import datetime
from time import sleep
from pandas.core.frame import DataFrame

from read_and_update_files import ReadUpdateFiles
from Sending_mail import SendMail


# Constant
SMTP_SERVER = "smtp.gmail.com"
SMTP_SSL_PORT = 465
SMTP_SERVICE_EMAIL = "<Your-Email-Here>"
SMTP_SERVICE_EMAIL_PASSWORD = "<Your-Password-Here>"

EMAILS_FILE = r"emails.csv"
QUOTE_JSON_FILE = r"quotes.json"


def html_quote_email_template_as_str(name: str, quote: str, author: str) -> str:
    '''
    UseCase
    ---
    Template of Email. 

    Args:
    ---
    - name: str -> Name of the recipient
    - quote: str -> quote for the email

    Returns:
    > `str:` HTML Template with the given name and the quote as string
    '''
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        html, body{
            width: 100%;
            height: 100%;
        }
        body{
            background-color: #cc9d9d;
        }
        h1{
            font-family: 'Lucida Sans Unicode';
            color: #6d4c4c;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        #greeting{
            font-size: 29;
            color: rgb(58, 48, 48);
            margin-left: 15px;
            padding: 10px;
        }
        #quote{
            font-weight: 700;
            letter-spacing: 5px;
            font-size: 31px;
            color: #473a3a;
            padding: 10px;
        }
        q{
            font-family: 'Lucida Grande';
            font-size: 29;
            color: rgb(58, 48, 48);
            padding: 10px;
        }
        cite{
            margin: 15px;
            font-size: 24;
            color: rgb(41, 30, 30);
        }
    </style>
    <title>Motivational Quote</title>
</head>
<body>
    <h1>Monday Motivational Quote</h1>
    <br />

    <p id="greeting">Dear ''' + f"{name}," + ''' 
    <br />
    We are glad that you subscribe our "Every Monday Motivational Quotes" via Email.
    <br />
    </p>
    
    <span id="quote">Quote:</span>
    
    <br />
    <q>''' + f"{quote}" '''</q>

    <footer><br /><cite>''' + f"{author}" + '''</cite>
    <br />
    <br />
    <cite>Sent by Saadullah Khan</cite>
    </footer>
</body>
</html>
    '''


if __name__ == "__main__":    
    
    print('''
---------------------------------------------------------
~~~~~-{ Email Sender via SMTP with SLL encryption }-~~~~~
>> Created by Saadullah Khan. 
Linkedin: https://www.linkedin.com/in/Saadullahkhan3
Github: https://www.github.com/Saadullahkhan3
_________________________________________________________        
''')

    today_week_day = datetime.today().weekday()

    # Checking if not monday close the program, else run the script
    if not today_week_day == 1:
        print("Today is not Monday, this program only works on Monday!\n")
        exit()

    # Objects
    mail_sender = SendMail(SMTP_SERVICE_EMAIL, SMTP_SERVICE_EMAIL_PASSWORD)
    read_and_update = ReadUpdateFiles()

    # Read Emails
    emails_list: DataFrame = read_and_update.read_csv_emails(EMAILS_FILE)

    # Read Quotes
    quotes_json_dict = read_and_update.read_json_quotes(QUOTE_JSON_FILE)
    # Extract Required Quotes | author, quote
    quote_author, quote = read_and_update.extract_quote_and_update_last_sent_quote_index(QUOTE_JSON_FILE, quotes_json_dict)

    subject: str = "Monday Motivational Quote!"
    
    for _, row_data in emails_list.iterrows():
        name: str = row_data["name"]
        email: str = row_data["email"]
        print("\nSending E-mail to -> ", email)

        message = html_quote_email_template_as_str(name.title(), quote, quote_author)
        mail_sender.send_email(SMTP_SERVICE_EMAIL, email, subject, message, SMTP_SERVER, SMTP_SSL_PORT, True)
        
        sleep(2)
