# pip install "git+https://github.com/GuiiFg/TuringMachine.git"
from TuringMachine.automatons import HotelOrderRecognizeAutomaton
from TuringMachine import TuringMachine
from TuringMachine.TokenWorker import TokenWorker
import json

with open('words.json') as json_file: 
  dicionary = json.load(json_file)


frase = input("Oq deseja? ")

# importar o dicionario de palavras
tkWorker = TokenWorker(dicionary)

tMachine = TuringMachine()

tMachine.coil = tkWorker.GenerateTokensWithPhrase(frase) 

tMachine.automatons['OrderRecognize'] = HotelOrderRecognizeAutomaton()

tMachine.run('OrderRecognize')

if tMachine.automatons['OrderRecognize'].isFinalState:
  # TODO: ProccessToken(frase)
  print('Entendi')
else:
  print('Não entendi, poderia repetir?')
