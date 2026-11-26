from time import sleep

def clear(frame):
    for i in range(len(frame)):
        if frame[::-1][i] == '\n':
            print("\r",end="")
        else:
            print("\b",end="")

def draw(frame_set):
    for i in range(len(frame_set)-1):
        print(frame_set[i])
        sleep(0.500) # Magic number for convincing animation, units miliseconds
        clear(frame_set[i])
    print(frame_set[len(frame_set)-1])
    return

frames = []

for i in range(1,4):
    with open("frames/" + str(i) + ".txt","r") as f:
        frames.append(f.read())

draw(frames)



