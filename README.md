https://medium.com/@elifsuaysel/building-an-event-driven-iot-system-in-python-9ae534621185

# EDP House System

The **EDP House System** is an event-driven programming (EDP) implementation that simulates the interaction between various IoT devices in a smart home. This system demonstrates how different components—such as sensors and controllers—can work together using asynchronous event-based communication, ensuring real-time responsiveness and modularity.

## Features

- **Motion Detection**: Simulates a motion sensor that emits events when movement is detected.
- **Temperature Monitoring**: Simulates a temperature sensor that provides periodic temperature updates.
- **Light Control**: Automatically turns lights on when motion is detected.
- **Door Lock Alerts**: Sends alerts if motion is detected near a locked door, enhancing security.
- **Event-Driven Architecture**: Built using Python's `asyncio` to enable efficient and concurrent event handling.

## Technology Stack

- **Programming Language**: Python
- **Framework/Library**: `asyncio`
- **Architecture**: Event-Driven Programming (EDP)

## How It Works

1. **Event Hub**: The central system connects sensors (event emitters) and controllers (event handlers). Sensors generate events, and the hub notifies relevant controllers.
2. **Asynchronous Design**: All components operate concurrently, allowing real-time communication.
3. **Sensor-Controller Interaction**: 
   - Motion sensors trigger events that control lights or send alerts.
   - Temperature sensors periodically broadcast updates that other components can use.

## Installation

To run the EDP House System, ensure you have Python 3.7+ installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/AyselOzbakir/EDP_House_System.git
   cd EDP_House_System
   ```

2. Install required packages (if any). For example:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

## Usage

- Customize sensor intervals and event data in the code to simulate different scenarios.
- Observe how components interact asynchronously in real time.

## Project Structure

```plaintext
EDP_House_System/
├── main.py           # Entry point for the application
├── event_hub.py      # Manages event subscriptions and notifications
├── sensors/
│   ├── motion_sensor.py      # Simulates motion detection
│   ├── temperature_sensor.py # Simulates temperature monitoring
├── controllers/
│   ├── light_controller.py   # Controls lights based on motion
│   ├── door_lock.py          # Alerts on motion near locked doors
├── README.md         # Project documentation
```

## Contribution

Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature description"`
4. Push the branch: `git push origin feature-name`
5. Create a pull request.

