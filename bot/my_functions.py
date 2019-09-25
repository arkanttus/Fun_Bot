import random
from chatterbot.conversation import Statement

functions = locals()

def jokers():
    jokers = ['O que é um pontinho vermelho no castelo?\n É uma Pimenta do reino\n',
              'Qual a diferença da lagoa para a padaria?\n Na lagoa há sapinho, na padaria assa pão\n',
              'O que um cromossomo disse para o outro?\n Cromossomos Bonitos\n',
              'Como a CIA prende os ladrões?\n Errando, porque é errando que CIA-prende\n',
              'O que é um pontinho preto no avião?\n Uma aero-mosca\n',
              'Por que a água foi presa?\n Porque matou a sede\n',
              'O que um gato faz na academia?\n Abdomiau\n',
              'Qual é o cachorro que nunca tem filhotes?\n O cachorro quente\n',
              'O que fazer se você encontrar um monstro verde?\n Correr, antes que ele amadureça\n',
              'Qual peixe que está sempre pronto pra briga?\n O peixe-espada\n'
    ]
    
    return random.choice(jokers)

def is_function(statement):
    if statement.text.split()[0]  == 'call()':
        return True
    return False
    
def call_function(statement):
    function = statement.text.split()[1]
    response = functions[function]()
        
    if response != None:
        response_statement = Statement(text=response)
        response_statement.confidence = 1
    else:
        response_statement = Statement(text="Desculpe")
        response_statement.confidence = 0
    
    return response_statement
