ip={"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for item in ip:
    print (item)
print ('---------------------------------------------------------------------------')
for accesspoints,accessport in ip.items():
    print(f'After iterating we got accesspoints and accessports as {accesspoints} and {accessport}')