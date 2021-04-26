# Challenge Three

## Factory Constructor

Added a @classmethod factory constructor method create(...) to the classes

It automatically creates an event_id:
  * as a randomly generated string token

It will automatically create the value for timestamp:
  * using the current system time

For example: UserClickedOnButtonEvent.create(button_id='blabla')
