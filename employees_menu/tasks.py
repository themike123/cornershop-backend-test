# Create your tasks here

from celery import shared_task
import requests

SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'

@shared_task
def send_reminder(message):
    payload = '{"text":"Hello! I share with you today\'s menu :) \n click here %s"}' % message
    response = requests.post(SLACK_WEBHOOK, data=payload) 
    print(response.text)