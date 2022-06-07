secret_message = input().split()

for word in secret_message: 
    chrs = ""
    dig = ""
    for char in word: 
        if char.isdigit(): 
            dig += "".join(char)
        if char.isalpha(): 
            chrs += "".join(char)
    decip_dig = chr(int(dig)) 
    if len(chrs) > 1:
        decip_chrs = chrs[-1:] + chrs[1:-1] + chrs[:1] 
    else:
        decip_chrs = chrs 

    print("".join(decip_dig+decip_chrs), end=" ")
