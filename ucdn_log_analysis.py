#-*- encoding: utf-8 -*-
from sdk import UcloudApiClient 
from config import *
import sys
import json

#实例化 API 句柄
ApiClient = UcloudApiClient(base_url, public_key, private_key)

def get_log_analysis():
    #调用cdn内容刷新API 
    response = ApiClient.get('/ucdn/loganalysis',
        cdn_domain='ucloud.cn',
        begin_time='2014-04-04',
        end_time='2014-04-06',
        type = 1,
        count = 5
    )
    print response

get_log_analysis();

#API 说明:
#   1,请输入您要分析的域名，开始查询时间，和结束时间,日志类型，显示结果数量。
#   2,开始时间和结束时间是字符串型，如"2014-04-04",字串长度为10，错误的格式会导致查询不成功。
#POST字段说明：
#   cdn_domain  //查询日志分析的域名
#   begin_time  //查询日志分析的起始时间
#   end_time    //查询日志分析的结束时间
#   type        // 日志分析 的类型 1：下载最多  2：流量最多
#   count       //查询结果显示数量
#返回值字段说明：
#ret_code      //执行结果状态码 0：执行成功 
#error_message //错误提示语
#data          //返回日志分析结果，结构如下：
#[{"file_download_count":"68","file_traffic":"0.32","file_url":"http:\/\/ucloud.cn\/LOGO.png"},{"file_download_count":"57","file_traffic":"0.51","file_url":"http:\/\/ucloud.cn\/acea4778cdec704477c905deacc61ca2.png"},{"file_download_count":"23","file_traffic":"6.81","file_url":"http:\/\/ucloud.cn\/c4026298060cf87c6ffa40ac785cfa5f.rar"},{"file_download_count":"8","file_traffic":"0.38","file_url":"http:\/\/ucloud.cn\/af09e055f522311dde8b6b2145a89a5d.png"},{"file_download_count":"7","file_traffic":"5.68","file_url":"http:\/\/ucloud.cn\/78708b3b6245b871c7618f4217277989.jpg"}]
