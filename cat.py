class Car:
    def __init__(self,regno,no_gears):
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False
    def start(self):
        if self.is_started:
            print(f"car already started")
        else:
            print(f"{self.regno} started...")
            self.is_started = True
    def stop(self):
        if self.is_started:
            print(f"{self.regno} stopped...")
            self.is_started = False
        else:
            print(f"{self.regno} already stopped...")
    def change_gear(self):
        if self.is_started:
            print(f"{self.regno} changed gear...")
        else:
            print(f"{self.regno} already stopped cannot change gear...")
