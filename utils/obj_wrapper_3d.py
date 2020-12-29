#!/bin/python

import numpy as np
import pandas as pd
import re
import sys

def read_obj(path="./models/windmill.obj"):
    f=open(path,'r')
    lines=f.readlines()
    v=[]
    f={}
    iv=1
    for line in lines:
    	if(bool(re.match("^v ",line))):
            v=v+[[float(x) for x in re.findall('-?[\d.]+',line)]]
        if(bool(re.match("usemtl",line))):
        	material=re.search("usemtl (.+)",line).group(1)
        	f[material]=[]
        if(bool(re.match("^f ",line))):
        	f[material]+=[[int(x) for x in re.findall(' ([\d.]+)/',line)]]
    return v,f

def blend(color, alpha, base=[255,255,255]):
    out = [int(round((alpha * color[i]) + ((1 - alpha) * base[i]))) for i in range(3)]
    return out

def to_hex(color):
    return ''.join(["%02x" % e for e in color])

def read_mtl(path="./models/windmill.mtl"):
    f=open(path,'r')
    lines=f.readlines()
    v=[]
    f={}
    iv=1
    for line in lines:
        if(bool(re.match("newmtl",line))):
        	material=re.search("newmtl (.+)",line).group(1)
        	f[material]=''
        if(bool(re.match("^Kd ",line))):
        	f[material]+=to_hex(blend([float(x)*255 for x in re.findall('([\d.]+)',line)],1))
    return f

def convert_3d(name,v,f,mtl):
	command = '<3dmodel id="'+name+'">\n\t'
	for batch in f:
		verts_all=[]
		color=mtl[batch]
		command+="<batch id=\""+batch+'" texture="Textures\concrete5.png" material="Materials\material1.xml" fvf="322" order="0">\n\t\t'
		for face in f[batch]:
                        if len(face)==3:
        			vertsInd=[i-1 for i in face]
        			verts=[v[int(i)-1] for i in face]
        			for Ind,vertex in zip(vertsInd,verts):
        				if Ind not in verts_all:
        					command+='<vertex id="%i" x="%0.4f" y="%0.4f" z="%0.4f" u1="%0.4f" v1="%0.4f" diffuse="0xff%s"/>\n\t\t' % tuple([Ind]+[float(vr) for vr in vertex]+[float(vertex[0]),float(vertex[2])]+[color])
        			# print(vertsInd)
        			verts_all+=vertsInd
        			command+='<face v1="%i" v2="%i" v3="%i"/>\n\t\t' % tuple(vertsInd)
		command+='</batch>\n\t'
	command+="</3dmodel>"
	return(command)




    # execute only if run as a script
model=sys.argv[1]
output=sys.argv[2]

v,f=read_obj(model+'.obj')
mtl=read_mtl(model+'.mtl')
res=convert_3d(model,v,f,mtl)

file=open(output+'.xml','w')
file.write(res)
file.close()
