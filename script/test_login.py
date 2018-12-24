import allure


class TestLogin:
    def test_a(self):
        print("\n111")
        assert 1
    @allure.step("测试登陆的步骤")
    def test_b(self):
        print("\n2222")
        allure.attach('描述1','请输入用户名')
        print("\n3333")
        allure.attach('描述','请输入密码')
        assert 0