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
	('/', MainPage),
	('/guidance', RoutePlanner)
], debug = True)