# purpose: write the purpose for the utility.

# import dependencies
import datetime

# import config
from utils.config_manager import Util as config_manager_util


get_config = config_manager_util().get_config
plugin_config = config_manager_util.get_plugin_config("smyk07/vinotes-demo-plugin")


# write utility class
class Util:
    def __init__(self, command_args=None):
        self.docstring = """Describe your utility here."""
        self.util_type = "independent"
        self.command_args = command_args

    @staticmethod
    def get_time():
        return datetime.datetime.now()
