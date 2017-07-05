import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content=-Type'] = 'text/html'
		self.response.write('<title>cdaotg</title>')
		self.response.write('<body><h1>Please input two words</h1>')
		self.response.write('<form>')
		self.response.write('<h3 style="color:cornflowerblue;">input 1 : <input type ="text" name="a"></h3>')
		self.response.write('<h3 style="color:orange;">input 2 : <input type ="text" name="b"></h3>')
		self.response.write('<input type = submit></form><br>')

		len_a = len(self.request.get("a"))
		len_b = len(self.request.get("b"))
		a = self.request.get("a")
		b = self.request.get("b")
		
		self.response.write('<h2>Output: ')
		if len_a == len_b:
			for i in range(len_a):
				self.response.write('<b style="color:cornflowerblue;">%s</b><b style="color:orange;">%s</b>' % (a[i],b[i]))
		elif len_a < len_b:
			for i in range(len_a):
				self.response.write('<b style="color:cornflowerblue;">%s</b><b style="color:orange;">%s</b>' % (a[i],b[i]))
			self.response.write('<b style="color:orange;">%s</b>' % b[len_a:len_b])
		else:
			for i in range(len_b):
				self.range.write('<b style="color:cornflowerblue;">%s</b><b style="color:orange;">%s</b>' % (a[i],b[i]))
			self.response.write('<b style="color:cornflowerblue;">%s</b>' % a[len_b:len_a])
		self.response.write('</h2></body>')


app = webapp2.WSGIApplication([
	('/', MainPage),
], debug = True)