def dragon_solution(is_dead, number_of_cows):
    fat_alive_cow_index = 0 #left
    thin_alive_cow_index = number_of_cows - 1 #right
    
    while (fat_alive_cow_index + 1) <= thin_alive_cow_index: 
        middle_cow = int((fat_alive_cow_index + 
                          thin_alive_cow_index) / 2)
        if is_dead(middle_cow):
            fat_alive_cow_index = middle_cow + 1
        else:
            thin_alive_cow_index = middle_cow
    
    return fat_alive_cow_index