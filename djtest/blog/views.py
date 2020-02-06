from django.shortcuts import render
from blog.models import Myuser
# Create your views here.
from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate,login as auth_login ,logout 
from blog.forms import SignupForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import requests, json
from pyecharts.charts import Pie ,Grid,Bar,Line
from pyecharts.faker import Faker
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType


global jifen

def home(request):
    return render(request,'index.html',locals())


def index(request):
    shuju = requests.post("https://service-nxxl1y2s-1252957949.gz.apigw.tencentcs.com/release/newpneumonia")
    data = shuju.json()
    data = data['data']['conf']['component'][0]['caseList'][28]
    k = shuju.json()
    total = k['data']['conf']['component'][0]['summaryDataIn']['confirmed']
    cured = k['data']['conf']['component'][0]['summaryDataIn']['cured']
    yisi = k['data']['conf']['component'][0]['summaryDataIn']['unconfirmed']
    anhui_total = data['confirmed']
    anhui_crued = data['crued']
    wuhu_total = data['subList'][1]['confirmed']
    
    
    shuju1 = requests.get("https://yiqing.ahusmart.com/news/%E5%AE%89%E5%BE%BD%E7%9C%81")
    data = shuju1.json()
    news1 = data[0]
    news2 = data[1]
    news3 = data[2]
    news4 = data[3]
    news5 = data[4]
    news6 = data[5]
    news7 = data[6]
    
    
    
    news1_time = news1['infoSource'][0:14]
    #by :liuzaoqi huanshuo0801@gmail.com
    news1_source = news1['infoSource'][18:25]
    news1_url = news1['sourceUrl']
    news1_title = news1['title']
    
    news2_time = news2['infoSource'][0:14]
    news2_source = news2['infoSource'][18:25]
    news2_url = news2['sourceUrl']
    news2_title = news2['title']
    
    news3_time = news3['infoSource'][0:14]
    news3_source = news3['infoSource'][18:25]
    news3_url = news3['sourceUrl']
    news3_title = news3['title']
    
    news4_time = news4['infoSource'][0:14]
    news4_source = news4['infoSource'][18:25]
    news4_url = news4['sourceUrl']
    news4_title = news4['title']
    
    news5_time = news5['infoSource'][0:14]
    news5_source = news5['infoSource'][18:25]
    news5_url = news5['sourceUrl']
    news5_title = news5['title']
    
    news6_time = news6['infoSource'][0:14]
    news6_source = news6['infoSource'][18:25]
    news6_url = news6['sourceUrl']
    news6_title = news6['title']
    
    news7_time = news7['infoSource'][0:14]
    news7_source = news7['infoSource'][18:25]
    news7_url = news7['sourceUrl']
    news7_title = news7['title']
 
    
    
    
    return render(request, 'index.html',locals())
    #logout(request)   # 这个方法，会将存储在用户session的数据全部清空
    #return render(request, 'login.html', {'msg': ''})
def map1(request):

    return render(request, 'map1.html',locals())

