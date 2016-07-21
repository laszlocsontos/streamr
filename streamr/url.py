import urlparse


class Url:

  def __init__(self, url):
    self.url_parts = urlparse.urlsplit(url)
    self.path_items = self.url_parts[2].split("/")

  def add_path(self, path, ignore_trailing_slash=False):
    for path_item in path.split("/"):
      if path_item == ".":
        continue
      if path_item == "..":
        self.path_items.pop()
        continue
      if path_item != "" or not ignore_trailing_slash:
        self.path_items.append(path_item)
    return self

  def remove_last_path_element(self):
    self.add_path("..")
    return self

  def get_url(self):
    path = "/".join(self.path_items)
    return urlparse.urlunsplit((self.url_parts[0], self.url_parts[1], path, None, None))
