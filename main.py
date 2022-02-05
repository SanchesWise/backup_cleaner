#!/usr/bin/env python3


import os
from datetime import datetime, timedelta

directory = "/home/ccsfarm/test"#"/tank01/backups"


class Cleaner:
    def __init__(self, path):
        self.dir = path
        self.files = []
        self.current_time = datetime.now()
        self.deadline = self.current_time - timedelta(days=7)  # date - days
        self.del_count =0
        self.save_count = 0

    def read(self):
        self.files = os.listdir(self.dir)
        self.files = list(filter(lambda x: x.endswith('.tar.gz'), self.files))
        print(self.files)


    def action(self):
        for filename in self.files:
            target = filename.rsplit(sep='.')
            target = datetime.strptime(target[2][:-6], "%d-%m-%Y")  # string to date
            print(filename)
            if target < self.deadline:
                print(f"{target},{self.current_time},{self.deadline}, delete")
                self.del_count+=1
            else:
                print(f"{target},{self.current_time},{self.deadline}, save")
                self.save_count+=1
example = Cleaner(directory)
example.read()
example.action()
print(f'saved: {example.save_count}, deleted {example.del_count}')
