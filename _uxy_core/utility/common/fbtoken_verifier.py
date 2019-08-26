"""
Facebook Token Verifier
"""


def verify(params, verifyToken):
  """
  Verify Token
  """
  if( params['hub.verify_token'] ==  verifyToken ):
    challenge = params['hub.challenge']
    return int(challenge)

  return 'Wrong Token'
  
  



