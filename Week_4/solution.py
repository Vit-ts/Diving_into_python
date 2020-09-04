import os.path
from tempfile import gettempdir, NamedTemporaryFile

class File:

    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w'):
                pass
    
    def __str__(self):
        return self.filename

    def write(self, text):
        with open(self.filename, 'w') as f:
            return f.write(text)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

   
    def __add__(self, obj):
        res_path = os.path.join(gettempdir(), str(NamedTemporaryFile()))
        res = File(res_path)
        res.write(self.read() + obj.read())
        return res

    def __iter__(self):
        self._num = 0
        return self

    def __next__(self):
        with open(self.filename, 'r') as f:
            f.seek(self._num)

            line = f.readline()
            if not line:
                self._num = 0
                raise StopIteration('End of File')

            self._num = f.tell()
            return line

