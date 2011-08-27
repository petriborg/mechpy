"""
mechpy event list
"""

class Event:
    """this is a superclass for any events that might be generated by an
    object and sent to the EventManager
    """
    def __init__(self):
        self.name = "Generic Event"

class QuitEvent(Event):
	"""sent to notify that the program should quit"""
	def __init__(self):
		self.name = "Quit Event"
		
class KeyboardEvent(Event):
	"""contains keyboard event data"""
	def __init__(self):
		self.name = "Keyboard Event"
		
class TickEvent(Event):
	"""cpu tick event (clock)"""
	def __init__(self):
		self.name = "Tick Event"
