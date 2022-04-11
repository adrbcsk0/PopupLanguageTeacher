from win10toast import ToastNotifier
import random
import time
from dictionaries import dictDE
from dictionaries import dictPL

# on this stage I coded as many popups as words we have in dictionary. In next versions I would like to let user to
# decided how many popups and how often will appear.

for i in range (1, 5):                          #hardcoded for testing purpose
    y = random.randint(1, 2)
    x = random.randint(1, len(dictDE))
    t = random.randint(60, 120)                 #hardcoded for testing purpose
    x = str(x)

    if y == 1:
        toaster = ToastNotifier()
        toaster.show_toast("Zgadnij słówko", dictDE.get(x), duration=6)
        toaster2 = ToastNotifier()
        toaster2.show_toast("Zgadnij słówko", dictPL.get(x), duration=6)
    else:
        toaster2 = ToastNotifier()
        toaster2.show_toast("Zgadnij słówko", dictPL.get(x), duration=6)
        toaster = ToastNotifier()
        toaster.show_toast("Zgadnij słówko", dictDE.get(x), duration=6)
    time.sleep(t)
    i += 1

# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)