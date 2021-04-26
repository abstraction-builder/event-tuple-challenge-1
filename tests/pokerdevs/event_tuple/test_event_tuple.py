import pytest
import logging
from pokerdevs import event_tuple # even_tuple.py is initialy empty


logger = logging.getLogger(__name__)

events = [
     ("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "UserClickedOnButton", "close_button"),
     ("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, "UserLongPressed", 340, 420),
]


def generate_test_events():
     yield ("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "UserClickedOnButton", "close_button")
     yield ("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, "UserLongPressed", 340, 420)


def serialize_event(event):
    raise f"Event '{event[2]}' occured at {event[1]} with ID: {event[0]}"


def test_event_tuple():
    logger.info(f"Starting the test !")
    pytest.fail(f"YOU NEED TO FINISH THIS")
     
