#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.

class reverse_iter:
  def __init__(self,n):
    self.i=n
    self.n=n
  def next(self):
    if self.i>=0:
      i=self.i
      self.i-=1
      return i
    else:
      raise StopIteration()
y=reverse_iter(5)
for j in range(5):
  print y.next()
