from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output
from warnings import warn
from pandas import DataFrame
from bokeh.core.properties import value
from bokeh.io import output_file,show
from bokeh.plotting import figure
import numpy as np
#from bokeh.palettes import Category20b


year=[]
carstypes=[]
carsnames=[]
AdultOccupant=[]
AdultOccupantvalue=[]
ChildOccupant=[]
ChildOccupantvalue=[]
Pedestrian=[]
Pedestrianvalue=[]
SafetyAssist=[]
SafetyAssistvalue=[]
start_time=time()
requests=0
yc=[]


headers={'Accpect-Language':'{zh-tw,zh;q=0.5'}
#用for迴圈抓取2010至2017間的資料
years=[str(i) for i in range(2010,2018)]
for years in years:
    response=get('https://www.euroncap.com/zh/%E8%AF%84%E7%BA%A7%E5%92%8C%E5%A5%96%E9%A1%B9/%E6%9C%80%E4%BD%B3%E8%BD%A6%E5%9E%8B/'+years+'/')
    #抓取檔案的速度
    requests+=1
    elapsed_time=time()-start_time
    print('Request: {}; Frequency: {} request/s'.format(requests,requests/elapsed_time))
    clear_output(wait=True)
    #判斷回傳值是否為200
    if response.status_code !=200:
        #print(response.status_code)
        print('Request: {}; Status_code: {}'.format(requests,response.status_code))
    if requests>30:
        warn('Number of requests was greater than expected')
        break
    page_html=BeautifulSoup(response.text,'html.parser')
    car_container=page_html.find_all('div',class_='car-container')
    #用for迴圈抓取年份,車種,車名,成人防護,兒童防護,行人防護,安全輔助
    for container in car_container:
        if container.find('div',class_='adult-occupant') is not None:
            
            everyyear=container.find('div',class_='year').text
            year.append(everyyear)


            types=container.find('div',class_='car-container-category').text
            carstypes.append(types)
            
            names=container.find('div',class_='car-name').text
            carsnames.append(names)
            
            adultoccupants=container.find('div',class_='adult-occupant')
            adultoccupant=adultoccupants.find('div',class_='rating-title').text
            AdultOccupant.append(adultoccupant)
            
            adultoccupantvalues=container.find('div',class_='adult-occupant')
            adultoccupantvalue=adultoccupants.find('div',class_='value').text
            adultoccupantvalue=adultoccupantvalue.strip('%')
            adultoccupantvalue=int(adultoccupantvalue)
            AdultOccupantvalue.append(adultoccupantvalue)
            
            childoccupants=container.find('div',class_='child-occupant')
            childoccupant=childoccupants.find('div',class_='rating-title').text
            ChildOccupant.append(childoccupant)
            

            childoccupantvalues=container.find('div',class_='child-occupant')
            childoccupantvalue=childoccupantvalues.find('div',class_='value').text
            childoccupantvalue=childoccupantvalue.strip('%')
            childoccupantvalue=int(childoccupantvalue)
            ChildOccupantvalue.append(childoccupantvalue)
            

            pedestrians=container.find('div',class_='pedestrian')
            pedestrian=pedestrians.find('div',class_='rating-title').text
            Pedestrian.append(pedestrian)


            pedestrianvalues=container.find('div',class_='pedestrian')
            pedestrianvalue=pedestrianvalues.find('div',class_='value').text
            pedestrianvalue=pedestrianvalue.strip('%')
            pedestrianvalue=int(pedestrianvalue)
            Pedestrianvalue.append(pedestrianvalue)

            safetyassists=container.find('div',class_='safety-assist')
            safetyassist=safetyassists.find('div',class_='rating-title').text
            SafetyAssist.append(safetyassist)
            


            safetyassistvalues=container.find('div',class_='safety-assist')
            safetyassistvalue=safetyassistvalues.find('div',class_='value').text
            safetyassistvalue=safetyassistvalue.strip('%')
            safetyassistvalue=int(safetyassistvalue)
            SafetyAssistvalue.append(safetyassistvalue)
#將year跟carsnames二個陣列二合為一<其值為上下相加非左右相加,如(0-0+1-0,0-1+1-1,0-2+1-2)>
np3=[]
np1=np.char.array(year)
np2=np.char.array(carsnames)
np3=np1+np2
print(len(np3))


