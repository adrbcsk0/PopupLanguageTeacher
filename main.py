from win10toast import ToastNotifier
import random
from dictionaries import dictDE
from dictionaries import dictPL

x = random.randint(1, len(dictDE))
x = str(x)

# print(dictDE.get(x))

y = random.randint(1, 2)

if y == 1:
    toaster = ToastNotifier()
    toaster.show_toast("Zgadnij słówko", dictDE.get(x), duration=10)
    toaster2 = ToastNotifier()
    toaster2.show_toast("Zgadnij słówko", dictPL.get(x), duration=10)
else:
    toaster2 = ToastNotifier()
    toaster2.show_toast("Zgadnij słówko", dictPL.get(x), duration=10)
    toaster = ToastNotifier()
    toaster.show_toast("Zgadnij słówko", dictDE.get(x), duration=10)



# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)