def tables(request):
    ########

    shuju = requests.post("https://service-nxxl1y2s-1252957949.gz.apigw.tencentcs.com/release/newpneumonia")
    data = shuju.json()
    ####1=确诊 
    ####2=死亡
    ####3=治愈
    #西藏
    xz_1 = data['data']['conf']['component'][0]['caseList'][0]['confirmed']
    xz_2 = data['data']['conf']['component'][0]['caseList'][0]['died']
    xz_3 = data['data']['conf']['component'][0]['caseList'][0]['crued']
    #澳门
    am_1 = data['data']['conf']['component'][0]['caseList'][1]['confirmed']
    am_2 = data['data']['conf']['component'][0]['caseList'][1]['died']
    am_3 = data['data']['conf']['component'][0]['caseList'][1]['crued']
    #青海
    qh_1 = data['data']['conf']['component'][0]['caseList'][2]['confirmed']
    qh_2 = data['data']['conf']['component'][0]['caseList'][2]['died']
    qh_3 = data['data']['conf']['component'][0]['caseList'][2]['crued']
    #台湾
    tw_1 = data['data']['conf']['component'][0]['caseList'][3]['confirmed']
    tw_2 = data['data']['conf']['component'][0]['caseList'][3]['died']
    tw_3 = data['data']['conf']['component'][0]['caseList'][3]['crued']
    #香港
    hk_1 = data['data']['conf']['component'][0]['caseList'][4]['confirmed']
    hk_2 = data['data']['conf']['component'][0]['caseList'][4]['died']
    hk_3 = data['data']['conf']['component'][0]['caseList'][4]['crued']
    #贵州
    gz_1 = data['data']['conf']['component'][0]['caseList'][5]['confirmed']
    gz_2 = data['data']['conf']['component'][0]['caseList'][5]['died']
    gz_3 = data['data']['conf']['component'][0]['caseList'][5]['crued']
    #吉林
    jl_1 = data['data']['conf']['component'][0]['caseList'][6]['confirmed']
    jl_2 = data['data']['conf']['component'][0]['caseList'][6]['died']
    jl_3 = data['data']['conf']['component'][0]['caseList'][6]['crued']
    #新疆
    xj_1 = data['data']['conf']['component'][0]['caseList'][7]['confirmed']
    xj_2 = data['data']['conf']['component'][0]['caseList'][7]['died']
    xj_3 = data['data']['conf']['component'][0]['caseList'][7]['crued']
    #宁夏
    #by :liuzaoqi huanshuo0801@gmail.com
    nx_1 = data['data']['conf']['component'][0]['caseList'][8]['confirmed']
    nx_2 = data['data']['conf']['component'][0]['caseList'][8]['died']
    nx_3 = data['data']['conf']['component'][0]['caseList'][8]['crued']
    #内蒙古
    nmg_1 = data['data']['conf']['component'][0]['caseList'][9]['confirmed']
    nmg_2 = data['data']['conf']['component'][0]['caseList'][9]['died']
    nmg_3 = data['data']['conf']['component'][0]['caseList'][9]['crued']
    #甘肃
    gs_1 = data['data']['conf']['component'][0]['caseList'][10]['confirmed']
    gs_2 = data['data']['conf']['component'][0]['caseList'][10]['died']
    gs_3 = data['data']['conf']['component'][0]['caseList'][10]['crued']
    #天津
    tj_1 = data['data']['conf']['component'][0]['caseList'][11]['confirmed']
    tj_2 = data['data']['conf']['component'][0]['caseList'][11]['died']
    tj_3 = data['data']['conf']['component'][0]['caseList'][11]['crued']
    #山西
    sx_1 = data['data']['conf']['component'][0]['caseList'][12]['confirmed']
    sx_2 = data['data']['conf']['component'][0]['caseList'][12]['died']
    sx_3 = data['data']['conf']['component'][0]['caseList'][12]['crued']
    #辽宁
    ln_1 = data['data']['conf']['component'][0]['caseList'][13]['confirmed']
    ln_2 = data['data']['conf']['component'][0]['caseList'][13]['died']
    ln_3 = data['data']['conf']['component'][0]['caseList'][13]['crued']
    #黑龙江
    hlj_1 = data['data']['conf']['component'][0]['caseList'][14]['confirmed']
    hlj_2 = data['data']['conf']['component'][0]['caseList'][14]['died']
    hlj_3 = data['data']['conf']['component'][0]['caseList'][14]['crued']
    #海南
    hn_1 = data['data']['conf']['component'][0]['caseList'][15]['confirmed']
    hn_2 = data['data']['conf']['component'][0]['caseList'][15]['died']
    hn_3 = data['data']['conf']['component'][0]['caseList'][15]['crued']
    #河北
    hb_1 = data['data']['conf']['component'][0]['caseList'][16]['confirmed']
    hb_2 = data['data']['conf']['component'][0]['caseList'][16]['died']
    hb_3 = data['data']['conf']['component'][0]['caseList'][16]['crued']
    #陕西
    sx1_1 = data['data']['conf']['component'][0]['caseList'][17]['confirmed']
    sx1_2 = data['data']['conf']['component'][0]['caseList'][17]['died']
    sx1_3 = data['data']['conf']['component'][0]['caseList'][17]['crued']
    #云南
    yn_1 = data['data']['conf']['component'][0]['caseList'][18]['confirmed']
    yn_2 = data['data']['conf']['component'][0]['caseList'][18]['died']
    yn_3 = data['data']['conf']['component'][0]['caseList'][18]['crued']
    #广西
    gx_1 = data['data']['conf']['component'][0]['caseList'][19]['confirmed']
    gx_2 = data['data']['conf']['component'][0]['caseList'][19]['died']
    gx_3 = data['data']['conf']['component'][0]['caseList'][19]['crued']
    #福建
    fj_1 = data['data']['conf']['component'][0]['caseList'][20]['confirmed']
    fj_2 = data['data']['conf']['component'][0]['caseList'][20]['died']
    fj_3 = data['data']['conf']['component'][0]['caseList'][20]['crued']
    #上海
    sh_1 = data['data']['conf']['component'][0]['caseList'][21]['confirmed']
    sh_2 = data['data']['conf']['component'][0]['caseList'][21]['died']
    sh_3 = data['data']['conf']['component'][0]['caseList'][21]['crued']
    #北京
    bj_1 = data['data']['conf']['component'][0]['caseList'][22]['confirmed']
    bj_2 = data['data']['conf']['component'][0]['caseList'][22]['died']
    bj_3 = data['data']['conf']['component'][0]['caseList'][22]['crued']
    #江苏
    js_1 = data['data']['conf']['component'][0]['caseList'][23]['confirmed']
    js_2 = data['data']['conf']['component'][0]['caseList'][23]['died']
    js_3 = data['data']['conf']['component'][0]['caseList'][23]['crued']
    #四川 
    sc_1 = data['data']['conf']['component'][0]['caseList'][24]['confirmed']
    sc_2 = data['data']['conf']['component'][0]['caseList'][24]['died']
    sc_3 = data['data']['conf']['component'][0]['caseList'][24]['crued']
    #山东
    sd_1 = data['data']['conf']['component'][0]['caseList'][25]['confirmed']
    sd_2 = data['data']['conf']['component'][0]['caseList'][25]['died']
    sd_3 = data['data']['conf']['component'][0]['caseList'][25]['crued']
    #江西
    jx_1 = data['data']['conf']['component'][0]['caseList'][26]['confirmed']
    jx_2 = data['data']['conf']['component'][0]['caseList'][26]['died']
    jx_3 = data['data']['conf']['component'][0]['caseList'][26]['crued']
    #重庆
    cq_1 = data['data']['conf']['component'][0]['caseList'][27]['confirmed']
    cq_2 = data['data']['conf']['component'][0]['caseList'][27]['died']
    cq_3 = data['data']['conf']['component'][0]['caseList'][27]['crued']
    #安徽
    ah_1 = data['data']['conf']['component'][0]['caseList'][28]['confirmed']
    ah_2 = data['data']['conf']['component'][0]['caseList'][28]['died']
    ah_3 = data['data']['conf']['component'][0]['caseList'][28]['crued']
    #湖南
    hn1_1 = data['data']['conf']['component'][0]['caseList'][29]['confirmed']
    hn1_2 = data['data']['conf']['component'][0]['caseList'][29]['died']
    hn1_3 = data['data']['conf']['component'][0]['caseList'][29]['crued']
    #河南
    hn2_1 = data['data']['conf']['component'][0]['caseList'][30]['confirmed']
    hn2_2 = data['data']['conf']['component'][0]['caseList'][30]['died']
    hn2_3 = data['data']['conf']['component'][0]['caseList'][30]['crued']
    #广东
    gd_1 = data['data']['conf']['component'][0]['caseList'][31]['confirmed']
    gd_2 = data['data']['conf']['component'][0]['caseList'][31]['died']
    gd_3 = data['data']['conf']['component'][0]['caseList'][31]['crued']
    #浙江
    zj_1 = data['data']['conf']['component'][0]['caseList'][32]['confirmed']
    zj_2 = data['data']['conf']['component'][0]['caseList'][32]['died']
    zj_3 = data['data']['conf']['component'][0]['caseList'][32]['crued']
    #湖北
    hubei_1 = data['data']['conf']['component'][0]['caseList'][33]['confirmed']
    hubei_2 = data['data']['conf']['component'][0]['caseList'][33]['died']
    hubei_3 = data['data']['conf']['component'][0]['caseList'][33]['crued']
    
    anhui = data['data']['conf']['component'][0]['caseList'][28]['subList']
    
    #安庆
    aq1 = anhui[0]['confirmed']
    aq2 = anhui[0]['died']
    aq3 = anhui[0]['crued']
    #芜湖
    wh1 = anhui[1]['confirmed']
    wh2 = anhui[1]['died']
    wh3 = anhui[1]['crued']
    #亳州
    bz1 = anhui[2]['confirmed']
    bz2 = anhui[2]['died']
    bz3 = anhui[2]['crued']
    #黄山
    hs1 = anhui[3]['confirmed']
    hs2 = anhui[3]['died']
    hs3 = anhui[3]['crued']
    #淮北
    hb1 = anhui[4]['confirmed']
    hb2 = anhui[4]['died']
    hb3 = anhui[4]['crued']
    #蚌埠
    bb1 = anhui[5]['confirmed']
    bb2 = anhui[5]['died']
    bb3 = anhui[5]['crued']
    #马鞍山
    mas1 = anhui[6]['confirmed']
    mas2 = anhui[6]['died']
    mas3 = anhui[6]['crued']
    #铜陵
    tl1 = anhui[7]['confirmed']
    tl2 = anhui[7]['died']
    tl3 = anhui[7]['crued']
    #池州
    cz1 = anhui[8]['confirmed']
    cz2 = anhui[8]['died']
    cz3 = anhui[8]['crued']
    #宿州
    sz1 = anhui[9]['confirmed']
    sz2 = anhui[9]['died']
    sz3 = anhui[9]['crued']
    #合肥
    hf1 = anhui[10]['confirmed']
    hf2 = anhui[10]['died']
    hf3 = anhui[10]['crued']
    #宣城
    xc1 = anhui[11]['confirmed']
    xc2 = anhui[11]['died']
    xc3 = anhui[11]['crued']
    #滁州
    cz1 = anhui[12]['confirmed']
    cz2 = anhui[12]['died']
    cz3 = anhui[12]['crued']
    #阜阳
    fy1 = anhui[13]['confirmed']
    fy2 = anhui[13]['died']
    fy3 = anhui[13]['crued']
    #淮南
    hn1 = anhui[14]['confirmed']
    hn2 = anhui[14]['died']
    hn3 = anhui[14]['crued']
    #六安
    la1 = anhui[15]['confirmed']
    la2 = anhui[15]['died']
    la3 = anhui[15]['crued']
    
    
    
    
    return render(request, 'tables.html',locals())

def map2(request):

    return render(request, 'map2.html',locals())

def test(request):

    return render(request, 'test.html',locals())


def charts(request):

    return render(request, 'charts.html',locals())

def line(request):

    return render(request, 'line.html',locals())

def pie1(request):

    return render(request, 'pie1.html',locals())
def pie2(request):

    return render(request, 'pie2.html',locals())

def map3(request):

    return render(request, 'map3.html',locals())