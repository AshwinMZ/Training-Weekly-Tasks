class ReservationQueue:

    def __init__(self, current_position):
        self.current_position = current_position

    def get_next_queue_position(self):
        try:
            if not isinstance(self.current_position, int):
                raise TypeError("Queue position must be an integer")

            if self.current_position < 0:
                raise ValueError("Queue position cannot be negative")

            return self.current_position + 1

        except TypeError as error:
            return f"Error: {error}"

        except ValueError as error:
            return f"Error: {error}"


# Create first object
queue_1 = ReservationQueue(3)

# Create second object
queue_2 = ReservationQueue(7)


# Test the objects
print("Next position in Queue 1:", queue_1.get_next_queue_position())

print("Next position in Queue 2:", queue_2.get_next_queue_position())


# Test error handling
invalid_queue = ReservationQueue("three")

print(invalid_queue.get_next_queue_position())