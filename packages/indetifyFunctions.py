from . import TuringMachine

# TODO: def intent(__verb__) 
# TODO: def intent(__obj__) 

def Reconhecimento (automaton, coil:list):
  turing_machine = TuringMachine.TuringMachine()
  turing_machine.coil = coil

  _ = automaton.Start(turing_machine)

  if automaton.state == 'Qf':
    return True
  else:
    return False