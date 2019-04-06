#!/usr/bin/env python

import yaml
import challenge as c

class Challenges():
    path=''
    challenges={}

    def __init__(self, path, name):
        self.path=path
        stream = file(path + 'challenge.yml', 'r')
        self.challenges=yaml.load(stream)
        for challenge in self.challenges:
            chal = c.Challenge(self.challenges[challenge])
