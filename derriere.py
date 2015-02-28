"""
derriere.py - Scraper for downloading weeb pr0n from Pururin

RIP Puro
You will be missed
fag <3

By Project Purity <projectpurity@kittymail.com>
This file is licensed under the MIT license
"""

import os #For joining paths
import time #For sleeping
import sys #For exiting
import urllib2 #Net stuff
import BeautifulSoup as bs #Net stuff
import gzip #For decoding Puro's sloppy shit (figure of speech)

hdr = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}

def read(url, out_folder, total):
  num = 1
  while True:
    time.sleep(1)
    if num > 99:
      url = url[:-8] + str(num) + ".html"
    elif num > 9:
      url = url[:-7] + str(num) + ".html"
    else:
      url = url[:-6] + str(num) + ".html"
    print url
    if num <= total:
      num = num + 1
      print "next page"
    else:
      print "Finished. Perv."
      sys.exit()
    main(url, out_folder)


def main(url, out_folder):
  request = urllib2.Request(url, headers=hdr)
  remotefile = urllib2.urlopen(request)
  data = remotefile.read()
  soup = bs.BeautifulSoup(data)
  for img in soup.findAll("img"):
    imgloc = ("http://pururin.com" + img["src"])
    print imgloc
    if not "header" in img["src"]:
      DownloadFile(imgloc, out_folder, img["src"])



def DownloadFile(url, out_folder, imagesource):
  """Downloads a file from the specified url to the local system.

  Keyword arguments:
  url -- the remote url to the resource to download
  out_folder -- the local path to save the downloaded resource 
  """
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
  print filepath
  if remotefile.info().get("content-encoding") == "gzip":
    data = zlib.decompress(data, zlib.MAX_WBITS + 16)
    print "File is gzip-encoded"
  
  code = open(filename, "wb")
  code.write(data)

  #with open(filepath, "wb") as code:
    #code.write(data) # this is resulting in a corrupted file



if __name__ == "__main__":
  """Syntax: python derriere.py <url of first page> <number of pages>"""
  print "Starting scraper..."
  
  try:
    sys.argv[-3] #Make sure the user read the fucking manual
  except:
    print "RTFM"
    sys.exit() #*sigh*
  
  url = sys.argv[-2]
  total = sys.argv[-1]
  print sys.argv
  out_folder = "test/"
  read(url, out_folder, total)

