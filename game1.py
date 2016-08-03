
print "Hi. Do you want to play, 'Guess the number'?"
print "'yes' or 'no'"
ans = raw_input("> ")
if ans == 'yes':
        print "Great! Let's get started. Pick a number from 1 to 3."

        num = raw_input("> ")

        if num == "1":
            print "You win a special prize!!!"
            print "Now, it's time to pick your prize. Ready?"
            print "Pick a number from 1 to 4."
            num = raw_input("> ")

            if num == "1":
                    print "You win a 2016 Mercedes Benz."
            if num == "2":
                    print "You win a 2016 Roles Royce."
            if num == "3":
                    print "You win a one week vacation to Germany."
            if num == "4":
                    print "You win a one day get-away to Orlando with Steve."

        elif num == "2":
            print "You get a small gift."
            print "Now, you can choose the small gift or receive money."
            print "Either answer 'gift' or 'money'."
            num2 = raw_input("> ")

            if num2 == "gift":
                print "You get a shiny apple."
            if num2 == "money":
                print "You get one hundred dollars."
            

        else:
            print "Sorry, you don't win anything (sniff!)."

if ans == 'no':
     print "No problem. Have a great day."
        

            
         
    

    
