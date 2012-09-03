import threading
import time

def _default_action(dico):
    print dico

class Logger(threading.Thread):
    def __init__(self, verdi, action=None, liste_param=None, delay=10):
        threading.Thread.__init__(self)
        self.verdi = verdi
        self.Terminated = False
        self.liste_param = liste_param
        self.action = _default_action if action is None else action
        self.delay = delay 
    def run(self):
        while not self.Terminated:
            if self.liste_param is not None:
                self.result = self.verdi.read_list_cmd(self.liste_param)
            else:
                self.result = self.verdi.read_all_parameters()
            self.result['time']=time.time()
            self.action(self.result)
            time.sleep(self.delay)
    def stop(self):
        self.Terminated = True
    def restart(self):
        self.Terminated = False
        self.start()
        
        
#verdi = PyCoherentVerdi.VerdiDriver(port='COM7')
#logger = Logger(verdi)
#logger.star()
     