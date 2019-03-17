#!/usr/bin/env python

import yaml
import time
import bot

class Bots():
    host='127.0.0.1'
    bots={}
    path=''

    def __init__(self, path):
        self.path=path
        stream = file(path + 'bots.yml', 'r')
        self.bots=yaml.load(stream)

    #def lint_bots:

    def main(self):
        botlist = {}
        for name in self.bots['bots']:
            botlist['name'] = bot.Bot(self.path + name + '/', name)

    #def main(self):
    #    while True:
    #        for bot in self.bots['bots']:
    #            self.loop_triggers(bot)
    #        time.sleep(5)

    #def loop_triggers(self, bot):
    #    for behaviour in self.bots[bot]:
    #        if behaviour['trigger'] == 'get':
    #            print(behaviour['name'])
    #        print(behaviour)

    def test(self):
        print (self.path)
        print (self.bots)
        return self.host
