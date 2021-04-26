class UserClickedOnButtonEvent:
    """ Class for user clicked events """

    def __init__(self, event_id, timestamp, button_id, event_type="UserClickedOnButtonEvent"):
        self.event = (event_type, event_id, timestamp, button_id)

    def timestamp(self):
        # return time stamp. e.g 1619146052
        return self.event[2]

    def event_id(self):
        # return event id. e.g "b5796505-68fd-40d5-814a-9d31f3f084b0"
        return self.event[1]

    def event_type(self):
        # return event type. e.g UserClickedOnButtonEvent
        return self.event[0]

    def button_id(self):
        # return event id. e.g "close_button"
        return self.event[3]

"""
class UserLongPressedEvent:
     Class for uer long-pressed event

    def __init__(self, event_id, timestamp, x, y):
        self.event_type = "UserLongPressedEvent"
        self.event = tuple()

    def timestamp():
        pass

    def event_id():
        pass

    def event_type():
        pass

    def x():
        pass

    def y():
        pass
"""

def main():
    my_event = UserClickedOnButtonEvent("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "close_button")
    print(f"Event '{my_event.event_type()}' occured at {my_event.timestamp()} with ID: {my_event.button_id()}")

if __name__ == '__main__':
    main() 
