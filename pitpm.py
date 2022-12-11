from flask import Flask, request

app = Flask(__name__)

users = []
musics = []

class User(object):

    def __init__(self, name, email, password, group, position, amounttask, coefficient, salary):
        self.name = name
        self.email = email
        self.password = password
        self.group = group
        self.position = position
        self.amounttask= amounttask
        self.coefficient= coefficient
        self.salary = salary

class Music(object):

    def __init__(self, name, group, performers,album):
        self.name = name
        self.group = group
        self.performers = performers
        self.album = album

@app.route('/')
def routes():
    s = "http://192.168.1.143:3005/api/users - получить всех пользователей <br/> " \
        "http://192.168.1.143:3005/api/modifyUser/ - изменить данные пользователя <br/> " \
        "http://192.168.1.143:3005/api/musics - Получить всю музыку <br/> " \
        "http://192.168.1.143:3005/api/modifyMusic/ - изменить музыку <br/> "
    return s

@app.route('/api/users', methods=['GET','POST'])
def GETPOST_Users():
    if request.method == 'GET':
        s = ''
        for u in users:
            user = u.name + " " + u.email + " " + u.password + " " + u.group + " " + u.position
            s += user + "<br/>"

        return s, 200

    if request.method == 'POST':
        data = request.get_json()

        name = None
        email = None
        password = None
        group = None
        position = None
        amounttask= None
        coefficient= None
        salary = None

        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указоно имя', 400
            if 'email' in data:
                email = data['email']
            else:
                return 'Не указана почта', 400
            if 'password' in data:
                password = data['password']
            else:
                return 'Не указан пароль', 400
            if 'group' in data:
                group = data['group']
            else:
                return 'Не указана группа', 400
            if 'position' in data:
                position = data['position']
            else:
                return 'Не указана должность', 400
            if 'amounttask' in data:
                amounttask = data['amounttask']
            else:
                return 'Не указано количество заданий', 400
            if 'coefficient' in data:
                coefficient = data['coefficient']
            else:
                return 'Не указан коэффициент', 400
            if 'salary' in data:
                salary = data['salary']
            else:
                return 'Не указана заработная плата', 400
        else:
            return 'Нет данных', 400

        if name & email & password & group & position & amounttask & coefficient & salary:
            user = User(name, email, password, group, position, amounttask, coefficient, salary)
            users.append(user)
            return 'Пользователь добавлен', 200
    return '404'

@app.route('/api/musics', methods=['GET','POST'])
def GETPOST_Music():
    if request.method=='GET':
        s = ''
        for m in musics:
            music = m.name + " " + m.group + " " + m.performers + " " + m.album
            s += music + "<br/>"

        return s, 200
    
    if request.method == 'POST':
        data = request.get_json()

        name = None
        group = None
        performers = None
        album = None

        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Название трека не указано', 400
            if 'group' in data:
                group = data['group']
            else:
                return 'Группа не указана ', 400
            if 'performers' in data:
                performers = data['performers']
            else:
                return 'Исполнитель не указан ', 400
            if 'album' in data:
                album = data['album']
            else:
                return 'Группа не указана ', 400
        else:
            return 'Нет информации', 400

        if name & group & performers & album:
            music = Music(name, group, performers, album)
            musics.append(music)
            return 'Музыка добавлена', 200
    return '404'
    
@app.route('/api/modifyUser/<int:id>', methods=['PUT','DELETE'])
def ModifyUser(id):
    if request.method == 'PUT':
        if len(users) < id:
            return 'Пользователя с таким id нет', 400

        data = request.get_json()

        if data:
            if 'name' in data:
                users[id].name = data['name']
            if 'email' in data:
                users[id].email = data['email']
            if 'password' in data:
                users[id].password = data['password']
            if 'group' in data:
                users[id].group = data['group']
            if 'position' in data:
                users[id].position = data['position']
            if 'amounttask' in data:
                users[id].amounttask = data['amounttask']
            if 'coefficient' in data:
                users[id].coefficient = data['coefficient']
            if 'salary' in data:
                users[id].salary = data['salary']
        else:
            return 'Данные не введены', 400
        return 'Пользователь изменен', 200
    if request.method == 'DELETE':
        if len(users) < id:
                return 'Пользователя с таким id нет', 400
        users.pop(id)
        return 'Пользователь удален', 200

@app.route('/api/modifyMusic/<int:id>', methods=['PUT','DELETE'])
def ModifyMusic(id):
    if request.method=='PUT':
        if len(musics) < id:
            return 'Музыки с таким id нет', 400

        data = request.get_json()

        if data:
            if 'name' in data:
                musics[id].name = data['name']
            if 'group' in data:
                musics[id].group = data['group']
            if 'performers' in data:
                musics[id].performers = data['performers']
            if 'album' in data:
                musics[id].album = data['album']
        else:
            return 'Пустые данные', 400
        return 'Музыка изменена', 200

    if request.method=='DELETE':
        if len(musics) < id:
                return 'Музыки с таким id нет', 400

        musics.pop(id)
        return 'Музыка удалена', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3005')