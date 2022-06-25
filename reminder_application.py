from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

toasttitle=input("\n enter the remineder::")
msg= input('\n meassage::')
minutes= float(input('how many minutes::'))

seconds = minutes*60

print("\n Reminder is set successfully!!! \n")

time.sleep(seconds)
toaster.show_toast(toasttitle, msg , duration=10, threaded=True)

while toaster.notification_active:
    time.sleep(0.1)
