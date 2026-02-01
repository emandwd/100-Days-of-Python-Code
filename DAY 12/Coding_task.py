''' SCOPE '''
''' local scope --> variable that is created inside the function not outside which mean something that is related to that function only 
--> you can only use it inside that function
 global scope --> variable that is created outside the function which means it is can be used anywhere in the code ---> inside or outside a function '''

game_level = 1
enemies = ["Skeleton", "Zombie", "ALien"]

def create_enemy() :
    new_enemy = " "
    if game_level < 5 :
        new_enemy = enemies[0]
    print(new_enemy)

player_health = 10 # global

def game():
    def drink_potion():
        player_health = 2 # local
        return print(player_health)  # it is terrible idea to call the local and global variables the same name
    drink_potion()
print(game())
print(player_health)

enemies = 1 # we want to tackle this variable

def increase_enemies():
    #  global enemies  --> we can use it but don't modify it with function that has local scope
    # enemies = 2 # and express it here
    print(f"enemies outside function: {enemies}")
    return enemies+1 # instead of global enemies and enemies = 2 , we use return enemies+1
increase_enemies()
print(f"enemies outside function: {enemies}")

google_url = "https://www.google.com/search?q="
def my_func():
    print(google_url)

''' this type of error that csn be caused from the global and local variable is named NameError '''

# quiz q3 :
# def bar():
#     my_variable = 9
#
#     if 16 > 9:   ---> this condidition is correct and it is in the same function so the variable named mu_variable will be 16 not 9
#       my_variable = 16
#
#     print(my_variable) ---> 16
#
# bar()  --> 16