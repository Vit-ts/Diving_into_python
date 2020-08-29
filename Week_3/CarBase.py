import os
import csv
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        root_ext = os.path.splitext(self.photo_file_name)[1]
        if root_ext == '.jpeg' or root_ext == '.png' or root_ext == '.gif' or root_ext == '.jpg':
            return root_ext

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count, car_type=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying) 
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl, body_length=None, body_width=None, body_height=None, car_type=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.body_whl = body_whl
        try:
            count = self.body_whl.index("x") 
            count_1 = self.body_whl.index("x", count + 1)
            self.body_length = float(self.body_whl[0:count])
            self.body_width = float(self.body_whl[count + 1 : count_1])
            self.body_height = float(self.body_whl[count_1 + 1 : len(self.body_whl)])
        except:
            self.body_length, self.body_width,self.body_height, self.body_whl = 0.0, 0.0, 0.0, 0.0   
        self.car_type = "truck"

    def get_body_volume(self):
        
        a = self.body_width * self.body_height * self.body_length
        return a

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra, car_type=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying) 
        self.extra = extra
        self.car_type = "spec_machine"

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 7:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if brand != '' and car_type != '' and photo_file_name != '':
                    if os.path.splitext(photo_file_name)[1] == '.jpg' or os.path.splitext(photo_file_name)[1] == '.jpeg' or os.path.splitext(photo_file_name)[1] == '.png' or os.path.splitext(photo_file_name)[1] == '.gif':
                        if car_type == 'car' and passenger_seats_count != '':  
                            try:
                                car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count, car_type))
                            except:
                                None
                        elif car_type == 'truck':  
                            try:                  
                                car_list.append(Truck(brand, photo_file_name, carrying, body_whl,car_type))
                            except:
                                None
                        elif car_type == 'spec_machine' and extra != '':                    
                            try:
                                car_list.append(SpecMachine(brand, photo_file_name, carrying, extra, car_type))
                            except:
                                None
    return car_list