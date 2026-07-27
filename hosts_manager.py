import os
import platform
import shutil
MARKER_START = "# rbrbnd-BLOCK-START"
MARKER_END = "# rbrbnd-BLOCK-END"
def get_data_dir():
    data_dir = os.path.join(os.path.expanduser("~"), ".rbrbnd")
    os.makedirs(data_dir, exist_ok=True)
    return data_dir
BACKUP_PATH = os.path.join(get_data_dir(), "hosts.rbrbnd_backup")
def _hosts_path():
    if platform.system() == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    return "/etc/hosts"
class HostsManager:
    def __init__(self):
        self.path = _hosts_path()
        self._ensure_backup()
    def _ensure_backup(self):
        if not os.path.exists(BACKUP_PATH):
            shutil.copyfile(self.path, BACKUP_PATH)
    def _read(self):
        with open(self.path, "r") as f:
            return f.read()
    def _write(self, content):
        with open(self.path, "w") as f:
            f.write(content)
    def _strip_block(self, content):
        if MARKER_START not in content:
            return content
        before, _, rest = content.partition(MARKER_START)
        _, _, after = rest.partition(MARKER_END)
        return before.rstrip() + "\n" + after.lstrip()
    def _build_block(self, domains):
        lines = [MARKER_START]
        for d in domains:
            d = d.strip()
            if not d or " " in d:
                continue
            lines.append(f"127.0.0.1 {d}")
            lines.append(f"127.0.0.1 www.{d}")
        lines.append(MARKER_END)
        return "\n".join(lines)
    def apply(self, domains):
        current = self._read()
        cleaned = self._strip_block(current)
        block = self._build_block(domains)
        self._write(cleaned.rstrip() + "\n\n" + block + "\n")
    def remove_block(self):
        current = self._read()
        self._write(self._strip_block(current).rstrip() + "\n")
    def is_block_present(self):
        return MARKER_START in self._read()
    def reapply_if_needed(self, domains):
        if not self.is_block_present():
            self.apply(domains)
    def restore_from_backup(self):
        if os.path.exists(BACKUP_PATH):
            shutil.copyfile(BACKUP_PATH, self.path)
            return True
        return False