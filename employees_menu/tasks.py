# Create your tasks here

from celery import shared_task
import requests

SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'

@shared_task
def send_reminder(message):
    payload = '{"text":"Hello! I share with you today\'s menu :) \n click here %s"}' % message
    response = requests.post(SLACK_WEBHOOK, data=payload) 
    print(response.text)