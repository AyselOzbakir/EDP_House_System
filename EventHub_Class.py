class EventHub:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    async def emit(self, event_type, data):
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                await callback(data)
