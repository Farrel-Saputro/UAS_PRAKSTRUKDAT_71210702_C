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
        
    def printAll(self) -> None:
        print("=== Prioritas : Tugas ===")
        for i in range(0, len(self._size) - 1):
            print(f"[{i+1}] : {self._data[i]}")
        print(self.data[-1])

    def _addHead(self, newNode) -> None:
        if self.isEmpty():
            self._head(newNode)

    def _addTail(self, newNode) -> None:
        if self.isEmpty():
            self._tail(newNode)

    def _addMiddle(self, newNode) -> None:
        if self.isEmpty():
            self._head(newNode)

    def add(self, data, priority) -> None:
        if self.isEmpty():
            self._tail.append((data, priority))
        else:
            bantu = 0
            while self._data[bantu][1] != priority:
                bantu += 1
            self._data.insert(bantu, (data, priority))

    def remove(self) -> None:
        self._head.pop(0)
        for i in range(0, len(self._size) - 1):
            print(f"Menghapus [{i}] : {self._head}")

    def removePriority(self, priority) -> None:
        bantu = 0
        while self._data[bantu][1] != priority:
            bantu += 1
        self._data.pop(bantu)

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
    tugasKu.removePriority(2)
    tugasKu.removePriority(4)
    
    tugasKu.printAll()