class UserClickedOnButtonEvent:
    """ Class for user clicked events """

    def __init__(self, event_id, timestamp, button_id, event_type="UserClickedOnButtonEvent"):
        self.event = (event_type, event_id, timestamp, button_id)

    @classmethod
    def create(cls, button_id):
        import ulid, time
        event_id = ulid.new()
        timestamp = round(time.time() * 1000)
        event = cls(event_id, timestamp, button_id, event_type="UserClickedOnButtonEvent")
        return event


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
        return f"Type: {self.event_type()}, ID: {self.button_id()} "

class UserLongPressedEvent:
    """ Class for uer long-pressed event """

    def __init__(self, event_id, timestamp, x=0, y=0, event_type="UserLongPressedEvent"):
        self.event = (event_type, event_id, timestamp, x, y)

    @classmethod
    def create(cls, x, y):
        import ulid, time
        event_id = ulid.new()
        timestamp = round(time.time() * 1000)
        event = cls(event_id, timestamp, x, y)
        return event

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

    def __repr__(self):
        return f"Type: {self.event_type()}, ID: {self.event_id()} "


def challenge_3():
    print(f"{5*'-'} From challenge 3 {5*'-'}")
    click_event = UserClickedOnButtonEvent.create(button_id='foobarid')
    print(f"UserClickedOnButtonEvent object -> {click_event}")
    long_press = UserLongPressedEvent.create(124, 12)
    print(f"UserLongPressedEvent object -> {long_press}")
    print(f"{5*'-'} From challenge 3 {5*'-'}")

def main():
    challenge_3()

if __name__ == '__main__':
    main() 

