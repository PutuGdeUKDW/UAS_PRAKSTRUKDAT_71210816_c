class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
    def getNamaPelanggan(self):
        return self._namaPelanggan

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0

    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelangkangnya
        if self.is_empty():
            return 'Kosong'
        guh = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) %len(self._data)
        self._size =- 1
        print(f"### Pelanggan {guh.getNamaPelanggan()} Selesai Membayar ###")

        poi = [None]*len(self._data)
        counter = 0
        for i in range(len(self._data)):
            if self._data[i] != None:
                poi[counter]=self._data[i]
                counter += 1
        self._data = poi
        self._front = 0


    def enqueue(self, namaPelanggan): #menambah data ke list
        newCust = NodePelanggan(namaPelanggan)
        if self._size == self.DEFAULT_CAPACITY:
            self.resizeBy3()
        #empSeat = (self._front+self._size)%len(self._data)
        self._data.insert(self._size,newCust)
        #print(self._size)
        if self._data[-1] == None:
            del self._data[-1]
        self._size = self._size + 1
    def resizeBy3(self): #menambah ukuran queue sebesar 3

        for i in range(3):
            self._data.append(None)
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY + 3
        print("### Melakukan Resize 3 ###")


    def printAll(self):
        print("=== WarungMakan ===")
        #print(self._data)
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")
        print()
# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()