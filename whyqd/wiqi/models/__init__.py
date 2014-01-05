from text import Text
from image import Image
from book import Book
#from geomap import Geomap
from base import *

DEFAULT_WIQISTACK_TYPE = "text"

WIQI_TYPE_DICT = {
                  'text': Text,
                  'image': Image,
                  'book': Book,
                  #'geomap': Geomap,
                  }