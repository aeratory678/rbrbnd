import json
import os
import sys
import threading
import time
import webview
from hosts_manager import HostsManager, get_data_dir
from process_blocker import kill_matching_processes
WATCH_INTERVAL_SECONDS = 3
def get_bundled_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
BLOCKLIST_FILE = os.path.join(get_data_dir(), "blocklist.json")
def load_blocklist():
    if os.path.exists(BLOCKLIST_FILE):
        with open(BLOCKLIST_FILE, "r") as f:
            return json.load(f)
    return ["twitter.com", "reddit.com", "youtube.com"]
def save_blocklist_to_disk(items):
    with open(BLOCKLIST_FILE, "w") as f:
        json.dump(items, f, indent=2)
class Api:
    def __init__(self):
        self.hosts = HostsManager()
        self.blocklist = load_blocklist()
        self.active = False
        self._stop_event = threading.Event()
        self._watch_thread = None
    def get_blocklist(self):
        return self.blocklist
    def save_blocklist(self, items):
        self.blocklist = items
        save_blocklist_to_disk(items)
        return True
    def start_block(self, items, duration_seconds=None):
        self.blocklist = items
        save_blocklist_to_disk(items)
        self.active = True
        self.hosts.apply(items)
        self._stop_event.clear()
        self._watch_thread = threading.Thread(target=self._watch_loop, daemon=True)
        self._watch_thread.start()
        return True
    def stop_block(self):
        self.active = False
        self._stop_event.set()
        self.hosts.remove_block()
        return True
    def _watch_loop(self):
        while not self._stop_event.is_set():
            if self.active:
                self.hosts.reapply_if_needed(self.blocklist)
                kill_matching_processes(self.blocklist)
            time.sleep(WATCH_INTERVAL_SECONDS)
if __name__ == "__main__":
    api = Api()
    window = webview.create_window(
        "rbrbnd",
        get_bundled_path("index.html"),
        js_api=api,
        width=420,
        height=680,
        resizable=False,
    )
    webview.start()