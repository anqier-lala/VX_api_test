import requests
import random

def get_token_id():
    get_param_data={
        'grant_type': 'client_credential',
        'appid': 'wxc036fc4ba09c7c16',
        'secret': 'bc85b7bc56a9c6bb2d7011f758ab9d7e'
    }
    response=requests.get( url='https://api.weixin.qq.com/cgi-bin/token',
                           params=get_param_data
                           )
    return response.json()['access_token']


def setup_case(name):
    print('测试用例[%s]开始执行~'% name)

def teardown_case(name):
    print('测试用例[%s]执行结束~'%name)

def setup_step(name):
    print('测试步骤[%s]开始执行~'%name )

def teardown_step(name):
    print("测试步骤 [%s]执行结束" %name)

def tag_name():
    i=1
    list1=[]
    for i in range(11):
        name='test_'+str(i)
        list1.append(name)
    return list1

#参数化实现_随机整数,参数化需要传入一个列表，所以这里做一个列表后进行操作,通过参数个数确定要执行的个数，如下写法说明列表执行3次，也可以重新传入次数
def get_randomints(min,max,count=3):
    randomint_list = []
    for i in range(count):
        randomint_list.append(random.randint(min,max))
    return randomint_list

##实现随机手机号
def get_tel_number(count=3):
    phonelist=[]
    for i in range(count):
        start_phone=random.choice(["130","131","132","133","155","186"])
        end_phone=''.join(random.sample('0123456789',8))
        phonelist.append((start_phone+end_phone).encode("utf-8").decode("iso8859-1"))
    return phonelist

#身份证号10个
def get_identity_id(count=10):
    identity_id=[]
    for i in range(count):
        start_identity_id = random.choice(["4304261994", "4108231989", "4304261995", "4304261996", "4304261993", "4304261992"])
        end_identity_id=''.join(random.sample('0123456789',8))
        identity_id.append(start_identity_id + end_identity_id)
    return identity_id



if __name__ == '__main__':
    # print(get_token_id())
    print(get_tel_number())
    print(get_identity_id())
    # print(tag_name())
    # print(random.randint(1,10))




