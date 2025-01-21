async def main():
    hub = EventHub()

    motion_sensor = MotionSensor(hub)
    temperature_sensor = TemperatureSensor(hub)
    light_controller = LightController(hub)
    door_lock = DoorLock(hub)

    await asyncio.gather(
        motion_sensor.detect_motion(),
        temperature_sensor.monitor_temperature()
    )
