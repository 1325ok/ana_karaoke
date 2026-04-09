import random
song = ["애국가","Tears","그대에게","Drowning"]
def speaker(name,score):
    global song #반성문을 영어로 하면 global[글로 벌]
    print(f"\n{name} 선배님이 부르신 {song[random.randint(0,3)]} 곡은")
    if score>=90:
        print("가수 데뷔 임박!")
    elif score>=80:
        print("그럭저럭 부르시네요")
    else:
        print("저질이군...쳐라!!!")

ana16 = ["김한울","장윤","강주영","고상우"]
for i in ana16:
    speaker(i,random.randint(50,100))