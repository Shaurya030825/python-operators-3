CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8

approved_apps =[
    "coding app",
    "math app",
    "science app",
    "reading app"
]

student_name= input("Enter your Name:")
requested_app= input("Enter the app name you want to access:") .lower()

print("\n---Identity Operator Check----")

if type(student_name) is str:
    print("The stuednt anme is stored as text.")

if type (requested_app) is not int:
    print("The requested app is not stored as a number")

print("\n-----Membership Operator Check------")

if requested_app in approved_apps:
    print(requested_app,"Is an approved student app.")
else:
    print(requested_app,"Is not in approved student app.")

restricted_apps = [
    "gaming app",
    "shooting app",
    "social media app"
]

if requested_app not in restricted_apps:
    print("This app is not in the restricted list.")

else:
    print("Access denied because app is restricted.")

print("\n----App Permission Settings----")

student_permissions= CAMERA|MICROPHONE|STORAGE

print("Permission value:", student_permissions)
print("Permissions bits:", bin(student_permissions))

if student_permissions& CAMERA:
    print("Camera permission: enabled")

if student_permissions & STORAGE:
    print("Storage permission: Enabled")

if student_permissions & MICROPHONE:
    print("Microphone permission: Enabled")

if student_permissions & LOCATION:
    print("Location permission: Enabled")
else:
    print("Location Permission: Disabled")

print("\n----Bit Shift Demonstration----")

next_permission =CAMERA<< 1

print("Camera Bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))

previous_permission= STORAGE >> 1

print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))

print("/n----Final Access Result----")

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)

