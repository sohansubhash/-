from flask import Flask, request
from flask_mysqldb import MySQL
import json
import requests

app = Flask(__name__)
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)


# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
FB_APP_TOKEN = 'EAAB3HnLuiGIBAPRPMo9ijBqEqf3jkZAUMWbqbeC0vWWbViDZAwsi4q5z2NUr7jYCTn6r1pBlI19RkwlhlKHKzZCGt9ZBl5xSDn9NqQnsqWLANCoHIwj5ezisiutis1UgGLBL2KhAvlnCnZCAnwKLokBSvAsY8ioTzQyPRPEcPm2bAva6KOq3Xj'
FB_ENDPOINT = 'https://graph.facebook.com/v2.6/me/{0}'
FB_MESSAGES_ENDPOINT = FB_ENDPOINT.format('messages')
FB_THREAD_SETTINGS_ENDPOINT = FB_ENDPOINT.format('thread_settings')

@app.route('/', methods=['GET'])
def handle_verification():
  print("Handling Verification.")
  if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
    print("Verification successful!")
    return request.args.get('hub.challenge', '')
  else:
    print("Verification failed!")
    return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print("Handling Messages")
  payload = request.get_data()
  print(payload)
  for sender, message in messaging_events(payload):
    print("Incoming from %s: %s" % (sender, message))
    send_message(FB_APP_TOKEN, sender, message)
  return "ok"

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
    else:
      yield event["sender"]["id"], "I can't echo this"


def send_message(token, recipient, text):
  """Send the message text to recipient with id recipient.
  """
  r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": text.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print(r.text)

# def send_FB_buttons(sender_id, text, buttons):
#     return send_FB_message(
#         sender_id,
#         {
#             'attachment': {
#                 'type': 'template',
#                 'payload': {
#                     'template_type': 'button',
#                     'text': text,
#                     'buttons': buttons
#                 }
#             }
#         }
#     )

# def send_FB_message(sender_id, message):
#     fb_response = requests.post(
#         FB_MESSAGES_ENDPOINT,
#         params={'access_token': FB_APP_TOKEN},
#         data=json.dumps(
#             {
#                 'recipient': {
#                     'id': sender_id
#                 },
#                 'message': message
#             }
#         ),
#         headers={'content-type': 'application/json'}
#     )
#     if not fb_response.ok:
#         app.logger.warning('Not OK: {0}: {1}'.format(
#             fb_response.status_code,
#             fb_response.text
#         ))

def configure_profile():
    p = requests.post(FB_ENDPOINT.format(messenger_profile?),
    params={"access_token": FB_APP_TOKEN},
    data=json.dumps({
"greeting":[
  {
    "locale":"default",
    "text":"Fuck you {{user_first_name}}! Fuck you right in your little asshole and not in a beautiful way like grandpa and Pedro."
  }
],
    }),
    headers={'Content-type': 'application/json'})
  if p.status_code != requests.codes.ok:
    print(p.text)


if __name__ == '__main__':
  app.run()

