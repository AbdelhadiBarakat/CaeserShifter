"""
Caesar Shifter

A Python-based encryption and decryption tool that implements the
Caesar cipher by shifting characters across a custom 95-character set
including letters, numbers, and symbols.
"""

def get_valid_boolean(question, true_value, false_value):
    """
    Prompts the user for a boolean input until they enter either the 'true_value' or 'false_value'.
    Returns the valid input as a string.
    """
    while True:
        user_input = input(question).lower().strip()
        if user_input == true_value or user_input == false_value:
            return user_input
        print(f"Invalid input. Please enter '{true_value}' or '{false_value}' only.\n")

def get_valid_number(question):
    """
    Prompts the user for a numeric input. Returns the integer if valid.
    """
    while True:
        try:
            user_input = int(input(question).strip())
            return user_input
        except ValueError:
            print("Invalid input. Please enter a numeric value using digits only (no decimals).\n")

def get_user_data(all_chars):
    # --- UX Headers and Spacing ---
    print("\n" + "="*35)
    print("      CIPHER ENCRYPTION TOOL")
    print("="*35)
    
    entered_word = input("➤ Enter message to process: ")
    entered_passcode = get_valid_number("➤ Enter your numeric passcode: ")
    
    # --- PROTECTED LOGIC: Original Key Reduction ---
    if entered_passcode > len(all_chars):
        new_key = entered_passcode // len(all_chars)
        entered_passcode = entered_passcode - (new_key * len(all_chars))
        
    return entered_word, entered_passcode

def run_cipher_process(word_to_shift, shift_key, all_chars):
    # --- UX Selection Menu ---
    print("\n" + "-"*35)
    print("        MODE SELECTION")
    print("-"*35)
    print("[1] Encrypt (Shift Forward)")
    print("[2] Decrypt (Shift Backward)\n")
    user_choice=get_valid_boolean("➤ Selection (1/2): ", "1", "2")

    encrypted_result_list = []
    
    for Letter in word_to_shift:
        if Letter in all_chars:
            if user_choice == "1":
                Letter_index = all_chars.index(Letter) + shift_key
            elif user_choice == "2":
                Letter_index = all_chars.index(Letter) - shift_key
            
            # --- PROTECTED LOGIC: Original Index Wrapping ---
            Letter_index = Letter_index % len(all_chars)
            # ------------------------------------------------
            
            encrypted_result_list.append(all_chars[Letter_index])
        else:
            # Keeps characters like emojis or tab spaces as they are
            encrypted_result_list.append(Letter)
    
    # --- UX Result Formatting ---
    print("\n" + "*"*35)
    print(f" FINAL OUTPUT: {''.join(encrypted_result_list)}")
    print("*"*35)
     
# --------------------------------------------------------------------
# CHARACTER SET (Collection)
# --------------------------------------------------------------------
all_chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' '
]

# --------------------------------------------
# MAIN PROGRAM EXECUTION
# --------------------------------------------
while True:
    current_input_data = get_user_data(all_chars)
    final_word = current_input_data[0]
    final_key = current_input_data[1]
    
    run_cipher_process(final_word, final_key, all_chars)
    
    print("\n" + "."*35)
    if get_valid_boolean("➤ Try again? (Yes/No): ", "yes", "no") == "no":
        break

print("\n[Program Terminated] Goodbye!")