class CPU:
    def __init__(self, name, fr=None):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = len(mem_slots)
        self.mem_slots = mem_slots

    def get_config(self):
        a = f'Материнская плата:  {self.name}'
        b = f'Центральный процессор: {self.cpu.name}, {str(self.cpu.fr)}'
        c = f'Слотов памяти: {str(self.total_mem_slots)}'
        d = 'Память: '
        f = [i.name + ' - ' + str(i.volume) for i in self.mem_slots]
        return [a, b, c, d + '; '.join(f)]


cpu = CPU('Xeon', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])
print(mb.get_config())