#將np3轉成list的型態
np4=[]
for npp in np4:
    np4.append(npp)



#判讀carstypes裡有哪裡類別與其數量
c=set(carstypes)
for c1 in c:
    vule=0
    for ct in carstypes:
        if c1==ct:
            vule+=1
    print(c1,':',vule)



# #抓取小型車所在位子與所在位子之值
# a=[i for i,n in enumerate(carstypes) if n=='小型家用车']
# print('小型家用车所有的位子',a)
# b=[np3[0],np3[9],np3[12],np3[21],np3[26],np3[33],np3[39],np3[46],np3[47]]
# print(b)
# AOv=[AdultOccupantvalue[0],AdultOccupantvalue[9],AdultOccupantvalue[12],AdultOccupantvalue[21],AdultOccupantvalue[26],AdultOccupantvalue[33],AdultOccupantvalue[39],AdultOccupantvalue[46],AdultOccupantvalue[47]]
# COv=[ChildOccupantvalue[0],ChildOccupantvalue[9],ChildOccupantvalue[12],ChildOccupantvalue[21],ChildOccupantvalue[26],ChildOccupantvalue[33],ChildOccupantvalue[39],ChildOccupantvalue[46],ChildOccupantvalue[47]]
# Pv=[Pedestrianvalue[0],Pedestrianvalue[9],Pedestrianvalue[12],Pedestrianvalue[21],Pedestrianvalue[26],Pedestrianvalue[33],Pedestrianvalue[39],Pedestrianvalue[46],Pedestrianvalue[47]]
# SAv=[SafetyAssistvalue[0],SafetyAssistvalue[9],SafetyAssistvalue[12],SafetyAssistvalue[21],SafetyAssistvalue[26],SafetyAssistvalue[33],SafetyAssistvalue[39],SafetyAssistvalue[46],SafetyAssistvalue[47]]


# #輸出小型車的圖
# output_file("小型家用車.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b':b,'成人防護':AOv,'兒童防護':COv,'行人防護':Pv,'安全輔助':SAv}
# #colors=Category20b[len(cv)]
# colors=['#AEDEFC','#FFF6F6','#FFDFDF','#FB929E']
# p=figure(x_range=b,plot_height=1000,title='2010~2017最佳小型家用車',toolbar_location=None,tools='hover',tooltips='$name @b: @$name')
# p.vbar_stack(cv,x='b',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1500
# p.plot_height=1200
# show(p)



# #抓取微型車所在位子與所在位子之值
# a1=[i for i,n in enumerate(carstypes) if n=='微型车']
# print('微型车所有的位子',a1)
# b1=[np3[1],np3[5],np3[13],np3[22],np3[29],np3[34],np3[44]]
# print(b1)
# AOv1=[AdultOccupantvalue[1],AdultOccupantvalue[5],AdultOccupantvalue[13],AdultOccupantvalue[22],AdultOccupantvalue[29],AdultOccupantvalue[34],AdultOccupantvalue[44]]
# COv1=[ChildOccupantvalue[1],ChildOccupantvalue[5],ChildOccupantvalue[13],ChildOccupantvalue[22],ChildOccupantvalue[29],ChildOccupantvalue[34],ChildOccupantvalue[44]]
# Pv1=[Pedestrianvalue[1],Pedestrianvalue[5],Pedestrianvalue[13],Pedestrianvalue[22],Pedestrianvalue[29],Pedestrianvalue[34],Pedestrianvalue[44]]
# SAv1=[SafetyAssistvalue[1],SafetyAssistvalue[5],SafetyAssistvalue[13],SafetyAssistvalue[22],SafetyAssistvalue[29],SafetyAssistvalue[34],SafetyAssistvalue[44]]


# #輸出微型車的圖
# output_file("微型車.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b1':b1,'成人防護':AOv1,'兒童防護':COv1,'行人防護':Pv1,'安全輔助':SAv1}
# #colors=Category20b[len(cv)]
# #colors=['#AEDEFC','#FFF6F6','#FFDFDF','#FB929E']
# colors=['#C5E5E3','#F0F1B3','#BAE2BE','#A3A7E4']
# #colors=['#EDEDED','#F1D18A','#F73859','#232931']
# #colors=['#FFCDB5','#A1C45A','#FFE5AB','#FFF6F6']


