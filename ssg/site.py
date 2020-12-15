from pathlib import Path
import os


class Site:
    def __init__(self, source,dest):
        self._source=Path()
        self._dest=Path()


    def create_dir(self,path):
        directory=self._dest+"/"+self._source.relative_to(self._dest)
        directory.mkdir(parents=True,exist_ok=True)


    def build(self):
        self._dest.mkdir(parents=True,exist_ok=True)
        for path in self._source.rglob("*"):
            if os.path.isdir(path):
                create_dir(path)