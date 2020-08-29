class FileReader:

    def __init__(self, way_to):
        self.way_to = way_to

    def read(self):
        try:
            with open(self.way_to, "r") as f:
               return f.read()
        except FileNotFoundError:
            return ''
