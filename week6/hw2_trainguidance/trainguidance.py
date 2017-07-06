import webapp2
import json
import urllib2

url = 'http://fantasy-transit.appspot.com/net?format=json'
data = json.load(urllib2.urlopen(url))

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Train Guidance</title>')
		self.response.write('<body><form action="/search-result"><h1>Train Guidance: Tokyo</h1>')
		self.response.write('<h3>From : <select name="from">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3>')

		self.response.write('<h3>To : <select name="to">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3><input type="submit" value="  Search Route  "></form>')

		self.response.write('<h3>Alternate worlds:</h3><ul>')
		self.response.write('<li><a href="../">Tokyo</a></li>')
		self.response.write('<li><a href="../alice">Alice in Wonderland</a></li>')
		self.response.write('<li><a href="../nausicaa">Nausicaa of the Valley of the wind</a></li>')
		self.response.write('<li><a href="../lotr">Middle Earth (Lord of the Rings)</a></li>')
		self.response.write('<li><a href="../pokemon">Pokemon: Kanto Region</a></li>')

		self.response.write('</ul></body>')

class AliceMainPage(webapp2.RequestHandler):
	def get(self):
		global url
		url = 'http://alice.fantasy-transit.appspot.com/net?format=json'
		global data
		data = json.load(urllib2.urlopen(url))
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Train Guidance: Alice in Wonderland</title>')
		self.response.write('<body><form action="../search-result"><h1>Train Guidance: Alice in Wonderland</h1>')
		self.response.write('<h3>From : <select name="from">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3>')

		self.response.write('<h3>To : <select name="to">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3><input type="submit" value="  Search Route  "></form>')

		self.response.write('<h3>Alternate worlds:</h3><ul>')
		self.response.write('<li><a href="../">Tokyo</a></li>')
		self.response.write('<li><a href="../alice">Alice in Wonderland</a></li>')
		self.response.write('<li><a href="../nausicaa">Nausicaa of the Valley of the wind</a></li>')
		self.response.write('<li><a href="../lotr">Middle Earth (Lord of the Rings)</a></li>')
		self.response.write('<li><a href="../pokemon">Pokemon: Kanto Region</a></li>')

		self.response.write('</ul></body>')

class NausicaaMainPage(webapp2.RequestHandler):
	def get(self):
		global url
		url = 'http://nausicaa.fantasy-transit.appspot.com/net?format=json'
		global data
		data = json.load(urllib2.urlopen(url))
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Train Guidance: Nausicaa</title>')
		self.response.write('<body><form action="../search-result"><h1>Train Guidance: Nausicaa</h1>')
		self.response.write('<h3>From : <select name="from">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3>')

		self.response.write('<h3>To : <select name="to">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3><input type="submit" value="  Search Route  "></form>')

		self.response.write('<h3>Alternate worlds:</h3><ul>')
		self.response.write('<li><a href="../">Tokyo</a></li>')
		self.response.write('<li><a href="../alice">Alice in Wonderland</a></li>')
		self.response.write('<li><a href="../nausicaa">Nausicaa of the Valley of the wind</a></li>')
		self.response.write('<li><a href="../lotr">Middle Earth (Lord of the Rings)</a></li>')
		self.response.write('<li><a href="../pokemon">Pokemon: Kanto Region</a></li>')

		self.response.write('</ul></body>')

class LotrMainPage(webapp2.RequestHandler):
	def get(self):
		global url
		url = 'http://lotr.fantasy-transit.appspot.com/net?format=json'
		global data
		data = json.load(urllib2.urlopen(url))
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Train Guidance: Middle Earth</title>')
		self.response.write('<body><form action="../search-result"><h1>Train Guidance: Middle Earth (Lord of the Rings)</h1>')
		self.response.write('<h3>From : <select name="from">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3>')

		self.response.write('<h3>To : <select name="to">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3><input type="submit" value="  Search Route  "></form>')

		self.response.write('<h3>Alternate worlds:</h3><ul>')
		self.response.write('<li><a href="../">Tokyo</a></li>')
		self.response.write('<li><a href="../alice">Alice in Wonderland</a></li>')
		self.response.write('<li><a href="../nausicaa">Nausicaa of the Valley of the wind</a></li>')
		self.response.write('<li><a href="../lotr">Middle Earth (Lord of the Rings)</a></li>')
		self.response.write('<li><a href="../pokemon">Pokemon: Kanto Region</a></li>')

		self.response.write('</ul></body>')

class PokemonMainPage(webapp2.RequestHandler):
	def get(self):
		global url
		url = 'http://pokemon.fantasy-transit.appspot.com/net?format=json'
		global data
		data = json.load(urllib2.urlopen(url))
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Train Guidance: Pokemon</title>')
		self.response.write('<body><form action="../search-result"><h1>Train Guidance: Pokemon: Kanto Region</h1>')
		self.response.write('<h3>From : <select name="from">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3>')

		self.response.write('<h3>To : <select name="to">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select></h3><input type="submit" value="  Search Route  "></form>')

		self.response.write('<h3>Alternate worlds:</h3><ul>')
		self.response.write('<li><a href="../">Tokyo</a></li>')
		self.response.write('<li><a href="../alice">Alice in Wonderland</a></li>')
		self.response.write('<li><a href="../nausicaa">Nausicaa of the Valley of the wind</a></li>')
		self.response.write('<li><a href="../lotr">Middle Earth (Lord of the Rings)</a></li>')
		self.response.write('<li><a href="../pokemon">Pokemon: Kanto Region</a></li>')

		self.response.write('</ul></body>')


