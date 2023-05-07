import json

class TokenWorker: 
    
  def __init__(self) :
    self.__currentToken = []
    self.__currentTokenIdentifyer = []

  def GenerateToken(self, phrase):
    phrase = phrase.upper()

    self.__currentToken = phrase.lstrip().split(' ')

    for i in self.__currentToken:
      self.__currentTokenIdentifyer.append(self.GetTypeOfValue(i))
    print(self.__currentToken)
    print(self.__currentTokenIdentifyer)

  def GetTypeOfValue (self, value):

    # TODO: Ler o arquivo de tokens do json words.json

    values = {
      "__suj__" : [
        "EU"
      ],
      "__verb__" : [
        "FAZER", 
        "REALIZAR", 
        "QUERER", 
        "QUERO", 
        "QUERIA", 
        "RESERVAR", 
        "PAGAR"
      ],
      "__obj__" : [
        "QUARTO", 
        "RESERVA", 
        "SUIT", 
        "DORMITORIO", 
        "CHECK-IN", 
        "CHECK-OUT",
        "BOLETO"
      ],
      "__pron__" : [
        "A", 
        "O", 
        "UM", 
        "UMA"
      ]
    }

    finalKey = "__undentify__"
    for key in list(values.keys()):
      if value in values[key]:
        finalKey = key
        break

    return finalKey
