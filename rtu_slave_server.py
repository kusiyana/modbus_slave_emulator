from collections import defaultdict

from lib.port_simulator import PortSimulator
from lib.slave_simulator import SlaveSimulator

data_store = defaultdict(int)
port_simulator = PortSimulator()
port_simulator.start_port_simulation()
slave = SlaveSimulator.initialise_slave(port_simulator.port_slave)

data_store[0] = 0
data_store[1] = 0
data_store[2] = 0
data_store[0x01A] = 0

@slave.route(
    slave_ids=list(range(0, 5)), function_codes=[3], addresses=list(range(0, 50))
)
def read_data_store(slave_id, function_code, address):
    """ " Return value of address."""
    print(
        f"\t-- Read value {data_store[address]} from slave ID {slave_id} with function code: {function_code} and address {address}"
    )
    return data_store[address]


@slave.route(slave_ids=[1], function_codes=[6], addresses=list(range(0, 10)))
def write_data_store(slave_id, function_code, address, value):
    """ " Set value for address."""
    print(
        f"\t-- Wrote value {value} to address {address} for slave_id {slave_id} with function code {function_code}"
    )
    data_store[address] = value


if __name__ == "__main__":
    try:
        print(" -- Simulating slave -- ")
        slave.serve_forever()
    finally:
        print("-- Shutting down slave -- ")
        slave.shutdown()
        port_simulator.end_port_simulation()
