import itertools

# Example password list (this can be a more complex list like RockYou.txt)
wordlist = ['123456', 'password', 'letmein', '12345', 'qwerty']

def brute_force_password_crack(target_password):
    print(f"Starting to crack the password: {target_password}\n")
    for guess in wordlist:
        print(f"Trying password: {guess}")
        if guess == target_password:
            print(f"\nPassword cracked! The password is: {guess}")
            break
    else:
        print("Password not found in the wordlist.")

# Example usage:
# You can change the target_password to any string you want to test
target_password = 'letmein'  # The password you are testing
brute_force_password_crack(target_password)
