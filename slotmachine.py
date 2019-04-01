class Slot():
    def __init__ (self):
        self.a = Colum()
        self.b = Colum()
        self.c = Colum()
        self.purse = Purse()
        self.take_bet()
    
    def pull_handle (self):
        self.a.change_face()
        self.b.change_face()
        self.c.change_face()
    
    def show_slot (self):
        print("{}{}{}".format(self.a.face,self.b.face,self.c.face))
    
    def take_bet (self):
        print ("minimum bet is 2. Type \"N\" to exit.")
        print ("you have " , self.purse.get_balance())
        print()
        while True:
            if self.purse.get_balance() < 2:
                print ("You are leaving with",self.purse.get_balance())
                break
            else:
                bet = input("How much do you bet: ")
                if bet.isdigit():
                    bet = float(bet)

                    if (bet > self.purse.get_balance()):
                        print ("You don't have enough money to bet",self.purse.get_balance(),". Type \"N\" to exit.")

                    elif bet < 2:
                        print ("minimum bet is 2. Type \"N\" to exit.")
                    
                    else:
                        self.score_slot(bet) 
                
                elif bet.capitalize()  == "N":
                    print("You are leaving with " , self.purse.get_balance() )
                    break
                
                else:
                    print("I did not understand your input")
                    print ("minimum bet is 2. Type \"N\" to exit.")
                    print ("you have " , self.purse.get_balance()) 

    def score_slot(self, bet):
        self.purse.debit(bet)
        self.pull_handle()
        self.show_slot()

        if (self.a.face == self.b.face == self.c.face):
            self.purse.credit(2*bet)
            print ("You Score " , 2*bet , " - you have ", self.purse.get_balance())
            return 
        
        elif (self.a.face == self.b.face) or (self.a.face == self.c.face) or (self.c.face == self.b.face):
            self.purse.credit(1.5*bet)
            print ("You Score ",1.5*bet," - you have ", self.purse.get_balance())
            return
        
        else:
            print ("You Score 0", end="") 
            if self.purse.get_balance() < 2:
                print ("Thank you for playing.")
                return
            else:
                print("- you have ", self.purse.get_balance())
                return