# p=figure(x_range=b1,plot_height=1000,title='2010~2017最佳微型車',toolbar_location=None,tools='hover',tooltips='$name @b1: @$name')
# p.vbar_stack(cv,x='b1',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1300
# p.plot_height=1200
# show(p)


# #抓取商務車所在位子與所在位子之值
# a2=[i for i,n in enumerate(carstypes) if n=='商务车']
# print('商务车所有的位子',a2)
# b2=[np3[2],np3[19],np3[41]]
# print(b2)
# AOv2=[AdultOccupantvalue[2],AdultOccupantvalue[19],AdultOccupantvalue[41]]
# COv2=[ChildOccupantvalue[2],ChildOccupantvalue[19],ChildOccupantvalue[41]]
# Pv2=[Pedestrianvalue[2],Pedestrianvalue[19],Pedestrianvalue[41]]
# SAv2=[SafetyAssistvalue[2],SafetyAssistvalue[19],SafetyAssistvalue[41]]


# #輸出商務車的圖
# output_file("商務車.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b2':b2,'成人防護':AOv2,'兒童防護':COv2,'行人防護':Pv2,'安全輔助':SAv2}
# #colors=Category20b[len(cv)]
# # colors=['#AEDEFC','#FFF6F6','#FFDFDF','#FB929E']
# # colors=['#C5E5E3','#F0F1B3','#BAE2BE','#A3A7E4']
# colors=['#EDEDED','#F1D18A','#F73859','#232931']
# # colors=['#FFCDB5','#A1C45A','#FFE5AB','#FFF6F6']
# p=figure(x_range=b2,plot_height=1000,title='2010~2017最佳商務車',toolbar_location=None,tools='hover',tooltips='$name @b2: @$name')
# p.vbar_stack(cv,x='b2',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=700
# p.plot_height=650
# show(p)


# #抓取大型MPV所在位子與所在位子之值
# a3=[i for i,n in enumerate(carstypes) if n=='大型 MPV']
# print('大型 MPV 所有的位子',a3)
# b3=[np3[14],np3[35]]
# print(b3)
# AOv3=[AdultOccupantvalue[14],AdultOccupantvalue[35]]
# COv3=[ChildOccupantvalue[14],ChildOccupantvalue[35]]
# Pv3=[Pedestrianvalue[14],Pedestrianvalue[35]]
# SAv3=[SafetyAssistvalue[14],SafetyAssistvalue[35]]


# #輸出大型MPV的圖
# output_file("大型MPV.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b3':b3,'成人防護':AOv3,'兒童防護':COv3,'行人防護':Pv3,'安全輔助':SAv3}
# #colors=Category20b[len(cv)]
# colors=['#53D397','#F7F9FF','#FF7A5C','#D1478C']
# p=figure(x_range=b3,plot_height=1000,title='2010~2017最佳大型MPV',toolbar_location=None,tools='hover',tooltips='$name @b3: @$name')
# p.vbar_stack(cv,x='b3',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=500
# p.plot_height=500
# show(p)





# #抓取小型MPV所在位子與所在位子之值
# a4=[i for i,n in enumerate(carstypes) if n=='小型 MPV']
# print('小型 MPV所有的位子',a4)
# b4=[np3[4],np3[6],np3[10],np3[11],np3[23],np3[24],np3[27],np3[36],np3[45]]
# print(b4)
# AOv4=[AdultOccupantvalue[4],AdultOccupantvalue[6],AdultOccupantvalue[10],AdultOccupantvalue[11],AdultOccupantvalue[23],AdultOccupantvalue[24],AdultOccupantvalue[27],AdultOccupantvalue[36],AdultOccupantvalue[45]]
# COv4=[ChildOccupantvalue[4],ChildOccupantvalue[6],ChildOccupantvalue[10],ChildOccupantvalue[11],ChildOccupantvalue[23],ChildOccupantvalue[24],ChildOccupantvalue[27],ChildOccupantvalue[36],ChildOccupantvalue[45]]
# Pv4=[Pedestrianvalue[4],Pedestrianvalue[6],Pedestrianvalue[10],Pedestrianvalue[11],Pedestrianvalue[23],Pedestrianvalue[24],Pedestrianvalue[27],Pedestrianvalue[36],Pedestrianvalue[45]]
# SAv4=[SafetyAssistvalue[4],SafetyAssistvalue[6],SafetyAssistvalue[10],SafetyAssistvalue[11],SafetyAssistvalue[23],SafetyAssistvalue[24],SafetyAssistvalue[27],SafetyAssistvalue[36],SafetyAssistvalue[45]]


