import os
import requests
import datetime

API_KEY = os.getenv('API_KEY')
ENDPOINT_TRANS = "https://api.assemblyai.com/v2/transcript"
HEADERS = {
    "authorization": API_KEY,
    "content-type": "application/json"
}

def url_transcript(url: str):
	json = {
		"audio_url": url
	}
	response = requests.post(ENDPOINT_TRANS, json=json, headers=HEADERS)
	request_id = response['id']
	request_status = response['status']
	print(response.json())
	while(request_status != 'completed'):
		response = requests.get(endpoint+"/{request_id}", headers=HEADERS)
		request_status = response['status']
		print(datetime.datetime.ctime(), request_status)
	print(response.json())