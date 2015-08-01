#!/usr/bin/python

import players
import games

bob = players.player(1)
nathan = players.player(2)

game = games.game()
game.add_player(bob)
game.add_player(nathan)
game.play_game()
