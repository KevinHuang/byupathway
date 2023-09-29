

def stage1():
    action_stage = input('You need to reach Tokyo Tower as quickly as possible. You have two transportation options in front of you - taking a plane or taking a boat. Which one would you choose? (boat/airplane)')
    if (action_stage.lower() == 'boat'):
        print("ಥ_ಥ, I'm sorry, taking the boat is too slow, and you won't make it to Tokyo in time. You're out of the game.");
        return
    elif (action_stage.lower() == 'airplane'):
        stage2()
    else:
        print("ಥ_ಥ, You chose a non-existent mode of transportation. You're out of the game.");
        return
    

def stage2():
    print('------')
    action_stage = input('You have arrived at the airport, and now you have two transportation options: a bus or a high-speed train. Which one would you choose? (bus/train)')
    print('')
    if (action_stage.lower() == 'bus'):
        print("ಥ_ಥ, I'm sorry, taking the bus is too slow, and you won't make it to Tokyo in time. You're out of the game.");
        return
    elif (action_stage.lower() == 'train'):
        stage3()
    else:
        print("ಥ_ಥ , You chose a non-existent mode of transportation. You're out of the game.");
        return
    
def stage3():
    print('------')
    action_stage = input('You have arrived in Tokyo, and now you have two transportation options: a taxi or the Shinkansen (bullet train). Which one would you choose to get to Tokyo Tower the fastest? (taxi/train)')
    print('')
    if (action_stage.lower() == 'taxi'):
        print("ಥ_ಥ, Tokyo city is congested with traffic, and a taxi is not the fastest mode of transportation. I'm sorry, but you have failed!");
    elif (action_stage.lower() == 'train'):
        print("ʘ‿ʘ Congratulations on arriving at Tokyo Tower in time and completing the mission!");
    else:
        print("ಥ_ಥ, You chose a non-existent mode of transportation. You're out of the game.");
    
stage1()