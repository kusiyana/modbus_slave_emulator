from pymodbus.client import ModbusSerialClient

master = ModbusSerialClient(
    method="rtu", port="/Users/haydeneastwood/tty00mast", baudrate=9600
)

slave_id = 1
slave_address = 1
number_addresses_to_read = 1

result = master.read_holding_registers(slave_address, number_addresses_to_read, unit=slave_id)  # convert to float
if result:
	print(result.registers)
else:
	print('Argh, no Modbus result!')


# write to register
new_value = 1
master.write_register(slave_address, new_value, unit=1)