# #輸出小型MPV的圖
# output_file("小型MPV.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b4':b4,'成人防護':AOv4,'兒童防護':COv4,'行人防護':Pv4,'安全輔助':SAv4}
# #colors=Category20b[len(cv)]
# colors=['#2931B3','#1874C3','#2AA9D2','#EFFF9D']
# p=figure(x_range=b4,plot_height=1000,title='2010~2017最佳小型MPV',toolbar_location=None,tools='hover',tooltips='$name @b4: @$name')
# p.vbar_stack(cv,x='b4',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1500
# p.plot_height=1200
# show(p)





# #抓取商用及家庭用廂式車所在位子與所在位子之值
# a5=[i for i,n in enumerate(carstypes) if n=='商用及家用厢式车']
# print('商用及家用厢式车所有的位子',a5)
# b5=[np3[17]]
# print(b5)
# AOv5=[AdultOccupantvalue[17]]
# COv5=[ChildOccupantvalue[17]]
# Pv5=[Pedestrianvalue[17]]
# SAv5=[SafetyAssistvalue[17]]


# #輸出商用及家庭用廂式車的圖
# output_file("商用及家庭用廂式車.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b5':b5,'成人防護':AOv5,'兒童防護':COv5,'行人防護':Pv5,'安全輔助':SAv5}
# #colors=Category20b[len(cv)]
# colors=['#F3EDED','#F5C16C','#DF8931','#AA530E']
# p=figure(x_range=b5,plot_height=1000,title='2010~2017最佳商用及家庭用廂式車',toolbar_location=None,tools='hover',tooltips='$name @b5: @$name')
# p.vbar_stack(cv,x='b5',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=250
# p.plot_height=850
# show(p)




# #抓取運動跑車所在位子與所在位子之值
# a6=[i for i,n in enumerate(carstypes) if n=='运动跑车']
# print('运动跑车所有的位子',a6)
# b6=[np3[37]]
# print(b6)
# AOv6=[AdultOccupantvalue[37]]
# COv6=[ChildOccupantvalue[37]]
# Pv6=[Pedestrianvalue[37]]
# SAv6=[SafetyAssistvalue[37]]


# #輸出運動跑車的圖
# output_file("運動跑車.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b6':b6,'成人防護':AOv6,'兒童防護':COv6,'行人防護':Pv6,'安全輔助':SAv6}
# #colors=Category20b[len(cv)]
# colors=['#D7F8F7','#BEE4D2','#FAB2AC','#EDA1C1']
# p=figure(x_range=b6,plot_height=1000,title='2010~2017最佳運動跑車',toolbar_location=None,tools='hover',tooltips='$name @b6: @$name')
# p.vbar_stack(cv,x='b6',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=220
# p.plot_height=850
# show(p)





# #抓取大型家用車所在位子與所在位子之值
# a7=[i for i,n in enumerate(carstypes) if n=='大型家用车']
# print('大型家用车所有的位子',a7)
# b7=[np3[8],np3[15],np3[20],np3[25],np3[32],np3[38]]
# print(b7)
# AOv7=[AdultOccupantvalue[8],AdultOccupantvalue[15],AdultOccupantvalue[20],AdultOccupantvalue[25],AdultOccupantvalue[32],AdultOccupantvalue[38]]
# COv7=[ChildOccupantvalue[8],ChildOccupantvalue[15],ChildOccupantvalue[20],ChildOccupantvalue[25],ChildOccupantvalue[32],ChildOccupantvalue[38]]
# Pv7=[Pedestrianvalue[8],Pedestrianvalue[15],Pedestrianvalue[20],Pedestrianvalue[25],Pedestrianvalue[32],Pedestrianvalue[38]]
# SAv7=[SafetyAssistvalue[8],SafetyAssistvalue[15],SafetyAssistvalue[20],SafetyAssistvalue[25],SafetyAssistvalue[32],SafetyAssistvalue[38]]


