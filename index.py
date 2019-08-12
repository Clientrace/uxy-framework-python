"""
Lambda events entry point
"""

from _uxy_core import core


def lambda_handler(event, context):
  try:
    return core.handler(event)
  except Exception as e:
    print(str(e))
  return {
    'status' : 500,
    'body' : 'Uxy app error'
  }



