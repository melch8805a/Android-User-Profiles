import android
droid = android.Android()

#Welcome message and dialog box setup
droid.makeToast("Welcome to Profile Switcher")
droid.dialogCreateAlert("Profile Switcher","Would you like to switch now?")
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
switch = droid.dialogGetResponse().result
droid.dialogDismiss()

#Response handling for dialog box
if switch.has_key("which"):
	result = switch["which"]
	if result == "positive":
		username = droid.dialogGetInput("User Name", "Please Enter Your User Name:").result
		password = droid.dialogGetPassword("Password", "Please Enter Your Password:").result
	elif result == "negative":
		droid.makeToast("Thank you, come again!")
elif switch.has_key("canceled"):
	droid.makeToast("Oops, that was the back button...")

# Random error handler....
else:
	print "Unknown response=",response

# this is here just to make sure username / password was saving off correctly
droid.makeToast(username)
droid.makeToast(password)