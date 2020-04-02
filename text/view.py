from django.http import HttpResponse
import json

data=[]

def add(name,score):
    rank=1
    if data==[]:
        data.append([name, score, rank])
        return  1
    for i in range(len(data)):
        if data[i][0]==name :
            t=[0,0,0]
            data[i][1]=score
            for i in range(len(data)):
                for j in range(i,len(data)):
                    if data[i][1]<data[j][1]:
                        t[0] = data[i][0]
                        t[1] = data[i][1]
                        t[2] = data[i][2]
                        data[i][0] = data[j][0]
                        data[i][1] = data[j][1]
                        data[i][2] = data[j][2]
                        data[j][0] = t[0]
                        data[j][1] = t[1]
                        data[j][2] = t[2]
                data[i][2]=i+1
            return 1
            break
    for i in range(len(data)):
        if data[i][1] > score:
            rank+=1
        else :
            data[i][2]+=1
    data.append([name,score,rank])

def search (a,b,name):
    user=[]
    for i in range(len(data)):
        if data[i][0]==name:
            user.append([data[i][0],data[i][1],data[i][2]])
    return data[a-1:b]+user[0:3]

def check(request):
    if request.method == 'POST':
        name = request.POST.get('name',0)
        check1 = int(request.POST.get('check1',0))
        check2 = int(request.POST.get('check2',0))
        if name and check1 and check2:
            result=search(check1, check2, name)
            return HttpResponse(result)
        else:
            return HttpResponse('输入为空')

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name',0)
        score = int(request.POST.get('score',0))
        if name and score:
            add(name,score)
            return HttpResponse(data)
        elif score<1 or score>10000000:
            return HttpResponse('输入错误')
        else:
            return HttpResponse('输入错误')
    else:
        return HttpResponse('方法错误')
