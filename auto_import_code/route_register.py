routes={}
import os

def registerDebug(routeString,version=1):
    def routeEncloser(func):
    	classPath=str(func)
    	classTokens=classPath.split(".")
    	className=classTokens[-1]
    	path=classTokens[0]+"/v"+str(version)+"/"
    	for x in classTokens[1:-2]:
            path+=x+"/"
        else:
        	path=path[:-1]
        routes[routeString]={
           "version" : version,
           "target" : func,
           "url" : path,
           "fileName": classTokens[-2],
           "className" : className
        }
        def executor(*args,**kwargs):
            return func(*args,**kwargs)
        return executor
    return routeEncloser

def register(route_string,version=1):
    def route_encloser(func):
    	classTokens=str(func).split(".")
    	className=classTokens[-1]
    	path=classTokens[0]+"/v"+str(version)+"/"
    	for x in classTokens[1:-2]:
            path+=x+"/"
        else:
        	path+=route_string
        if(path not in routes):
           routes[path]=func
        else:
           print ("[Warning] Route Registration Failed | Path: "+str(func)+" version:"+str(version))
        def executor(*args,**kwargs):
            return func(*args,**kwargs)
        return executor
    return route_encloser

# Map of Registration

# Registration Decorator