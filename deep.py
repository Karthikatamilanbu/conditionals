deep=input("What is the Answer to the Great Question of Life, the Universe and Everything?")
deep=deep.strip().capitalize()
match deep:
      case "42"|"Forty Two"|"forty-two"|"forty two"|"FoRty TwO":
            print("Yes")
      case _:
            print("No")
