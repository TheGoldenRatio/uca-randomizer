def randomstudent():
    import sys
    import random

    students = [
        "Abdul Hakim",
        "Adelina ",
        "Adnan",
        "Afraz",
        "AliZain",
        "AlyNa",
        "Anisa",
        "Atai",
        "Bagymdat",
        "Beknazar",
        "Bermet",
        "Burulsun",
        "Butabek",
        "Buzurgmehr",
        "Dias",
        "Eldiiar ",
        "Elgiz",
        "Elzar",
        "Eraj",
        "Faridun",
        "Firuzai ",
        "Fotima",
        "Gulnoza",
        "Iskender ",
        "Ismat",
        "Jahanzaib",
        "Jalol",
        "Jonbegim ",
        "Jyldyz",
        "Karlygash",
        "Khudunazar",
        "Khursand",
        "Khursheda ",
        "Manuchekhr",
        "Marat ",
        "Mizhgona",
        "Munira ",
        "Muratrauf",
        "Murod",
        "Murodali",
        "Muybalikhon",
        "Myrza ",
        "Nadira",
        "Najmiya",
        "Nozanin",
        "Nurlan",
        "Ozar",
        "Parvina",
        "Risolat",
        "Rukhmina",
        "Rukhmina ",
        "Sadbarg ",
        "Safarmamad",
        "Safdar",
        "Saif ",
        "Sear",
        "Shahrom",
        "Suyuna ",
        "Syimyk",
        "Temirhan",
        "Timima",
        "Uran ",
        "Viacheslav",
        "Zarastin",
        "Zarrina",
        "Zubair",
        "Zulfiqori",
    ]

    print("\n")

    if len(sys.argv) > 1:
        print ("The lucky students are: \n")
        for i in random.sample(students,int(sys.argv[1])):
            print(i,"!!!")
    else:
        print ("The lucky student is: ",random.choice(students),"!!!")

    print("\n")

randomstudent()
