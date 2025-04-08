from django import forms
from feedback.tasks import send_feedback_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        send_feedback_email_task.delay(      #  Calling .delay() is the quickest way to send a task message to Celery.
            self.cleaned_data["email"], self.cleaned_data["message"]
            )