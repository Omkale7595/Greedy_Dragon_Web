import pygame

pygame.init()

import random, game.assets.image as image

dis_s=pygame.display.set_mode()
surface=pygame.Surface((10000,10000),pygame.SRCALPHA)
pygame.display.set_caption("Dragon game")

pygame.draw.rect(surface,(128,128,128,105),(0,0,1100,2150))
pause=False

def reset():
	global score, timer, Velocity, dragon_img, next_meat_score,move_u, move_d, move_l, move_r, pause, score_board_text, timer_text,show_green_box
	score=0
	timer=60
	Velocity=5
	pause=False
	move_r=move_l=move_u=move_d=False
	dragon_img=dragon_right
	dragon_rect.center=(400,700)
	coin_rect.center=(700,700)
	meat_img_rect.center=(400,300)
	next_meat_score=0
	score_board_text = score_board.render(f"Score:{score}", True, Dark_green)
	timer_text=score_board.render(f"Time:{timer}",True,Black)
	show_green_box=False
	pygame.time.set_timer(start_game_event,300)
	bg_music.play(-1,0,0)
					
#Loading values
score=0
high_score=0
Velocity=5
timer=60

#Colors
White = (255,255,255)
Dark_green=(34, 139, 34)
Red=(255,0,0)
Blue=(0,0,255)
Grey=(50,50,50)
Green=(0,200,0)
Black=(0,0,0)

#FPS system
FPS =60
clock=pygame.time.Clock()

#Loading assets
#dragon assets
dragon_left,_=image.image("dragon_game/dragon_right.png",(0,0),True)
dragon_right,_=image.image("dragon_game/dragon_right.png",(0,0))
dragon_up,_=image.image("dragon_game/dragon_right.png",(0,0),False,90)
dragon_down,_=image.image("dragon_game/dragon_right.png",(0,0),False,-90)
dragon_img=dragon_right
dragon_rect=dragon_right.get_rect()
dragon_rect.center=(400,700)
#coin assets
coin_img,coin_rect=image.image("dragon_game/coin.png",(700,700))
#meat assets
meat_img,meat_img_rect=image.image("dragon_game/meat1.png",(400,300))
next_meat_score=0
meat_active=False
#pause_button, return_button, & home_button assets
pause_img,pause_img_rect=image.image("dragon_game/pause.png",(550,50))
return_img,return_img_rect=image.image("dragon_game/return.png",(450,900))
home_img,home_img_rect=image.image("dragon_game/home.png",(650,900))
#background music
bg_music=pygame.mixer.Sound('dragon_game/music.wav')
bg_music.play(-1,0,0)
#click music
click=pygame.mixer.Sound('dragon_game/click.wav')
#pickup music
coin_pickup=pygame.mixer.Sound('dragon_game/pickup.wav')
meat_pickup=pygame.mixer.Sound('dragon_game/meat_pickup.wav')
#dragon_wings
dragon_wings=pygame.mixer.Sound("dragon_game/dragon_wings.mp3")
#dragon_death
dragon_death=pygame.mixer.Sound('dragon_game/dragon_death.mp3')
#start button assets
start,start_rect=image.image("dragon_game/start.png",(550,1000),True,0)
#font assets
score_board=pygame.font.SysFont('calibri',64)
score_board_text=score_board.render(f"Score:{score}",True,Dark_green)
timer_text=score_board.render(f"Time:{timer}",True,Black)

#Volume adjustor
bg_music.set_volume(4)
coin_pickup.set_volume(.5)

#controller variables
move_l=move_r=move_u=move_d=False

game_mode='Menu'

