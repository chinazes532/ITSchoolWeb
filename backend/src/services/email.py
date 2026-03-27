import asyncio

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from abc import ABC, abstractmethod


class AbstractEmailService(ABC):
    @abstractmethod
    async def send_email(
            self,
            subject: str,
            body: str,
            to: str,
    ):
        raise NotImplementedError


class SMTPEmailService(AbstractEmailService):
    def __init__(
            self,
            smtp_host: str,
            smtp_port: int,
            login: str,
            password: str,
    ):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.login = login
        self.password = password

    async def send_email(
            self,
            subject: str,
            body: str,
            to: str,
    ):
        def send_email_sync() -> bool:
            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = to
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'html', 'utf-8'))

            try:
                with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as server:
                    server.login(self.login, self.password)
                    server.send_message(msg)
                print("Письмо отправлено")
                return True
            except Exception as e:
                print(f"Ошибка отправки email: {e}")
                return False

        return await asyncio.to_thread(send_email_sync)