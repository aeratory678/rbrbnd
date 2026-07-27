import psutil
def _is_process_entry(entry):
    entry = entry.strip().lower()
    if not entry:
        return False
    if entry.endswith(".exe"):
        return True
    if "." not in entry:
        return True
    return False
def kill_matching_processes(blocklist):
    targets = {e.strip().lower() for e in blocklist if _is_process_entry(e)}
    if not targets:
        return
    for proc in psutil.process_iter(["name"]):
        try:
            name = (proc.info["name"] or "").lower()
            name_no_ext = name[:-4] if name.endswith(".exe") else name
            if name in targets or name_no_ext in targets:
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue