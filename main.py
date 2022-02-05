#!/usr/bin/env python3


import os
from datetime import datetime, timedelta

directory = "/tank01/backups" #target dir


class Cleaner:
    def __init__(self, path):
        self.dir = path
        self.files = []
        self.current_time = datetime.now()
        self.deadline = self.current_time - timedelta(days=7)  # date - days
        self.filename = ''
        self.del_count = 0
        self.save_count = 0

    def read(self):
        self.files = os.listdir(self.dir)
        self.files = list(filter(lambda x: x.endswith('.tar.gz'), self.files))

    def action(self):
        for self.filename in self.files:
            target = self.filename.rsplit(sep='.')
            target = datetime.strptime(target[2][:-6], "%d-%m-%Y")  # string to date
            if target < self.deadline and target.day != 20:
                self.del_target()
                self.del_count += 1
            else:
                self.save_count += 1

    def del_target(self):
        path = os.path.join(os.path.abspath(self.dir), self.filename)
        os.remove(path)

example = Cleaner(directory)
example.read()
example.action()
print(f'saved: {example.save_count}, deleted {example.del_count}')
