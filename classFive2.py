#-*- coding:utf-8 -*-
from classFive import yq
import sys


if len(sys.argv)==1:
    yq = yq('yq_in.txt','yq_out.txt')
    yq.yq_arrange()
elif len(sys.argv)==3:
    yq = yq(sys.argv[1], sys.argv[2])
    yq.yq_sort()
elif len(sys.argv)==4:
    yq = yq(sys.argv[1], sys.argv[2])
    yq.yq_province(sys.argv[3])
else:
    print('input error')

