"""
Lambda events entry point
"""

import _uxy_core
from _uxy_core import core
from _uxy_core.utility.common import fbtoken_verifier


def lambda_handler(event, context):
  try:
    if( event['http_method'] == 'GET' ):
      return fbtoken_verifier.verify(event['query_params'], \
        _uxy_core.appconfig['fb:verifyToken'])

    if( event['http_method'] == 'POST' ):
      return core.handler(event['body'])

    return {
      'status' : 405,
      'body' : 'Method not supported'
    }
  except Exception as e:
    print(str(e))
  return {
    'status' : 500,
    'body' : 'Uxy app error'
  }

