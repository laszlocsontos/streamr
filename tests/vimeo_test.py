import unittest
from streamr import vimeo

MASTER_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469105472-7df5884046f0a1359a35580f2709c8de8dcd286b/165473248/video/526296221,526296236,526296231,526296220/master.json?base64_init=1"
BASE_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469105472-7df5884046f0a1359a35580f2709c8de8dcd286b/165473248"
VIDEO_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469105472-7df5884046f0a1359a35580f2709c8de8dcd286b/165473248/video/526296221/chop/"

SEGMENT_526296221_1_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469105472-7df5884046f0a1359a35580f2709c8de8dcd286b/165473248/video/526296221/chop/segment-1.m4s"
SEGMENT_526296231_1_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469105472-7df5884046f0a1359a35580f2709c8de8dcd286b/165473248/video/526296231/chop/segment-1.m4s"

class VimeoTest(unittest.TestCase):

  def setUp(self):
    master_json = open("174158118.json").read()
    self.vimeo = vimeo.from_json(MASTER_URL, master_json)

  @unittest.skip
  def test_download_video(self):
    vimeo.download_video(MASTER_URL, "/tmp")

  def test_get_base_url(self):
    self.assertEqual(BASE_URL, self.vimeo.get_base_url())

  def test_get_best_video_id(self):
    self.assertEqual(526296220, self.vimeo.get_best_video_id())

  def test_get_clip_id(self):
    self.assertEqual(165473248, self.vimeo.get_clip_id())

  def test_get_video_count(self):
    self.assertEqual(4, self.vimeo.get_video_count())

  def test_get_video_url(self):
    self.assertEqual(VIDEO_URL, self.vimeo.get_video_url(526296221))

  def test_get_segment_count(self):
    self.assertEqual(16, self.vimeo.get_segment_count(526296221))

  def test_get_segment_url(self):
    self.assertEqual(SEGMENT_526296221_1_URL, self.vimeo.get_segment_url(526296221, 1))
    self.assertEqual(SEGMENT_526296231_1_URL, self.vimeo.get_segment_url(526296231, 1))
