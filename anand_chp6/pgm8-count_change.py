#write a function count_change to count the number of ways to change any given amount

def count_change(amount,ways):
   """Return the number of ways to change the amount using given coins."""
   if amount == 0:
      return 1
   if amount < 0 or len(ways) == 0:
      return 0
   n = ways[0]
   return count_change(amount,ways[1:]) + count_change(amount-n,ways)
ways=(1,5,10,25,50)
print count_change(100,ways)
