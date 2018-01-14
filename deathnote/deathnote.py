import os
import sys
import threading
import subprocess as sp
import datetime
import argparse


class DeathNote:

    def __init__(self, hour, minute, pid):
        self.alarm_time = None
        self._alarm_thread = None
        self.update_interval = 1
        self.event = threading.Event()
        self.hour = hour
        self.minute = minute
        self.pid = pid

        self._set_alarm()

    def _set_alarm(self):
        now = datetime.datetime.now()
        alarm = now.replace(hour=int(self.hour), minute=int(self.minute))
        delta = int((alarm - now).total_seconds())
        if delta <= 0:
            alarm = alarm.replace(day=alarm.day + 1)
            delta = int((alarm - now).total_seconds())
        if self._alarm_thread:
            self._alarm_thread.cancel()
        self._alarm_thread = threading.Timer(delta, self.kill_process)
        self._alarm_thread.daemon = True
        self._alarm_thread.start()
        print('PID %s shall be killed at %02d:%02d:%02d on %02d-%02d-%02d.' %(\
            self.pid, alarm.hour, alarm.minute, alarm.second,\
            alarm.year, alarm.month, alarm.day))

    def run(self):
        while True:
            self.event.wait(self.update_interval)
            if self.event.isSet():
                break
            now = datetime.datetime.now()
            if self._alarm_thread and self._alarm_thread.is_alive():
                alarm_symbol = '+'
            else:
                alarm_symbol = ' '
                self._alarm_thread.join()
                sys.exit()

    def kill_process(self):
        sp.run(['kill', '-KILL', str(self.pid)])
        sys.stdout.write('Just now PID %s killed as planed.\n' % (self.pid))
        sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hour_minute", type=int, nargs=2,\
                        help="Teach hour and minute, for example, if p.m 2:30 then 14 30")
    parser.add_argument("--pid", "-p", type=int, required=True,\
                        help="Target process pid")
    args = parser.parse_args()

    hour, minute = args.hour_minute
    note = DeathNote(hour, minute, args.pid)
    note.run()
