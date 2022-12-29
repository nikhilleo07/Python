class Device():
    pi = 3.142
    def __init__(self) -> None:
        print("Running constructor for base class")
        self.debug = False
    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")
    def calculate_crc(self, frame:str)->int:
        print("Checking CRC from base")
        crc = 123456789
        return crc
    def configure_device(self):
        pass

class Firewall(Device):
    def __init__(self, parameter1) -> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_device(self):
        print("Configuring Firewall")
    def calculate_crc(self, frame:str)->int:
        print("Checking CRC from child")
        crc = 123456
class Switch(Device):
    def __init__(self, parameter1) -> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_device(self):
        print("Configuring Switch")
    def calculate_crc(self, frame:str)->int:
        print("Checking CRC from child")
        crc = 123456
class Loadbalancer(Device):
    def __init__(self, parameter1) -> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_device(self):
        print("Configuring Loadbalancer")
    def calculate_crc(self, frame:str)->int:
        print("Checking CRC from child")
        crc = 123456