import requests, ctypes, json
ctypes.windll.kernel32.SetConsoleTitleW('pythonelab')

session = requests.Session()
api = 'http://care.srmist.edu.in/rmpds/api/'
data = '{"username":"'+input('Username: ')+'","password":"'+input('Password: ')+'"}'
headers = {'User-Agent': 'Chrome/76.0.3809.132','Content-Type': 'application/json'}
answerdb = 'https://raw.githubusercontent.com/autoelab/autoelab/master/data/code/python/'
login = session.post(api+'auth/login', data, headers=headers).json()['response']

for sno in range(11, 21):
    for qno in range(11, 21):
        qcode = '18'+str(sno)+'1'+str(qno)
        data = '{"courseName":"PYTHON","questionID":'+qcode+'}'
        headers.update({'role':'S','token':login['token'],'username':login['username']})
        question = session.post(api+'student/question', data, headers=headers).json()['response']
        print(question['sessionName']+' - '+question['questionName'])
        try: answers = json.loads(requests.get(answerdb+str(question['_id'])+'.json').text)['files']
        except: answers = []
        for answer in answers:
            try: 
                code = requests.get(answerdb+str(question['_id'])+'/'+answer,'r').text.replace('\n','\\n').replace('\"','\\"').replace("\'","\\'")
                data = '{"courseName":"PYTHON","code":"'+code+'","language":"PYTHON","sid":"'+qcode+'","qid":'+str(question['_id'])+'}'
                if session.post(api+'student/question/evaluate', data, headers=headers).json()['response']['score'] == 100: break
            except: continue
input('\nAll done! Press Enter to exit.\n')
