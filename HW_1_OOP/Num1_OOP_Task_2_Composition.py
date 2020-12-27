class System:
    def __init__(self, name):
        self.name = name


class Laptop:
    def __init__(self):
        name = System('Ubuntu')
        name2 = System('Windows 10')
        name3 = System('Mac OS')
        self.operating_system = [name, name2, name3]

    def system_config(self):
        for config in self.operating_system:
            print(config.name)


if __name__ == '__main__':
    laptop = Laptop()
    laptop.system_config()