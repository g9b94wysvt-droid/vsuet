def process_numbers():
    num = int(input())
    if num == 0:
        return
    
    static_counter = 0
    
    def recursive_print(current_num):
        nonlocal static_counter
        
        if current_num == 0:
            return
        
        if static_counter % 2 == 0:
            print(current_num)
            
        static_counter += 1
        next_num = int(input())
        recursive_print(next_num)

    recursive_print(num)

process_numbers()
