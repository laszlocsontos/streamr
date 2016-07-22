#!/usr/bin/env python

from streamr.vimeo import download_video
import sys


def main():
  if len(sys.argv) < 3:
    print "Usage: %s <master.json URL> <path to save>" % sys.argv[0]
    sys.exit(1)
  download_video(sys.argv[1], sys.argv[2])
  print "Completed: %s" % sys.argv[1]

if __name__ == "__main__":
    main()

