# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:01:04 2019

@author: 万
"""

import pymysql
import time
import datetime

#  会员充值分类
def recharge(userid,number):
    # 用户充值金额number赋值给本地变量money
    money = number
    #  设定月、季、年、永久会员金额
    month = 15
    quarter = 30
    year = 399
    life = 599
    #  定义最大金额
    maxMoney = 99999
    #  定义userType
#    nonType = 0
    monthType = 7
    quarterType = 8
    yearType = 9
    lifeType = 10
    # 设定月、季、年、永久会员相应换算的时间戳
    monthtimestamp = 30 * 24 * 3600
    quartertimestamp = monthtimestamp * 4
    yeartimestamp = monthtimestamp * 12 + 5 
    
    endTimeMonth = 0
    endTimeQuarter = 0
    endTimeYear = 0
    endTimeLife = 0
    endtimestamp = 0
    # 获取当前日期
#    currentdate = time.strftime("%Y-%m-%d", time.localtime())
    # 获取当前时间戳
    currenttimestamp = time.time()

    # 打开数据库连接
    db = pymysql.connect("localhost","root","mcg123","wp" )
     
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    
    # SQL语句处理
    sql = "SELECT * FROM wp_ice_info WHERE ice_user_id = %s" % (userid)
    
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
          endtime = row[5]
          print(endtime)
          # 将endtime 转换为时间戳形式       
          endtimestamp = time.mktime(endtime.timetuple())
    except:
        # 
        print("endtime get fail --- userid = %s --- wp_ice_info"% (userid))
        # 发生错误时回滚
        db.rollback()
     
    # 分为过期与未过期（非会员）进行处理
    if endtimestamp <= currenttimestamp:
        # if 过期/不是会员 即 1970-01-01 换算为时间戳 == 0
        # 当前时间戳 + 会员时间戳 -> 总时间戳再换算成日期newendtime
        if money == month:
            endTimeMonth = ''.join(time.strftime("%Y-%m-%d",time.localtime(currenttimestamp + monthtimestamp)).split("-"))     
            print(endTimeMonth)
        elif money == quarter:
            endTimeQuarter = ''.join(time.strftime("%Y-%m-%d",time.localtime(currenttimestamp + quartertimestamp)).split("-"))
        elif money == year:
            endTimeYear = ''.join(time.strftime("%Y-%m-%d",time.localtime(currenttimestamp + yeartimestamp)).split("-"))
        elif money == life:
            endTimeLife = "21000101"
            print("here 1")
    else :
        # else 未过期  
        # 获取endtime，将endtime转换成时间戳再再加上money所产生的会员时间（同样换算成时间戳），相加再转换成日期形式newendtime
        if money == month:
            endTimeMonth = ''.join(time.strftime("%Y-%m-%d",time.localtime(currenttimestamp + monthtimestamp)).split("-"))
        elif money == quarter:
            endTimeQuarter = ''.join(time.strftime("%Y-%m-%d",time.localtime(currenttimestamp + quartertimestamp)).split("-"))
        elif money == year:
            endTimeYear = ''.join(time.strftime("%Y-%m-%d",time.localtime(currenttimestamp + yeartimestamp)).split("-"))
        elif money == life:
            endTimeLife = "21000101"
            print("here 2")
            
    # "wp_ce_info"执行会员操作，设置：ice_have_money、ice_get_money、userType、endTime 
    # SQL 语句  ***暂未考虑数据库的表是否有初始默认值***
    sql_month = "UPDATE wp_ice_info SET ice_have_money = %s,  ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (maxMoney,month,monthType,endTimeMonth,userid)   
    sql_quarter = "UPDATE wp_ice_info SET ice_have_money = %s,ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (maxMoney,quarter,quarterType,endTimeQuarter,userid)   
    sql_year = "UPDATE wp_ice_info SET ice_have_money = %s,   ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (maxMoney,year,yearType,endTimeYear,userid)
    sql_life = "UPDATE wp_ice_info SET ice_have_money = %s,   ice_get_money = ice_get_money + %s,userType = %s,endTime = %s WHERE ice_user_id = %s" % (maxMoney,life,lifeType,endTimeLife,userid)   
    
    try:
         # 执行sql语句
        if money == month:
            print(sql_month)
            cursor.execute(sql_month)
        elif money == quarter:
            cursor.execute(sql_quarter)
        elif money == year:
            cursor.execute(sql_year)
        elif money == life:
            cursor.execute(sql_life)
        # 提交
        db.commit()
        
    except:
        print("updata fail --- userid : %s --- wp_ice_info "%(userid))
        # 发生错误时回滚
        db.rollback()
   
    # 关闭数据库连接
    db.close()

def expired(userid):
    currenttimestamp = time.time()
    print(currenttimestamp)
    endtimestamp = 0
    # 打开数据库连接
    db = pymysql.connect("localhost","root","mcg123","wp" )
     
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
   
    # SQL语句处理:遍历整个表
    sql = "SELECT * FROM wp_ice_info WHERE ice_user_id = %s" % (userid)
    
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       print(results)
       for row in results:
           endtime = row[5]
           # 将endtime 转换为时间戳形式       
           endtimestamp = time.mktime(endtime.timetuple())
           print(endtimestamp)
           # 判定程序
           if endtimestamp <= currenttimestamp:    
               # 此时该用户会员过期
               # 设置该userid：ice_have_money = 0,userType = 0
               sql_updata = "UPDATE wp_ice_info SET ice_have_money = %s,userType = %s WHERE ice_user_id = %s" % (0,0,userid)
               try:
                   cursor.execute(sql_updata)
                   db.commit()
               except:
                   print("updata get fail --- userid = %s --- wp_ice_info "% (userid))
                   db.rollback()

           
    except:
        # 
        print("endtime get fail --- userid = %s --- wp_ice_info "% (userid))
        # 发生错误时回滚
        db.rollback()
        # 关闭数据库连接
    db.close()
 
def main():
    userid = 1
    number = 599
    recharge(userid,number)
#    expired(userid)
    
main()