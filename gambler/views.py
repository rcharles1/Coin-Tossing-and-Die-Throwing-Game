from django.shortcuts import redirect, render
from django.http import HttpResponse
import secrets
from django.contrib import messages
import random
from django.conf import settings
import time


# Create your views here
def myview(request):
    return HttpResponse('Hello, World!')

def pay(request):

   #validate payment input
    if request.method == 'POST':

        amount = request.POST.get('amount')
        request.session["amount"] = amount


        if amount is not None:

            # Input is valid, process the data
            if int(amount) < 2000000:
                messages.error(request, "Insufficient amount!")
        
            else:


                #generate token
                def generate_token(n):
                    return secrets.token_hex(n)

                token = generate_token(16)
          
                request.session["token"] = token
                return redirect(copy_Token)
                    
        else:
            messages.error(request, "Empty fields are not allowed")
            redirect(pay)
    
    return render(request, "pay/pay.html")

def copy_Token(request):
    tkn = request.session.get("token")
    
    #render view
    return render(request, "copy token/copy token.html", {"token": tkn})


def enter_Token(request):
  
    if request.method == 'POST':

        user_tkn = request.POST.get('user_tkn')

        if user_tkn is not None:

            tkn = request.session.get("token")
            #validate token inputed by user
            if user_tkn == tkn:
                return redirect(toss)
            else:
                messages.error(request,"Wrong token.")
                
        else:
            messages.error(request, "Empty fields are not allowed")
            redirect(enter_Token)
    
    return render(request, "enter token/enter token.html")


def gambler(request):
    trial_chances = 3
    for i in range(trial_chances):
        result = random.choice(['heads', 'tails'])
        if result == 'heads':
            return redirect('dice')
        else:
            return redirect('game-over')
    
    return redirect('game-over')

def roll_die():
    return random.randint(1, 6)

def toss(request):
   
    image_path = settings.STATIC_URL + '/coin_toss.gif'  
    return render(request, "toss/toss.html", {'image_path': image_path})


def game_over(request):
    return render(request, "game over/game over.html")

def dice(request):
    image_path = settings.STATIC_URL + '/roll_dice.gif'
    side = roll_die()
    if side is not None:
        request.session['landing_side'] = side
        return redirect('cashout')
    return render(request, "dice/dice.html", {'image_path': image_path})


def cashout(request):
    landing_side = request.session.get("landing_side")
    amount_paid = request.session.get("amount")

    if amount_paid == 2000000:
        total_cashout = 1000000
    else:


        total_cashout = int(landing_side)*int(amount_paid)

    return render(request, "cashout/cashout.html", {"landing_side": total_cashout})