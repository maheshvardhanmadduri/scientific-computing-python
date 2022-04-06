class Category:
  
  def __init__(self, categories):
    self.categories = categories
    self.ledger = []
    self.spent = 0
    self.percentage_spent = 0

  def __str__(self):
    categories_length = len(self.categories)
    output = ""
    
    #First Line
    for i in range(0, int((30-categories_length)/2)):
      output += "*"
    if (categories_length % 2) != 0:
      output += "*"
    output += self.categories
    for i in range(0, int((30-categories_length)/2)):
      output += "*"
    output += "\n"

    #Description + Amount
    line = []
    for i in self.ledger:
      line = i['description'][0:23]
      for j in range(len(line), 23):
        line += " "

      amt = str("{:.2f}".format(i['amount']))   
      for j in range(0, 7 % len(amt)):
        line += " "
      line += amt + "\n"
      output += line
  
    #Category Total Balance
    output += "Total: " + str(self.get_balance())
    
    return output

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.spent += -amount
      return True
    else:
      return False
  
  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i['amount'] 
    return balance

  def transfer(self, amount, budget_dest):
    if self.withdraw(amount, "Transfer to " + budget_dest.categories):
      budget_dest.deposit(amount, "Transfer from " + self.categories)
      return True
    else:
      return False
  
  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False
  
def create_spend_chart(categories):
  
  total_spent = 0
  for i in categories:
    total_spent += i.spent

  for i in categories:
    i.percentage_spent = int(i.spent*100/total_spent) 

  output = "Percentage spent by category\n"
  for i in range (100, -1, -10):
    output += str(i).rjust(3) + "| "
    for j in categories:
      if j.percentage_spent >= i:
        output += "o  "
      else:
        output += "   "
    output += "\n"

  output += "    -"
  for i in range(0, len(categories)):
    output += "---"
  output += "\n"

  #List Comprehension - max len of categories name
  max_len_categories_name = max([len(i.categories) for i in categories])
  
  for i in range(0, max_len_categories_name):
    output += "     "
    for j in categories:
      if i < len(j.categories):
        output += j.categories[i] + "  "
      else:
        output += "   "
    if i != max_len_categories_name - 1:
      output += "\n"

  return output