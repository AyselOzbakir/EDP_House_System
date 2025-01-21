class DoorLock:
    def __init__(self, hub):
        self.hub = hub
        self.is_locked = True
        self.hub.subscribe("motion_detected", self.handle_motion)

    async def handle_motion(self, data):
        if self.is_locked:
            print("Motion near door detected. Sending alert.")
