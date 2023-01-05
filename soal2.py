class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None
class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
    def isEmpty(self) -> bool:
        return self._size == 0
    def printAll(self):
        helper = self._head
        print("=== Prioritas : Tugas ===")
        while helper != None:
            print(f'[{helper._priority}] {helper._data}')
            helper = helper._next
        print()
    def _addHead(self, newNode):
        helper = self._head
        while newNode._next._priority == helper._priority:
            helper._next
        helper2 = helper._next
        helper._next = newNode
        helper2._prev = newNode
        newNode._next = helper2
        newNode._prev = helper
        self._size = self._size + 1

    def _addTail(self, newNode) -> None:
        newNode = self._tail._next
        newNode._prev = self._tail
        self._tail = newNode
        self._size = self._size + 1

    def _addMiddle(self, newNode) -> None:
        helper = self._tail
        while newNode._priority < helper._priority:
            helper = helper._prev
        helper2 = helper._next
        helper._next = newNode
        newNode._next = helper2
        newNode._prev = helper
        helper2._prev = newNode
    def add(self, data, priority):
        baru = Node(data, priority)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._size = self._size + 1
            #print(self._size)
        elif self._size == 1:
            if self._head._priority >priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
            self._size = self._size + 1
        else:
            if baru._priority == self._head._priority:
                self._addHead(baru)
            elif baru._priority == self._tail._priority:
                self._addTail(baru)
            else:
                self._addMiddle(baru)
        

    def remove(self) -> None:
        if self.isEmpty == False:
            ete = self._head
            self._head = self._head._next
            self._head._prev = None
            print(f'Menghapus[{ete._priority}] : {ete._data}')
            del ete
        else:
            print('Sudah tidak ada tugas yang bisa dihapus')
    def removePriority(self, priority) -> None:
        if self.isEmpty == True:
            print("")
        else:
            helper = self._head
            counter = 1
            guh = True
            while helper != self._tail:
                if helper._priority == priority:
                    guh = False
                helper = helper._next
            if helper._priority == priority and self._tail._priority != priority:
                helper2 = self._head
                while helper2._priority == priority:
                    helper2 = helper2._next
                    counter = counter + 1
                self._head = helper2
                self._size = self._size -1 - counter
            elif helper._priority != priority and self._tail._priority == priority:
                helper = self._tail
                while helper._priority == priority:
                    helper = helper._prev
                    counter = counter + 1
                helper._next = None
                self._tail = helper
                self.size = self._size - counter
            
            else:
                print(f'Tidak terdapat tugas prioritas {priority}')




 #isi kode anda
        pass
if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 5)
 tugasKu.add("Cuci Baju", 4)
 tugasKu.add("Beli Alat Tulis", 3)
 tugasKu.add("Cuci Sepatu", 4)
 tugasKu.printAll()
 tugasKu.remove()
 tugasKu.printAll()
 #tugasKu.removePriority(2)
 #tugasKu.removePriority(4)
 #tugasKu.printtAll()