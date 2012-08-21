from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import os

RAW_DROPBOX_ROOT = settings.RAW_DROPBOX_ROOT
RAW_STATICXML_ROOT = settings.RAW_STATICXML_ROOT
RAW_HEARTBEAT_ROOT = settings.RAW_HEARTBEAT_ROOT

"""
curl -F "manifest=@file_path;" http://127.0.0.1:8080/heartbeat/MEID/

manifest - nameinpost 
"""
@csrf_exempt
def heartbeat(request, meid):

	path = os.path.join(RAW_HEARTBEAT_ROOT, 'manifest', meid)
	manifest_name = os.path.join(path, str(datetime.now())+'.xml')
	if not os.path.isdir(path):
		os.mkdir(path)
		
	filehandle = open(manifest_name, 'wb+')
        
        #
        # stevko: receive a hearbeat not as a file but as a POST parameter
        #
        #for chunk in request.FILES['manifest'].chunks():
	#	#write it out
	#	filehandle.write(chunk)
        filehandle.write(request.POST['heartbeat'])

	#close filehandle
	filehandle.close()

        #return HttpResponseRedirect("/")
        return HttpResponse()
		


