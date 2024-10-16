def is_palindrome(s):
    return s == s[::-1]

def min_shifts_to_palindrome(s):
    n = len(s)
    
    if is_palindrome(s):
        return 0  # Already a palindrome
    
 
    for shifts in range(1, n):
        s = s[1:] + s[0]  # Cyclic shift from the head
        if is_palindrome(s):
            return shifts
    
    return -1  

def main():
  
    T = int(input().strip())
    

    for _ in range(T):
        s = input().strip()
        print(min_shifts_to_palindrome(s))

if _name_ == "_main_":
    main()