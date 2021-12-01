import turtle as t
import random
import time

def find_card(x,y):
      min_idx = 0
      min_dis = 100

      for i in range(36):
          distance = turtles[i].distance(x, y)
          if distance < min_dis:
              min_dis = distance
              min_idx = i
      return min_idx

def score1_update(m):
      score1_pen.clear()
      score1_pen.write(f"{m}  {score1}점/{attempt}번 시도", False, "center", ("", 15))

def result(m):
      t.goto(0, -60)
      t.write(m, False, "center", ("", 30,"bold"))

def play(x, y):
      global click_num
      global first_pick
      global second_pick
      global attempt
      global score1

      if attempt == 30:#30번 틀릴시 실패
          result("Game over")


      else:
            click_num += 1
            card_idx = find_card(x,y)# 클릭한 이미지 찾기
            turtles[card_idx].shape(img_list[card_idx])

            if click_num == 1:
                first_pick = card_idx
            elif click_num == 2:
                second_pick = card_idx
                click_num = 0
                attempt += 1

                if img_list[first_pick] == img_list[second_pick]:
                    score1 += 1
                    score1_update("정답")
                    if score == 14:
                        result("성공")
                else:
                    score1_update("오답")
                    turtles[first_pick].shape(default_img)
                    turtles[second_pick].shape(default_img)
                    current_time=int(time.time())
          
t.bgcolor("blue")
t.setup(1000, 1000)
t.up()
t.ht()
t.goto(0, 280)
t.write("카드 매칭 게임", False, "center", ("", 30, "bold"))

#점수 펜 객체 생성
score1_pen = t.Turtle()
score1_pen.up()
score1_pen.ht()
score1_pen.goto(0, 260)

#터틀 객체 생성
turtles = []
pos_x = [-350, -210, -70, 70, 210, 350]
pos_y = [-300, -200, -100, 0, 100, 200]

for x in range(6):
     for y in range(6):
          new_turtle = t.Turtle()
          new_turtle.up()
          new_turtle.color("blue")
          new_turtle.speed(0)
          new_turtle.goto(pos_x[x], pos_y[y])
          turtles.append(new_turtle)

default_img = "im/player.gif"
t.addshape(default_img)
img_list = []
for i in range(18):
     img = f"im/img{i}.gif"
     t.addshape(img)
     img_list.append(img)
     img_list.append(img)

random.shuffle(img_list)
for i in range(36):
     turtles[i].shape(img_list[i])

time.sleep(10)

for i in range(36):
     turtles[i].shape(default_img)

click_num = 0 # 클릭 횟수 (매 2회 클릭마다 정답체크)
score1 = 0 # 점수1
attempt = 0 #시도한 횟수
first_pick = "" # 첫 번째 클릭한 이미지
second_pick = "" # 두 번째 클릭한 이미지

t.onscreenclick(play)
t.done()
