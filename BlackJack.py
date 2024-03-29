import tkinter
import random
from  pyinputplus import inputInt

def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade',]
    face_cards = ['jack', 'queen', 'king']
    extension = "png"
    for suit in suits:
        for card in range(1,11):
            
            name = f"C:\\mycode\\python\\Functions\\tkinter\\cards\\{card}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,),)

        for face_card in face_cards:
            name = f"C:\\mycode\\python\\Functions\\tkinter\\cards\\{face_card}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,),)


def deal_cards(frame):
    global deck, cards
    next_card = deck.pop(0) # pop the next card off of the top of the deck
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    deck.append(next_card)
    # if not deck:
    #     deck[:] = cards
    #     random.shuffle(deck)
    return next_card


def score_hand(hand):
    # calculates the totla all the elements in the hand
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value ==1 and not ace:
            ace = True
            card_value+=11
        score+=card_value
        if score > 21 and ace: 
            score-=10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0<dealer_score<17:
        dealer_hand.append(deal_cards(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if dealer_score > 21 or dealer_score < player_score and player_score <=21:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    elif dealer_score == player_score:
        result_text.set("Draw!!")


def deal_player():
    player_hand.append(deal_cards(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

    # functions should generally not change global variables, even if they're specified. So, a better way is to just make a new function which 
    # will have a similar functionality. the score_hand is the name of that function
    # global player_score, player_ace
    # card_value = deal_cards(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score +=card_value
    # if player_score >21 and player_ace:
    #     player_ace = False
    #     player_score-=10
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins")


def new_game():
    global dealer_card_frame, player_card_frame, dealer_hand, player_hand, result_text
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, columnspan=2, sticky="ew")
    result_text.set("")
    dealer_hand.clear()
    player_hand.clear()
    deal_player()
    dealer_hand.append(deal_cards(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


    # card_frame.destroy()
    # card_frame = tkinter.Frame(mainwindow, relief="sunken", borderwidth=1, background="green")
    # card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)
    # deal_player()
    # dealer_hand.append(deal_cards(dealer_card_frame))
    # dealer_score_label.set(score_hand(dealer_hand))
    # deal_player()

def shuffle():
    random.shuffle(deck)
    
def play_test():
    global play_yes_no
    if __name__ == "__main__":
        play()
        return
        
def play():
    mainwindow.mainloop()
       

mainwindow = tkinter.Tk()
mainwindow.title("BlackJack")
mainwindow.geometry("1280x700+100+25")
mainwindow.configure(background="green")
result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainwindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# dealer info and cards
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
# the embedded frame to hold the card pics
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player info and cards
player_score_label = tkinter.IntVar()
player_score = 0 # this is the variable that holds the player's score
player_ace = False
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# the embdeeded frame to hold the player's cards
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, columnspan=2, sticky="ew")

# the buttons
button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=3, )
exit_button = tkinter.Button(button_frame, text="Exit", command=mainwindow.destroy)
exit_button.grid(row=0, column=4)
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle) 
shuffle_button.grid(row=0, column=5)

cards = []
load_images(cards)

# now to create a new deck of cardsand shuffle them
deck = []
deck[:] = cards # this means there is one set of cards in the deck. If you want n set of cards, add cards to it n times, so cards + cards is 2 set of cards
# random.shuffle(deck)
shuffle()
dealer_hand = []
player_hand = []
new_game()  
# deal_player()
# dealer_hand.append(deal_cards(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()
play_test()
