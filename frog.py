# coding: UTF-8
import pygame
from pygame.locals import *
import sys
import datetime
from tts import Tts
import subprocess, sys

def main():
  pygame.init()
  tts = Tts()
  screen = pygame.display.set_mode((256, 256 + 128))
  font = pygame.font.Font("./fonts/RictyDiminished-Regular.ttf", 20)
  frog = pygame.image.load("frog.png").convert_alpha()

  button = pygame.Rect(30+130, 10, 80, 30)  # creates a rect object
  btn_text = font.render("upload", True, (0,0,0))

  ck = pygame.time.Clock()
  dt_start = datetime.datetime.now()
  while True:
    ck.tick(1) #1秒間で1フレーム 30frame -> 33msecのwait
    screen.fill((255,255,255))
    screen.blit(frog, (0, 64), (0, 0, 256, 256))

    pygame.draw.rect(screen, (98,114,164), button)
    screen.blit(btn_text, (40+130, 15)) # button text
    
    dt_now = datetime.datetime.now()
    hour = dt_now.hour
    minute = dt_now.minute
    second = dt_now.second
    clock = dt_now.strftime('%m/%d %H:%M:%S')

    text = font.render(clock, True, (98,114,164), (255,255,255))
    screen.blit(text, (60, 336))
    
    if (dt_now - dt_start).seconds == 2:
      tts.talk("hi, what's up?")

    if hour == 1 and minute == 46 and second == 0:
      tts.talk("It's time")

    pygame.display.update()                                         # 画面更新
    # イベント処理
    for event in pygame.event.get():  # イベントキューからキーボードやマウスの動きを取得
      if event.type == QUIT:        # 閉じるボタンが押されたら終了
        pygame.quit()             # Pygameの終了(ないと終われない)
        sys.exit()                # 終了（ないとエラーで終了することになる）

      if event.type == pygame.MOUSEBUTTONDOWN:
        if button.collidepoint(event.pos):
          tts.talk("OK, Let’s get started.")
          upload()

def upload():

  p = "C:/Users/frog7/python/pygame/tumbler-blog"
  dt_now = datetime.datetime.now()
  dt_str = dt_now.strftime('%m-%d %H:%M')

  try:
    proc = subprocess.run('git add .', cwd=p, shell=True)
    print(proc.returncode)
  except subprocess.CalledProcessError:
    print("a command processing failed")
    sys.exit(1)

  try:
    proc = subprocess.run(f'git commit -m "posted {dt_str}"', cwd=p, shell=True)
    print(proc.returncode)
  except subprocess.CalledProcessError:
    print("a command processing failed")
    sys.exit(1)

  try:
    proc = subprocess.run('git push', cwd=p, shell=True)
    print(proc.returncode)
  except subprocess.CalledProcessError:
    print("a command processing failed")
    sys.exit(1)


if __name__ == "__main__":
    main()
