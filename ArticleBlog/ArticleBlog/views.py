"""
# from django.http import HttpResponse
from django.shortcuts import HttpResponse, render, redirect


def index(request):
    return HttpResponse('<h1 style="color: skyblue;">Hello World</h1>')


def login(request):
    return render(request, 'login.html')


def show(request):
    return redirect("https://github.com/bestwishfang")


def introduce(request, name, num):
    return HttpResponse('<h1 style="color: blue;">Hello name: {}, number: {}</h1>'.format(name, num))
"""
from django.http import HttpResponse
from django.template.loader import get_template


def index(request):
    template = get_template("index.html")
    ret = template.render({})  # 要给render()传参 参数是dict
    return HttpResponse(ret)


# def page_list(request, page):
#     print(type(page))  # <class 'str'>
#     template = get_template("pageList.html")
#     ret = template.render({"number": page})
#     print(type(ret))  # <class 'django.utils.safestring.SafeText'>
#     print(ret)
#     return HttpResponse(ret)


def template_variable(request):
    """渲染变量"""
    data = {
        "name": "fang",
        "age": 29,
        "course": ['Python', 'C#', 'JavaScript', 'Go']
    }
    temp = get_template("template_variable.html")
    ret = temp.render(data)
    return HttpResponse(ret)


def template_label(request):
    """渲染标签"""
    data = {
        "teacher": [
            {"name": "li", "age": 30, "gender": "male"},
            {"name": "wang", "age": 30, "gender": "male"},
            {"name": "shen", "age": 30, "gender": "male"},
            {"name": "wen", "age": 30, "gender": "male"},
            {"name": "bian", "age": 30, "gender": "male"},
        ],
        "course": [
            {"name": "Python", "fee": 23800, "period": "five months"},
            {"name": "Java", "fee": 23800, "period": "five months"},
            {"name": "Linux", "fee": 21800, "period": "four months"},
            {"name": "Web", "fee": 21800, "period": "four months"},
            {"name": "UI/UE", "fee": 21800, "period": "four months"},
            {"name": "Android", "fee": 21800, "period": "four months"},
        ],

    }
    temp = get_template("template_label.html")
    ret = temp.render(data)
    return HttpResponse(ret)


articles = [
    {"id": 1, "title": "背影", "author": "朱自清", "public_time": "1883-3-3", "content": "买橘子的故事", "image": "image/beiying.jpg"},
    {"id": 2, "title": "骆驼祥子", "author": "老舍", "public_time": "1885-3-3", "content": "北京最早的D哥的爱情故事", "image": "image/luotuoxiangzi.jpg"},
    {"id": 3, "title": "鬼吹灯", "author": "三叔", "public_time": "1873-3-3", "content": "空气对流的故事", "image": "image/guichuideng.jpg"},
    {"id": 4, "title": "蜀道难", "author": "李白", "public_time": "1643-3-3", "content": "那是一条神奇的天路", "image": "image/shudaonan.jpg"},
    {"id": 5, "title": "道德经", "author": "老子", "public_time": "1873-3-3", "content": "教育的故事", "image": "image/daodejing.jpg"},
    {"id": 6, "title": "三国志", "author": "陈寿", "public_time": "270-3-4", "content": "东汉末年到魏晋的故事", "image": "image/sanguozhi.jpg"},
]


def page_list(request):
    """列表页"""
    template = get_template("page_list.html")
    ret = template.render({"articles": articles})
    return HttpResponse(ret)


def page(request, num):
    """详情页"""
    article = None
    for art in articles:
        if art["id"] == int(num):
            article = art

    template = get_template("page.html")
    ret = template.render({"article": article})
    return HttpResponse(ret)


"""forloop"""

