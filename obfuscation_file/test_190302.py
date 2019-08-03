# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:01:04 2019

@author: 万
"""

import pymysql
import time
import datetime

#  会员充值分类
def recharge(vq3dfcqej3bg9iza,4rjne25j91tiduqh):
    # 用户充值金额number赋值给本地变量money
    3fkemoyzr14c5g4u=4rjne25j91tiduqh
    #  设定月、季、年、永久会员金额
    ziu7eswqioz2vxls=15
    qn7lhjatakhmwwcx=30
    zl7sdhjdm1sizgpc=399
    86bsc9npcx5nuxgn=599
    #  定义最大金额
    3cmthj9qsn4o83vd=99999
    #  定义userType
#    nonType = 0
    p5s2lnmpl3o06cez=7
    syq514l91p8ry3hu=8
    u3gggqo1zp7f9hts=9
    06lkj99z3h4tjnsb=10
    # 设定月、季、年、永久会员相应换算的时间戳
    d66yk1kqy6kkh9im=30 * 24 * 3600
    mp6q6yewdc4413c3=d66yk1kqy6kkh9im * 4
    wc8nskwnc7gvtf5s=d66yk1kqy6kkh9im * 12 + 5 
    
    fed19g8lwdn02e26=0
    ybvf6k1l02f8cxkm=0
    r8svjw3gy2eh3exh=0
    twoevc8s7snvx5ho=0
    dxi4743wlmmr8u44=0
    # 获取当前日期
#    currentdate = time.strftime("%Y-%m-%d", time.localtime())
    # 获取当前时间戳
    9xjso0o18ivxrg2t=time.time()

    # 打开数据库连接
    d8wk7b0kdknyr7s1=pymysql.connect("localhost","root","mcg123","wp" )
     
    # 使用 w6eydpv0aw1g7kv0() 方法创建一个游标对象 w6eydpv0aw1g7kv0
    w6eydpv0aw1g7kv0=d8wk7b0kdknyr7s1.w6eydpv0aw1g7kv0()
    
    # SQL语句处理
    pyaxqfc3pcmyt9eh="SELECT * FROM wp_ice_info WHERE ice_user_id = %s" % (vq3dfcqej3bg9iza)
    
    try:
       # 执行SQL语句
       w6eydpv0aw1g7kv0.execute(pyaxqfc3pcmyt9eh)
       # 获取所有记录列表
       vpfu80qezlik2q08=w6eydpv0aw1g7kv0.fetchall()
       for row in vpfu80qezlik2q08:
          j83nwu0jqebmem4m=row[5]
          print(j83nwu0jqebmem4m)
          # 将endtime 转换为时间戳形式       
          dxi4743wlmmr8u44=time.mktime(j83nwu0jqebmem4m.timetuple())
    except:
        # 
        print("j83nwu0jqebmem4m get fail --- vq3dfcqej3bg9iza = %s --- wp_ice_info"% (vq3dfcqej3bg9iza))
        # 发生错误时回滚
        d8wk7b0kdknyr7s1.rollback()
     
    # 分为过期与未过期（非会员）进行处理
    if dxi4743wlmmr8u44 <= 9xjso0o18ivxrg2t:
        # if 过期/不是会员 即 1970-01-01 换算为时间戳 == 0
        # 当前时间戳 + 会员时间戳 -> 总时间戳再换算成日期newendtime
        if 3fkemoyzr14c5g4u == ziu7eswqioz2vxls:
            fed19g8lwdn02e26=''.join(time.strftime("%Y-%m-%d",time.localtime(9xjso0o18ivxrg2t + d66yk1kqy6kkh9im)).split("-"))     
            print(fed19g8lwdn02e26)
        elif 3fkemoyzr14c5g4u == qn7lhjatakhmwwcx:
            ybvf6k1l02f8cxkm=''.join(time.strftime("%Y-%m-%d",time.localtime(9xjso0o18ivxrg2t + mp6q6yewdc4413c3)).split("-"))
        elif 3fkemoyzr14c5g4u == zl7sdhjdm1sizgpc:
            r8svjw3gy2eh3exh=''.join(time.strftime("%Y-%m-%d",time.localtime(9xjso0o18ivxrg2t + wc8nskwnc7gvtf5s)).split("-"))
        elif 3fkemoyzr14c5g4u == 86bsc9npcx5nuxgn:
            twoevc8s7snvx5ho="21000101"
            print("here 1")
    else :
        # else 未过期  
        # 获取endtime，将endtime转换成时间戳再再加上money所产生的会员时间（同样换算成时间戳），相加再转换成日期形式newendtime
        if 3fkemoyzr14c5g4u == ziu7eswqioz2vxls:
            fed19g8lwdn02e26=''.join(time.strftime("%Y-%m-%d",time.localtime(9xjso0o18ivxrg2t + d66yk1kqy6kkh9im)).split("-"))
        elif 3fkemoyzr14c5g4u == qn7lhjatakhmwwcx:
            ybvf6k1l02f8cxkm=''.join(time.strftime("%Y-%m-%d",time.localtime(9xjso0o18ivxrg2t + mp6q6yewdc4413c3)).split("-"))
        elif 3fkemoyzr14c5g4u == zl7sdhjdm1sizgpc:
            r8svjw3gy2eh3exh=''.join(time.strftime("%Y-%m-%d",time.localtime(9xjso0o18ivxrg2t + wc8nskwnc7gvtf5s)).split("-"))
        elif 3fkemoyzr14c5g4u == 86bsc9npcx5nuxgn:
            twoevc8s7snvx5ho="21000101"
            print("here 2")
            
    # "wp_ce_info"执行会员操作，设置：ice_have_money、ice_get_money、userType、endTime 
    # SQL 语句  ***暂未考虑数据库的表是否有初始默认值***
    sql_month = "UPDATE wp_ice_info SET ice_have_money = %s,  ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (3cmthj9qsn4o83vd,ziu7eswqioz2vxls,p5s2lnmpl3o06cez,fed19g8lwdn02e26,vq3dfcqej3bg9iza)   
    sql_quarter = "UPDATE wp_ice_info SET ice_have_money = %s,ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (3cmthj9qsn4o83vd,qn7lhjatakhmwwcx,syq514l91p8ry3hu,ybvf6k1l02f8cxkm,vq3dfcqej3bg9iza)   
    sql_year = "UPDATE wp_ice_info SET ice_have_money = %s,   ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (3cmthj9qsn4o83vd,zl7sdhjdm1sizgpc,u3gggqo1zp7f9hts,r8svjw3gy2eh3exh,vq3dfcqej3bg9iza)
    sql_life = "UPDATE wp_ice_info SET ice_have_money = %s,   ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (3cmthj9qsn4o83vd,86bsc9npcx5nuxgn,06lkj99z3h4tjnsb,twoevc8s7snvx5ho,vq3dfcqej3bg9iza)   
    
    try:
         # 执行sql语句
        if 3fkemoyzr14c5g4u == ziu7eswqioz2vxls:
            print(sql_month)
            w6eydpv0aw1g7kv0.execute(sql_month)
        elif 3fkemoyzr14c5g4u == qn7lhjatakhmwwcx:
            w6eydpv0aw1g7kv0.execute(sql_quarter)
        elif 3fkemoyzr14c5g4u == zl7sdhjdm1sizgpc:
            w6eydpv0aw1g7kv0.execute(sql_year)
        elif 3fkemoyzr14c5g4u == 86bsc9npcx5nuxgn:
            w6eydpv0aw1g7kv0.execute(sql_life)
        # 提交
        d8wk7b0kdknyr7s1.commit()
        
    except:
        print("updata fail --- vq3dfcqej3bg9iza : %s --- wp_ice_info "%(vq3dfcqej3bg9iza))
        # 发生错误时回滚
        d8wk7b0kdknyr7s1.rollback()
   
    # 关闭数据库连接
    d8wk7b0kdknyr7s1.close()

def expired(vq3dfcqej3bg9iza):
    9xjso0o18ivxrg2t=time.time()
    print(9xjso0o18ivxrg2t)
    dxi4743wlmmr8u44=0
    # 打开数据库连接
    d8wk7b0kdknyr7s1=pymysql.connect("localhost","root","mcg123","wp" )
     
    # 使用 w6eydpv0aw1g7kv0() 方法创建一个游标对象 w6eydpv0aw1g7kv0
    w6eydpv0aw1g7kv0=d8wk7b0kdknyr7s1.w6eydpv0aw1g7kv0()
   
    # SQL语句处理:遍历整个表
    pyaxqfc3pcmyt9eh="SELECT * FROM wp_ice_info WHERE ice_user_id = %s" % (vq3dfcqej3bg9iza)
    
    try:
       # 执行SQL语句
       w6eydpv0aw1g7kv0.execute(pyaxqfc3pcmyt9eh)
       # 获取所有记录列表
       vpfu80qezlik2q08=w6eydpv0aw1g7kv0.fetchall()
       print(vpfu80qezlik2q08)
       for row in vpfu80qezlik2q08:
           j83nwu0jqebmem4m=row[5]
           # 将endtime 转换为时间戳形式       
           dxi4743wlmmr8u44=time.mktime(j83nwu0jqebmem4m.timetuple())
           print(dxi4743wlmmr8u44)
           # 判定程序
           if dxi4743wlmmr8u44 <= 9xjso0o18ivxrg2t:    
               # 此时该用户会员过期
               # 设置该userid：ice_have_money = 0,userType = 0
               sql_updata = "UPDATE wp_ice_info SET ice_have_money = %s,userType = %s WHERE ice_user_id = %s" % (0,0,vq3dfcqej3bg9iza)
               try:
                   w6eydpv0aw1g7kv0.execute(sql_updata)
                   d8wk7b0kdknyr7s1.commit()
               except:
                   print("updata get fail --- vq3dfcqej3bg9iza = %s --- wp_ice_info "% (vq3dfcqej3bg9iza))
                   d8wk7b0kdknyr7s1.rollback()

           
    except:
        # 
        print("j83nwu0jqebmem4m get fail --- vq3dfcqej3bg9iza = %s --- wp_ice_info "% (vq3dfcqej3bg9iza))
        # 发生错误时回滚
        d8wk7b0kdknyr7s1.rollback()
        # 关闭数据库连接
    d8wk7b0kdknyr7s1.close()
 
def main():
    vq3dfcqej3bg9iza=1
    4rjne25j91tiduqh=599
    recharge(vq3dfcqej3bg9iza,4rjne25j91tiduqh)
#    expired(vq3dfcqej3bg9iza)
    
main()