# request file is similar to what we had before, but we request the site periodically, so some things are different.
import urllib.request
import os

if not os.path.exists("html_files"):
	os.mkdir("html_files")

