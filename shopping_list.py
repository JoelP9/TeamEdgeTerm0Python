#********************************************************************
#
#  Team Edge List Mini-project: THE SHOPPING LIST HELPER
#
#  This project prompts users using input() to prompt users
#  to add (or remove) items from a shopping list. It starts empty
#  and each time the program is run it asks you to either add or
#  remove an item from the list. It also updates the user of its
#  contents. The shopping list also checks to see if an item
#  is already present in the list and prevents you from adding it
#  again, giving feedback along the way.
#
# ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)
# "That will be it" means loop termination

#-->Todo: declare a shopping_list list
shopping_list = []

def prompt_user(check_answer):
  reply = input("What do you want to add or remove?  >>  ")
  reply_list = reply.split(" ")
  action = reply_list[0]
  item = reply_list[1]
  # return reply
  return action + " " + item
  
def check_answer(ans):
  is_this_your_item = input("Are you sure you want to           add/remove this?")
  if is_this_your_item == "no":
    print(prompt_user)
  else:
    if 
    
    
      
def add_item(item):
  #this function can take in a string and store it in an array
  if shopping_list.count(item) >= 1:
    return "This item is already in the shopping list"
  else: 
    shopping_list.append(item)
  return "Item added!"

def remove_item(item):
    if shopping_list.count(item) >= 1:
      shopping_list.remove(shopping_list.getIndex(item))
    else:
      return "Please enter in an existing item to remove!"

def print_shopping_list(): 
  print(str(shopping_list))

while active:
  check_answer(prompt_user()) 
  #this makes the program continously prompt and check     
  # response while the boolean 'active' returns True
  # add *item*
  if str(order) == "That will be it":
    active = False
    print("Shopping list finished. Ok, Here is your list!")
    break
  elif str(order) == "Show shopping list":
    print_shopping_list()
  elif str

print_shopping_list()