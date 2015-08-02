import sys
from PyQt4 import QtCore, QtGui
import form
import newPlayer
import game_play
import sqlite3 as sql
import players 
import games
 
class MainMenu(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = form.Ui_Dialog()
    self.ui.setupUi(self)
        
    # push button setup
    self.ui.pushButton.clicked.connect(self.add_player)
    self.ui.newPlayer.clicked.connect(self.new_player)
    self.ui.removePlayer.clicked.connect(self.remove_player)
    self.ui.playGame.clicked.connect(self.play_game)
        
        
    # player list setup
    self.load_players()
    self.display_players()
    self.game_players = []
    self.ui.listWidget.itemSelectionChanged.connect(self.display_stats)
 
 
  def add_player(self):
    row = self.ui.listWidget.currentRow()
    if (row != -1):
      self.ui.listWidget_2.addItem(self.players[row]._name)
      self.game_players.append(self.players[row])
      
  def new_player(self):
    # get new player name
    self.input_window = NewPlayer()
    
    if (self.input_window.name != None and self.input_window.name != ""):
    
      # add player to database
      self.players.append(players.player())
      self.players[-1].set_name(self.input_window.name)
      self.players[-1].export_data()
      
      # update list of players
      self.display_players()
      
      # add player to game
      self.ui.listWidget_2.addItem(self.players[-1].get_name())
      self.game_players.append(self.players[-1])
      
    # get rid of input_window
    self.input_window = None
    
  def remove_player(self):
    row = self.ui.listWidget_2.currentRow()
    if (row != -1):
      self.ui.listWidget_2.takeItem(row)
      del self.game_players[row]
    
  
  def load_players(self):
    self.players = []
    con = sql.connect('darts.db')
    with con:
      cur = con.cursor()
      cur.execute("SELECT Id FROM Players")
      data = cur.fetchall()
      for pt in data:
        self.players.append(players.player(pt[0]))
    
  def display_players(self):
    self.ui.listWidget.clear()
    for p in self.players:
      self.ui.listWidget.addItem(p.get_name())
        
  def display_stats(self):
    row = self.ui.listWidget.currentRow()
    self.ui.textBrowser.setText("Stats for {0}".format(self.players[row].get_name()))
    self.ui.textBrowser.append("  Games played: {0}".format(self.players[row]._games_played))
    self.ui.textBrowser.append("  Win fraction: {0}".format(self.players[row]._win_frac))
    self.ui.textBrowser.append("  Average: {0}".format(self.players[row]._average))
    self.ui.textBrowser.append("  Fraction over 60: {0}".format(self.players[row]._over_60))
    self.ui.textBrowser.append("  Fraction over 100: {0}".format(self.players[row]._over_100))
        
  def play_game(self):
    if len(self.game_players) != 0:
      self.hide()
      self.game = GamePlay(self.game_players)
      self.show()
      self.display_stats()
        
class NewPlayer(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self,parent)
    self.ui = newPlayer.Ui_Dialog()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.okay)
    self.name = None
    self.exec_()
    
  def okay(self):
    self.name = str(self.ui.lineEdit.text())
    self.close()
    
class GamePlay(QtGui.QDialog):
  def __init__(self,players,parent=None):
    QtGui.QWidget.__init__(self,parent)
    self.ui = game_play.Ui_Dialog()
    self.ui.setupUi(self)   
    
    # push buttons
    self.ui.submit.clicked.connect(self.submit)
    self.ui.undo.clicked.connect(self.undo)
    self.ui.quit.clicked.connect(self.close)
    
    # game setup    
    self.players = players
    self.num_players = len(players)
    self.score = [501]*self.num_players
    self.active_player = 0
    self.tosses = []
    
    # display score, stats
    self.setup_toss()
    
    # no error message to start
    self.ui.label_error.setText("")
     
    # execute 
    self.exec_()
        
        
  def submit(self):
    self.process_toss()
    self.setup_toss()
    
  def undo(self):
    if len(self.tosses) > 0:
      
      # roll back to previous player
      self.active_player += self.num_players-1
      self.active_player %= self.num_players
      
      # return score to previous value, remove toss
      self.score[self.active_player] += self.tosses[-1][1]
      del self.tosses[-1]
    
    self.setup_toss()
    
  def display_score(self):
    self.ui.text_scores.clear()
    for p in range(0,len(self.players)):
      self.ui.text_scores.append("{0}: \t{1}".format(self.players[p]._name,
            self.score[p]))
  
  def display_stats(self):
    player = self.players[self.active_player]
    self.ui.text_stats.setText("Stats for {0}".format(player.get_name()))
    self.ui.text_stats.clear()
    self.ui.text_stats.append("Games played: {0}".format(player._games_played))
    self.ui.text_stats.append("Win fraction: {0}".format(player._win_frac))
    self.ui.text_stats.append("Average: {0}".format(player._average))
    self.ui.text_stats.append("Fraction over 60: {0}".format(player._over_60))
    self.ui.text_stats.append("Fraction over 100: {0}".format(player._over_100))   
    
  def setup_toss(self):
    self.ui.inputField.clear()
    self.ui.label_player.setText("Player {0} to throw".format(self.players[self.active_player]._name))
    self.display_score()
    self.display_stats()
    self.display_tosses()
    
  def display_tosses(self):
    self.ui.text_toss.clear()
    toss_strings = [""]*self.num_players
    for t in xrange(0,len(self.tosses)):
      p = t % self.num_players
      toss_strings[p] += str(self.tosses[t][1]) + ", "
    
    for p in xrange(0,self.num_players):
      self.ui.text_toss.append(self.players[p]._name+":")
      self.ui.text_toss.append(toss_strings[p][0:-2]+"\n")
      
    
  def process_toss(self):
    
    # get score from input box.  try/except prevents junk input from crashing 
    #   program.
    try:
      val = int( self.ui.inputField.text() )
    except:
      self.ui.label_error.setText("Invalid score.")
      return
    
    # check that score is within bounds
    if (val > 180 or val < 0):
      self.ui.label_error.setText("Invalid score.")
      return
    
    # valid score, clear error message
    self.ui.label_error.setText("")
      
    # check for bust
    if (val > self.score[self.active_player]):
      self.ui.label_error.setText("Bust.")
      val = 0
      
    # update score  
    self.tosses.append((self.score[self.active_player],
                        val,self.players[self.active_player]._id))
    self.score[self.active_player] -= val
    
    # check for win
    if (self.score[self.active_player] == 0):
      self.save_game()
      self.close()
    
    # increment player
    self.active_player += 1
    self.active_player %= self.num_players  
     
    
  def save_game(self):
    con = sql.connect('darts.db')
    with con:
      cur = con.cursor()
      cur.execute("INSERT INTO Games(Type,WinnerId) VALUES('501',?)",
                (self.players[self.active_player].get_id(),))
      cur.execute("SELECT Id FROM Games ORDER BY Id DESC LIMIT 1")
      game_id = cur.fetchone()[0]
      for p in self.players:
        cur.execute("INSERT INTO GamePlayers(GameId,PlayerId) VALUES(?,?)",
                  (game_id,p.get_id()))
      for t in xrange(0,len(self.tosses)):
        cur.execute("INSERT INTO GameScores(GameId,Round,PlayerId,ScoreBefore,Score) "
                    "VALUES(?,?,?,?,?)", (game_id,t,self.tosses[t][2],
                    self.tosses[t][0],self.tosses[t][1]))
    con.close()
    
    for p in self.players:
      p.import_data()
 
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MainMenu()
  myapp.show()
  sys.exit(app.exec_())
    
