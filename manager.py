from cat import Car
bmw = Car("KA013060",5)
bmw1 = Car("KA013061",4)
bmw2 = Car("KA013062",5)
bmw.start()
bmw1.start()
bmw2.start()
bmw.change_gear()
bmw.change_gear()
bmw1.change_gear()
bmw1.change_gear()
bmw1.change_gear()
bmw.change_gear()
bmw.stop()
lst=[bmw,bmw1,bmw2]
print(len(list(filter(lambda x: x.is_started and x.c_gear == 0,lst))))