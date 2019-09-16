import requests, base64, ctypes, json, os 
ctypes.windll.kernel32.SetConsoleTitleW('pythonelab')
if not os.path.isdir('Reports'): os.mkdir('Reports')

session = requests.Session()
api = 'http://care.srmuniv.ac.in/rmpds/api/'
data = '{"username":"'+input('Username: ')+'","password":"'+input('Password: ')+'"}'
headers = {'User-Agent': 'Chrome/76.0.3809.132','Content-Type': 'application/json'}
answerdb = 'https://raw.githubusercontent.com/autoelab/autoelab/master/data/code/python/'
login = session.post(api+'auth/login', data, headers=headers).json()['response']

counter = 0
for sno in range(11, 21):
    for qno in range(11, 21):
        counter += 1
        solved = False
        qcode = '18'+str(sno)+'1'+str(qno)
        data = '{"courseName":"PYTHON","questionID":'+qcode+'}'
        headers.update({'role':'S','token':login['token'],'username':login['username']})
        question = session.post(api+'student/question', data, headers=headers).json()['response']
        print(str(counter).rjust(2,'0')+' - '+question['sessionName']+' - '+question['questionName'], end=' - ')
        try: answers = json.loads(requests.get(answerdb+str(question['_id'])+'.json').text)['files']
        except: answers = []
        for answer in answers:
            code = requests.get(answerdb+str(question['_id'])+'/'+answer,'r').text.replace('\n','\\n').replace('\"','\\"').replace("\'","\\'")
            data = '{"courseName":"PYTHON","code":"'+code+'","language":"PYTHON","sid":"'+qcode+'","qid":'+str(question['_id'])+'}'
            try:
                if session.post(api+'student/question/evaluate', data, headers=headers).json()['response']['score'] == 100: 
                    report = session.post(api+'shared/wkhtml', data, headers=headers).json()['response']
                    open('Reports\\'+str(counter).rjust(2,'0')+'.jpg', 'wb').write(base64.b64decode(report))
                    print('Solved')
                    solved = True
                    break
            except: continue
        if not solved: print('Failed')
input('\nAll done! Press Enter to exit.\n')