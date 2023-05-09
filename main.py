import packages as pkg

frase = input("Oq deseja? ")

tkWorker = pkg.TokenWorker()

tkWorker.GenerateToken(frase) 

coil = ['<'] + tkWorker.token

automaton = pkg.TuringMachine.HotelOrderRecognizeAutomaton()

isValid = pkg.Reconhecimento(automaton, coil)

# TODO: tkWorker.ProccessToken(frase) 