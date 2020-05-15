class Dafe:

    def __init__(self, filename):
        self.filename = filename

    def show(self, p=None):
        if not p:
            return str(vars(self))
        elif hasattr(self, p):
            return (getattr(self, p))
        else:
            return f">> no attribute '{p}'"

    def read_tab(self, tab_name):
        # Open File
        # Read tab
        # read data into objects
        pass