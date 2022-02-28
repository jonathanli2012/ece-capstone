class queue_struct:
  def __init__(self, max_size):
    self.max_size = max_size
    self.queue = [None] * max_size
    self.head_index = 0
    self.tail_index = 0
    self.current_len = 0

  def enqueue_front(self, data_packet):
    new_index = (self.tail_index + 1) % self.max_size
    self.current_len += 1
    self.head_inex = new_index
    self.queue[new_index] = data_packet
    pass

  def enqueue_rear(self, data_packet):
    new_index = (self.tail_index + 1) % self.max_size
    self.current_len += 1
    self.tail_index = new_index
    self.queue[new_index] = data_packet
    return

  def dequeue_front(self):
    new_index = (self.tail_index + 1) % self.max_size
    self.current_len -= 1
    self.head_index = None
    return self.queue[new_index]

  def dequeue_rear(self):
    new_index = (self.tail_index + 1) % self.max_size
    self.current_len -= 1
    self.head_index = None
    return self.queue[new_index] 
  
  def clear_queue(self):
    self.head_index = 0
    self.tail_index = 0
    self.current_len = 0
    self.queue = [None] * self.max_size
  
  def cpy_queue(self):
    return None
  
p1 = queue_struct(512)