class RoutePlanner(webapp2.RequestHandler):
	def get_line(self, target): # get the line of target station
		line = set([])
		for dictionary in data:
			for station in dictionary['Stations']:
				# build set of station and line
				if station == target:
					line.add(dictionary['Name'])
		return line

	def get_whole_line(self, line): # get the whole dictionary of the line
		for dictionary in data:
			if dictionary['Name'] == line:
				return dictionary

	def get_index(self, target, list):
		for index in range(len(list)):
			if list[index] == target:
				return index

	def get_station_num(self, line):
		return len(self.get_whole_line(line)['Stations'])

	def check_same_line(self, start, end): # check if the two stations are in the same line
		start_line = self.get_line(start)
		end_line = self.get_line(end)
		for line in start_line:
			if line in end_line:
				return True
		return False

	def check_in_line(self, current_lines, target): # check if the station is in current lines
		for line in current_lines:
			if target in self.get_whole_line(line)['Stations']:
				return True
		return False

	def get_intersection_station(self, a, b):
		line_a = set()
		line_b = set()
		for station in self.get_whole_line(a)['Stations']:
			line_a.add(station)
		for station in self.get_whole_line(b)['Stations']:
			line_b.add(station)
		intersection_station = [i for i in (line_a & line_b)]
		return intersection_station

	def transferable_line(self, line): # return set of lines can be transferred through the given line
		line_set = set()
		for station in self.get_whole_line(line)['Stations']:
			for line in self.get_line(station):
				line_set.add(line)
		return line_set

	def transfer_line(self, start, end): # return a list of lines have to transfer
		current_lines = self.get_line(start)
		end_lines = self.get_line(end)
		count = 0
		route_line = []
		trans_line = []

		while not self.check_in_line(current_lines, end):
			route_line.append(current_lines)
			next_lines = set()
			for line in current_lines:
				next_lines |= self.transferable_line(line)
			current_lines = next_lines
			count += 1

		last_line = ''
		for line in (end_lines & current_lines): # initialize
			last_line = line
		trans_line.append(last_line)

		for line_set in route_line[::-1]:
			for line in (line_set & self.transferable_line(last_line)):
				last_line = line
			trans_line.append(line)

		trans_line.reverse()
		if count != 0:
			self.response.write('<br><hr>Need to transfer %d time(s).' %count)

		return trans_line

	def plan(self, start, end):
		next_line = self.transfer_line(start, end)
		route = []
		transfer_station = {}

		for index in range(1, len(next_line)):
			transfer = self.get_intersection_station(next_line[index-1], next_line[index])
			transfer_station[(next_line[index-1], next_line[index])] = transfer
			route.append(transfer[0])
		if len(transfer_station) != 0:
			self.response.write('<br>Transfer Stations(s): ')
			for station in route:
				self.response.write('<b style="color:chocolate"> %s </b>'% station)
				if station != route[len(route)-1]:
					self.response.write('and')
			self.response.write('<hr><br>')

			route.insert(0, start)
			route.append(end)
			for i in range(0, len(route)-1):
				if i != 0:
					self.response.write('<br><b style="color:orange">Tranfer to >> </b>')
				self.print_route(route[i], route[i+1])

	def print_route(self, start, end):
		intersection_line = (self.get_line(start) & self.get_line(end))
		if len(intersection_line) > 1:
				self.response.write('There are %d ways to go to <b>%s</b>:<br>' % (len(intersection_line), end))

		for line in intersection_line:
			self.response.write('<b style="color:orange">[ %s: ' % self.get_whole_line(line)['Name'])
			start_index = self.get_index(start, self.get_whole_line(line)['Stations'])
			end_index = self.get_index(end, self.get_whole_line(line)['Stations'])
			if start_index < end_index:
				if (end_index-start_index) > (self.get_station_num(line)/2):
					route = self.get_whole_line(line)['Stations'][end_index:]
					for i in range(1, start_index+1):
						route.append(self.get_whole_line(line)['Stations'][i])
					route.reverse()
					self.response.write('up ]')
				else: 
					route = self.get_whole_line(line)['Stations'][start_index:end_index+1]
					self.response.write('down ]')
			else:
				if (start_index-end_index) > (self.get_station_num(line)/2):
					route = self.get_whole_line(line)['Stations'][start_index:]
					for i in range(1, end_index+1):
						route.append(self.get_whole_line(line)['Stations'][i])
					self.response.write('down ]')
				else:
					route = self.get_whole_line(line)['Stations'][end_index:start_index+1]
					route.reverse()
					self.response.write('up ]')

			self.response.write('</b><br>')
			for station in route:
				if station == route[0] or station == route[len(route)-1]:
					self.response.write('>> <b style="color:cornflowerblue">%s</b>' % station)
				else:
					self.response.write('>> %s' % station)
			self.response.write('<br>')

	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Search Result</title>')
		self.response.write('<body><h1>Search Result</h1>')
		start = self.request.get("from")
		end = self.request.get("to")

		self.response.write('<b>From: </b><b style="color:cornflowerblue">%s</b><br>' % start)
		self.response.write('<b>To: </b><b style="color:cornflowerblue">%s</b><br>' % end)
		if self.check_same_line(start, end):
			self.response.write('<br><hr><b>No need to transfer.</b><hr><br>')
			self.print_route(start, end)
		else:
			self.plan(start, end)

		self.response.write('<br><br><form action="../"><input type="submit" value=" Reset "></form>')
		self.response.write('</body>')		


app = webapp2.WSGIApplication([
	('/', MainPage),
	('/alice',AliceMainPage),
	('/nausicaa',NausicaaMainPage),
	('/lotr',LotrMainPage),
	('/pokemon',PokemonMainPage),
	('/search-result', RoutePlanner)
], debug = True)