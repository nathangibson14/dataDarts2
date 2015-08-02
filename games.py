import players
import sqlite3 as sql
import sys

class game:
  def __init__(self):
    self._players = []
    self._num_legs = 1
    self._num_sets = 1
    self._num_players = 0
    self._score = []
    self._tosses = []
    self._active_player = 0
    
  def add_player(self,player):
    self._players.append(player)
    self._score.append(501)
    
  def set_num_legs(self,num_legs):
    self._num_legs = num_legs
    
  def set_num_sets(self,num_sets):
    self._num_sets = num_sets
  
  #
  # method: play_game
  # description: executes a game of 501
  # details: initializes game data, executes loop until game finishes
  #    
  def play_game(self, first=0):
    self._num_players = len(self._players)
    if self._num_players == 0:
      print "Error: must have player to play game."
      sys.exit(-1)
      
    for p in self._players:
      p.display_player_info()
      print ""
    
    self._active_player = first
    play = True  
    while play:
      play = self.toss()
      self._active_player = (self._active_player + 1) % self._num_players      
      print ""
  
  #
  # method: toss
  # description: single toss by active player
  # details: displays current status, prompts for score.
  #          special inputs 'undo' and 'quit' do obvious.
  #          records score in game list
  # return: true if game continues, false if game ends
  #    
  def toss(self):
    player = self._active_player    
    player_id = self._players[player].get_id()
    for p in xrange(0,self._num_players):
      if p == player:
        print "*%s: %d" % (self._players[p].get_name(),self._score[p])
      else:
        print "%s: %d" % (self._players[p].get_name(),self._score[p])
        
    inp = raw_input("Score: ")
    
    if (inp == "undo"):
      return self.undo()
      
    elif (inp == "quit"):
      return False
      
    else:
      val = int(inp)
    
    if (val > 180 or val < 0):
      print "Invalid score."
      print ""
      return self.toss()
      
    elif (val > self._score[player]):
      print "Bust."
      self._tosses.append((self._score[player],0,player_id))
      return True
       
    elif (val == self._score[player]):
      self._tosses.append((self._score[player],val,player_id))
      self._score[player] -= val
      print "Player %s wins!" % self._players[player].get_name()
      self.save_game()
      return False
      
    else:
      self._tosses.append((self._score[player],val,player_id))
      self._score[player] -= val
      return True
    
  #
  # method: undo
  # description: undoes the previous entry
  # details: adds back previous score, returns action to previous player
  # return: return value of new toss call
  #  
  def undo(self):
    if len(self._tosses) > 0:
      
      # roll back to previous player
      self._active_player += self._num_players-1
      self._active_player %= self._num_players
      
      # return score to previous value, remove toss
      self._score[self._active_player] += self._tosses[-1][0]
      del self._tosses[-1]
    
    print ""
    return self.toss()
  
  #
  # method: save_game
  # description: records game details in database
  #
  def save_game(self):
    con = sql.connect('darts.db')
    with con:
      cur = con.cursor()
      cur.execute("INSERT INTO Games(Type,WinnerId) VALUES('501',?)",
                (self._players[self._active_player].get_id(),))
      cur.execute("SELECT Id FROM Games ORDER BY Id DESC LIMIT 1")
      game_id = cur.fetchone()[0]
      print game_id
      for p in self._players:
        cur.execute("INSERT INTO GamePlayers(GameId,PlayerId) VALUES(?,?)",
                  (game_id,p.get_id()))
      for t in xrange(0,len(self._tosses)):
        cur.execute("INSERT INTO GameScores(GameId,Round,PlayerId,ScoreBefore,Score) "
                    "VALUES(?,?,?,?,?)", (game_id,t,self._tosses[t][2],
                    self._tosses[t][0],self._tosses[t][1]))
    con.close()
    
  def play_match(self):
    pass
    
