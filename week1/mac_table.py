mac_table = {
    "00:11:22:33:44:55": "Ethernet0",
    "00:11:22:33:44:66": "Ethernet4",
    "00:11:22:33:44:77": "Ethernet8",
}

print(mac_table.get("00:11:22:33:44:70"))
print(mac_table.get("00:11:22:33:44:70", "NOT FOUND"))

mac_table["00:11:22:33:44:88"] = "Ethernet12"

print(mac_table)
print(len(mac_table))

del mac_table["00:11:22:33:44:55"]

print(mac_table)
print(len(mac_table))

print("00:11:22:33:44:66" in mac_table)
print("00:11:22:33:44:55" in mac_table)
