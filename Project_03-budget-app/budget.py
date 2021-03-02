class Category:  

  def __init__(self, name):
    self.name = name
    self.ledger = []

  # when print() is called
  def __str__(self):
    return print_budget(self)  

  def deposit(self, amount, *description): 
    if type(description) == tuple:
      description = ''.join(description)     
    self.ledger.append({"amount": amount, "description": description})
    
  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else:      
      return False

  def withdraw(self, amount, *description):
    if type(description) == tuple:
      description = ''.join(description)
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to %s" % category.name)
      category.deposit(amount, "Transfer from %s" % self.name)
      return True
    else:
      return False

  def get_balance(self):
    sum = 0.0 
    for transaction in self.ledger:
      sum = sum + float(transaction["amount"])
    return round(sum, 2)

  # sum of all deposits
  def get_budget_total(self):
    budget_total = 0.00
    for transaction in self.ledger:
      if transaction["amount"] > 0:
        budget_total = budget_total + float(transaction["amount"])
    return budget_total

  # sum of all withdrawals
  def get_budget_spent(self):
    budget_spent = 0.00
    for transaction in self.ledger:
      if transaction["amount"] < 0:
        budget_spent = budget_spent - float(transaction["amount"])
    return budget_spent

# creates budget printout row by row 
def print_budget(self):
  budget_rows = []

  # create category title with title centered
  line_characters = 30
  line_filler_char = "*"

  title_name_length = len(self.name)
  title_padding = floor(
      (line_characters-title_name_length) / 2
    )
  title_extra_chars = line_characters - title_name_length - title_padding*2

  title = line_filler_char * title_padding + self.name + line_filler_char * title_padding + line_filler_char * title_extra_chars + "\n"

  budget_rows.append(title)  

  
  # create ledger entries 
  for transaction in self.ledger:
    # format description to be presentable
    description = ''.join(transaction["description"]) # make the description more clean
    description = description[0:23] # max 23 chars

    # format amount to be presentable
    amount = format(transaction["amount"], '.2f') # 2 decimal precision  
    amount = amount[0:7] # max 7 chars

    # calculate empty space in a row between description & amount
    entry_empty_space = line_characters - len(description) - len(amount)

    # add complete row 
    budget_rows.append(description + " " * entry_empty_space + amount + "\n")

  # total amount of money in ledger
  budget_rows.append("Total: " + str(self.get_balance()))

  # concatenate all rows to 1 string and return it 
  return concatenate_rows_to_string(budget_rows)

def create_spend_chart(categories):
  # transactionects provided so extract ledger names & length first
  list_of_categories = []
  list_of_category_name_lengths = []
  list_of_budget_spent = []
  chart_rows = []

  # collect data needed for drawing the bar chart
  for val in categories:
    list_of_categories.append(val.name)
    list_of_category_name_lengths.append(len(val.name))
    list_of_budget_spent.append(val.get_budget_spent())
  
  # title row
  chart_rows.append("Percentage spent by category\n")

  # percentage rows
  for row in reversed(range(0,110,10)):
    # create bar chart row
    temp_row = " "
    for i in range(0,len(list_of_categories),1):
      spent_percentage = round_down(floor(
        (list_of_budget_spent[i]/sum(list_of_budget_spent))*100
      ), 10)

      if row <= spent_percentage:
        temp_row = temp_row + "o  "
      else:
        temp_row = temp_row + "   "

    chart_rows.append(str(row).rjust(3, " ") + "|" + temp_row + "\n")

  # spacer row
  chart_rows.append("    -" + "---" * len(list_of_categories) + "\n")

  # vertical category name rows
  for i in range(0,longest_str_in_list(list_of_categories),1):
    temp_row = "     "
    for j in range(0,len(list_of_categories),1):
      if list_of_category_name_lengths[j] > i:
        temp_row = temp_row + list_of_categories[j][i:i+1] + "  "
      else:
        temp_row = temp_row + "   "

    chart_rows.append(temp_row + "\n")

  # remove last line break here to make things simpler...
  return concatenate_rows_to_string(chart_rows).rstrip("\n")

def longest_str_in_list(list):
  longest = 0
  for val in list:
    if len(val) > longest:
      longest = len(val) 
  return longest

def concatenate_rows_to_string(rows):
  formatted_str = ""
  for row in rows:
    formatted_str = formatted_str + row
  return formatted_str

# math.floor implementation
def floor(n):
  return int(n - (n % 1))

# round down
def round_down(n, divisor):
    return n - (n % divisor)