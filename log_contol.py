class LogControl:
    def __init__(self):
        self.logs = []
        
    def add_log(self, log:str):
        self.logs.append(log)
        
    def get_log(self):
        return self.logs