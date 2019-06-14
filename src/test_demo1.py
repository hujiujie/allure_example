# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 10:16
# @Author  : hjj
# @Site    : 
# @File    : test_demo1.py

import logging
import allure
import random
import time
import pytest
#from utils import capturepic
import shutil

@allure.feature('测试登录功能')
#@allure.feature('testloginfunction')
class TestLogin:
    @allure.story('测试成功的登录场景')
    @allure.severity('blocker')
    @allure.testcase("http://www.testlink.com/id=2474608")
    @allure.issue("http://www.jira.com/id=2474608")
    def test_2474608(self):

        with allure.step("通过电话密码的方式登录雪球"):
            logging.info('输入电话、密码')
            time.sleep(random.randint(2,4))

        with allure.step("点击用户icon，以便检查登录是否成功"):
            time.sleep(random.randint(2, 4))

        with allure.step("检查登录是否成功"):
            logging.debug('获取登录名字')
            time.sleep(random.randint(2, 4))
            user_name_text= '杠基'
        assert user_name_text=="杠基"

    @allure.severity('normal')
    @allure.story('测试失败的登录场景')
    @allure.testcase("http://www.testlink.com/id=2474609")
    def test_2474609(self):
        with allure.step("通过电话密码的方式登录雪球"):
            logging.info('输入错误的电话、密码')
            time.sleep(random.randint(2, 4))

        with allure.step("点击用户icon，以便检查登录是否成功"):
            time.sleep(random.randint(2, 4))

        with allure.step("检查登录是否成功"):
            logging.debug('获取登录名字')
            time.sleep(random.randint(2, 4))
            name = str(int(str(int(time.time()))))
            #capturepic.capture_screen(name)
            #file = open(name + '.jpg', 'rb').read()
            #allure.attach(name, file, allure.attach_type.PNG)
            #shutil.rmtree(name + '.jpg')
            user_name_text = ''

        assert user_name_text == ""

    @pytest.mark.parametrize('username', ['tom', 'jim'])
    @pytest.mark.parametrize('password', ['tom123', '123im'])
    def test_with_two_username_passwords(self,username, password):
        logging.info('param1:'+str(username)+',param2'+str(password))


