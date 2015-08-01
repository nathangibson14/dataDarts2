#!/usr/bin/python

import sqlite3 as sql

class player:
  def __init__(self,uid=-1):
    self._id = uid
    
    if uid==-1:
      self._name = ""
      self._average = 0
      self._games_played = 0
      self._over_60 = 0
      self._over_100 = 0
      self._win_frac = 0
  
    else:
      self.import_data()
  
  
  def set_id(self,uid):
    self._id = uid
    
  def get_id(self):
    return self._id
    
  def import_data(self):
    
    # open db connection
    con = sql.connect('darts.db')
    cur = con.cursor()
    
    # get name
    cur.execute("SELECT Name FROM Players WHERE Id=?",(self._id,))
    data = cur.fetchone()
    self._name = data[0]
    
    # compute average
    cur.execute("SELECT Score FROM GameScores WHERE PlayerID=?",(self._id,))
    data = cur.fetchall()
    if len(data)==0:
      self._average = 0
    else:
      total = 0
      for pt in data:
        total += pt[0]
      self._average = float(total)/len(data)
    
    # get games played
    cur.execute("SELECT GameId FROM GamePlayers WHERE PlayerID=?",(self._id,))
    data = cur.fetchall()
    self._games_played = len(data)
    
    # compute fraction over XX
    cur.execute("SELECT Score FROM GameScores WHERE PlayerID=?",(self._id,))
    data = cur.fetchall()
    if len(data)==0:
      self._over_60 = 0
      self._over_100 = 0
    else:
      num60 = 0
      num100 = 0
      for pt in data:
        if pt[0]>=60:
          num60 += 1
        if pt[0]>=100:
          num100 +=1
      self._over_60 = float(num60)/len(data)    
      self._over_100 = float(num100)/len(data)    
      
    # compute win fraction
    cur.execute("SELECT Id FROM Games WHERE WinnerID=?",(self._id,))
    data = cur.fetchall()
    if (self._games_played == 0):
      self._win_frac = 0
    else:
      self._win_frac = float(len(data))/self._games_played
    
    # close connection
    con.close()
    
  def export_data(self):
    con = sql.connect('darts.db')
    with con:
      cur = con.cursor()
      cur.execute("INSERT INTO Players(Name) VALUES(?)",(self._name,))
    con.close()
    
  def get_average(self):
    return self._average


  def set_name(self,name):
    self._name = name
    
  def get_name(self):
    return self._name

  def display_player_info(self):
    print self._name
    print "  Games played: ", self._games_played
    print "  Win fraction: ", self._win_frac
    print "  Average: ", self._average
    print "  Fraction over 60: ", self._over_60
    print "  Fraction over 100: ", self._over_100
