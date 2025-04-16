import os
import subprocess
import shutil
import psutil
from pathlib import Path

def kill_cricut_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name']
            if name and 'cricut' in name.lower():
                print(f"Killing: {name} (PID {proc.pid})")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def clear_cricut_cache():
    localdata_path = Path.home() / ".cricut-design-space" / "LocalData"
    if localdata_path.exists():
        for item in localdata_path.iterdir():
            try:
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
                print(f"Deleted: {item}")
            except Exception as e:
                print(f"Failed to delete {item}: {e}")

def launch_cricut():
    app_path = "/Applications/Cricut Design Space.app"
    if os.path.exists(app_path):
        subprocess.Popen(["open", app_path])
        print("Launched Cricut Design Space.")
    else:
        print("Cricut Design Space not found in /Applications.")

if __name__ == "__main__":
    kill_cricut_processes()
    clear_cricut_cache()
    launch_cricut()
