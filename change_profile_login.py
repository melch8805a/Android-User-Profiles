import android
droid = android.Android()

#Welcome message and dialog box setup
droid.makeToast("Welcome to Profile Switcher")
droid.dialogCreateAlert("Profile Switcher","Would you like to switch now?")
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
response = droid.dialogGetResponse().result
droid.dialogDismiss()

#Response handling for dialog box
if response.has_key("which"):
	result = response["which"]
	if result == "positive":
		droid.dialogGetInput("User Name", "Please Enter Your User Name:")
		droid.dialogGetPassword("Password", "Please Enter Your Password:")
	elif result == "negative":
		droid.makeToast("Thank you, come again!")
elif response.has_key("canceled"):
	droid.makeToast("Oops, that was the back button...")

# Random error handler....
else:
	print "Unknown response=",response

print "Done"