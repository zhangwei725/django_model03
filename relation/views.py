from django.http import HttpResponse
from django.shortcuts import render
from relation.models import *

"""
1>  注意  添加子表数据的时候主表的数据一定要存在
2>  主表添加数据不影响子表
3>   往子表添加数据
4>   注意  外键字段 可以是对象   也可以是主键   


"""


# 91助手

# pk  表示主键
# 外键字段 系统会默认生成一个 外键名_id的字段
def insert(request):
    stu = Student(stu_name='强鹏')
    stu.save()
    # stu.stu_id
    # stu.pk
    # stu = Student.objects.filter(stu_id=3).first()
    stu_detail = StuDetail(no=1024, sex=False, height=189, email='123@qq.com', stu_id=stu.stu_id)
    stu_detail.save()
    return HttpResponse('一对一添加')


# 一对一查询的时候 通过主表查询子表  如果想获取响应的子表的数据 直接可以通过主表对象.子表的类名小写获取
#  主模型对象.子表类名小写

def find(request):
    # 通过主表查子表
    students = Student.objects.filter(is_delete=False)
    for stu in students:
        print(stu.stu_name)
        print(stu.studetail.no)
    return render(request, 'students.html', {'stu_list': students})


# 通过子表查主表
# 也能获取主表的数据
#  子表对象.外键字段.
def find1(request):
    sd_list = StuDetail.objects.all()
    for detail in sd_list:
        print(detail.no)
        print(detail.stu_id.stu_name)
    return HttpResponse('1111')
    # return render(request, 'students.html', {'stu_list': sd_list})
