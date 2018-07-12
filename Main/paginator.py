

class MyPaginator:
    def __init__(self, items, page_size, current, path):
        self.page_size = page_size
        self.path = path
        self.length = len(items)
        #self.items = items
        self.num_pages = self.length // self.page_size
        if (self.length / self.page_size) > (self.length // self.page_size):
            self.num_pages += 1

        self.current = current
        if self.current > self.num_pages:
            self.current = self.num_pages

        self.offset = self.page_size * (self.current - 1)
        self.top = self.offset + self.page_size
        if self.top > self.length:
            self.top = self.length


    def has_next(self):
        return self.current < self.num_pages
    

    def has_prev(self):
        return self.current > 1
    

    def pages(self):
        return list(range(1, self.num_pages + 1))


    def prev(self):
        if self.has_prev():
            return self.current - 1
        else:
            return -1


    def next(self):
        if self.has_next():
            return self.current + 1
        else:
            return -1
