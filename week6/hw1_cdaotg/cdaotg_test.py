import cdaotg
import webtest

def test_get():
	app = webtest.TestApp(cdaotg.app)

	response1 = app.get('\pata?a=cat&b=dog')
	
	assert response1.status_int == 200
	assert response1.content_type == 'text/html'
	assert response1.body.contains('cdaotg')