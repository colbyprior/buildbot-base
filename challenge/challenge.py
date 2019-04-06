#!/usr/bin/env python

import yaml
#import trigger_http

class Challenge():
    path=''
    challenge={}

    def __init__(self, challenge):
        self.challenge=challenge
        for stage in self.challenge:
            print (stage)

    def loop_triggers(self):
        for challenge in self.challenges:
            res, msg = eval('trigger_' + challenge['trigger'] + '(challenge)')
            if res == False:
                self.do_action(challenge['action'])

    def do_action(self, action):
        pb = PlayBook(playbook= path + challenge['action'] )
        pb.run()
