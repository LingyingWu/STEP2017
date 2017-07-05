import webapp2
import json
import urllib2

url = 'http://fantasy-transit.appspot.com/net?format=json'
data = json.load(urllib2.urlopen(url))

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		#file = open('input.html').read()
		#self.response.out.write(file)
		self.response.write('<title>Train Guidance</title>')
		self.response.write('<body><form action="/search-result"><h1>Train Guidance</h1>')
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
		self.response.write('</select></h3><input type=submit value="  Search Route  ">')
		self.response.write('</body>')


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
		n = len(self.get_whole_line(line)['Stations'])

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
		intersection_station = [str(i) for i in (line_a & line_b)]
		return intersection_station

	def transferable_line(self, line): # return set of lines can be transferred through the given line
		line_set = set()
		for station in self.get_whole_line(line)['Stations']:
			for line in self.get_line(station):
				line_set.add(line)
		return line_set

	def recommend_line(self, start, end): # return a list of recommend lines
		current_lines = self.get_line(start)
		end_lines = self.get_line(end)
		count = 0
		route_line = []
		rec_line = []

		while not self.check_in_line(current_lines, end):
			route_line.append(current_lines)
			next_lines = set()
			for line in current_lines:
				next_lines |= self.transferable_line(line)
			current_lines = next_lines
			count += 1

		for line in (end_lines & current_lines):
			rec_line.append(line)

		for line_set in route_line[::-1]:
			for line in (line_set & self.transferable_line(end_lines)):
				rec_line.append(line)

		candidate.reverse()
		if count != 0:
			self.response.write('<h4> Recommend to take </h4>')
			for line in rec_line:
				self.response.write('>> %s' % line)
			self.response.write('<h4> (transfer %d times)</h4><br>' % count)

		return candidate

	def plan(self, start, end):
		next_line = self.recommend_line(start, end)
		route = []
		transfer_station = {}

		for index in range(1, len(next_line)):
			transfer = self.get_intersection_station(next_line[index-1], next_line[index])
			transfer_candidate[(next_line[index-1], next_line[index])] = transfer
			route.append(transfer[0])
		if len(transfer_station) != 0:
			self.response.write('<h3>Need transfer: </h3>')
			for station in route:
				self.response.write('>> %s<br> '% station)

	def print_result(self, start, end):
		intersection_line = (self.get_line(start) & self.get_line(end))
		self.response.write('<br><b>From: </b><b style="color:cornflowerblue">%s</b><br><br>' % start)
		self.print_route(start, end)
		self.response.write('<br><b>To: </b><b style="color:cornflowerblue">%s</b>' % end)

	def print_route(self, start, end):
		intersection_line = (self.get_line(start) & self.get_line(end))
		for line in intersection_line:
			start_index = self.get_index(start, self.get_whole_line(line)['Stations'])
			end_index = self.get_index(end, self.get_whole_line(line)['Stations'])
			if start_index < end_index:
				if (end_index-start_index) > self.get_station_num(line):
					route = self.get_whole_line(line)['Stations'][end_index:]
					route.append(self.get_whole_line(line)['Stations'][1:start_index+1])
					route.reverse()
				else: 
					route = self.get_whole_line(line)['Stations'][start_index:end_index+1]
			else:
				route = self.get_whole_line(line)['Stations'][end_index:start_index+1]
				route.reverse()

			for station in route:
				self.response.write('>> %s<br>' % station)

	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Search Result</title>')
		self.response.write('<body><h1>Search Result</h1>')
		start = self.request.get("from")
		end = self.request.get("to")

		if self.check_same_line(start, end):
			self.print_result(start, end)
		else:
			self.plan(start, end)
		self.response.write('</body>')		


app = webapp2.WSGIApplication([
	('/', MainPage),
	('/search-result', RoutePlanner)
], debug = True)