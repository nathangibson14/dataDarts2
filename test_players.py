#!/usr/bin/python

import players

print "Starting test."

for i in xrange(1,4):
  person = players.player(i)
  person.display_player_info()