start_game_event=pygame.USEREVENT + 1
pygame.time.set_timer(start_game_event,300)
show_green_box=False
game_timer_event=pygame.USEREVENT + 2
pygame.time.set_timer(game_timer_event,1000)
running = True
while running:
	if (game_mode=='Menu'):
		dis_s.fill(White)
		dis_s.blit(start,start_rect)
		if (show_green_box):
			pygame.draw.rect(dis_s,Dark_green,start_rect)
		pygame.display.update()
		for event in pygame.event.get():
			if (event.type==pygame.MOUSEBUTTONDOWN):
				touch_pos=event.pos
				if (start_rect.collidepoint(touch_pos)):
					click.play()
					show_green_box=True
			if (show_green_box):
				pygame.draw.rect(dis_s,Dark_green,start_rect)
				if (event.type==start_game_event):
					pygame.time.set_timer(start_game_event,0)
					show_green_box=False
					game_mode='Gameplay'
		
	elif (game_mode=='Gameplay'):
		dis_s.fill(White)
		start_small,start_small_rect=image.image("dragon_game/start.png",(450,1000),True,0,True,(64,64))
		score_board_text_rect=score_board_text.get_rect()
		score_board_text_rect.center=(100,50)
		timer_text_rect=timer_text.get_rect()
		timer_text_rect.center=(950,50)
		left_button=pygame.draw.rect(dis_s,Red,(300,1850,100,100))
		right_button=pygame.draw.rect(dis_s,Red,(700,1850,100,100))
		up_button=pygame.draw.rect(dis_s,Red,(500,1700,100,100))
		down_button=pygame.draw.rect(dis_s,Red,(500,2000,100,100))
		for event in pygame.event.get():
			if (event.type==pygame.QUIT):
				running=False
			if (event.type==game_timer_event and timer>0):
				timer-=1
				timer_text=score_board.render(f"Time:{timer}",True,Black)
				dis_s.blit(timer_text,timer_text_rect)
			if (event.type==pygame.MOUSEBUTTONDOWN):
				touch_pos=event.pos
				if (pause_img_rect.collidepoint(touch_pos) and not pause):
					click.play()
					if (not pause):
						pause=True
					else:
						pause=False
						pygame.time.set_timer(game_timer_event,1000)
						next_meat_score=0
				if (home_img_rect.collidepoint(touch_pos)):
					click.play()
					reset()
					game_mode='Menu'
					pygame.time.set_timer(game_timer_event,1000)
				if (start_small_rect.collidepoint(touch_pos)):
					pause=False
					bg_music.play(-1,0,0)
					pygame.time.set_timer(game_timer_event,1000)
					click.play()
				if (left_button.collidepoint(touch_pos) and not pause):
					move_l=True
					dragon_img=dragon_left
					dragon_wings.play()
				if (right_button.collidepoint(touch_pos) and not pause):
					move_r=True
					dragon_img=dragon_right
					dragon_wings.play()
				if (up_button.collidepoint(touch_pos) and not pause):
					move_u=True
					dragon_img=dragon_up
					dragon_wings.play()
				if (down_button.collidepoint(touch_pos) and not pause):
					move_d=True
					dragon_img=dragon_down
					dragon_wings.play()
			if (event.type==pygame.MOUSEBUTTONUP):
				move_r=move_l=move_u=move_d=False
				dragon_wings.stop()
		if (move_l and dragon_rect.centerx>0 and not pause):
			dragon_rect.x-=Velocity
			if (dragon_rect.left<0):
				dragon_rect.left=0
		if (move_r and dragon_rect.x<1080 and not pause):
			dragon_rect.x+=Velocity
			if (dragon_rect.right>1080):
				dragon_rect.right=1080
		if (move_u and dragon_rect.y>0 and not pause):
			dragon_rect.y-=Velocity
			if (dragon_rect.top<0):
				dragon_rect.top=0
		if (move_d and dragon_rect.y<1600 and not pause):
			dragon_rect.y+=Velocity
			if (dragon_rect.bottom>1600):
				dragon_rect.bottom=1600
		if (dragon_rect.colliderect(coin_rect) or coin_rect.colliderect(score_board_text_rect) or coin_rect.colliderect(timer_text_rect) or coin_rect.colliderect(pause_img_rect)):
			coin_rect.x=random.randint(0,1000)
			coin_rect.y=random.randint(0,1600)
			coin_pickup.play()
			if score < 20:
				Velocity+=0.2
			elif (score<50):
				Velocity+=0.1
			else:
				Velocity+=0.05
			Velocity=round(Velocity,2)
			score+=1
			dis_s.blit(score_board_text,score_board_text_rect)
			score_board_text=score_board.render(f"Score:{score}",True,Dark_green)
		if (score>=next_meat_score and not meat_active and score>=0):
			meat_active=True
		if (timer<=10):
			timer_text=score_board.render(f"Timer:{timer}",True,Red)
		if meat_active:
		  dis_s.blit(meat_img, meat_img_rect)
		  if dragon_rect.colliderect(meat_img_rect):
		  	meat_active = False
		  	next_meat_score=score+4
		  	meat_pickup.set_volume(random.uniform(0.5, 0.8))
		  	meat_pickup.play()
		  	if (score<50):
		  		timer+=8
		  	elif (score<100):
		  		timer+=6
		  	elif (score>=100):
		  		timer+=4
		if (dragon_rect.colliderect(meat_img_rect) or meat_img_rect.colliderect(score_board_text_rect) or meat_img_rect.colliderect(timer_text_rect) or meat_img_rect.colliderect(pause_img_rect)):
				meat_img_rect.x=random.randint(0,1000)
				meat_img_rect.y=random.randint(0,1600)
		if (timer==0):
			dragon_death.play()
			bg_music.stop()
			game_mode='Lost'
			#high_score+=score
			lost_text1=score_board.render(f"Highscore:{high_score}",True,Red)
			lost_text1_rect=lost_text1.get_rect()
			lost_text1_rect.center=(550,800)
			lost_text2=score_board.render("Dragon died out of starvation!",True,Red)
			lost_text2_rect=lost_text2.get_rect()
			lost_text2_rect.center=(550,1000)
		dis_s.blit(score_board_text,score_board_text_rect)
		dis_s.blit(timer_text,timer_text_rect)
		clock.tick(FPS)
		dis_s.blit(dragon_img,dragon_rect)
		dis_s.blit(coin_img,coin_rect)
		dis_s.blit(pause_img,pause_img_rect)
		if (pause):
			pause_text=score_board.render("Paused",True,Black)
			pause_text_rect=pause_text.get_rect()
			pause_text_rect.center=(550,800)
			bg_music.stop()
			dis_s.blit(surface,(0,0))
			pygame.draw.rect(dis_s,Green,(250,700,600,500))
			pygame.time.set_timer(game_timer_event,0)
			dis_s.blit(start_small,start_small_rect)
			home_img_rect.center=(640,1000)
			dis_s.blit(home_img,home_img_rect)
			dis_s.blit(pause_text,pause_text_rect)
		pygame.display.update()
	if (score>high_score):
		high_score=score
		
		
	elif (game_mode=='Lost'):
		dis_s.fill(White)
		return_box=pygame.draw.rect(dis_s,Red,(415,870,70,70))
		home_box=pygame.draw.rect(dis_s,Dark_green,(610,860,80,80))
		home_img,home_img_rect=image.image("dragon_game/home.png",(650,900))
		for event in pygame.event.get():
			if (event.type==pygame.MOUSEBUTTONDOWN):
				touch_pos=event.pos
				if (return_box.collidepoint(touch_pos)):
					click.play()
					reset()
					game_mode='Gameplay'
				if (home_box.collidepoint(touch_pos)):
					click.play()
					reset()
					game_mode='Menu'
		dis_s.blit(lost_text1,lost_text1_rect)
		dis_s.blit(lost_text2,lost_text2_rect)
		dis_s.blit(return_img,return_img_rect)
		dis_s.blit(home_img,home_img_rect)
		pygame.display.update()