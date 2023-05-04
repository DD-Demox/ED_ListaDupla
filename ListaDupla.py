class NodeDouble:
    def __init__(self, data, next_node=None, before_node=None):
        self.data = data
        self.before_node: NodeDouble = before_node
        self.next_node: NodeDouble = next_node

    def __repr__(self):
        if self.next_node is None:
            return f"{self.data}"
        else:
            return f"{self.data}, {self.next_node}"


class ListaDupla:

    def __init__(self):
        self.head: NodeDouble = None
        self.tail: NodeDouble = None

    def __repr__(self):
        return f"[{self.head}]"

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        assert self.head, "Empty list"
        if self.current is not None:
            data = self.current.data
            self.current = self.current.next_node
            return data
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.__find(item).data

    def append(self, data):
        new_node = NodeDouble(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.before_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def __remove_node(self, node: NodeDouble):
        if node == self.head:
            self.head = self.head.next_node
            self.head.before_node = None
            if self.head.next_node is None:
                self.tail = self.head
            return node.data
        elif node == self.tail:
            self.tail = self.tail.before_node
            self.tail.next_node = None
            if self.tail.before_node is None:
                self.head = self.tail
            return node.data
        else:
            node_before = node.before_node
            node.before_node.next_node = node.next_node
            node.next_node.before_node = node_before
            return node.data

    def pop(self, position: int = -1):
        assert self.head, "Cant remove from empty list"
        self.__remove_node(self.__find(position))

    def __find(self, position: int):
        if position >= 0:
            current = self.head
            current_index = 0
            while current_index != position:
                assert current, "List index out of range"
                current = current.next_node
                current_index = current_index.__add__(1)
            return current
        else:
            current = self.tail
            position = position * -1
            current_index = 1
            while current_index != position:
                assert current, "List index out of range"
                current = current.before_node
                current_index = current_index.__add__(1)
            return current

    def clear(self):
        self.head = None
        self.tail = None

    def insert(self, position, data):
        current = self.__find(position)
        if current == self.tail:
            self.append(data)
        elif current == self.head:
            new_node = NodeDouble(data)
            new_node.next_node = current
            self.head = new_node
            current.before_node = new_node
        else:
            new_node = NodeDouble(data)
            new_node.next_node = current
            new_node.before_node = current.before_node
            new_node.before_node.next_node = new_node
            new_node.next_node.before_node = new_node

    def count(self, element):
        assert self.head, "Empty List"
        count = 0
        current = self.head
        while current:
            if current.data == element:
                count += 1
            current = current.next_node
        return count

    def extend(self, list_to_extend):
        for i in list_to_extend:
            self.append(i)

    def index(self, data):
        assert self.head, "Empty List"
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            index = index.__add__(1)
            current = current.next_node
        raise ValueError(f"{data} is not in the list")

    def remove(self, data):
        assert self.head, "Empty List"
        current = self.head
        while current:
            if current.data == data:
                return self.__remove_node(current)
            current = current.next_node
        raise ValueError("Data not in list")

    def reverse(self):
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = current.before_node
            current.before_node = next_node
            current = next_node
        head = self.head
        self.head = self.tail
        self.tail = head
