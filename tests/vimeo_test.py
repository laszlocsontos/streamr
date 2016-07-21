import unittest
from streamr import vimeo

MASTER_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469098042-b3a140ccbdc17f186984f9ac9ac0a9d06b940c83/165473248/video/526296221,526296236,526296231,526296220/master.json"
BASE_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469098042-b3a140ccbdc17f186984f9ac9ac0a9d06b940c83/165473248/video"
STREAM_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469098042-b3a140ccbdc17f186984f9ac9ac0a9d06b940c83/165473248/video/526296221"

class VimeoTest(unittest.TestCase):

  def setUp(self):
    master_json = open("174158118.json").read()
    self.vimeo = vimeo.from_json(MASTER_URL, master_json)

  def test_get_base_url(self):
    self.assertEqual(BASE_URL, self.vimeo.get_base_url())

  def test_get_best_video_id(self):
    self.assertEqual(526296220, self.vimeo.get_best_video_id())

  def test_get_clip_id(self):
    self.assertEqual(165473248, self.vimeo.get_clip_id())

  def test_get_stream_count(self):
    self.assertEqual(4, self.vimeo.get_stream_count())

  def test_get_stream_url(self):
    self.assertEqual(STREAM_URL, self.vimeo.get_stream_url(526296221))

  def test_get_segment_count(self):
    self.assertEqual(16, self.vimeo.get_segment_count(526296221))
