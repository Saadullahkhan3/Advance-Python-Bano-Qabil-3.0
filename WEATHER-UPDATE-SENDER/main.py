from app import main

# Configurations:
# SMTP:
SMTP_EMAIL = r"<YOUR-EMAIL>"
SMTP_EMAIL_PASSWORD = r"<YOUR-EMAIL-PASSWORD>"
SMTP_SERVER = r"<SMTP-SERVER>"  # for gmail it will be 'smtp.gmail.com'
SMTP_TLS_PORT = 587 # This is for gmail TLS, make sure to modify it according to you

# APIs:
OPEN_WEATHER_MAP_API = '<YOUR-OPEN-WEATHER-API>'
SHEETY_END_POINT = '<YOUR-SHEETY-END-POINT>'

# Email Subject:
SUBJECT = "Daily Weather Update"


if __name__ == "__main__":
    main(SHEETY_END_POINT, OPEN_WEATHER_MAP_API, SMTP_SERVER, SMTP_TLS_PORT, SMTP_EMAIL, SMTP_EMAIL_PASSWORD, SUBJECT)



