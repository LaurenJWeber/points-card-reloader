from datetime import datetime


class VerySimpleLogger:

    def __init__(self, file_path):
        self.log_file_path = file_path

    def log_message(self, message):
        current_timestamp = datetime.now()
        with open(self.log_file_path, 'a') as my_log:
            my_log.write(f'{current_timestamp}:{message}\n')
