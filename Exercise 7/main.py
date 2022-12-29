from device import Firewall,Switch,Loadbalancer
firewall27 = Firewall("firewall27")
firewall27.configure_device()
firewall28 = Firewall("firewall28")
firewall28.calculate_crc("dummy data")

switch37 = Switch("switch37")
switch37.configure_device()
switch38 = Switch("switch38")
switch37.calculate_crc("dummy data")

loadbalancer47 = Loadbalancer("loadbalancer47")
loadbalancer47.configure_device()
loadbalancer48 = Loadbalancer("loadbalancer47")
loadbalancer47.calculate_crc("dummy data")