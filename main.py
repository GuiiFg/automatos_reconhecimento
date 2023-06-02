# pip install "git+https://github.com/GuiiFg/TuringMachine.git"
from TuringMachine.automatons import HotelOrderRecognizeAutomaton
from TuringMachine import TuringMachine
from TuringMachine.TokenWorker import TokenWorker
import json


def selectKey(tokens:list, keys:list):

  keys.reverse()
  tokens.reverse()

  __obj = None
  __verb = None

  for index, key in enumerate(tokens):
    if key == '__obj__':
      __obj = keys[index]
      break
  
  for index, key in enumerate(tokens):
    if key == '__verb__':
      __verb = keys[index]
      break

  return (__verb, __obj)


with open('words.json') as json_file: 
  dicionary = json.load(json_file)

input_teste = [
  'Eu queria fazer uma reserva',
  'Eu quero reservar um quarto',
  'Eu quero reservar a sauna',
  'Eu desejo pagar um boleto',
  'Eu quero pagar uma conta',
  'Eu quero fazer check-in',
  'Eu desejo fazer check-in',
  'Eu quero fazer check-out'
]

tkWorker = TokenWorker(dicionary)
tMachine = TuringMachine()
tMachine.automatons['OrderRecognize'] = HotelOrderRecognizeAutomaton()

for frase in input_teste:
  # importar o dicionario de palavras
  tkWorker = TokenWorker(dicionary)

  tMachine.coil = []
  tMachine.coil = tkWorker.GenerateTokensWithPhrase(frase) 
  tMachine.pointer = 1
  tMachine.run('OrderRecognize')
  if tMachine.automatons['OrderRecognize'].isFinalState:
    # TODO: ProccessToken(frase)
    print(selectKey(tkWorker.tokenslist, tkWorker.objectslist))
  else:
    print('Não entendi, poderia repetir?')