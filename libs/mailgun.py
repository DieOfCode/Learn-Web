import os
from typing import List
from requests import Response, post


class MailgunExeption(Exception):
    def __init__(self, message):
        self.message = message


class Mailgun():

    FROM_TITLE = "Pricing service"
    FROM_EMAIL = "do-not-reply@sandboxeca91e93a2204a1c9389dd96df24b02b.mailgun.org"

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        mailgun_api_key = os.environ.get("MAILGUN_API_KEY", None)
        mailgun_domain = os.environ.get("MAILGUN_DOMIAN", None)
        if mailgun_api_key:
            raise MailgunExeption("Failed to load API key")

        if mailgun_domain:
            raise MailgunExeption("Failed to load Mailgun domian")

        response = post(
            f"{mailgun_domain}/messages",
            auth=("api", mailgun_api_key),
            data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                  "to": email,
                  "subject": subject,
                  "text": text,
                  "html": html})
        if response.status_code != 200:
            print(response.json())
            raise MailgunExeption("An error occurred while sending e-mail")
        return response
