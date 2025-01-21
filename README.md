Building an Event-Driven IoT System with Python and asyncio
In the world of Internet of Things (IoT), systems often need to communicate between different devices (or components) to take actions based on events that occur. These systems may include sensors, actuators, and controllers that rely on event-driven architecture to function efficiently. In this post, we’ll explore how to build a basic IoT system using Python’s asyncio library and a custom event hub.

Problem Overview
Imagine an IoT setup where you have:

A motion sensor that detects movement in a room.
A temperature sensor that monitors the ambient temperature.
A light controller that turns the lights on when motion is detected.
A door lock that sends alerts when motion is detected near the door.
The goal is to create a system where these components can communicate with each other, but without tightly coupling them. We can achieve this by using an event-driven approach, where each component subscribes to certain events and responds accordingly.

Solution: Using Event-Driven Programming in Python
1. EventHub Class
We start by creating an EventHub class, which acts as the central dispatcher of events. Components (such as sensors and controllers) can subscribe to specific events, and when an event occurs, the EventHub will notify all subscribed components.

python
Kopyala
Düzenle
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
Here, the EventHub maintains a list of subscribers for each event type. Components can subscribe to events (like motion_detected or temperature_update) by providing a callback function. When an event is emitted using emit(), the EventHub calls all the subscribed callbacks with the event data.

2. MotionSensor Class
Next, we create the MotionSensor class, which simulates a motion detection system. It emits a motion_detected event when motion is detected in the room.

python
Kopyala
Düzenle
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
This sensor periodically checks for motion (simulated by generating random numbers) and, if motion is detected, emits the motion_detected event with a location payload. The asyncio.sleep(5) simulates a delay between sensor readings.

3. TemperatureSensor Class
The TemperatureSensor class monitors temperature and emits a temperature_update event with the current temperature value.

python
Kopyala
Düzenle
class TemperatureSensor:
    def __init__(self, hub):
        self.hub = hub

    async def monitor_temperature(self):
        while True:
            temperature = randint(18, 30)
            print(f"Temperature: {temperature}°C")
            await self.hub.emit("temperature_update", {"value": temperature})
            await asyncio.sleep(10)
Similar to the motion sensor, this class generates random temperature values (between 18°C and 30°C) and emits the temperature_update event every 10 seconds.

4. LightController Class
The LightController class subscribes to the motion_detected event. When motion is detected, it turns on the lights if they are off.

python
Kopyala
Düzenle
class LightController:
    def __init__(self, hub):
        self.hub = hub
        self.lights_on = False
        self.hub.subscribe("motion_detected", self.handle_motion)

    async def handle_motion(self, data):
        if not self.lights_on:
            self.lights_on = True
            print("Lights turned on due to motion.")
When motion is detected, the handle_motion() method is called, and if the lights are off, it turns them on.

5. DoorLock Class
The DoorLock class subscribes to the motion_detected event as well. If motion is detected near the door, it sends an alert.

python
Kopyala
Düzenle
class DoorLock:
    def __init__(self, hub):
        self.hub = hub
        self.is_locked = True
        self.hub.subscribe("motion_detected", self.handle_motion)

    async def handle_motion(self, data):
        if self.is_locked:
            print("Motion near door detected. Sending alert.")
In this case, if motion is detected near the door (where the sensor is placed), the door lock system sends an alert indicating that motion was detected.

6. Bringing Everything Together
Now, we’ll set up the main() function to initialize all components and start their asynchronous tasks.

python
Kopyala
Düzenle
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
The asyncio.gather() function is used to run both the detect_motion() and monitor_temperature() methods concurrently. This allows the system to handle multiple sensors running in parallel.

7. Running the System
Finally, we start the event loop with asyncio.run(main()).

python
Kopyala
Düzenle
if __name__ == "__main__":
    asyncio.run(main())
This initiates the event-driven system, where motion sensors detect movement, temperature sensors monitor changes, and other components react to these events.

Key Takeaways
Event-Driven Architecture: By using the EventHub, we can decouple components and allow them to respond to events without directly interacting with each other. This improves modularity and scalability.

Asynchronous Programming: The use of Python’s asyncio library allows for non-blocking, concurrent execution of sensor tasks, making the system responsive and efficient.

Scalability: Adding new sensors or controllers (e.g., adding a humidity sensor or a smart fan) is easy. Simply subscribe to the relevant events and implement the appropriate handler logic.

Simulating IoT Systems: Although we used random data for motion detection and temperature values, this architecture could easily be extended to integrate with real sensors in an actual IoT environment.

Conclusion
This example illustrates the power of event-driven programming in building scalable and responsive IoT systems. By leveraging Python’s asyncio and a custom EventHub, we can create a flexible, modular system where components interact based on events. Whether you’re building smart home applications or complex sensor networks, this pattern can be a valuable approach to organizing your code.
