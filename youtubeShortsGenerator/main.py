from flask import Flask, jsonify, request
from flask_cors import CORS
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from flask import send_from_directory

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')  

@app.route('/invokeGetChannelId', methods=['GET'])
def invokeGetChannelId():
    channelLink = request.args.get('channelLink', default=1, type=str)
    result = getChannelId(channelLink)
    return jsonify({'result': result})

def getChannelId(channelLink):
    s = Service(executable_path="chromedriver.exe")

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('headless')

    driver = webdriver.Chrome(service=s, options=chromeOptions)


    driver.get(channelLink)
    time.sleep(1)
    print("starting driver")
    htmlSource = driver.page_source
    htmlSourceSplit = htmlSource.split("?channel_id=", 1)
    channelIdSplit = htmlSourceSplit[1].split('"', 1)
    channelId = channelIdSplit[0]
    print(channelId)
    return channelId

if __name__ == '__main__':
    app.run(debug=True, port=5500)