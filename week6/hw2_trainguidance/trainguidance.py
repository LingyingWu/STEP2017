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
		self.response.write('<body><form action="/guidance"><h1>Train Guidance</h1>')
		self.response.write('From :<select name="from">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select><br>')

		self.response.write('To :<select name="to">')
		for dictionary in data:
			self.response.write('<option disabled>-------------</option>')
			self.response.write('<option disabled>%s</option>' % dictionary['Name'])
			for station in dictionary['Stations']:
				self.response.write('<option>%s</option>' % station)
		self.response.write('</select><br><br><input type=submit value="  Search Route  ">')
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

	def get_whole_line(self, line): # get the information of the whole line
		for dictionary in data:
			if dictionary['Name'] == line:
				return dictionary

	def get_index(self, target, list):
		for index in range(len(list)):
			if list[index] == target:
				return index
"""
	def check_station(self, start, end): # check if the stations in the same line
		start_line = self.get_line(start)
		end_line = self.get_line(end)
		intersection_list = [str(stat) for stat in (start_line & end_line)]
		return intersection_list

	def check_line(self, current_line, end): # check if destination in current line
		for line in current_line:
			if end in current_line:
				return True
		return False

	def unknown(self, line):
		line_set = set()
		line_dict = self.get_whole_line(line)
		for station in line_dict['Stations']:
			for line in self.get_line(station):
				line_set.add(line)
		return line_set

	def get_intersection_station(self, a, b): # get a list of intersection station
		line_a = self.get_whole_line(a)
		line_b = self.get_whole_line(b)
		set_a = set()
		set_b = set()
		for station in line_a['Stations']:
			set_a.add(station)
		for station in line_b['Stations']:
			set_b.add(station)
		return [str(stat) for stat in (set_a & set_b)]


	def get_intersection_line(self, current): # get a set of intersection line
		current_line = self.get_whole_line(current)
		line_set = set()
		for station in current_line['Stations']:
			line_set |= self.get_line(station)
		return line_set
"""

	def print_result(self, start, end):
		intersection_line = (self.get_line(start) & self.get_line(end))
		self.response.write('<br><b>Depart from: </b><b style="color:orange">%s</b>' % start)
		self.print_route(start, end)
		self.response.write('<br><b>Arrive at: </b><b style="color:orange">%s</b>' % end)

	def print_route(self, start, end):
		intersection_line = (self.get_line(start) & self.get_line(end))
		for line in intersection_line:
			start_index = self.get_index(start, self.get_whole_line(line)['Stations'])
			end_index = self.get_index(end, self.get_whole_line(line)['Station'])
			if start_index < end_index:
				route = self.get_whole_line(line)['Stations'][start_index:end_index+1]
			else:
				route = self.get_whole_line(line)['Stations'][end_index:start_index+1]
				route.reverse()

			for station in route:
				line_string = '/'.join([str(i) for i in self.get_line(start)])
				self.response.write('>> [%s] %s<br>' % (line_string, station))

	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<title>Search Result</title>')
		self.response.write('<body><h1>Search Result</h1>')
		start = self.request.get("from")
		end = self.request.get("to")

		self.print_result(start, end)
		self.response.write('</body>')		


app = webapp2.WSGIApplication([
	('/', MainPage)
	('/search-result',RoutePlanner)
], debug = True)