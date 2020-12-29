from math import sin,cos,radians
import sys
from numpy import arange

n=int(sys.argv[1])
r1=float(sys.argv[2])
r2=float(sys.argv[3])
angle_from=float(sys.argv[4])
angle_to=float(sys.argv[5])


height=float(sys.argv[6])
z_offset=float(sys.argv[7])
output_file=sys.argv[8]



step_angle=(angle_to-angle_from)/n
print('tak')
coors_str=['<pillar refx1="inrun" refx2="inrun" refy="inrun-top" type="glass" t="Textures\\metal.png" m="Materials\\material1.xml" c="0x444455" top="false" bottom="false" x1="2" x2="18" try="'+str(round(cos(radians(a))*r1+height,4))+'" tly="'+str(round(cos(radians(a))*r2+height,4))+'" bry="'+str(round(cos(radians(a+step_angle))*r1+height,4))+'" bly="'+str(round(cos(radians(a+step_angle))*r2+height,4))+'" trz="'+str(round(sin(radians(a))*r1+z_offset,4))+'" tlz="'+str(round(sin(radians(a))*r2+z_offset,4))+'" brz="'+str(round(sin(radians(a+step_angle))*r1+z_offset,4))+'" blz="'+str(round(sin(radians(a+step_angle))*r2+z_offset,4))+'" />' for a in arange(angle_from,angle_to,step_angle)]

res='\n'.join(coors_str)
print(coors_str[0])
print('tak')
file=open(output_file,'w')
file.write(res)
file.close()
