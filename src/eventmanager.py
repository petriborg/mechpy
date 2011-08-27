"""
mechpy manager for all (most?) game events
controllers and views will register here to share events
"""

import events

#
# eventmanager singleton
#
evManager = None

def init():
    """
    Initialize the singleton once in main
    """
    global evManager
    evManager = EventManager()

class EventManager:
    """this object is responsible for coordinating most communication
    between the Model, View, and Controller.
    """
    def __init__(self ):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    #----------------------------------------------------------------------
    def RegisterListener( self, listener ):
        self.listeners[ listener ] = 1

    #----------------------------------------------------------------------
    def UnregisterListener( self, listener ):
        if listener in self.listeners.keys():
            del self.listeners[ listener ]
        
    #----------------------------------------------------------------------
    def Post( self, event ):
        """Post a new event.  It will be broadcast to all listeners"""
        for listener in self.listeners.keys():
            #NOTE: If the weakref has died, it will be 
            #automatically removed, so we don't have 
            #to worry about it.
            listener.Notify( event )
