class DuplicatedEntry(Exception):
    def __init__(self, err=None , model='', columns=None, values=None):
        self.err = err
        self.model = model
        self.columns = columns
        self.values = values
