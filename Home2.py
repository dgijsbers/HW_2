import requests
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/movie/<movie_name>')
def enter_movie(movie_name):
	base_url = "https://itunes.apple.com/search/"
	params = {} 
	params['media']='movie' 
	params['term'] = movie_name 
	params['limit'] = 10 
	response = requests.get(base_url, params)
	return response.text 