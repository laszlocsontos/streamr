import json
import urllib2
import urlparse


class Vimeo:

  def __init__(self, master_url, master_json=None):
    self.master_url = urlparse.urlsplit(master_url)

    if master_json:
      self.master_data = json.loads(master_json)
    else:
      try:
        response = urllib2.urlopen(self.master_url.geturl())
        self.master_data = json.loads(response.read())
      finally:
        response.close()

    path = "/".join(self.master_url[2].split("/")[:-2])
    self.base_url = urlparse.urlunsplit((self.master_url[0], self.master_url[1], path, self.master_url[3], self.master_url[4]))

  def get_base_url(self):
    return self.base_url

  def get_clip_id(self):
    return self.master_data["clip_id"]

  def get_stream_count(self):
    return len(self.master_data["video"])

  def get_stream_url(self, video_id):
    video = self._get_video(video_id)
    return "/".join([self.get_base_url(), str(video["id"])]) if video else None

  def get_segment_count(self, video_id):
    video = self._get_video(video_id)
    return len(video["segments"]) if video else None

  def _get_video(self, video_id):
    return next((video for video in self.master_data["video"] if video["id"] == video_id), None)


def from_url(master_url):
    return Vimeo(master_url)


def from_json(master_url, master_json):
    return Vimeo(master_url, master_json)
