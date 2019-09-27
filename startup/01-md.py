import time
import sys
from bluesky.simulators import summarize_plan
from pathlib import Path
from historydict import HistoryDict

# Set up a RunEngine and use metadata backed by a sqlite file.
print(__file__)
from bluesky import RunEngine

from bluesky.utils import get_history
RE = RunEngine({})

# Set up a Broker.


# Subscribe metadatastore to documents.
# If this is removed, data is not saved to metadatastore.



try:
    RE.md = HistoryDict('/nsls2/xf08id/metadata/bluesky_history.db')
    print('gpfs')
except Exception as exc:
    print('local')
    print(exc)
    RE.md = HistoryDict('{}/.config/bluesky/bluesky_history.db'.format(str(Path.home())))
RE.is_aborted = False


