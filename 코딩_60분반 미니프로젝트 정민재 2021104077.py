dict_eng={"ethics":"윤리학", "weather":"날씨", "number":"숫자", "grape":"포도"}

for i in dict_eng:
    user_input=input(f"{i}의 뜻은? >>")

    if user_input==dict_eng[i]:
        print("GOOD!!!")
    else:
        print(f"That's wrong. Answer is {dict_eng[i]}.")
