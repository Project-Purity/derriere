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

def read(url, out_folder):
  num = 1
  main(url, out_folder)
  while True:
    #time.sleep(1)
    request = urllib2.Request(url, headers=hdr)
    remotefile = urllib2.urlopen(request)
    data = remotefile.read()
    soup = bs.BeautifulSoup(data)
    for elink in soup.findAll("a"): #Here's inefficient code, but it wasn't even Purr*
      for thing in elink.attrs:
        if "class" in thing:
          if elink["class"] == "image-next":
            if "finish" not in elink["href"]:
              url = "http://pururin.com" + elink["href"]
              main(url, out_folder)
            else:
              print "Done!"
              sys.exit()


def main(url, out_folder):
  request = urllib2.Request(url, headers=hdr)
  remotefile = urllib2.urlopen(request)
  data = remotefile.read()
  soup = bs.BeautifulSoup(data)
  for img in soup.findAll("img"):
    imgloc = ("http://pururin.com" + img["src"])
    if not "header" in img["src"]:
      downloadFile(imgloc, out_folder, img["src"])


def downloadFile(url, out_folder, imagesource):
  global hdr
  request = urllib2.Request(url, headers=hdr)
  remotefile = urllib2.urlopen(request)

  filename = imagesource.split("/")[-1]

  filepath = os.path.join(out_folder, filename)
  if not (os.path.exists(out_folder)):
    os.makedirs(out_folder)

  data = remotefile.read()
  print url
  if remotefile.info().get("content-encoding") == "gzip":
    data = zlib.decompress(data, zlib.MAX_WBITS + 16)
    print "File is gzip-encoded"

  with open(filepath, "wb") as code:
    code.write(data)



if __name__ == "__main__":
  """Syntax: python derriere.py <url of first page>"""
  print "Starting scraper..."

  try:
    sys.argv[-2] #Make sure the user read the fucking manual
  except:
    print "Please enter the url of the first page of the doujin:"
    url = raw_input()
  else:
    url = sys.argv[-1]

  out_folder = "dl"
  read(url, out_folder)

#*jk bae u kno i luv u
