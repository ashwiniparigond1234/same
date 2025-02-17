status = input("Enter status (online/offline): ")

tick_status = input("Enter tick status (single tick/double tick grey/double tick blue): ")

if status == "online" and tick_status == "double tick grey":
    print("They are ignoring your message.")
elif status == "online" and tick_status == "double tick blue":
    print("They have seen your message.")
elif status == "offline" and tick_status == "single tick":
    print("Message sent but not delivered.")
else:
    print("Invalid status or tick input.")