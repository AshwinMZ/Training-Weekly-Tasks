def get_next_queue_position(current_position):
    "Returns the next reservation queue position."

    if current_position < 0:
        return "Invalid queue position"
    return current_position + 1


# Boundary value test
print(get_next_queue_position(0))