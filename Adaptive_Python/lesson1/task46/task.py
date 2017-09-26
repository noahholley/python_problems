class Buffer:
    def __init__(self):
        self.b = []

    def add(self, *a):
        for number in a:
            self.b.append(number)
            if len(self.b) >= 5:
                print(sum(self.b[0:5]))
                del self.b[0:5]

    def get_current_part(self):
        return self.b

#buf = Buffer()
#buf.add(1, 2, 3)
#buf.get_current_part() # return [1, 2, 3]
#buf.add(4, 5, 6) # print(15) – output of the sum of the first five elements
#buf.get_current_part() # return [6]
#buf.add(7, 8, 9, 10) # print(40) – output the sum of the second five elements
#buf.get_current_part() # return []
#buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – output the sum of the third and fourth five elements
#buf.get_current_part() # return [1]
