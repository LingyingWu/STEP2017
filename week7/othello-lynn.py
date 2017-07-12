# Reference: https://github.com/step17/hw7/blob/master/python/main.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import json
import logging
import random
import webapp2

# Read json description of the board and provides simple interface.

class Game:
	def __init__(self, body=None, board=None): # Take json or a board directly
		if body:
			game = json.loads(body)
			self._board = game["board"]
		else:
			self._board = board

	def position(self, x, y): # Return piece on the board
		# 0 for no pieces, 1 for player1, 2 for player2, None for coordicate out of scope
		return position(self._board["Pieces"], x, y)

	def next(self): # Return who plays next
		return self._board["Next"]

	def validMoves(self): # Return the array of valid moves for next player
		moves = []
		for y in xrange(1,9):
			for x in xrange(1,9):
				# Each move is a dict, "As": next player
				move = {"Where": [x,y], "As": self.next()}
				if self.nextBoardPosition(move):
					moves.append(move)
		return moves

	def _updateBoardDirection(self, newBoard, x, y, delta_x, delta_y): # Hepler function of nextBoardPosition.
		# It looks towards (delta_x, delta_y) direction for one of our own pieces
		# and flips pieces in between if the move is valid.
		# Return True if pieces are captured in this direction.
		player = self.next()
		opponent = 3 - player
		look_x = x + delta_x
		look_y = y + delta_y
		flip_list = []
		while position(newBoard, look_x, look_y) == opponent:
			flip_list.append([look_x, look_y])
			look_x += delta_x
			look_y += delta_y

		if position(newBoard, look_x, look_y) == player and len(flip_list) > 0:
			setPos(newBoard, x, y, player)
			for flip_move in flip_list:
				flip_x = flip_move[0]
				flip_y = flip_move[1]
				setPos(newBoard, flip_x, flip_y, player)
			return True
		return False

	def nextBoardPosition(self, move):
		x = move["Where"][0]
		y = move["Where"][1]
		if self.position(x, y) != 0: # the position already occupied
			return None

 		newBoard = copy.deepcopy(self._board)
		pieces = newBoard["Pieces"]

		if not (self._updateBoardDirection(pieces, x, y, 1, 0)
			or self._updateBoardDirection(pieces, x, y, 0, 1)
			or self._updateBoardDirection(pieces, x, y, -1, 0)
			or self._updateBoardDirection(pieces, x, y, 0, -1)
			or self._updateBoardDirection(pieces, x, y, 1, 1)
			or self._updateBoardDirection(pieces, x, y, -1, 1)
			or self._updateBoardDirection(pieces, x, y, 1, -1)
			or self._updateBoardDirection(pieces, x, y, -1, -1)):
			return None # Move is invalid

		newBoard["Next"] = 3 - self.next()
		return newBoard


def position(board, x, y):
	if x >= 1 and x <= 8 and y >= 1 and y <= 8:
		return board[y-1][x-1]
	return None

def setPos(board, x, y, piece): # Set piece on the board at (x,y) coordinate
	if x < 1 or x > 8 or y < 1 or y > 8 or piece not in [0,1,2]:
		return False
	board[y-1][x-1] = piece

def prettyPrint(board, nl="<br>"): # Debug function to pretty print the array representation of board.
	s = ""
	for row in board:
		for piece in row:
			s += str(piece)
		s += nl
	return s

def prettyMove(move):
	m = move["Where"]
	return '%s%d' % (chr(ord('A') + m[0]-1), m[1])


class MainHandler(webapp2.RequestHandler):
	# Handling GET request, just for debugging purposes.
    # If you open this handler directly, it will show you the HTML form here 
    # and let you copy-paste some game's JSON here for testing.
	def get(self):
		if not self.request.get('json'):
			self.response.write("""
				<body>
				<form method=get>Paste JSON here:<p/>
				<textarea name=json cols=80 rows=24></textarea>
				<p/><input type=submit>
				</form>
				</body>
			""")
			return
		else:
			g = Game(self.request.get('json'))
			self.pickMove(g)

	def post(self):
		g = Game(self.request.body)
		self.pickMove(g)

	def pickMove(self, g):
		valid_moves = g.validMoves() # Get all valid moves.
		if len(valid_moves) == 0:
			self.response.write("PASS")
		else:
			# move = random.choice(valid_moves) # pick randomly
			move = self.choose(g)
			self.response.write(prettyMove(move))

	def choose(self, g):
		player = {}
		for move in g.validMoves():
			nextBoard = g.nextBoardPosition(move)
			score = self.heuristicScore(nextBoard)
			player[score] = move

		best = max(player)
		return player[best]


	def heuristicScore(self, board):
		player = self.next()
		opponent = 3 - player
		player_score = 0
		opponent_score = 0
		for row in board:
			for piece in row:
				if piece == player:
					player_score += 1
				elif piece == opponent:
					opponent_score += 1
				else:
					continue
		return player_score

	def coinParity(self, board):
		player = self.next()
		opponent = 3 - player
		player_score = 0
		opponent_score = 0

		# Corner occupncy
		if board[0][0] == player:
			player_score++
		elif board[0][0] == opponent:
			opponent_score++
		if board[0][7] == player:
			player_score++
		elif board[0][7] == opponent:
			opponent_score++
		if board[7][0] == player:
			player_score++
		elif board[7][0] == opponent:
			opponent_score++
		if board[7][7] == player:
			player_score++
		elif board[7][7] == opponent:
			opponent_score++
		corner = 25 * (player_score - opponent_score)

		# Corner neighber
		mine = 0
		opponent = 0


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
