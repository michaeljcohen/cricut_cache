import os
import shutil
import psutil
import subprocess
import stat
import sys
import traceback
import win32com.shell.shell as shell
import win32com.shell.shellcon as shellcon

# nuitka --onefile --windows-uac-admin --windows-disable-console --msvc=latest resetcricut.py


log_file = "resetcricut.log"

def log(msg):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{msg}\n")
        f.flush()

def handle_exception(exc_type, exc_value, exc_traceback):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("=== Unhandled Exception ===\n")
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)

sys.excepthook = handle_exception

def kill_cricut():
    log("ï¿½ï¿½ Checking for Cricut processes to kill...")

    current_pid = os.getpid()
    current_name = psutil.Process(current_pid).name()

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

        # Skip self
        if pid == current_pid or name == current_name:
            continue

        if name and 'cricut' in name.lower():
            try:
                log(f"âš ï¸ Attempting to kill: {name} (PID {pid})")
                proc.kill()
                proc.wait(timeout=3)
                log(f"âœ… Killed process: {name} (PID {pid})")
            except psutil.TimeoutExpired:
                log(f"â³ Timeout waiting for process to die: {name}")
            except Exception as e:
                log(f"âŒ Failed to kill process {name}: {e}")

    log("ï¿½ï¿½ exiting kill_cricut...")


def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
        log(f"âœ… Force-removed: {path}")
    except Exception as e:
        log(f"âŒ Failed to remove {path}: {e}")

def clean_local_data():
    log("ï¿½ï¿½ Starting cleanup of LocalData folders...")
    users_dir = "C:\\Users"
    for user in os.listdir(users_dir):
        user_path = os.path.join(users_dir, user)
        local_data_path = os.path.join(user_path, ".cricut-design-space", "LocalData")

        if not os.path.exists(local_data_path):
            log(f"â­ Skipped (not found): {local_data_path}")
            continue

        try:
            # Check read access before attempting
            test_file = os.path.join(local_data_path, "test_access.tmp")
            with open(test_file, "w") as f:
                f.write("test")
            os.remove(test_file)

            log(f"ï¿½ï¿½ Attempting to clear: {local_data_path}")
            shutil.rmtree(local_data_path, onerror=remove_readonly)
            log(f"âœ… Successfully cleared: {local_data_path}")
        except PermissionError as e:
            log(f"ï¿½ï¿½ Permission denied: {local_data_path}")
        except Exception as e:
            log(f"âŒ Error clearing {local_data_path}: {e}")

def empty_recycle_bin():
    log("ï¿½ï¿½ Attempting to empty Recycle Bin...")
    try:
        shell.SHEmptyRecycleBin(
            None, None,
            shellcon.SHERB_NOCONFIRMATION | shellcon.SHERB_NOSOUND | shellcon.SHERB_NOPROGRESSUI
        )
        log("âœ… Recycle Bin emptied.")
    except Exception as e:
        log(f"âŒ Failed to empty Recycle Bin: {e}")

def find_and_launch_cricut():
    log("ï¿½ï¿½ Searching for Cricut Design Space executable...")
    base_dir = "C:\\Users"
    exe_name = "Cricut Design Space.exe"
    for root, dirs, files in os.walk(base_dir):
        if exe_name in files:
            exe_path = os.path.join(root, exe_name)
            try:
                subprocess.Popen(exe_path)
                log(f"ï¿½ï¿½ Launched: {exe_path}")
                return
            except Exception as e:
                log(f"âŒ Failed to launch {exe_path}: {e}")
                return
    log("âŒ Cricut Design Space.exe not found.")

if __name__ == "__main__":
    log("====== Reset Cricut Script Started ======")
    kill_cricut()
    log("====== clean_local_data ======")
    clean_local_data()
    log("====== empty_recycle_bin ======")
    empty_recycle_bin()
    log("====== find_and_launch_cricut ======")
    find_and_launch_cricut()
    log("âœ… Script completed.\n")
