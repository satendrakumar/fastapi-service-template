import random

""" Dummy Payment Service"""


def get_status():
    status = random.choice(["Pending", "Completed", "Failed"])
    return status
