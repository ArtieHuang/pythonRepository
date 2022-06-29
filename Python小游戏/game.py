import os
import sys
import pygame
from utils import *
from config import *


def main():
	pygame.init()
	
	#游戏主界面
	gameSurface = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("JOJO's Candy Crush Saga")
	
	#音效

	#初始化
	pygame.mixer.init()
	#设置音量大小
	pygame.mixer.music.set_volume(VOLUME)

	#背景音乐的路径
	bgFile1 = r'resources/audios/bg1.mp3'
	bgFile2 = r'resources/audios/bg2.mp3'
	bgFile3 = r'resources/audios/bg3.mp3'
	bgFile4 = r'resources/audios/bg4.mp3'
	bgFile5 = r'resources/audios/bg5.mp3'
	#创建背景音乐播放列表
	bgList = list()
	bgList.append(bgFile1)
	bgList.append(bgFile2)
	bgList.append(bgFile3)
	bgList.append(bgFile4)
	bgList.append(bgFile5)
	#加载背景音乐播放列表
	pygame.mixer.music.load(bgList.pop())
	pygame.mixer.music.queue(bgList.pop())
	pygame.mixer.music.set_endevent(pygame.USEREVENT)
	pygame.mixer.music.play()
		
	#游戏音效的路径
	sFile0 = r'resources/audios/s0.mp3'
	sFile1 = r'resources/audios/s1.wav'
	sFile2 = r'resources/audios/s2.wav'
	sFile3 = r'resources/audios/s3.wav'
	sFile4 = r'resources/audios/s4.wav'
	sFile5 = r'resources/audios/s5.wav'
	sFile6 = r'resources/audios/s6.wav'
	#创建游戏音效的字典
	sounds = {}
	sounds['mismatch'] = pygame.mixer.Sound(sFile0)
	sounds['match'] = []
	sounds['match'].append(pygame.mixer.Sound(sFile1))
	sounds['match'].append(pygame.mixer.Sound(sFile2))
	sounds['match'].append(pygame.mixer.Sound(sFile3))
	sounds['match'].append(pygame.mixer.Sound(sFile4))
	sounds['match'].append(pygame.mixer.Sound(sFile5))
	sounds['match'].append(pygame.mixer.Sound(sFile6))

	#加载游戏字体
	fFile = r'resources/f.ttf'
	font = pygame.font.Font(fFile, 20)

	#游戏图片的路径
	iFile0 = r'resources/images/i0.png'
	iFile1 = r'resources/images/i1.png'
	iFile2 = r'resources/images/i2.png'
	iFile3 = r'resources/images/i3.png'
	iFile4 = r'resources/images/i4.png'
	iFile5 = r'resources/images/i5.png'
	iFile6 = r'resources/images/i6.png'
	#创建游戏图片的列表
	imgs = list()
	imgs.append(iFile0)
	imgs.append(iFile1)
	imgs.append(iFile2)
	imgs.append(iFile3)
	imgs.append(iFile4)
	imgs.append(iFile5)
	imgs.append(iFile6)
	
	
	#主循环
	game = gemGame(gameSurface, sounds, font, imgs)
	
	while True:
		#顺序播放背景音乐列表
		for event in pygame.event.get():
			if event.type == pygame.USEREVENT:
				pygame.mixer.music.queue(bgList.pop())

		score = game.start()
		flag = False

		#游戏结束一轮后用户可以选择是否重玩
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYUP and event.key == pygame.K_r:
					flag = True
			if flag:
				break

			#RGB值纯色填充背景
			gameSurface.fill((100, 100, 100))

			#一轮游戏结束后提示用户当前分数以及选择是否重玩
			text0 = 'Final score: %s' % score
			text1 = 'Press <R> to restart the game.'
			text2 = 'Press <Esc> to quit the game.'
			rcttop = RCTTOP
			for index, text in enumerate([text0, text1, text2]):
				#设置分数字体颜色大小
				text_render = font.render(text, 1, (200, 200, 200))
				rect = text_render.get_rect()
				if index == 0:
					rect.left, rect.top = (200, rcttop)
				elif index == 1:
					rect.left, rect.top = (100, rcttop)
				else:
					rect.left, rect.top = (100, rcttop)
				rcttop += 100
				gameSurface.blit(text_render, rect)
			pygame.display.update()
		game.reset()


'''test'''
if __name__ == '__main__':
	main()