from hosts_manager import HostsManager
if __name__ == "__main__":
    hosts = HostsManager()
    if hosts.restore_from_backup():
        print("Hosts file restored from backup. You're unblocked.")
    else:
        print("No backup found — nothing to restore (hosts file was never modified).")
    input("\nPress Enter to close..")