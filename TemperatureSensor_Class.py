class TemperatureSensor:
    def __init__(self, hub):
        self.hub = hub

    async def monitor_temperature(self):
        while True:
            temperature = randint(18, 30)
            print(f"Temperature: {temperature}°C")
            await self.hub.emit("temperature_update", {"value": temperature})
            await asyncio.sleep(10)
