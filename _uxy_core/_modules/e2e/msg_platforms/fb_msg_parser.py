"""
Authored by Kim Clarence Penaflor
07/30/2019
version 0.0.1
Documented via reST
"""

import _uxy_core
from _uxy_core.utility.api_wrappers.facebook import Facebook


def parse_string_codes(fb, string_msg):
  if( ':username:' in string_msg ):
    userName = fb.get_user_info('first_name', 'last_name')
    userName = userName['first_name']+' '+userName['last_name']
    string_msg = string_msg.replace(':username:', userName)

  if( ':firstname:' in string_msg ):
    userName = fb.get_user_info('first_name')
    firstName = userName['first_name']
    string_msg = string_msg.replace(':firstname:', firstName)

  if( ':botname:' in string_msg ):
    string_msg = string_msg.replace(':botname:', _uxy_core.appconfig['app:name'])

  return string_msg


def send_text_msg(fb, blueprint):
  fb.send_txt_msg(blueprint['data'])


def send_quick_reply(fb, blueprint):
  options = blueprint['options']
  buttons = []
  for option in options:
    buttons.append(option['data'])

  fb.send_quick_reply(
    blueprint['data'],
    buttons
  )

def send_btn_template(fb, blueprint):
  options = blueprint['options']
  buttons = []
  for option in options:
    if( option['type'] == 'postback' ):
      buttons.append(
        ['postback', option['buttonName']]
      )
    
    if( option['type'] == 'web_url' ):
      buttons.append(
        ['web_url', option['buttonName'], option['url'], option['size'],\
          option['webview']]
      )

  fb.send_btn_template(buttons, blueprint['data'])

# TODO Send image multimedia
def send_img():
  pass


def exe(userID, response):
  facebook = Facebook(userID, _uxy_core.environment.get('FACEBOOK','FB_PAGE_TOKEN'))
  facebook.send_action()

  response['data'] = parse_string_codes(facebook, response['data'])
  if( response['type'] == 'txt' or response['type'] == 'text' ):
    send_text_msg(facebook, response)

  if( response['type'] == 'quick_reply' ):
    send_quick_reply(facebook, response)


