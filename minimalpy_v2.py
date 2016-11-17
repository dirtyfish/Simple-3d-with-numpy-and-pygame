import numpy as np
from numpy.random import *
import pygame 

pygame.init()
mainClock = pygame.time.Clock()

winx=1280
winy=720

rendx=800
rendy=600

screen=pygame.display.set_mode((winx,winy))


screenarr=np.ndarray(winx*winy)
screenarr=screenarr.reshape(winx,winy)
screensurf=(pygame.display.set_mode((winx, winy), 0, 32))

#x=np.linspace(-.5, .5, num=winx, endpoint=0)
#y=np.linspace(-.5,.5,num=winx, endpoint=0)
#xpix=x*winx+winx/2
#xpix=xpix.astype(int)
#print xpix
#print y

def file2obj (filepath):
  #filepath = "3d.obj"
  print "Reading file:"+filepath
  buffer = "Read buff:\n"
  buffer += open(filepath, 'rU').read()
  #print buffer
  #linelist = buffer.splitlines(1)
  verts=[]
  polys=[]

  for lines in buffer.splitlines(1):
    if lines.startswith('v'):
      vdat=lines.split()
      vertice=[float(vdat[1]),float(vdat[2]),float(vdat[3])]
      verts.append(vertice)


    if lines.startswith('f'):
      pdat=lines.split()
      #poly=[]
      poly=[int(pdat[1]),int(pdat[2]),int(pdat[3])]
      polys.append(poly)

  return [verts,polys]

fileobj = file2obj("mario3.obj")
polys=np.array(fileobj[1])-1
points=np.array(fileobj[0])/2
points[:,2]+=5
zpoints=points[:,2]

print zpoints[:3]
print polys[:3]


screenarr[155,255]=255

tic=50
running=1
frame=0
while running:
	frame+=1
	
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=0

		if event.type == pygame.KEYDOWN:
			pass

		if event.type == pygame.JOYAXISMOTION:
			print event

	screensurf.fill((0,0,0))

	pixpoints=points[:,:2]*1
	points[:,1]-=.1
	zpoints+=.005*frame #zoomout
	pixpoints[:,0]/=zpoints #converts 3d to 2d
	pixpoints[:,1]/=zpoints #and then integers
	pixpoints=pixpoints*winx+winx/2
	pixpoints=pixpoints.astype(int)


	for pointindex in polys:
		#pointindex=np.array(pointindex)-1
		pygame.draw.line(screensurf, (255,0,0), pixpoints[pointindex[0]],pixpoints[pointindex[1]])
		pygame.draw.line(screensurf, (255,0,0), pixpoints[pointindex[1]],pixpoints[pointindex[2]])
		pygame.draw.line(screensurf, (255,0,0), pixpoints[pointindex[0]],pixpoints[pointindex[2]])
	#pygame.draw.circle(screensurf,(255,0,0),(50,50),40)
	#pygame.surfarray.blit_array(screensurf,screenarr)
	screen.blit(screensurf,(0,0))


	pygame.display.update()

	mainClock.tick(tic)