#This file is to test that the tools work.
import random
import colorama
from colorama import Fore, Back ,Style
colorama.init(autoreset=False)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
ip = int(input(Fore.GREEN + 'Enter IP (Without breaks) (0 for random): '))
if ip == 0:
    ip = (random.choice(numbers) +  random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers) +  random.choice(numbers) + random.choice(numbers))
sending = int(input(Fore.YELLOW + 'How many packets to send? '))
sent = -1
for x in range(sending):
    sent = sent + 1
    print(Fore.RED + 'Sent packet to',Fore.YELLOW + ip,'   |Total:', sent + 1, '   |Remaining:', sending - 1 - sent)
print(Fore.GREEN + 'Succesfully ddosed. Packets sent:', sent, '. IP sent to:', ip)
