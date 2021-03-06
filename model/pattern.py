#!/usr/bin/env python
# coding:utf-8

import re

o = [
    u'[前昨今明后][天日]?[早晚][晨上间]?',
    u'\\d+个?[年月日天][以之]?[前后]',
    u'\\d+个?半?(小时|钟头|h|H)',
    u'半个?(小时|钟头)',
    u'\\d+(分钟|min)',
    u'[13]刻钟',
    u'[上这本下]*个?(周|星期)([一二三四五六七天日]|[1-7])?',
    u'[早晚]?([0-2]?[0-9][点时]半)(am|AM|pm|PM)?',
    u'[早晚]?(\\d+[:：]\d+([:：]\d+)*)\s*(am|AM|pm|PM)?',
    u'[早晚]?([0-2]?[0-9][点时][13一三]刻)(am|AM|pm|PM)?',
    u'[早晚]?(\d+[时点](\d+)?分?(\d+秒?)?)\s*(am|AM|pm|PM)?',
    u'大+[前后]天',
    u'[零一二三四五六七八九十百千万\d]+世',
    u'[0-9]?[0-9]?[0-9]{2}\.(10|11|12|[1-9])\.(?<!\\d)([0-3][0-9]|[1-9])',
    u'现在',
    u'届时',
    u'这个月',
    u'[前后]日',
    u'晚些时候',
    u'今年',
    u'长期',
    u'以前',
    u'过去',
    u'时期',
    u'时代',
    u'当时',
    u'近来',
    u'[零一二三四五六七八九十百千万\d]+夜',
    u'当前',
    u'\d+点',
    u'今年[零一二三四五六七八九十百千万\d]+',
    u'\d+[:：]\d+分?',
    u'\d+/\d+/\d+',
    u'未来',
    u'最近',
    u'早上',
    u'日前',
    u'新世纪',
    u'小时',
    u'([0-3][0-9]|[1-9])[日号]',
    u'明天',
    u'上周',
    u'[零一二三四五六七八九十百千万\d]+年',
    u'[一二三四五六七八九十百千万几多]+[天日周月年][后前左右]*',
    u'每[年月日天小时分秒钟]+',
    u'(\d+分)+(\d+秒)?',
    u'[一二三四五六七八九十]+来?[岁年]',
    u'[新?|\d*]世纪末?',
    u'\d+时',
    u'世纪',
    u'[零一二三四五六七八九十百千万\d]+岁',
    u'[零一二三四五六七八九十百千万\d]+年',
    u'[本后昨当新后明今去前那这][一二三四五六七八九十]?[年月日天]',
    u'晚上',
    u'回归前后',
    u'晚间',
    u'(\d+点)+(\d+分)?(\d+秒)?(左右)?',
    u'\d+年代',
    u'本月\d+',
    u'第\d+天',
    u'\d+岁',
    u'\d+年\d+月',
    u'[去今明]?[年月][底末]',
    u'[零一二三四五六七八九十百千万\d]+世纪',
    u'昨天[上中下]+午',
    u'\d+年度',
    u'[零一二三四五六七八九十百千万\d]+星期',
    u'年底',
    u'[下本]+个?赛季',
    u'今年\d+月\d+日',
    u'\d+月\d+日[上中下]午\d+时',
    u'今年晚些时候',
    u'两个星期',
    u'过去[零一二三四五六七八九十百千万\d]+周',
    u'\d+号晚',
    u'[零一二三四五六七八九十百千万\d]+个?小时',
    u'凌晨',
    u'\d+年\d+月\d+日|\d+个月',
    u'今天早[晨上间]',
    u'第[一二三四五六七八九十\d+]+季',
    u'当地时间',
    u'早晨',
    u'一段时间',
    u'凌晨\d+点',
    u'去年\d+月\d+日',
    u'年关',
    u'如今',
    u'当晚|\d+日晚\d+时',
    u'每年\d+月\d+日',
    u'[零一二三四五六七八九十百千万\d]+周',
    u'\d+月',
    u'农历',
    u'两个小时',
    u'长久',
    u'清晨',
    u'\d+号晚',
    u'春节',
    u'星期日',
    u'圣诞',
    u'[零一二三四五六七八九十百千万\d]+段',
    u'现年',
    u'当日',
    u'[零一二三四五六七八九十百千万\d]+个?分钟',
    u'\d+[天日周月年][后前]?',
    u'\d+[年月天]',
    u'清早',
    u'两年',
    u'昨天[上中下]午[零一二三四五六七八九十百千万\d]+时',
    u'[零一二三四五六七八九十百千万\d]+年',
    u'圣诞节',
    u'学期',
    u'\d+来?分钟',
    u'过去[零一二三四五六七八九十百千万\d]+年',
    u'星期天',
    u'夜间',
    u'\d+日凌晨',
    u'[零一二三四五六七八九十百千万\d]+月底',
    u'当天',
    u'\d+日',
    u'[零一二三四五六七八九十百千万\d]+月',
    u'今年\d+月份',
    u'晚[上间]?[零一二三四五六七八九十百千万\d]+时([零一二三四五六七八九十百千万\d]+分钟?)?',
    u'连[年月日夜]',
    u'\d+年\d+月\d+日',
    u'[一二两三四五六七八九十百千万几多上\d+]+个?[天日周月年][后前半]?',
    u'早[上晨间]?[零一二三四五六七八九十百千万\d]+点',
    u'周末',
    u'([小学|初中?|高中?|大学?|研][一二三四五六七八九十]?\d*)?[上下]半?学期',
    u'[零一二三四五六七八九十百千万\d]+时期',
    u'午间',
    u'次年',
    u'这时候',
    u'农历新年',
    u'[春夏秋冬][天季]',
    u'\d+天',
    u'元宵节',
    u'[零一二三四五六七八九十百千万\d]+分钟?',
    u'傍晚',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)午\d+时\d+分',
    u'同日',
    u'\d+年\d+月底',
    u'\d+分钟',
    u'\d+世纪',
    u'冬季',
    u'国庆',
    u'年代',
    u'[零一二三四五六七八九十百千万\d]+年半',
    u'今年年底',
    u'新年',
    u'当地时间(星期|周)[零一二三四五六七日天末\d]+',
    u'半小时',
    u'[零一二三四五六七八九十百千万\d]+周年',
    u'[零一二三四五六七八九十百千万\d]+期间',
    u'今后',
    u'[零一二三四五六七八九十百千万\d]+段时间',
    u'明年',
    u'[12][09][0-9]{2}年度?',
    u'[零一二三四五六七八九十百千万\d]+生',
    u'今天凌晨',
    u'过去\d+年',
    u'元月',
    u'\d+月\d+日凌晨',
    u'[前去今明后新]+年',
    u'\d+月\d+',
    u'夏天',
    u'\d+日凌晨\d+时许',
    u'\d+月\d+日',
    u'\d+点半',
    u'去年底',
    u'最后一[天刻]',
    u'[零一二三四五六七八九十百千万\d]+个?月',
    u'圣诞节?',
    u'\d+(数|多|多少|好几|几|差不多|近|前|后|上|左右)年',
    u'当天(数|多|多少|好几|几|差不多|近|前|后|上|左右)午',
    u'每年的\d+月\d+日',
    u'\d+日晚(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'星期[零一二三四五六七八九十百千万\d]+晚',
    u'深夜',
    u'现如今',
    u'[上中下]+午',
    u'第[一二三四五六七八九十百千万几多\d]+个?[天日周月年]',
    u'昨晚',
    u'近年',
    u'今天清晨',
    u'中旬',
    u'星期[零一二三四五六七八九十百千万\d]+早',
    u'[零一二三四五六七八九十百千万\d]+战期间',
    u'星期',
    u'昨天?晚上?',
    u'较早时',
    u'个(数|多|多少|好几|几|差不多|近|前|后|上|左右)小时',
    u'元旦',
    u'[一二三四五六七八九十百千万\d]+个礼拜',
    u'昨日',
    u'[年月]初',
    u'\d+年的\d+月',
    u'每年',
    u'[一二三四五六七八九十百千万\d]+月份',
    u'今年\d+月\d+号',
    u'今年[一二三四五六七八九十百千万\d]+月',
    u'\d+月底',
    u'未来\d+年',
    u'第[零一二三四五六七八九十百千万\d]+季',
    u'\d?多年',
    u'[零一二三四五六七八九十百千万\d]+个星期',
    u'\d+年[零一二三四五六七八九十百千万\d]+月',
    u'[下上中]午',
    u'早(数|多|多少|好几|几|差不多|近|前|后|上|左右)\d+点',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)月',
    u'[零一二三四五六七八九十百千万\d]+个(数|多|多少|好几|几|差不多|近|前|后|上|左右)月',
    u'同[零一二三四五六七八九十百千万\d]+天',
    u'\d+号凌晨',
    u'夜里',
    u'两个(数|多|多少|好几|几|差不多|近|前|后|上|左右)小时',
    u'昨天',
    u'罗马时代',
    u'目(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'[零一二三四五六七八九十百千万\d]+月',
    u'\d+年\d+月\d+号',
    u'(10|11|12|[1-9])月份?',
    u'[12][0-9]世纪',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)[零一二三四五六七八九十百千万\d]+天',
    u'工作日',
    u'稍后',
    u'\d+号(数|多|多少|好几|几|差不多|近|前|后|上|左右)午',
    u'未来[零一二三四五六七八九十百千万\d]+年',
    u'[0-9]+[天日周月年][后前左右]*',
    u'[零一二三四五六七八九十百千万\d]+日(数|多|多少|好几|几|差不多|近|前|后|上|左右)午',
    u'最(数|多|多少|好几|几|差不多|近|前|后|上|左右)[零一二三四五六七八九十百千万\d]+刻',
    u'\d+(数|多|多少|好几|几|差不多|近|前|后|上|左右)岁',
    u'去年\d+月\d+号',
    u'两个月',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)午\d+时',
    u'两天',
    u'\d+个?(小时|星期)',
    u'\d+年半',
    u'较早',
    u'[零一二三四五六七八九十百千万\d]+个小时',
    u'[一二三四五六七八九十]+周年',
    u'星期[零一二三四五六七八九十百千万\d]+(数|多|多少|好几|几|差不多|近|前|后|上|左右)午',
    u'时刻',
    u'(\d+天)+(\d+点)?(\d+分)?(\d+秒)?',
    u'\d+日[零一二三四五六七八九十百千万\d]+时',
    u'\d+周年',
    u'[零一二三四五六七八九十百千万\d]+早',
    u'[零一二三四五六七八九十百千万\d]+日',
    u'去年\d+月',
    u'过去[零一二三四五六七八九十百千万\d]+年',
    u'\d+个星期',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)(数|多|多少|好几|几|差不多|近|前|后|上|左右)天',
    u'[当前昨今明后春夏秋冬]+天',
    u'去年\d+月份',
    u'今(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'\d+周',
    u'两星期',
    u'[零一二三四五六七八九十百千万\d]+年代',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)天',
    u'昔日',
    u'两个半月',
    u'(印尼|北京|美国)?当地时间',
    u'连日',
    u'本月\d+日',
    u'第[零一二三四五六七八九十百千万\d]+天',
    u'\d+点\d+分',
    u'[长近多]年',
    u'\d+日(数|多|多少|好几|几|差不多|近|前|后|上|左右)午\d+时',
    u'那时',
    u'[零一二三四五六七八九十百千万\d]+天',
    u'这个星期',
    u'去年',
    u'昨天傍晚',
    u'近期',
    u'星期[零一二三四五六七八九十百千万\d]+早些时候',
    u'\d+[零一二三四五六七八九十百千万\d]+年',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)两个月',
    u'\d+个小时',
    u'[零一二三四五六七八九十百千万\d]+个月',
    u'当年',
    u'本月',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)[零一二三四五六七八九十百千万\d]+个月',
    u'\d+点(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'目前',
    u'去年[零一二三四五六七八九十百千万\d]+月',
    u'\d+时\d+分',
    u'每月',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)段时间',
    u'\d+日晚',
    u'早(数|多|多少|好几|几|差不多|近|前|后|上|左右)\d+点(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'下旬',
    u'\d+月份',
    u'逐年',
    u'稍(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'\d+年',
    u'月底',
    u'这个月',
    u'\d+年\d+个月',
    u'\d+大寿',
    u'周[零一二三四五六七八九十百千万\d]+早(数|多|多少|好几|几|差不多|近|前|后|上|左右)',
    u'半年',
    u'今日',
    u'末日',
    u'昨天深夜',
    u'今年\d+月',
    u'\d+月\d+号',
    u'\d+日夜',
    u'(早些|某个|晚间|本星期早些|前些)+时候',
    u'同年',
    u'每个月',
    u'一早',
    u'\d+来?[岁年]',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)个月',
    u'[鼠牛虎兔龙蛇马羊猴鸡狗猪]年',
    u'季度',
    u'早些时候',
    u'今天',
    u'每天',
    u'年半',
    u'下个?月',
    u'午后',
    u'\d+日(数|多|多少|好几|几|差不多|近|前|后|上|左右)午',
    u'(数|多|多少|好几|几|差不多|近|前|后|上|左右)个星期',
    u'(今天(数|多|多少|好几|几|差不多|近|前|后|上|左右)午)',
    u'同[一二三四五六七八九十][年|月|天]',
    'T\d+:\d+:\d+',
    '\d+/\d+/\d+:\d+:\d+.\d+',
    '\?\?\?\?-\?\?-\?\?T\d+:\d+:\d+',
    '\d+-\d+-\d+T\d+:\d+:\d+',
    '\d+/\d+/\d+ \d+:\d+:\d+.\d+',
    '\d+-\d+-\d+|[0-9]{8}',
]

p = re.compile('|'.join(o), re.UNICODE)
