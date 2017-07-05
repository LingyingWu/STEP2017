import cdaotg
import webtest

def test_get():
	app = webtest.TestApp(cdaotg.app)

	# test when same length
	response1 = app.get('\pata?a=123&b=456')
	assert response1.status_int == 200
	assert response1.content_type == 'text/html'
	assert response1.body.contains('123456')

	# test when a longer than b
	response2 = app.get('\pata?a=1234&b=56')
	assert response2.status_int == 200
	assert response2.content_type == 'text/html'
	assert response2.body.contains('152634')

	# test when a shorter than b
	response1 = app.get('\pata?a=12&b=3456')
	assert response1.status_int == 200
	assert response1.content_type == 'text/html'
	assert response1.body.contains('132456')