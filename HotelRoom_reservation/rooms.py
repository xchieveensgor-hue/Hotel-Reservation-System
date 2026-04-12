class Room:
    def __init__(self, room_type="Standard", rate=50, nights=1, discount=0):
        self.room_type = room_type
        self.rate = rate
        self.nights = nights
        self.discount = discount
    def calculate_cost(self, extra_fee=0):
        base = self.rate * self.nights
        return (base - self.discount) + extra_fee
    def get_details(self):
        return f"{self.room_type}: {self.nights} nights @ RM{self.rate}/night"
class DeluxeRoom(Room):
    def __init__(self, nights=1):
        super().__init__("Deluxe", 150, nights, 15)