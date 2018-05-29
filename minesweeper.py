import math
import random

class Board():
  def __init__(self, columns=5, rows=5, bombPercentage=20):
    self.numBombs = math.floor(bombPercentage / 100 * columns * rows)
    self.numFlags = 0
    self.board = self.makeBoard(rows, columns, 0)
    self.placeBombs()
    self.view = self.makeBoard(rows, columns, ' ')
    self.play()

  def play(self):
    playing = True
    while playing:
      playing = False
      coordinates = self.selectSpace('check')
      while coordinates:
        playing = True
        if not self.checkSpace(coordinates):
          self.render(self.board)
          print('Oops! You lose.')
          return;
        self.render(self.view)
        coordinates = self.selectSpace('check')
      coordinates = self.selectSpace('flag')
      while coordinates:
        playing = True
        self.flagSpace(coordinates)
        self.render(self.view)
        if self.numFlags == self.numBombs and self.checkWinner():
          self.render(self.board)
          print('You win!')
          return
        coordinates = self.selectSpace('flag')
    keepPlaying = input('Keep playing? ')
    if keepPlaying.lower() == 'no' or len(keepPlaying) == 0:
      return;
    self.play()

  def checkWinner(self):
    for x, col in enumerate(self.board):
      for y, row in enumerate(col):
        if self.board[x][y] == 'B':
          if self.view[x][y] != 'B':
            return False
    return True

  def flagSpace(self, coordinates):
    if self.view[coordinates[0]][coordinates[1]] == ' ':
      self.view[coordinates[0]][coordinates[1]] = 'B'
      self.numFlags += 1

  def checkSpace(self, coordinates):
    if self.board[coordinates[0]][coordinates[1]] == 'B':
      return False

    visited = {}
    
    def iterate(coordinates):
      if str(coordinates) in visited.keys():
        return;
      visited[str(coordinates)] = True
      if self.board[coordinates[0]][coordinates[1]] == 0: 
        self.view[coordinates[0]][coordinates[1]] = '-'
        for dx in range(-1, 2):
          if coordinates[0] + dx >= 0 and coordinates[0] + dx < len(self.board):
            for dy in range(-1, 2):
              if coordinates[1] + dy >= 0 and coordinates[1] + dy < len(self.board[0]):
                iterate([coordinates[0] + dx, coordinates[1] + dy])
      elif self.board[coordinates[0]][coordinates[1]] != 'B':
        self.view[coordinates[0]][coordinates[1]] = self.board[coordinates[0]][coordinates[1]]

    iterate(coordinates)
    return True

  def selectSpace(self, action):
    coordinates = input('Enter row,column to ' + action + ': ').split(",")
    if len(coordinates) == 2:
      return list(map(lambda x: int(x), coordinates))

  def placeBombs(self):
    coordinates = []
    for row in range(len(self.board[0])):
      for column in range(len(self.board)):
        coordinates.append([row, column])
    for _ in range(self.numBombs):
      index = random.randint(0, len(coordinates) - 1)
      bombCoordinates = coordinates[index]
      coordinates = coordinates[:index] + coordinates[index + 1:]
      self.board[bombCoordinates[1]][bombCoordinates[0]] = 'B'
      for dx in range(-1, 2):
        for dy in range(-1, 2):
          x = bombCoordinates[1] + dx
          y = bombCoordinates[0] + dy
          if x >= 0 and x < len(self.board) and y >= 0 and y < len(self.board[0]):
            val = self.board[x][y]
            if val != 'B' and val >= 0:
              self.board[x][y] += 1

  def makeBoard(self, rows, columns, char):
    board = []
    for column in range(columns):
      board.append([])
      for row in range(rows):
        board[column].append(char)
    return board
  
  def render(self, board):
    for row in range(len(board[0])):
      renderRow = []
      for column in range(len(board)):
        renderRow.append(str(board[column][row]))
      print('|'.join(renderRow))
