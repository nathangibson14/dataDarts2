import sys
from PyQt4 import QtCore, QtGui
from form import Ui_Dialog
import newPlayer
import sqlite3 as sql
import players 
 
class MainMenu(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
        
    # push button setup
    self.ui.pushButton.clicked.connect(self.add_player)
    self.ui.newPlayer.clicked.connect(self.new_player)
        
    # player list setup
    self.load_players()
    self.display_players()
    self.ui.listWidget.itemSelectionChanged.connect(self.display_stats)
 
 
  def add_player(self):
    item = self.ui.listWidget.currentItem()
    if (item != None):
      self.ui.listWidget_2.addItem(item.text())
      
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
      
    # get rid of input_window
    self.input_window = None
  
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
        
class NewPlayer(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self,parent)
    self.ui = newPlayer.Ui_Dialog()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.okay)
    self.name = None
    self.exec_()
    
  def okay(self):
    self.name = str(self.ui.nameInput.toPlainText())
    self.close()
    
    
    
        
 
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MainMenu()
  myapp.show()
  sys.exit(app.exec_())
    
