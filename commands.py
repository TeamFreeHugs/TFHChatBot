import random


def help(args):
    return 'Hi. I\'m Uni\\*\'s Chatbot, in TFHCB, to challenge annoying girls who think they can fight programming.'


kill_types = ['$1 was murdered',
              'Voldermort (aka Shadow Wizard) used Avada Kedavra on $1', '$1 disappeared for no reason',
              '$1 played too much Minecraft and got eaten by a zombie', '$1 sleeps with the fishes',
              '$1 has been entered into a Death Note', '$1 was accidentally decapitated in an old factory',
              'A noose appeared around $1\'s neck and he tripped and fell off a cliff', 'An axe fell on $1\'s head.',
              'in\u0252z\u0258m\u0252\u042f.A.M poured trifluoromethanesulfonic acid on $1']


def kill(args):
    if args is not None:
        return kill_types[random.randrange(0, len(kill_types))].replace('$1', ''.join(args))
    else:
        return 'Kill who?'
