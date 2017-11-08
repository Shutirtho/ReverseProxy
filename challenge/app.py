from flask import Flask, render_template, redirect
import requests
import time
from xml.etree import ElementTree as ET


app = Flask(__name__)

#used to store data for slowest request to an endpoint and number of queries to an endpoint 
STATS = [ 
          
          {"slow_requests": [ {"/listroutes/<string:tag>" : 0 } , {"/listroutes" : 0 }  ] },

           {"queries": [ {"/listroutes/<string:tag>" : 0 } , {"/listroutes" : 0 }  ]  } , 

          ] 


@app.route('/')
def index():
    return redirect("http://localhost:9999/stats", code=302)


@app.route('/stats')
def stats():
    return render_template('stats.html', stats=STATS) 



@app.route('/listroutes/<string:tag>') 
@app.route('/listroutes')
def listRoutes(tag=None): # use nextbus's "routeConfig" command to get list of stops for a route
    if tag is not None:
        start = time.time()
        root = ET.fromstring(requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r="+tag).content)
        roundtrip = time.time() - start # get response time for endpoint /listroutes/<string:tag>'
        

        if roundtrip > 0.02:
            STATS[0]["slow_requests"][0]["/listroutes/<string:tag>"] = roundtrip # update with response time greater than 0.02s

        STATS[1]["queries"][0]["/listroutes/<string:tag>"] += 1 
        stop_list = []
        for route in root.findall('route'):
            for stop in route.findall('stop'):
                stop_list.append(stop.get('title'))
            return render_template('stops.html', stop_list=stop_list)    

    else: # use nextbus's "routeList" command to get list of routes for sf-muni
        start = time.time()
        root = ET.fromstring(requests.get("http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni").content)
        roundtrip = time.time() - start # get response time for endpoint /listroutes

        if roundtrip > 0.02:
            STATS[0]["slow_requests"][1]["/listroutes"] = roundtrip # update with response time greater than 0.02s

        STATS[1]["queries"][1]["/listroutes"] += 1

        route_list = {}
        for child in root:
            route_list.update({child.attrib['title']:child.attrib['tag']})
        return render_template('base.html', route_list=route_list)
  



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 9999)

