# to run from command line just use "python randomstudent.py"
# optionally, can pass in extra integer parameter from terminal,
# eg "python randomstudent.py 5" to return multiple names

def randomstudent():
    import sys
    import random


    students = [
        "Abazganova Tumar Erikovna",
        "Abdul Hakim",
        "Abdulloev Buzurgmehr",
        "Adnan Ali",
        "Afzunov Kishvar",
        "Ali Zain Hussain Ali",
        "Alidodkhonov Afraz",
        "Almazova Adelina",
        "AlyNa Rahim",
        "Anisa",
        "Atabaeva Bagymdat  Asanovna",
        "Atai",
        "Berdiev Iskender",
        "Bermet Burkanova",
        "Burulsun",
        "Butabek Butabekov",
        "Eldiiar Dzhunusov",
        "Elgiz Dzholdoshov",
        "Eraj Uzoqov",
        "Faridun Mamadbekov",
        "Firuzai Muzaffar",
        "Fotima Qozibekova",
        "Gulnoza Dilloeva",
        "Ismat Rahmatshoev",
        "jahanzaib khan danish",
        "Jonbegim Mukhtor",
        "Jumabaev Beknazar ",
        "Jumakhonov Muybalikhon",
        "Jyldyz Sarieva",
        "Kabykenov Dias",
        "Khudododova Mizhgona Sharafdodovna",
        "Khudonazar Imomyorbekov",
        "Khursand Sharipov",
        "Kudaiberdi Sulaimanov",
        "Kussainova Karlygash",
        "Manuchekhr Makhsutshoev",
        "Marat",
        "Mirzoeva Sadbarg Khushqadamovna",
        "Munira",
        "Murodali Sharipov",
        "Nadira Karataeva",
        "Najmiya Abdurahmonova Abdulghayosovna ",
        "Nasratshoeva Timima ",
        "Nozanin",
        "Nurlan Nogoibaev",
        "Nursultan Mukhamediya",
        "Ozar",
        "Risolat Okhirnazarova",
        "Rukhmina Imronshoeva",
        "Rukhmina Nagzibekova",
        "Safarmamad",
        "Safarmamadova Khursheda",
        "SafdarJan",
        "Saif ur rehman ",
        "Shahrom Dehoti",
        "Sultangaziyev Muratrauf",
        "Sultonmamadova Parvina Tokhirovna",
        "Suyuna Dadybaeva",
        "Syimik",
        "Temirkhan",
        "Uran",
        "Zarastin",
        "Zarrina Gafurova",
        "Zubair Ahmad Khan",
        "Zulfiqori Talabkhuja",
        "Murod",
        "Viacheslav",
        "Jalol"
    ]



    if len(sys.argv) > 1:
        print ("The lucky student is: ",random.sample(students,int(sys.argv[1])),"!!!")
    else:
        print ("The lucky student is: ",random.choice(students),"!!!")


randomstudent()
