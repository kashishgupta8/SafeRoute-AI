# SafeRoute AI - Pseudocode Logic

def SafelyProcessMetroEvent(event):
    if event.type == "check_in":
        message = f"User has safely checked IN at {event.location} at {event.time}."
    elif event.type == "check_out":
        message = f"User has checked OUT and left {event.location} at {event.time}."
    else:
        message = "Unknown metro event received."

    send_notification_to_family(message)



def send_notification_to_family(text):
    # Make.com handles actual sending
    return f"Notification sent: {text}"
