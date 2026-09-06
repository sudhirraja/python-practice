ports = ["Ethernet0", "Ethernet4", "Ethernet8", "Ethernet12"]

print(ports)
print(len(ports))
print(ports[0])
print(ports[2])

print(ports[-1])
print(ports[-2])
print(ports[1:3])

print(ports[0:2])
print(ports[2:4])
print(ports[:2])
print(ports[2:])

#print(ports[4])      # IndexError — crashes
print(ports[2:100])  # no error — gives you what exists

for port in ports:
    if port == "Ethernet8":
        print(f"{port} - SKIP, reserved")
    else:
        print(f"{port} - configure")


enabled_ports = []

for port in ports:
    if port != "Ethernet8":
        enabled_ports.append(port)

print(enabled_ports)
print(len(enabled_ports))
      