# #輸出大型家用車的圖
# output_file("大型家用車.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b7':b7,'成人防護':AOv7,'兒童防護':COv7,'行人防護':Pv7,'安全輔助':SAv7}
# #colors=Category20b[len(cv)]
# colors=['#A7095C','#FA9E05','#FFDD00','#FB929E']
# p=figure(x_range=b7,plot_height=1000,title='2010~2017最佳大型家用車',toolbar_location=None,tools='hover',tooltips='$name @b7: @$name')
# p.vbar_stack(cv,x='b7',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1200
# p.plot_height=1000
# show(p)





# #抓取小型越野所在位子與所在位子之值
# a8=[i for i,n in enumerate(carstypes) if n=='小型越野']
# print('小型越野所有的位子',a8)
# b8=[np3[3],np3[18],np3[28],np3[31],np3[40],np3[43]]
# print(b8)
# AOv8=[AdultOccupantvalue[3],AdultOccupantvalue[18],AdultOccupantvalue[28],AdultOccupantvalue[31],AdultOccupantvalue[40],AdultOccupantvalue[43]]
# COv8=[ChildOccupantvalue[3],ChildOccupantvalue[18],ChildOccupantvalue[28],ChildOccupantvalue[31],ChildOccupantvalue[40],ChildOccupantvalue[43]]
# Pv8=[Pedestrianvalue[3],Pedestrianvalue[18],Pedestrianvalue[28],Pedestrianvalue[31],Pedestrianvalue[40],Pedestrianvalue[43]]
# SAv8=[SafetyAssistvalue[3],SafetyAssistvalue[18],SafetyAssistvalue[28],SafetyAssistvalue[31],SafetyAssistvalue[40],SafetyAssistvalue[43]]


# #輸出小型越野的圖
# output_file("小型越野.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b8':b8,'成人防護':AOv8,'兒童防護':COv8,'行人防護':Pv8,'安全輔助':SAv8}
# #colors=Category20b[len(cv)]
# colors=['#537791','#C1C0B9','#F7F6E7','#E7E6E1']
# p=figure(x_range=b8,plot_height=1000,title='2010~2017最佳小型越野',toolbar_location=None,tools='hover',tooltips='$name @b8: @$name')
# p.vbar_stack(cv,x='b8',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1200
# p.plot_height=1000
# show(p)





# #抓取大型越野所在位子與所在位子之值
# a9=[i for i,n in enumerate(carstypes) if n=='大型越野']
# print('大型越野所有的位子',a9)
# b9=[np3[7],np3[16],np3[30],np3[42]]
# print(b9)
# AOv9=[AdultOccupantvalue[7],AdultOccupantvalue[16],AdultOccupantvalue[30],AdultOccupantvalue[42]]
# COv9=[ChildOccupantvalue[7],ChildOccupantvalue[16],ChildOccupantvalue[30],ChildOccupantvalue[42]]
# Pv9=[Pedestrianvalue[7],Pedestrianvalue[16],Pedestrianvalue[30],Pedestrianvalue[42]]
# SAv9=[SafetyAssistvalue[7],SafetyAssistvalue[16],SafetyAssistvalue[30],SafetyAssistvalue[42]]


# #輸出大型越野的圖
# output_file("大型越野.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'b9':b9,'成人防護':AOv9,'兒童防護':COv9,'行人防護':Pv9,'安全輔助':SAv9}
# #colors=Category20b[len(cv)]
# colors=['#E8FCF6','#FFF07A','#A2EF44','#08085E']
# p=figure(x_range=b9,plot_height=1000,title='2010~2017最佳大型越野',toolbar_location=None,tools='hover',tooltips='$name @b9: @$name')
# p.vbar_stack(cv,x='b9',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1000
# p.plot_height=800
# show(p)





# #輸出每個年份的圖,請由上方for迴圈調整年份
# output_file("2017.html")


