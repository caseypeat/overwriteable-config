import sys

from config.overwriteable_config import OverwriteableConfig

cfg = OverwriteableConfig()

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        cfg.load_yaml(arg)