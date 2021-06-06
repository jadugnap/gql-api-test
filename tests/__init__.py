import os, sys
# sys.path.insert(parent_dir)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib import gql
from lib.query import raw, template