# cv=['成人防護','兒童防護','行人防護','安全輔助']
# data={'np3':np3,'成人防護':AdultOccupantvalue,'兒童防護':ChildOccupantvalue,'行人防護':SafetyAssistvalue,'安全輔助':Pedestrianvalue}
# colors=['#F3F798','#EAB4F8','#FCC8F8','#C7F5FE']
# p=figure(x_range=np3,plot_height=1000,title='',toolbar_location=None,tools='hover',tooltips='$name @np3: @$name')
# p.vbar_stack(cv,x='np3',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
# p.y_range.start=0
# p.x_range.range_padding=0.1
# p.xgrid.grid_line_color='#ff6600'
# p.axis.minor_tick_line_color='#cc6699'
# p.legend.location='top_right'
# p.legend.orientation='vertical'
# p.plot_width=1000
# p.plot_height=800
# show(p)

#將年式及車型合併成一個陣列
np5=np.char.array(year)
np6=np.char.array(carstypes)
np7=np5+np6

np8=[]
for cc in np7:
    np8.append(cc)
#判讀各年度個車型(需調整)所在位子      
aa=[i for i,n in enumerate(np8) if n=='2010运动跑车']
aa1=[i for i,n in enumerate(np8) if n=='2011运动跑车']
aa2=[i for i,n in enumerate(np8) if n=='2012运动跑车']
aa3=[i for i,n in enumerate(np8) if n=='2013运动跑车']
aa4=[i for i,n in enumerate(np8) if n=='2014运动跑车']
aa5=[i for i,n in enumerate(np8) if n=='2015运动跑车']
aa6=[i for i,n in enumerate(np8) if n=='2016运动跑车']
aa7=[i for i,n in enumerate(np8) if n=='2017运动跑车']
#print(aa,'|',aa1,'|',aa2,'|',aa3,'|',aa4,'|',aa5,'|',aa6,'|',aa7)
ct=[1,1,1,1,1,1,1,2]#小型家用车
ct1=[0,1,1,1,1,1,1,0]#大型家用车
ct2=[1,1,2,2,1,1,0,1]#小型 MPV
ct3=[0,0,1,0,0,1,0,0]#大型 MPV
ct4=[1,0,0,1,1,1,1,1]#小型越野
ct5=[0,1,1,0,0,1,0,1]#大型越野
ct6=[1,1,1,1,1,1,0,1]#微型车
ct7=[0,0,1,0,0,0,0,0]#商用及家用厢式车
ct8=[0,0,0,0,0,1,0,0]#运动跑车
year1=['2010','2011','2012','2013','2014','2015','2016','2017']

cv=['小型家用車','大型家用車','小型MPV','大型MPV','小型越野','大型越野','微型車','商用及家用廂式車','運動跑車']
output_file("2010~2017.html")
data={'year1':year1,'小型家用車':ct,'大型家用車':ct1,'小型MPV':ct2,'大型MPV':ct3,'小型越野':ct4,'大型越野':ct5,'微型車':ct6,'商用及家用廂式車':ct7,'運動跑車':ct8}
colors=['#F3F798','#EAB4F8','#FCC8F8','#C7F5FE','#FF2C2C','#FFEFEF','#A0B6F5','#7386D5','#B7F5DE']
p=figure(x_range=year1,plot_height=1000,title='',toolbar_location=None,tools='hover',tooltips='$name @year1: @$name')
p.vbar_stack(cv,x='year1',width=0.9,color=colors,source=data,legend=[value(x) for x in cv])
p.y_range.start=0
p.x_range.range_padding=0.1
p.xgrid.grid_line_color='#ff6600'
p.axis.minor_tick_line_color='#cc6699'
p.legend.location='top_left'
p.legend.orientation='vertical'
p.plot_width=1000
p.plot_height=800
show(p)

car_type=pd.DataFrame({'年式':year,'車型':carstypes,'車名':carsnames,'成人乘座防護':AdultOccupantvalue,'兒童乘坐防護':ChildOccupantvalue,'行人防護':Pedestrianvalue,'安全輔助':SafetyAssistvalue,})
print(car_type.info())
car_type.to_csv('BEST IN CLASS CARS OF 2010~2017.csv')