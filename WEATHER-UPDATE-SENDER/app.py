import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# City ID mapping
CITY_IDS = {
    'karachi': '1174872',
    'lahore': '1172451',
    'islamabad': '1162015'
    # Add more cities as needed
}

# { id: 'weather'}
CACHED_WEATHER = {}


def weather_email_message(city_name: str, 
                          weather_update: str):
    '''
    UseCase:
    ---
    Use to create good looking HTML based email message and fill with given args.

    Args:
    - city_name: str -> City name for the fetched weather by `City ID`.
    - weather_update: str -> Weather update for the city.

    Returns:
    ---
    HTML based email filled with given values.
    '''
    return  f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WEATHER UPDATE</title>
    </head>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px;">
            <h2 style="text-align: center; color: #007bff;">Weather Update for {city_name}</h2>
            <p>Dear Employee,</p>
            <p>Here's the latest weather update for your city:</p>
            <table style="border-collapse: collapse; width: 100%; margin-top: 20px;">
                <tr>
                    <th style="border: 1px solid #dddddd; text-align: left; padding: 10px; background-color: #f2f2f2;">Description</th>
                    <th style="border: 1px solid #dddddd; text-align: left; padding: 10px; background-color: #f2f2f2;">Details</th>
                </tr>
                <tr>
                    <td style="border: 1px solid #dddddd; text-align: left; padding: 10px;">Weather</td>
                    <td style="border: 1px solid #dddddd; text-align: left; padding: 10px;">{weather_update}</td>
                </tr>
            </table>
            <p style="margin-top: 20px;">Best regards,<br>[Shayan Adnan | Saadullah Khan]</p>
        </div>
    </body>
    </html>
    """


def fetch_email_and_city(sheety_api):
    '''
    UseCase:
    ---
    Fetch data from google sheet with the help of `Sheety` by using its API.

    Args:
    ---
    - sheety_api: str -> API to communicate with the Sheety's server.

    Returns:
    ---
    - If succeed:
        - list[tuple] -> Returns list of tuple in below format:

        ```python
        [(user_email, city_name)]
        ```
    - If not, raise exception and stop the program!
    '''
    try:
        response = requests.get(sheety_api)
        response.raise_for_status()
        data = response.json()

        return [(row['email'], (row['city']).lower()) for row in data['sheet1']]
    
    except requests.RequestException as e:
        print(f'Error fetching data from Sheety: {e}')
        raise Exception("Can't Fetch the date from google sheet, program can't go further.")
    

def is_city_id_in_cached_data(city_id: str, 
                              CACHED_WEATHER: dict):
    '''
    UseCase:
    ---
    Check that city id is exists if yes mean that weather for that city is already fetched so return True, if not returns False

    Args:
    ---
    - city_id: str -> City id of the city
    - CACHED_WEATHER: dict -> Dict of the cached weather at the global scope 

    Returns:
    ---
    - bool -> True when data exists and False for not found
    '''
    if city_id in CACHED_WEATHER:
        return True
    else:
        False


def fetch_weather_update(api_key: str,
                         city_id: str | int):
    '''
    UseCase:
    ---
    Fetched the weather from `Open Weather Map`'s API for given city. Also check at first that weather is exists in cached data, if yes then returns from cached data else fetched the data.

    Args:
    ---
    - api_key: str -> API key to communicate with sever, Register API key from [Open Weather Map](https://openweathermap.org/).
    - city_id: str | int -> Id of the city, such as for 'Karachi' id is '1174872', if id is int then it typecast to str.

    Returns:
    ---
    - Returns weather data in below format:\n
        `f"{weather_description}, Temperature: {temperature}°C"`
    - When can't fetch the weather, returns False.
    '''
    
    global CACHED_WEATHER

    if is_city_id_in_cached_data(city_id, CACHED_WEATHER):
        print(f"{city_id} is already exists in cached.")
        return CACHED_WEATHER[city_id]

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?id={str(city_id)}&appid={api_key}&units=metric'

    try:
        response = requests.get(weather_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']

        fetched_weather = f"{weather_description}, Temperature: {temperature}°C"

        # Add the data in cached
        CACHED_WEATHER[city_id] = fetched_weather

        print(f"Fetched the weather for {city_id} and save to cached weather")

        return fetched_weather
    
    except requests.RequestException as e:
        print(f'Error fetching weather data: {e}')
        if response is not None:
            print(f'Status Code: {response.status_code}')
            print(f'Response Body: {response.text}')
        
        return False


def send_email(smtp_server: str, 
               smtp_tls_port: int, 
               email_address: str, 
               email_password: str, 
               to_email: str, 
               subject: str,
               body:str, 
               html: bool=False):

    '''
    UseCase:
    ---
    Used to sent HTML/PLAIN email through SMTP with TLS encryption.

    Args:
    ---
    - smtp_server: str -> SMTP server address, such as: 'smtp.gmail.com' for gmail SMTP service.
    - smtp_port: int -> TLS port for SMTP server.
    - email_adress: str -> Email address that uses to login for SMTP, also to use as _sender_ email.
    - email_password: str -> Email address password as login credential.
    - to_email: str -> Recipent email.
    - subject: str -> Subject of the email.
    - body: str -> Body of the email.
    - html: bool (defaults False): True when body of the email is HTML based, otherwise False

    Returns:
    ---
    - bool -> True when email is succeed and False for Failure
    '''

    try:
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_email
        msg['Subject'] = subject

        html_or_plain = "html" if html else "plain"

        msg.attach(MIMEText(body, html_or_plain))

        with smtplib.SMTP(smtp_server, smtp_tls_port) as server:
            server.starttls()
            server.login(email_address, email_password)

            server.sendmail(email_address, to_email, msg.as_string())

            return True

    except smtplib.SMTPException as e:
        print(f'Error sending email to {to_email}. \nError: {e}')
        return False


def get_city_id(city_name):
    '''
    UseCase:
    ---
    Use to get cities ID from our saved dictionary/hashmap that will may used to fetch weather.
    
    Args:
    ---
    city_name: str -> City name to reterive its ID. such as 'Karachi'

    Returns:
    - If succeed, returns city id.
    - If not, returns False
    '''
    return CITY_IDS.get(city_name, False)


def main(SHEETY_END_POINT: str,
         WEATHER_API: str,
         SMTP_SERVER: str,
         SMTP_TLS_PORT: int,
         SMTP_EMAIL: str,
         SMTP_EMAIL_PASSWORD: str,
         SUBJECT: str):
    
    email_city_pairs = fetch_email_and_city(SHEETY_END_POINT)

    for email, city_name in email_city_pairs:
        city_id = get_city_id(city_name)

        if city_id is None:
            print(f'City ID not found for {city_name}, Skipped emai: {email}')
            continue

        weather_update = fetch_weather_update(WEATHER_API, city_id)

        if not weather_update:
            print(f"Can't Fetch weather. \nDetails -> city: {city_name} | ID: {city_id}")
            continue

        body = weather_email_message(city_name.title(), weather_update)

        mail_status = send_email(SMTP_SERVER, SMTP_TLS_PORT, SMTP_EMAIL, SMTP_EMAIL_PASSWORD, email, SUBJECT, body, html=True)
        if not mail_status:
            print(f"Weather update can't sent to '{email}' for city {city_name}")
        else:
            print(f"Successfully fetch the weather and sent to '{email}'")


