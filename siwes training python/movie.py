global f
f = 0
def T_movie():
    global f
    f += 1
    print("which movie do you want to watch?")
    print("Terminator,movie1")
    print("Vanguard,movie2")
    print("The Unholy,movie3")
    movie = input("choose your movie: ")
    if movie == 4:
        center()
        theater()
        return 0
    if f == 1:
        theater()
def theater():
    print("which screen do you want to watch movie?")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = input("choose your screen: ")
    timing(a)
def timing(a):
    time1 ={
        "1" : "12.00 - 3.00",
        "2" : "1.00 - 2.00",
        "3" : "3.20 - 5.20"
    }

    time2 = {
       "1" : "12.00 - 3.00",
       "2" : "1.20 - 4.20",
       "3" : "7.30 - 10.30"
    }
    time3= {
        "1" : "10.30 - 12.30",
        "2" : "1.20 - 4.20",
        "3" : "7.30 - 10.30"
    }
    

    if a == 1:
        print("choose your time: ")
        print(time1)
        t = input("select your time: ")
        w = time1[t]
        print("successfull!, enjoy movie at " +w)
    elif a == 2:
        print("choose your time: ")
        print(time2)
        t = input("select your time: ")
        w = time2[t]
        print("successfull!, enjoy movie at " +w)
    elif a == 3:
        print("choose your time: ")
        print(time3)
        t = input("select your time: ")
        w = time3[t]
        print("successfull!, enjoy movie at " +w)
    return 0
def movie(theater):
    if theater == 1:
        T_movie()
    elif theater == 2:
        T_movie()
    elif theater == 3:
        T_movie()
    else:
        print("wrong choice")
  
