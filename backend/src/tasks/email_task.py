import asyncio
from backend.src.tasks.celery_worker import celery_app
from backend.src.services.email import SMTPEmailService
from backend.config import config


@celery_app.task(name="send_admin_notification")
def send_admin_notification(full_name: str, phone: str):
    email_service = SMTPEmailService(
        smtp_host="smtp.gmail.com",
        smtp_port=465,
        login=config.email.gmail_sender,
        password=config.email.gmail_password
    )

    subject = "Новая заявка на консультацию!"
    body = (f"<b>ФИО:</b> {full_name} <br>"
            f"<b>Номер телефона:</b> {phone} <br>")

    loop = asyncio.get_event_loop()

    return loop.run_until_complete(
        email_service.send_email(
            subject=subject,
            body=body,
            to=config.email.admin_mail,
        )
    )
