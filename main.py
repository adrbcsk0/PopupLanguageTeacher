from win10toast import ToastNotifier
from datetime import datetime

toaster = ToastNotifier()
toaster.show_toast("Zgadnij słówko", "Słówko po niemiecku", duration=10)


toaster2 = ToastNotifier()
toaster2.show_toast("Zgadnij słówko", "Słówko po polsku", duration=10)



# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)