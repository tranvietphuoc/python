import signal
from time import sleep


class Timeout:
    def __init__(self, seconds, *, timeout_message=""):
        self.seconds = seconds
        self.timeout_message = timeout_message

    def _timeout_handle(self, signum, frame):
        raise TimeoutError(self.timeout_message)

    def __enter__(self):
        signal.signal(
            signal.SIGALRM, self._timeout_handle
        )  # set timeout handler for SIGALRM
        signal.alarm(self.seconds)  # start count down for SIGALRM to be raised

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)  # Cancel SIGALRM if it's scheduled
        return exc_type is TimeoutError  # Suppress TimeoutError


with Timeout(3):
    sleep(10)
