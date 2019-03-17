#!/usr/bin/env python

import yaml
import trigger_http
import trigger_time

class Bot():
    path=''
    behaviours={}

    def __init__(self, path, name):
        self.path=path
        stream = file(path + 'behaviours.yml', 'r')
        self.behaviours=yaml.load(stream)['behaviours']
        self.loop_triggers()

    def loop_triggers(self):
        for behaviour in self.behaviours:
            res, msg = eval('trigger_' + behaviour['trigger'] + '(behaviour)')
            if res == False:
                self.do_action(behaviour['action'])

    def do_action(self, action):
        pb = PlayBook(playbook= path + behaviour['action'] )
        pb.run()
