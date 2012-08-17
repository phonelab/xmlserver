from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import os

RAW_DROPBOX_ROOT = settings.RAW_DROPBOX_ROOT
RAW_STATICXML_ROOT = settings.RAW_STATICXML_ROOT

def push_manifest(requset):
  pass

def download_manifest(request, meid):
  paths = [os.path.join(RAW_DROPBOX_ROOT, meid, 'manifest.xml'), 
          os.path.join(RAW_STATICXML_ROOT, meid, 'manifest.xml'),
          os.path.join(RAW_STATICXML_ROOT, 'default', 'manifest.xml')]
  for path in paths:
    if os.path.isfile(path):
      return HttpResponse(
               open(path).read(), 
               content_type="application/xml"
             )
