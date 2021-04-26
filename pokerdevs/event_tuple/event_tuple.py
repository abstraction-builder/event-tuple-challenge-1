import ulid

class UserClickedOnButtonEvent:
    """ Class for user clicked events """

    def __init__(self, event_id, button_id, event_type="UserClickedOnButtonEvent"):
        # TODO: deduce timestamp from event_id
        # str -> int
        timestamp = ulid.parse(event_id).int
        self.event = (event_type, event_id, timestamp, button_id)

    @classmethod
    def create(cls):
        pass 

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

    def __repr__(self):
        return f"{self.event_id} with ID: {self.event_id}"

class UserLongPressedEvent:
    """ Class for uer long-pressed event """

    def __init__(self, event_id, timestamp, x, y, event_type="UserLongPressedEvent"):
        timestamp = ulid.parse(event_id).int
        self.event = (event_type, event_id, timestamp, x, y)

    @classmethod
    def create(cls):
        pass

    def timestamp(self):
        # return time stamp. e.g 1619146052
        return self.event[2]

    def event_id(self):
        # return event id. e.g "b5796505-68fd-40d5-814a-9d31f3f084b0"
        return self.event[1]

    def event_type(self):
        # return event id. e.g "close_button"
        return self.event[0]

    def x(self):
        # return x coordinate on a grid
        return self.event[3]

    def y(self):
        # return y coordinate on a grid
        return self.event[4]

def challenge_3_test():
    pass

def challenge_2_test():
    # testing UserClickedOneButoonEvent class
    my_event = UserClickedOnButtonEvent("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "close_button")
    print(f"Event '{my_event.event_type()}' occured at {my_event.timestamp()} with ID: {my_event.button_id()}")

    # testing UserLongPressedEvent class
    my_second_event = UserLongPressedEvent("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, 340, 420)
    print(f"Event '{my_second_event.event_type()}' occured at {my_second_event.timestamp()} with x = {my_second_event.x()} and y = {my_second_event.y()}")

def main():
     challenge_2_test()
    # challenge_3_test()

if __name__ == '__main__':
    main() 

