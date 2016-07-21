import unittest
from streamr import url

MASTER_URL = "https://01-lvl3-skyfire-gce.vimeocdn.com/1469098042-b3a140ccbdc17f186984f9ac9ac0a9d06b940c83/165473248/video/526296221,526296236,526296231,526296220/master.json"
VIDEO_URL =  "https://01-lvl3-skyfire-gce.vimeocdn.com/1469098042-b3a140ccbdc17f186984f9ac9ac0a9d06b940c83/165473248/video/526296221/chop/"

class UrlTest(unittest.TestCase):

  def test_no_url_change(self):
    u = url.Url(MASTER_URL)
    u.add_path(".")
    self.assertEqual(MASTER_URL, u.get_url())

  def test_remove_last_path_element(self):
    u = url.Url(MASTER_URL)
    u.add_path("..")
    self.assertEqual("/".join(MASTER_URL.split("/")[:-1]), u.get_url())

  def test_remove_last_two_path_elements(self):
    u = url.Url(MASTER_URL)
    u.add_path("../..")
    self.assertEqual("/".join(MASTER_URL.split("/")[:-2]), u.get_url())

  def test_video_url(self):
    u = url.Url(MASTER_URL)
    u.remove_last_path_element()\
      .add_path("../../", True)\
      .add_path("video/526296221/chop/")
    self.assertEqual(VIDEO_URL, u.get_url())
