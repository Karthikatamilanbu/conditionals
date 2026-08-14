greetings=input("Greeting:")
greetings=greetings.strip()

if greetings=="Hello" or greetings=="Hello, Newman":
    print("$0")
    greetings=greetings.startswith("h")
elif greetings=="Hey"or greetings=="Hello,there":
    print("$20")
elif greetings=="How you doing?":
    print("$20")
    greetings=greetings.casefold()
elif greetings=="What's happening?":
    print("$100")
elif greetings=="What's up?":
    print("$100")  
else:
    print("enter a valid Greeeting")  
