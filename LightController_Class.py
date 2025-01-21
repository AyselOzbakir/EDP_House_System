class LightController:
    def __init__(self, hub):
        self.hub = hub
        self.lights_on = False
        self.hub.subscribe("motion_detected", self.handle_motion)

    async def handle_motion(self, data):
        if not self.lights_on:
            self.lights_on = True
            print("Lights turned on due to motion.")
