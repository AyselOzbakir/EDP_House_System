class MotionSensor:
    def __init__(self, hub):
        self.hub = hub

    async def detect_motion(self):
        while True:
            motion_detected = bool(randint(0, 1))
            if motion_detected:
                print("Motion detected!")
                await self.hub.emit("motion_detected", {"location": "Living Room"})
            await asyncio.sleep(5)
