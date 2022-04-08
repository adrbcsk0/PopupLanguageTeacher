from win10toast import ToastNotifier
import random

x = random.randint(1, len(dictPL))


dictDE = {
    "1" : "der Himmel",
    "2" : "der Hund",
    "3" : "das Gimpfel"
}

dictPL = {
    "1" : "niebo",
    "2" : "pies",
    "3" : "szczyt"
}




# print(dictionary)
# print(dictionary.get("szczyt"))
print(dictDE)
print(dictPL)

# toaster = ToastNotifier()
# toaster.show_toast("Zgadnij słówko", x, duration=10)
#
#
# toaster2 = ToastNotifier()
# toaster2.show_toast("Zgadnij słówko", x, duration=10)



# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)