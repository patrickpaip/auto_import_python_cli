
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Rest API Creation CLI')
parser.add_argument('-version', action='store', dest='version',
                    help='Select the version of API',default=1)
parser.add_argument('-endpoint', action='store', dest='endpoint',
                    help='Select the URL Endpoint')
parser.add_argument('-name', action='store', dest='name',
                    help='Select the Folder Name and ClassName')
result=parser.parse_args()


if(result.endpoint==None or result.name==None):
	print ("Missing Parameters, Type -h to know more")
	sys.exit(1)

template_target_class="""
import route_register
from validation_decorator import decorator_4xx
from access_permit_decorators import access_permit
from commit_interface import commit

@route_register.register('{}',version={})
class {}:
    def __init__(self):
        self.res = {{
            "res_dict" : None,
            "res_str": "Data Received Succesfully",
            "res_code": "200"
        }}
        self.commit_obj=commit('')

    def get(self,uri_ctx):
        pass
    def post(self,uri_ctx):
        pass
    def put(self,uri_ctx):
        pass
    def delete(self,uri_ctx):
        pass
"""

def createAPI(name,endpoint,version):
	content=template_target_class.format(endpoint,version,name)
	os.mkdir(name.lower())
	with open("{}/__init__.py".format(name.lower()),"w") as file:
		file.write("")
	with open("{}/{}.py".format(name.lower(),name.lower()),"w") as file:
		file.write(content)

createAPI(''.join(x for x in result.name.title() if not x.isspace()),result.endpoint,result.version)