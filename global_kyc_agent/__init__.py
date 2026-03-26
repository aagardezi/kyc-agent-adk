import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Ensure the parent directory is in sys.path to allow absolute imports like 'from global_kyc_agent...'
package_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(package_dir)
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from . import agent
