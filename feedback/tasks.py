from time import sleep
from django.core.mail import send_mail
from celery import shared_task
# from .models import Subscriber, Newsletter
# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage
# from django_celery.celery import app
# from celery.schedules import crontab


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20) # Simulate expensive operation(s) that freeze Django
    send_mail(
    "Your Feedback",
    f"\t{message}\n\nThank you!",
    "support@example.com",
    [email_address],
    fail_silently=False,
    )


@shared_task
def send_mail_task():
    print("Mail sending.......")
    subject = 'welcome to Celery world'
    message = 'Hi thank you for using celery'
    email_from = "feedback@gmail.com"
    recipient_list = ['yourmail@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )
    return "Mail has been sent........"




# @shared_task
# def send_newsletter_task(newsletter_id):
#     newsletter = Newsletter.objects.get(id=newsletter_id)
#     subscribers = Subscriber.objects.all()

#     for subscriber in subscribers:
#         subject = newsletter.subject
#         content = newsletter.content

#         message = render_to_string('feedback/newsletter_template.html', {'newsletter': newsletter, 'subscriber': subscriber})
        
#         email = EmailMessage(subject, message, to=[subscriber.email])
#         email.send()

#     return f"Newsletter {newsletter.subject} sent to {subscribers.count()} subscribers."



# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # This will run the task every day at 8 am
#     sender.add_periodic_task(
#         crontab(hour=18, minute=40),
#         send_newsletter_task.s(newsletter_id=1),  # This assumes a newsletter with ID 1
#         name='send daily newsletter',
#     )