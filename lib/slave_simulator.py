import json

from serial import Serial
from umodbus.server.serial import get_server
from umodbus.server.serial.rtu import RTUServer


class SlaveSimulator:
    default_config = {"baudrate": 9600, "stopbits": 1, "timeout": 1, "parity": "N"}

    @classmethod
    def initialise_slave(cls, port_name, config: dict = None) -> get_server:
        if not config:
            config = cls.default_config
        print("\n-- RTU connection settings --")
        print(json.dumps(config, indent=4))
        serial_device = Serial(port_name)
        serial_device.baudrate = config.get("baudrate", cls.default_config["baudrate"])
        serial_device.timeout = config.get("timeout", cls.default_config["timeout"])
        serial_device.stopbits = config.get("stopbits", cls.default_config["stopbits"])
        serial_device.parity = config.get("parity", cls.default_config["parity"])
        app = get_server(RTUServer, serial_device)
        return app
