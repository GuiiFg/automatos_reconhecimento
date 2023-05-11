from TuringMachine.automatons import HotelOrderRecognizeAutomaton
from TuringMachine import TuringMachine
from TuringMachine.TokenWorker import TokenWorker

frase = input("Oq deseja? ")

# importar o dicionario de palavras
dicionary = None
tkWorker = TokenWorker(dicionary)

tMachine = TuringMachine()

tMachine.coil = ['<'] + tkWorker.GenerateTokensWithPhrase(frase) 

tMachine.automatons['OrderRecognize'] = HotelOrderRecognizeAutomaton()

tMachine.run('OrderRecognize')


# TODO: tkWorker.ProccessToken(frase) 