from SOFASonix import SOFAFile
import logging
import contextlib

logging.basicConfig(
    filename='loadsofa.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

class OutputLogger:
    def __init__(self, logger_name, level):
        self.logger = logging.getLogger(logger_name)
        self.level = getattr(logging, level.upper())
    
    def write(self, message):
        if message.strip():
            self.logger.log(self.level, message.strip())

    def flush(self):
        pass

sofa_path = input('Paste directory to sofa file here: ')

loadsofa = SOFAFile.load(str(sofa_path), verbose=False)

with contextlib.redirect_stdout(OutputLogger("my_logger", "INFO")):
    print("---***---")
    print("File path: " + sofa_path)
    loadsofa.view()
    print("---***---")