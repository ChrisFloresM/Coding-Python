#Christian Flores 14/02/2021

from random import randint

class Lottery:
    """Jugar loteria"""

    def __init__(self, playing_numbers=(10, 9, 12, 15, 16, 17, 18, 19, 22, 10, "g", "h", "r", "o", "o")):
        self.playing_numbers = playing_numbers

    def select_a_winner(self):
        """Determina un ganador"""
        winners = []
        for _ in range(4):
            winner = self.playing_numbers[randint(1, 10)]
            winners.append(winner)
        return winners

my_lottery = Lottery()

my_ticket = []
ticket_count = 0
I_won = False

while I_won == False:
    new_ticket = my_lottery.playing_numbers[randint(1,10)]
    my_ticket.append(new_ticket)
    winners = my_lottery.select_a_winner()
    if new_ticket in winners:
        I_won = True
    ticket_count += 1
    
print(f"The winning number was {new_ticket} and it took you {ticket_count} attempts")
print("\nTickets used: ")
[print(f"{ticket}", end="\t") for ticket in my_ticket]


