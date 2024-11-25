class Car:
  def __init__(self, make, model, year, odometer_reading=0):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = odometer_reading

  def get_description(self):
    long_description = {self.year} {self.make} {self.model}

  def read_odometer(self):
    print("This car {self.odometer_reading} miles on the odometer reading.")

  def update_odometer(self, mileage):
    self.odometer_reading = mileage

  odometer_reading = 0
