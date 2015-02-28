"""
derriere.py - Scraper for downloading manga from Pururin

RIP Puro
You will be missed
fag <3

By Project Purity
This file is licensed under the MIT license
"""

import os
import sys
import time
import urllib2
import BeautifulSoup as bs
import requests
import gzip

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

print 'Starting scraper...'

def read(url, out_folder, total):
  num = 1
  while True:
    url = (url + '_' + str(num) + '.html')
    print url
    if num <= total:
      num = num + 1
    else:
      print "Finished. Perv."
      break
    main(url, out_folder)


def main(url, out_folder):
  request = urllib2.Request(url, headers=hdr)
  remotefile = urllib2.urlopen(request)
  data = remotefile.read()
  soup = bs.BeautifulSoup(data)
  for img in soup.findAll("img"):
    if url[:-4] in img['src']:
      url = 'http://pururin.com' + image['src']
      dlimage = requests.get(url)
    imgloc = ('http://pururin.com' + img["src"])
    print imgloc
    DownloadFile(imgloc, out_folder, img["src"])



def DownloadFile(url, out_folder, imagesource):
  '''Downloads a file from the specified url to the local system.

  Keyword arguments:
  url -- the remote url to the resource to download
  out_folder -- the local path to save the downloaded resource 
  '''
  global hdr
  request = urllib2.Request(url, headers=hdr)
  remotefile = urllib2.urlopen(request)
  # Get the filename from the content-disposition header

  # use RegEx to slice out the part we want (filename)
  filename = imagesource.split("/")[-1]
  filepath = os.path.join(out_folder, filename)
  if (os.path.exists(filepath)):
    return

  data = remotefile.read()
  if remotefile.info().get('content-encoding') == 'gzip':
    data = zlib.decompress(data, zlib.MAX_WBITS + 16)
    print 'File is gzip-encoded'

  with open(filepath, "wb") as code:
    code.write(data) # this is resulting in a corrupted file



if __name__ == "__main__":
  print 'Processing input...'
  url = sys.argv[-2]
  total = sys.argv[-1]
  print sys.argv
  out_folder = '/test/'
  read(url, out_folder, total)

