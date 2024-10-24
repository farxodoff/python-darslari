print("Tana Massa Indexsini aniqlash")
boy = float(input("Bo'yingizni kiriting: "))
vazn = float(input("Vazningizni kiriting: "))
t_index = vazn / ((boy**2) / 10000)

if(t_index < 18.5):
    print("Sizning TMI: 'ZAIF'")
elif(t_index>18.5 and t_index<25):
    print("Sizning TMI: 'NORMAL'")
elif(t_index>=25 and t_index<30):
    print("Sizning TMI: 'ORTIQCHA'")
elif(t_index>=30):
    print("Sizning TMI: 'SEMIZ'")
