from django.db import models

# Create your models here.
# 所谓的关系  指的的表与表之间有关系
#   用户 收货地址
#  90%表与表之间都是有关系的
#  使用外键约束
"""
1>必须有两个表 (两个模型)
2>必须区分主表跟子表
3>外键建立在子表上
4>把主表的某个字段(参照字段 必须是唯一约束, 一般情况下把主表的主键作为从表外键的参照字段)作为从表的外键字段

# 通过某个表查询另外表的   

"""

# 用户表 跟 地址     用户表跟购车表

# 通过用户查找地址


""""
create  table   user  (
    uid  int auto_increment  primary key,
    username   varchar(64) not  null   unique,
)

create  table  address(
    addr_id   int auto_increment  primary key,
    city  varchar(64) 
    uid   int,
    constrain fk_address_uid foreign key(uid) references  user(uid)
)
"""


#
#  已知用户名 查询该用户的信息以及用户的地址信息
#   SELECT  * FROM  USER   WHERE  USERNAME='小明'
#   通过用户的id然后在去查询地址表
#   SELECT  * FROM  ADDRESS  WHERE  UID = 1
# 如何建立表与表之间的关系  通过外键约束
# orm 如何实现
#   一个老公对应一个老婆()   商品信息跟商品详情   学生详情一对一的关系
#   主表里的一条记录对应从表里面的多条记录

#  一对一   OneToOneFields
#  多对一(一对多)  一个用户对应多个地址    ForeignKey
#  多对多 性能差    ManyToMany()

class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=64, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'student'


class StuDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    no = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    email = models.CharField(max_length=100)
    height = models.IntegerField()
    """
    to  表示参照的主表    在模型里面是类的名称
    on_delete  删除策略 (主要是针对主表删除某条记录 子表的数据如何处理)
         取值范围   CASCADE 当主表数据删除之后 ,子表相关联的数据也删除
                   SET_NULL 当主表数据删除之后 ,子表关联字段设置为null ( 关联字段必须使用null=True) 
                   DO_NOTHING 当主表数据删除之后 子表数据没有任何影响
               
     db_column   设置数据库外键字段的名称
     to_field    设置参照的外键   默认是主表的主键字段
    """
    # 外键字段在数据库里 默认生成 属性名称_ID
    stu_id = models.OneToOneField('Student', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'stu_detail'
