import re
import commands

command_re = re.compile('!!/([^ ]+) ?(.+)?')


def callback(content, sender, room, client):
    content = str(content)
    if content.startswith('!!/'):
        command_parts = command_re.split(content)
        command = command_parts[1]
        args = command_parts[2]
        if args is not None:
            args = args.split(' ')
        print('COMMAND: ' + command + '; Arguments: ' + str(args))
        try:
            room.send_message(str(commands.__getattribute__(command.lower())(args)))
        except AttributeError:
            room.send_message('Command ' + command + ' wasn\'t found!')
            pass
