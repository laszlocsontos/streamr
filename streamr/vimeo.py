import json
import urllib2
from streamr import url

class Vimeo:

  def __init__(self, master_url, master_json=None):
    self.master_url = url.Url(master_url)

    if master_json:
      self.master_data = json.loads(master_json)
    else:
      self.master_data = json.loads(self._read_url(self.master_url.get_url()))

    self.base_url = self.master_url\
      .remove_last_path_element()\
      .add_path(self.master_data["base_url"], ignore_trailing_slash=True)\
      .get_url()

    self.video_map = {}
    for video in self.master_data["video"]:
      self.video_map[video["id"]] = video

  def get_base_url(self):
    return self.base_url

  def get_best_video_id(self):
    best_video = max(self.video_map.values(), key=(lambda video: video["bitrate"]))
    return best_video["id"]

  def get_clip_id(self):
    return self.master_data["clip_id"]

  def get_video_count(self):
    return len(self.video_map)

  def get_video_url(self, video_id):
    video = self._get_video(video_id)
    return url.Url(self.base_url).add_path(video["base_url"]).get_url() if video else None

  def get_segment_count(self, video_id):
    video = self._get_video(video_id)
    return len(video["segments"]) if video else None

  def get_segment_data(self, video_id, segment_index):
    segment_url = self.get_segment_url(video_id, segment_index)
    return bytearray(self._read_url(segment_url))

  def get_segment_url(self, video_id, segment_index):
    return self.get_video_url(video_id) + "segment-%s.m4s" % segment_index

  def _get_video(self, video_id):
    return self.video_map[video_id]

  def _read_url(self, url):
    response = None
    try:
      response = urllib2.urlopen(url)
      return response.read()
    except urllib2.HTTPError, e:
      print "url=%s, status=%s" % (url, e.code)
    finally:
      if response is not None:
        response.close()


def download_video(master_url, path_to_save):
  vimeo = from_url(master_url)
  best_video_id = vimeo.get_best_video_id()

  try:
    video_file = open("%s/%s.mp4" % (path_to_save, best_video_id), "wb")
    for index in range(0, vimeo.get_segment_count(best_video_id) + 1):
      video_file.write(vimeo.get_segment_data(best_video_id, index))
  finally:
    video_file.close()


def from_url(master_url):
    return Vimeo(master_url)


def from_json(master_url, master_json):
    return Vimeo(master_url, master_json)
