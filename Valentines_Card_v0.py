#counts
hug_count = 1
total_hugs = 0
candy_count = 0
guess_count = 0
swing_count = 0

#tuples
good_responses = ("good","terrific","great","ok","fine","fantastic","wonderful","okay","better","calm","happy")
bad_responses = ("bad","awful","terrible","sad","lonely","depressed","angry","anxious","stressed","overwhelmed","worse","nervous")
other_responses = ("bloated","gassy","hungry","tired","sleepy")

ans_yes = ("yes","y","1","t")
ans_no = ("no","n","0","f")

#variables
cbee_mood = ""
card_open = "y"
hug_effective = "n"
candy_effective = "n"
coded_msg = "WANMZSTBVDCEHDJTRNPALADL"
hint = "HINT: WANM!ZSTBVDCE!HDJTRNPALADL!\n      CCCE!CCEEEEEE!CCCCCCEEEEEE!"
magic_response = "Wo Ai Ni Merlo Zhe shi the best valentines day card ever Hao de jin tian rang ni play apex legends all day long"
secret_esc = "close card"

#limits
hug_threshold = 3
candy_limit = 3
candy_secret_limit = 5
guess_limit = 10

#run this code as long as card is open
while card_open == "y":
    #initial input
    cbee_mood = input("\n\n\nHello CBee - Happy Valentine's day! What is one word to describe how you feel today?\n")
    while cbee_mood.lower() not in good_responses and cbee_mood.lower() not in bad_responses and cbee_mood.lower() not in other_responses:
        cbee_mood = input(f"\n\nSorry, I don't understand the word '{cbee_mood}' Please use another word to describe how do you feel.\n")


    # CBee in good mood - DONE
    if cbee_mood.lower() in good_responses:
        print(f"\n\n\n{cbee_mood.upper()}? WONDERFUL!")
        print("Makes sense: you're married to Merlo...")
        print("Happy V-Day!\n")

    #CBee in bad mood
    elif cbee_mood.lower() in bad_responses:
        #this needs to be reset to no each time cbee in bad mood
        hug_effective = "n"
        #ask questions
        input(f"\n\n\n{cbee_mood}? What's wrong? What are you thinking about? Please tell me more.\n")
        #offer hug
        hug = input("\n\nI'm sorry! That sounds awful! Would you like a hug from Merlo? Y or N?\n").lower()
        while hug not in ans_yes and hug not in ans_no:
            hug = input("\n\nPlease respond with Y or N\n")

        #count initial hug
        if hug in ans_yes:
            hug_count = 1
            total_hugs += 1

        #CBee want's a hug (within reason)
        while hug in ans_yes and hug_effective in ans_no and hug_count < hug_threshold:

            #re-assess hug effectiveness
            hug_effective = input("\n\n\nThere you go... I'm sure you're feeling better now? Y or N?\n").lower()
            while hug_effective not in ans_yes and hug_effective not in ans_no:
                hug_effective = input("\n\nPlease respond with Y or N\n").lower()

            #hug is enough - DONE
            if hug_effective in ans_yes:
                print("\n\n\nWONDERFUL!")
                print("Merlo's hugs are amazing. Happy V-Day!\n")
            
            #hug is not enough - offer another Hug
            elif hug_effective in ans_no:
                hug = input("\n\n\nNo? Would you like ANOTHER hug? Y or N?\n").lower()
                while hug not in ans_yes and hug not in ans_no:
                    hug = input("\n\nPlease respond with Y or N\n").lower()
                if hug in ans_yes:
                    hug_count += 1
                    total_hugs += + 1
                elif hug in ans_no:
                    hug = "n"

        #if hug count reaches limit - switch to candy
        if hug in ans_yes and hug_count == hug_threshold:

            #reassess final hug effectiveness
            hug_effective = input(f"\n\n\nThere... That's {total_hugs} hugs CBee! Is it working? Y or N?\n").lower()
            while hug_effective not in ans_yes and hug_effective not in ans_no:
                hug_effective = input("\n\nPlease respond with Y or N\n").lower()

            #if last hug is effective - DONE
            if hug_effective in ans_yes:
                print("\n\n\nFinally... ok Happy V-Day!\n")

            #if last hug is not effective - offer candy
            elif hug_effective in ans_no:
                candy = input("\n\n\nHmm, you're VERY needy... Let's try another approach. Would you like a Hi-Chew?\n").lower()
                while candy not in ans_yes and candy not in ans_no:
                    candy = input("\n\nPlease respond with Y or N\n").lower()

                #CBee wants candy
                if candy in ans_yes and candy_count < candy_limit:
                    
                    #count intial piece of candy
                    candy_count += 1

                    #reset to no as long as candy count < limit
                    candy_effective = "n"
                    
                    #limit candy
                    while candy in ans_yes and candy_effective in ans_no and candy_count < candy_limit:
                        
                        #assess candy effectiveness
                        candy_effective = input("\n\n\nDid that help? Y or N?\n").lower()
                        while candy_effective not in ans_yes and candy_effective not in ans_no:
                            candy_effective = input("\n\nPlease respond with Y or N\n").lower()
                        
                        #if candy works - DONE
                        if candy_effective in ans_yes:
                            print("\n\n\nHi-Chews are Great, huh!? You're welcome! Happy V-Day!\n")
                        
                        #candy is not enough - offer more candy
                        elif candy_effective in ans_no:
                            candy = input("\n\n\nNo? Would it help if I gave you ANOTHER Hi-Chew? Y or N?\n").lower()
                            while candy not in ans_yes and candy not in ans_no:
                                candy = input("\n\nPlease respond with Y or N\n").lower()
                            if candy in ans_yes:
                                candy_count += 1
                    
                    #if candy limit is reached - confirm that's the last one
                    if candy_count == candy_limit:    
                        confirm = input("\n\nLAST ONE, OK? Y or N?\n").lower()
                        while confirm not in ans_yes and confirm not in ans_no:
                            confirm = input("\n\nPlease respond with Y or N\n").lower()
                        
                        #if CBee doesn't agree - then she doesn't get the last Hi-Chew
                        if confirm in ans_no:
                            print("\n\nGreedy...No more for you!\n")
                            candy_count -= 1
                            candy_effective = "y"
                        #if final Hi-Chew is sufficient - recap everything CBee has received and close loop
                        elif confirm in ans_yes:
                            print(f"\n\n\nGreat! That's {total_hugs} hugs and {candy_count} Hi-Chews! One heck-of-a V-Day for CBee...!\n")
                            candy_effective = "y"
                
                #if candy limit is reached - turn down request for candy
                elif candy_count == candy_limit:
                    print(f"\n\nYou already got {candy_count} Hi-Chews... there's no more...")
                    #if secret limit hasn't been triggered, drop easter egg.
                    if candy_limit < candy_secret_limit:
                        print("(.............................or are they just hidden...?\n")
                
                #if CBee rejects candy - more for Merlo
                if candy in ans_no:
                    print("\n\nFine - more for Merlo...\n")

        #if CBee rejects hug - mean message
        if hug in ans_no:
            print("\n\nFine, Merlo doesn't want to hug you either!\n")

    #if CBee chooses joke response - stuuuupid
    elif cbee_mood.lower() in other_responses:
        print("\n\nSTOOOOO-PID...!")
        print("Hmm - did you hear something? Sounded like wrappers...")
        candy_limit = candy_secret_limit
    
    #ask CBee if she wants to close the card
    card_open = input("~~~ Would you like to update me on how you're feeling now? Y or N? ~~~\n").lower()
    while card_open not in ans_yes and card_open not in ans_no:
        card_open = input("\n\nPlease respond with Y or N\n").lower()
    if card_open in ans_yes:
        swing_count += 1
    
    #confirm once
    if card_open in ans_no:
        confirm1 = input("\n\nARE YOU SURE?\n").lower()
        while confirm1 not in ans_yes and confirm1 not in ans_no:
            confirm1 = input("\n\nPlease rsepond with Y or N\n").lower()

        #double confirm
        if confirm1 in ans_yes:
            confirm2 = input("\n\nVERY VERY SURE?\n").lower()
            while confirm2 not in ans_yes and confirm2 not in ans_no:
                confirm2 = input("\n\nPlease respond with Y or N\n").lower()

            #triple confirm
            if confirm2 in ans_yes:
                confirm3 = input("\n\nEXTRA VERY VERY SURE?\n").lower()
                while confirm3 not in ans_yes and confirm3 not in ans_no:
                    confirm3 = input("\n\nPlease respond with Y or N\n").lower()


                #special confirmation
                if confirm3 in ans_yes:
                    
                    #ask for decoded message
                    confirmS = input(f"\n\n\nTo confirm & EXIT: Please de-code the following message: {coded_msg} (Answer is NOT case-sensitive. Punctuation not required.)\n").lower()
                    
                    #track # of guess and then give a hit if it takes more than 10 tries
                    while confirmS != secret_esc and confirmS != magic_response.lower():
                        guess_count += 1
                        if guess_count < guess_limit:
                            confirmS = input(f"\n\n\nPlease de-code: {coded_msg} - (NO punctuation & NOT-case sensitive).\nAttempts: {guess_count}/{guess_limit}\n").lower()
                        elif guess_count >= guess_limit:
                            confirmS = input(f"\n\n\nPlease de-code: {coded_msg} - (NO punctuation & NOT-case sensitive).\nAttempts: {guess_count}/{guess_limit}\n"
                                f"BTW I was j/k... you have unlimited tries - GL!\n"
                                f"{hint}\n").lower()
                    
                    #print summary card benefit summary
                    if confirmS == magic_response.lower():
                        print(f"\n\n\nGreat! You have:\n"
                        f"Received {total_hugs} HUGS\n"
                        f"Received {candy_count} out of {candy_secret_limit} Hi-Chews\n"
                        f"Received 8 new pairs of Victoria's Secret underwear\n"
                        f"Experienced {swing_count} mood-swing(s)\n"
                        f"And now you're feeling {cbee_mood}...\n"
                        f"You also love me and want me to play Apex Legends all day today... I'll turn on the PS4!\n"
                        f"BEST Valentine's day card INDEED!\n")

                #re-opens card if 3rd confirm is not 'yes'
                elif confirm3 in ans_no:
                    card_open = "y"

            #re-opens card if 2nd confirm is not 'yes'
            elif confirm2 in ans_no:
                card_open = "y"

        #re-opens card if 1st confirm is not 'yes'
        elif confirm1 in ans_no:
            card_open = "y"



