class Laptop:
    def __init__(self, brand, model, os, ram, hdd, ssd, screen, keyboard, price):
        self.brand = brand
        self.model = model
        self.os = os
        self.ram = ram
        self. hdd = hdd
        self.ssd = ssd
        self.screen = screen
        self.keyboard = keyboard
        self.price = price
        self.info = f"Brand:{brand} Model:{model} OS:{os} RAM:{ram}Gb HDD:{hdd}Gb SSD:{ssd}Gb Screen:{screen}in Keyboard:{keyboard} Price:${price}"
        self.is_on = False
        self.window_open = False

    def power_on(self):
        self.is_on = True
        return f"The PC is on"

    def power_off(self):
        self.is_on = False
        return f"The PC is off"

macbook_air_1 = Laptop("Apple", "Macbook Air 1", "IOS 24", 16, 0, 250, 14, "QWERTY", 1450)
dell_latitude_4450 = Laptop("Dell", "Latitude 4450", "Windows 11", 16, 500, 250, 16, "QWERTY", 950 )
acer_gamer = Laptop("Acer", "Nitro 1", "Windows 11", 32, 1000, 500, 16, "QWERTY", 1250 )

print(macbook_air_1.info)

