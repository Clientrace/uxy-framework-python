"""
Authored by Kim Clarence Penaflor
07/30/2019
version 0.0.2
Documented via reST
Holds Chatbot-User conversation data
"""

from _uxy_core.utility.aws_services.dynamodb import Dynamodb
from _uxy_core import appconfig

global DYNAMODB
DYNAMODB = Dynamodb(
  appconfig['app:name']+'-uxy-session-'+appconfig['app:stage']
)

# Save DB Item
def save_item(userID, key, data):
  global DYNAMODB

  itemKey = {
    'userID' : { 'S' : userID }
  }

  updateVal = {
    key : {
      'Value' : {
        'S' : data
      }
    }
  }

  data = DYNAMODB.update_item(
    itemKey,
    updateVal
  )

# Get DB Item
def get_item(userID, key):
  global DYNAMODB

  itemKey = {
    'userID' : { 'S' : userID }
  }

  data = DYNAMODB.get_item(itemKey)
  print(data['Item'])
  if( 'Item' in data ):
    if( key in data['Item'] ):
      if( 'S' in data['Item'][key] ):
        return data['Item'][key]['S']
      if( 'N' in data['Item'][key] ):
        return data['Item'][key]['N']
    return None
  return None

# Increment DB Item attrib
def increment(userID, attribute):
  global DYNAMODB

  itemKey = {
    'userID' : { 'S' : userID }
  }

  data = DYNAMODB.increment(itemKey, attribute)
  return data['Attribute'][attribute]['N']

# Reset DB Item attrib
def reset(userID, attribute):
  global DYNAMODB

  itemKey = {
    'userID' : { 'S' : userID }
  }

  item = {
    attribute : {
      'Value' : { 'N' : '0 '}
    }
  }

  data = DYNAMODB.update_item(itemKey, item)
  return data

