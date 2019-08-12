
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data


def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  if( not valid ):
    if( maxRetry ):
      return [], valid

  response += router.route(userID, 'main')
  return response, valid






