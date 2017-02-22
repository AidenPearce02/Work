import datetime
from cmd import Cmd

import requests
import xlwt

'''Find date of last commit'''
def lastcommit(json, username):
    listd = []
    for i in range(len(json)):
        c = requests.get('https://api.github.com/repos/' + username + '/' + json[i].get('name') + '/commits')
        if c.status_code == 200:
            dates = []
            for commit in range(len(c.json())):
                date = c.json()[commit].get('commit').get('author').get('date')
                dates.append(date)
            sdate = dates[0]
            for d in dates:
                if d > sdate:
                    sdate = d
            listd.append(sdate)
    mdate = listd[0]
    for d in listd:
        if d > mdate:
            mdate = d
    return mdate

'''Find the most popular program language in repo'''
def mostlanguage(json):
    dictionaryl = {}
    for i in range(len(json)):
        if json[i].get('language') in dictionaryl.keys():
            if str(json[i].get('language')) == 'None':
                dictionaryl[json[i].get('language')] = 0
            else:
                dictionaryl[json[i].get('language')] += 1
        else:
            if str(json[i].get('language')) == 'None':
                dictionaryl[json[i].get('language')] = 0
            else:
                dictionaryl[json[i].get('language')] = 1
    mname = dictionaryl.get(0)
    for k in dictionaryl.keys():
        if dictionaryl[k] > dictionaryl[mname]:
            mname = k
    return mname


'''Size of all repo'''
def size(json, username):
    sizem = 0
    for i in range(len(json)):
        c = requests.get('https://api.github.com/repos/' + username + '/' + json[i].get('name'))
        if c.status_code == 200:
            sizem += float(c.json().get('size')) / 1024
    return sizem

'''Count of followers'''
def followers(username):
    followersl = []
    r = requests.get('https://api.github.com/' + username + '/followers')
    if r.status_code == 200:
        for i in range(len(r.json())):
            followersl.append(r.json()[i].get('login'))
    else:
        followersl.append('Null')
    return followersl

'''Information about repo'''
def info(jsonr, jsonb, jsonc, reponame):
    for i in range(len(jsonr)):
        if jsonr[i].get('name') == reponame:
            print("Input reponame is right")
            print("Name: " + jsonr[i].get('name'))
            print("Full name: " + jsonr[i].get('full_name'))
            print("Language: " + str(jsonr[i].get('language')))
            print("Count commits: " + str(len(jsonc)))
            print("Count branches: " + str(len(jsonb)))
            print("Forks count: " + str(jsonr[i].get('forks_count')))
            print("Open issues count: " + str(jsonr[i].get('open_issues_count')))


class MyCmd(Cmd):

    def do_exit(*args, **kwargs):
        exit()

    '''Information about rate'''
    def do_rate(*args, **kwargs):
        r = requests.get("https://api.github.com/users/whatever")
        print("Limit: " + str(r.headers.get('X-RateLimit-Limit')))
        print("Remain: " + str(r.headers.get('X-RateLimit-Remaining')))
        print("Reset time: " + str(
            datetime.datetime.fromtimestamp(int(r.headers.get('X-RateLimit-Reset'))).strftime('%Y-%m-%d %H:%M:%S')))

    '''List of all user's repo'''
    def do_ls(*args, **kwargs):
        username = input("Input username: ")
        r = requests.get('https://api.github.com/users/' + username + '/repos')
        if r.status_code == 200:
            print("Input username is right")
            json = r.json()
            print("Your repositories:")
            for i in range(len(json)):
                print(str(i + 1) + ": " + json[i].get('name'))
        else:
            print("Input username is wrong")

    '''Create new repo'''
    def do_create(*args, **kwargs):
        username = input("Input username: ")
        password = input("Input password: ")
        name = input("Input name:")
        data = '{"name":"' + name + '"}'
        r = requests.post('https://api.github.com/user/repos', data=data, auth=(username, password))
        if r.status_code == 201:
            print("Repo created")
        else:
            print("Repo not created")

    '''Information about repo'''
    def do_repinfo(*args, **kwargs):
        username = input("Input username: ")
        reponame = input("Input reponame: ")
        r = requests.get('https://api.github.com/users/' + username + '/repos')
        c = requests.get('https://api.github.com/repos/' + username + '/' + reponame + '/commits')
        b = requests.get('https://api.github.com/repos/' + username + '/' + reponame + '/branches')
        if r.status_code == 200 and c.status_code==200:
            print("Input username is right")
            jsonr = r.json()
            jsonc = c.json()
            jsonb = b.json()
            print("Info about repo:")
            info(jsonr, jsonb, jsonc, reponame)
        else:
            print("Input username and reponame are wrong")

    '''Export data to csv or xml'''
    def do_export(*args, **kwargs):
        username = input("Input username: ")
        expansion = input("Input expansion: ")
        filename = "Statistics"
        r = requests.get('https://api.github.com/users/' + username + '/repos')
        if r.status_code == 200:
            mlang = mostlanguage(r.json())
            mdate = lastcommit(r.json(), username)
            msize = size(r.json(), username)
            followerl = followers(username)
            data = [username, len(r.json()), mlang, mdate, msize, followerl]
            desc = ['Username', 'Count of repositories', 'Main language', 'Date of last commit',
                    'The total size of all repositories(MB)', 'List of followers']
            if expansion == "csv":
                mainl=[desc,data]
                out = open(filename+".csv",'w')
                for row in mainl:
                    for column in row:
                        out.write('%s;' % column)
                    out.write('\n')
                out.close()
            elif expansion == "xls":
                book = xlwt.Workbook()
                sh = book.add_sheet("Info")
                for n, (v_desc, v) in enumerate(zip(desc, data)):
                    sh.write(0, n, v_desc)
                    sh.write(1, n, v)
                book.save(filename + ".xls")


c1 = MyCmd()
c1.cmdloop()
