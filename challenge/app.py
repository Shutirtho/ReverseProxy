#!flask/bin/python
from flask import Flask, render_template
import requests
import time
from xml.etree import ElementTree as ET


app = Flask(__name__)


STATS = [ 
          
          {"slow_requests": [ {"/listroutes/<string:tag>" : 0 } , {"/listroutes" : 0 }  ] },

           {"queries": [ {"/listroutes/<string:tag>" : 0 } , {"/listroutes" : 0 }  ]  } , 

          ] 


@app.route('/')
def index():
    r return redirect("http://localhost:9999/stats", code=302)


@app.route('/stats')
def stats():
    return render_template('stats.html', stats=STATS) 



@app.route('/listroutes/<string:tag>') 
@app.route('/listroutes')
def listRoutes(tag=None):
    if tag is not None:
        start = time.time()
        root = ET.fromstring(requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r="+tag).content)
        roundtrip = time.time() - start
        print roundtrip

        if STATS[0]["slow_requests"][0]["/listroutes/<string:tag>"] < roundtrip:
            STATS[0]["slow_requests"][0]["/listroutes/<string:tag>"] = roundtrip 

        STATS[1]["queries"][0]["/listroutes/<string:tag>"] += 1 
        stop_list = []
        for route in root.findall('route'):
            for stop in route.findall('stop'):
                stop_list.append(stop.get('title'))
            return render_template('stops.html', stop_list=stop_list)    

    else:
        start = time.time()
        root = ET.fromstring(requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni").content)
        roundtrip = time.time() - start
        print roundtrip

        if STATS[0]["slow_requests"][1]["/listroutes"] < roundtrip:
            STATS[0]["slow_requests"][1]["/listroutes"] = roundtrip

        STATS[1]["queries"][1]["/listroutes"] += 1

        route_list = {}
        for child in root:
            route_list.update({child.attrib['title']:child.attrib['tag']})
        return render_template('base.html', route_list=route_list)
  



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 9999)

