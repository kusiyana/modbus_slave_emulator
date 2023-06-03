import os
import subprocess
import time

import psutil


class PortSimulator:
    def __init__(self):
        self.port_master = f"{os.environ['HOME']}/tty00mast"
        self.port_slave = f"{os.environ['HOME']}/tty00slav"

    def start_port_simulation(self) -> None:
        command_raw = f"socat -d -d PTY,link={self.port_slave},raw PTY,link={self.port_master},raw >/dev/null 2>&1 &"
        process = subprocess.Popen(
            command_raw, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        stdout, stderr = process.communicate()
        time.sleep(2)
        self.pid = process.pid
        print(f"\n -- Port simulation started:  -- ")
        print(f"\n -- Connect Slave to: {self.port_slave} -- ")
        print(f" -- Connect master to: {self.port_master} --")
        return

    def end_port_simulation(self) -> None:
        """Kills the socat process"""
        parent = psutil.Process(self.pid + 1)
        for child in parent.children(recursive=True):
            child.kill()
        try:
            parent.kill()
        except:
            pass
