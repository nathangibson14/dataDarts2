#!/usr/bin/python

import sqlite3 as sql
import sys
import os

try:
  os.remove("darts.db")
except:
  pass
  
try:
    con = sql.connect('darts.db')
    with con:
    
      # Build tables
      cur = con.cursor()    
      cur.execute("CREATE TABLE Players(Id INTEGER PRIMARY KEY, "
                  "Name TEXT)")
      cur.execute("CREATE TABLE Games(Id INTEGER PRIMARY KEY, "
                  "Type TEXT, Time TEXT, WinnerId INT)")
      cur.execute("CREATE TABLE GamePlayers(GameId INT, PlayerId INT)")
      cur.execute("CREATE TABLE GameScores(GameID INT, Round INT, PlayerID INT, "
                  "ScoreBefore INT, Score INT)")
      
      # Populate Players table
      cur.execute("INSERT INTO Players(Name) VALUES('Bob')")
      cur.execute("INSERT INTO Players(Name) VALUES('Nathan')")
      
      # Populate game information
      cur.execute("INSERT INTO Games(Type,Time,WinnerId) "
                  "VALUES('501','07/31/2015 PM 05:03',1)")
      cur.execute("INSERT INTO GamePlayers VALUES(1,1)")
      cur.execute("INSERT INTO GamePlayers VALUES(1,2)")
      cur.execute("INSERT INTO GameScores VALUES(1,1,1,501,180)")
      cur.execute("INSERT INTO GameScores VALUES(1,2,2,501,100)")
      cur.execute("INSERT INTO GameScores VALUES(1,3,1,321,180)")
      cur.execute("INSERT INTO GameScores VALUES(1,4,2,401,60)")
      cur.execute("INSERT INTO GameScores VALUES(1,5,1,141,141)")
    
except sql.Error, e:
  print "Error %s:" % e.args[0]
  sys.exit(1)
    
finally:
  if con:
    con.close()



