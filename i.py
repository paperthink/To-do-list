work = ["huu"]

def command(com):
    
    if com == "show":
        print(work)
    if "show" in work:
        work.remove("show")
    if com == "done":
        d = input("Enter the item: ")
        if d in work:
            work.remove(d)
        if "done" in work:
            work.remove("done")
    else:
        pass


while True:
    
    w = input("Enter ur work to do for today!: ")
    if w == "bye":
        print("Thank you for using paperthink list!")
        break

    command(w)
    work.append(w)
    if "show" in work:
        work.remove('show')

    if "done" in work:
        work.remove('done')