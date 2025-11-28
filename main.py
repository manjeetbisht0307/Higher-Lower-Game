import random
import art
import game_data


def front(dis1):
    """It prints 1 Object for comparison """
    return f"Compare A: {dis1['name']}, a {dis1['description']} from {dis1['country']}"
def front2(dis2):
    """It prints 2 Object for comparison"""
    return f"Against B: {dis2['name']}, a {dis2['description']} from {dis2['country']}"



real=True


comp1=random.choice(game_data.data)#3
comp2=random.choice(game_data.data)#4

print(art.logo)
print(front(comp1))
print(art.vs)
print(front2(comp2))



score = 0
while real:
    new_front = comp2
    user_input = input("Who has more followers? Type 'A' or 'B':").lower()

    if user_input=="a" and comp1["follower_count"]>comp2["follower_count"]:

        score += 1
        print("\n"*10)
        print(f"{art.logo} \n You're right , Total score: {score}\n {front(new_front)}")
        comp3=random.choice(game_data.data)
        print(f"{art.vs} \n {front2(comp3)}")
        comp1=comp2
        comp2=comp3
    elif user_input=="b" and comp1["follower_count"]<comp2["follower_count"]:

        score += 1
        print("\n" * 10)
        print(f"{art.logo} \n You're right , Total score: {score}\n {front(new_front)}")
        comp3 = random.choice(game_data.data)
        print(f"{art.vs} \n {front2(comp3)}")
        comp1 = comp2
        comp2 = comp3
    else:
        print("\n"*10+f"{art.logo} \n Sorry, that's wrong. Final score: {score}")
        real=False












