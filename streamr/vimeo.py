import json
import urllib2
import urlparse
from streamr import url

class Vimeo:

  def __init__(self, master_url, master_json=None):
    self.master_url = url.Url(master_url)

    if master_json:
      self.master_data = json.loads(master_json)
    else:
      try:
        response = urllib2.urlopen(self.master_url.geturl())
        self.master_data = json.loads(response.read())
      finally:
        response.close()

    self.base_url = self.master_url\
      .remove_last_path_element()\
      .add_path(self.master_data["base_url"], ignore_trailing_slash=True)\
      .get_url()

  def get_base_url(self):
    return self.base_url

  def get_best_video_id(self):
    best_video = max(self.master_data["video"], key=(lambda video: video["bitrate"]))
    return best_video["id"]

  def get_clip_id(self):
    return self.master_data["clip_id"]

  def get_stream_count(self):
    return len(self.master_data["video"])

  def get_stream_url(self, video_id):
    video = self._get_video(video_id)
    return url.Url(self.base_url).add_path(video["base_url"]).get_url() if video else None

  def get_segment_count(self, video_id):
    video = self._get_video(video_id)
    return len(video["segments"]) if video else None

  def _get_video(self, video_id):
    return next((video for video in self.master_data["video"] if video["id"] == video_id), None)


def from_url(master_url):
    return Vimeo(master_url)


def from_json(master_url, master_json):
    return Vimeo(master_url, master_json)
