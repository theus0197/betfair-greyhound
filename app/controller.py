from django.contrib.auth import authenticate, login as loginProcess, logout
from django.conf import settings
import json
import os
import datetime
import ftplib
import requests
from . import models


'''
    ---------------------------------- Functions Configurations ----------------------------------
'''
def remove_data():
    models.Races.objects.all().delete()
    models.collectHistoryDay.objects.all().delete()
    models.racesDay.objects.all().delete()

if settings.DEBUG:
    host = '127.0.0.1:8000'
    url = 'http://{}/media/json'.format(host)
else:
    host = ''
    url = 'http://{}/BotMilionario'.format(host)

def ftp(file, name):
    if settings.DEBUG is False:
        server = ftplib.FTP()
        server.connect('31.170.160.95', 21)

        server.login('u403612333', 'Hz;gMM&0')
        #server.dir()

        #save file in path Frogti in server
        server.cwd('/domains/engenbot.com/public_html/VictoryTips')
        server.storbinary('STOR {}.json'.format(name), file)
        file.close()

def load_json(data):
    try:
        data = json.loads(data)
    except:
        try:
            data = json.load(data)
        except:
            data = data

    return data

def method_not_allowed():
    return {
        'status': False,
        'message': 'Método não autorizado!',
        'containers': {}
    }

def get_date(formated="%Y-%m-%d"):
    now_date = datetime.datetime.now()
    format_date = now_date.strftime(formated)
    return format_date

def get_time(formated="%H:%M"):
    now_time = datetime.datetime.now()
    format_time = now_time.strftime(formated)
    return format_time

'''
    ---------------------------------- Functions website view client ----------------------------------
'''
def signin(data, request):
    data = load_json(data)
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        loginProcess(request, user)
        status = True
        message = 'Login realizado com sucesso!'
    else:
        status = False
        message = 'Autenticação inválida!'

    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def signout(request):
    logout(request)
    return {
        'status': True,
        'message': 'Logout realizado com sucesso!',
        'containers': {}
    }

def get_clients():
    clients = models.Clients.objects.all()
    status = True
    message = 'Clientes carregados com sucesso!'
    containers = {
        'clients': clients
    }

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def add_new_client(data):
    data = load_json(data)
    id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name = data['name']
    cpf = data['cpf'].replace(' ', '')
    email = data['email']
    roleta = True if data['roleta'] == 'true' else False
    dados = True if data['dados'] == 'true' else False
    football = True if data['football'] == 'true' else False

    if name != '':
        if cpf != '':
            if models.Clients.objects.filter(cpf=cpf).exists():
                status = False
                message = 'Esse usuário já está cadastrado!'
            else:
                new_client = models.Clients(
                    id=id,
                    name=name,
                    cpf=cpf,
                    email=email,
                    roleta=roleta,
                    dados=dados,
                    football=football
                )
                new_client.save()
                status = True
                message = 'Grupo adicionado com sucesso!'
        else:
            status = False
            message = 'CPF do client não pode estar vazio!'
    else:
        status = False
        message = 'Nome do cliente não pode estar vazio!'
            

    return{
        'status': status,
        'message': message,
        'containers': {}
    }
    
def view_client(data):
    data = load_json(data)
    id_ = data['id']
    if models.Clients.objects.filter(id=id_).exists():
        status = True
        message = 'Usuário encontrado com sucesso!'
        user = models.Clients.objects.get(id=id_)
        containers = {
            'client': {
                'id': user.id,
                'name': user.name,
                'cpf': user.cpf,
                'email': user.email,
                'roleta': 'true' if user.roleta is True else 'false',
                'dados': 'true' if user.dados is True else 'false',
                'football': 'true' if user.football is True else 'false'
            }
        }
    else:
        status = False
        message = 'Esse não está cadastrado'
        containers = {}
        

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def update_client(data):
    data = load_json(data)
    id_ = data['id']
    name = data['name']
    cpf = data['cpf']
    email = data['email']
    roleta = True if data['roleta'] == 'true' else False
    dados = True if data['dados'] == 'true' else False
    football = True if data['football'] == 'true' else False
    if models.Clients.objects.filter(id=id_).exists():
        status = True
        message = 'Usuário encontrado com sucesso!'
        user = models.Clients.objects.get(id=id_)
        user.name = name
        user.cpf = cpf
        user.email = email
        user.roleta = roleta
        user.dados = dados
        user.football = football
        user.save()
    else:
        status = False
        message = 'Usuário não encontrado'


    return{
        'status': status,
        'message': message,
        'containers': {}
    }

def delete_client(data):
    data = load_json(data)
    id_ = data['id']

    if models.Clients.objects.filter(id=id_).exists():
        user = models.Clients.objects.get(id=id_)
        user.delete()
        status = True
        message = 'Usuário removido com sucesso!'
    else:
        status = False
        message = 'Usuário não encontrado'
    
    return{
        'status': status,
        'message': message,
        'containers': {}
    }

def api_get_clients(data):
    data = load_json(data)
    cpf = data['cpf']
    if cpf != '':
        if models.Clients.objects.filter(cpf=cpf).exists():
            user = models.Clients.objects.get(cpf=cpf)
            status = True
            message = 'Olá {}, seu acesso foi liberado ;)'
            containers = {
                'name': user.name,
                'email': user.email,
                'dados': user.dados,
                'roleta': user.roleta,
                'football': user.football
            }
        else:
            status = False
            message = 'Infelizmente seu acesso ainda não está liberado, contate o suporte!'
            containers = {}
    else:
        status = False
        message = 'Preencha o campo CPF para verificar se você possui acesso!'
        containers = {} 
    
    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def authorized_app(data):
    data = load_json(data)
    cpf = data['cpf']
    game = data['game']
    if cpf != '':
        if models.Clients.objects.filter(cpf=cpf).exists():
            user = models.Clients.objects.get(cpf=cpf)
            if game == 'roleta':
                status_game = True if user.roleta else False
            elif game == 'dados':
                status_game = True if user.dados else False
            elif game == 'dice':
                status_game = True if user.dice else False
            else:
                status_game = False
            status = True
            message = 'Condição do game foi coletada com sucesso!'
            containers = {
                'status_game': status_game
            }
        else:
            status = False
            message = 'Infelizmente seu acesso ainda não está liberado, contate o suporte!'
            containers = {}
    else:
        status = False
        message = 'Preencha o campo CPF para verificar se você possui acesso!'
        containers = {} 

    return {
        'status': status,
        'message': message,
        'containers': containers
    }


'''
    ---------------------------------- Functions API greyhounds and races ----------------------------------
'''
# Functions to manage greyhound
def is_greyhound_already_registered(data):
    data = load_json(data)
    if data['id'] != '' and data['id'] != None:
        _id = int(data['id'])
        greyhounds = models.Greyhound.objects.filter(id=_id)
        if greyhounds.exists():
            greyhound = greyhounds[0]
            status = True
            message = 'Greyhound successfully found'
            containers = {
                'its-possible-register': False,
                'id': _id,
                'name': greyhound.name,
                'type-greyhound': greyhound.type_greyhound,
                'gender': greyhound.gender,
                'color': greyhound.color,
                'birth_date': greyhound.birth_date
            }
        else:
            status = False
            message = 'This greyhound is not in our database'
            containers = {
                'its-possible-register': True,
            }
    else:
        status = False
        message = 'Error in the Galgo query, inform at least the ID'
        containers = {
            'its-possible-register': False,
            'why': 'You need to pass greyhound ID'
        }

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def filters_greyhounds(data):
    data = load_json(data)
    try:
        if data['criteria'] == '*':
            greyhounds = models.Greyhound.objects.all()
        elif data['criteria'] is not None:
            greyhounds = models.Greyhound.objects.filter(**{data['model']: data['criteria']})
        else:
            return {
                'status': False,
                'message': 'Invalid criteria provided',
                'containers': {}
            }
        
        results = []
        if len(greyhounds) >0:
            for greyhound in greyhounds:
                results.append({
                    'id': greyhound.id,
                    'name': greyhound.name,
                    'type-greyhound': greyhound.type_greyhound,
                    'gender': greyhound.gender,
                    'color': greyhound.color,
                    'birth_date': greyhound.birth_date
                })

            status = True
            message = 'Greyhounds retrieved successfully'
            containers = {'greyhounds': results}
        else:
            status = False
            message = 'Greyhounds not finded'
            containers = {'greyhounds': results}
    except Exception as e:
        status = False
        message = f'Error retrieving greyhounds: {str(e)}'
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def create_new_greyhound(data):
    data = load_json(data)
    is_permited_create = is_greyhound_already_registered(data)
    if is_permited_create['status'] is False and is_permited_create['containers']['its-possible-register'] is True:
        try:
            new_greyhound = models.Greyhound.objects.create(
                id=int(data['id']),
                name=data['name'],
                type_greyhound=data['type_greyhound'],
                gender=data['gender'],
                gender_abbreviation=data['gender-abbreviation'],
                color=data['color'],
                color_abbreviation=data['color-abbreviation'],
                birth_date=data['birth_date'],
                birth_year=data['birth-year'],
                birth_month=data['birth-month'],
                birth_day=data['birth-day'],
                dam_name=data['dam-name'],
                sire_name=data['sire-name']
            )
            status = True
            message = 'Greyhound created successfully'
            containers = {
                'id': new_greyhound.id,
                'name': new_greyhound.name,
                'type-greyhound': new_greyhound.type_greyhound,
                'gender': new_greyhound.gender,
                'color': new_greyhound.color,
                'birth_date': new_greyhound.birth_date
            }
        except Exception as e:
            status = False
            message = f'Error creating greyhound: {str(e)}'
            containers = {}
    else:
        status = is_permited_create['status']
        message = is_permited_create['message']
        containers = is_permited_create['containers']

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

# Functions to manage Race
def create_race(data):
    data = load_json(data)
    greyhound_id = data['greyhound_id']
    greyhound = is_greyhound_already_registered({'id': greyhound_id})
    if greyhound['status']:
        race_greyhound = '{}-{}'.format(data['race_id'], greyhound_id)
        response_races = filter_races({
            'models': 'race_greyhound',
            'criteria': race_greyhound
        })
        
        if response_races['status'] is False:
            race = models.Races.objects.create(
            race_id = data['race_id'],
            race_greyhound=race_greyhound,
            id_greyhound=greyhound_id,
            greyhound=models.Greyhound.objects.get(id=greyhound_id),
            avaible=data['avaible'],
            avaible_calculate=data['avaible_calculate'],
            race_date=data['race_date'],
            uk_time=data['uk_time'],
            br_time=data['br_time'],
            track=data['track'],
            track_name=data['track_name'],
            category=data['category'],
            subcategory=data['subcategory'],
            distance=data['distance'],
            weight=data['weight'],
            trap=data['trap'],
            post_pick_racing_post=data['post_pick_racing_post'],
            rpr=data['rpr'],
            timeform_prediction=data['timeform_prediction'],
            timeform_stars=data['timeform_stars'],
            result=data['result'],
            course=data['course'],
            observations=data['observations'],
            odd_back=data['odd_back'],
            odd_lay=data['odd_lay'],
            num_greyhounds=data['num_greyhounds'],
            start=data['start'],
            final_time=data['final_time'],
            brt=data['brt'],
            recovery=data['recovery'] if 'recovery' in data else ''
        )
            race.save()
            status =  True
            message = 'Race created successfully'
            containers = {
                'race_id':data['race_id']
            }
        else:
            status = False
            message = 'Está corrida já foi criada anteriormente'
            containers = {}
    else:
        status = greyhound['status']
        message = greyhound['message']
        containers = greyhound['containers']
    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def filter_races(data):
    data = load_json(data)
    try:
        ascending = True
        if data['criteria'] == '*':
            races = models.Races.objects.all().order_by(f'{"" if ascending else "-"}race_date')
        elif data['model'] == 'greyhound':
            greyhound = models.Greyhound.objects.get(id=data['criteria'])
            races = models.Races.objects.filter(greyhound=greyhound).order_by(f'{"" if ascending else "-"}race_date')
        elif data['criteria'] is not None:
            races = models.Races.objects.filter(**{data['model']: data['criteria']}).order_by(f'{"" if ascending else "-"}race_date')
        else:
            return {
                'status': False,
                'message': 'Criterio inválido',
                'containers': {}
            }

        results = []
        for race in races:
            results.append({
                'id': race.id,
                'race_id': race.race_id,
                'race_greyhound': race.race_greyhound,
                'greyhound_id': race.greyhound.id,
                'avaible': race.avaible,
                'avaible_calculate': race.avaible_calculate,
                'race_date': race.race_date,
                'uk_time': race.uk_time,
                'br_time': race.br_time,
                'track': race.track,
                'track_name': race.track_name,
                'category': race.category,
                'subcategory': race.subcategory,
                'distance': race.distance,
                'trap': race.trap,
                'post_pick_racing_post': race.post_pick_racing_post,
                'rpr': race.rpr,
                'timeform_prediction': race.timeform_prediction,
                'timeform_stars': race.timeform_stars,
                'result': race.result,
                'course': race.course,
                'observations': race.observations,
                'odd_back': race.odd_back,
                'odd_lay': race.odd_lay,
                'num_greyhounds': race.num_greyhounds,
                'start': race.start,
                'final_time': race.final_time,
                'brt': race.brt,
            })

        if len(results) > 0:
            status = True
            message = 'As corridas foram encontrada com sucesso!'
            containers = {'races': results}
        else:
            status = False
            message = 'Nenhuma corrida encontra com esse critério: {}'.format(data['criteria'])
            containers = {}
    except Exception as e:
        status = False
        message = f'Error retrieving races: {str(e)}'
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def update_result_race(data):
    data = load_json(data)
    race = models.Races.objects.filter(**{data['model']: data['criteria']})[0]
    race.avaible = data['avaible']
    race.avaible_calculate = data['avaibleResult']
    race.result = data['result'] if data['result'] != 'passed' else race.result
    race.course = data['course']
    race.observations = data['observation'] if data['observation'] != 'passed' else race.observations
    race.trap = data['trap'] if data['trap'] != 'passed' else race.trap
    race.start = data['start'] if data['start'] != 'passed' else race.start
    race.final_time = data['final'] if data['final'] != 'passed' else race.final_time
    race.num_greyhounds = data['numGreyhounds']
    race.recovery = data['recovery']
    race.save()

    status = True
    message = 'As corridas foram atualizadas corretamente!'
    containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def remove_race(data):
    data = load_json(data)
    races = models.Races.objects.filter(**{data['model']: data['criteria']})
    for race in races:
        race.delete()
    status = True
    message = 'A corrida do dia com id {} foi removidas com sucesso!'.format(data['criteria'])
    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def calculate_races(data):
    data = load_json(data)
    races = models.Races.objects.filter(race_greyhound=data['race_greyhound'])
    if races.exists():
        race = races[0]
        race.avaible_calculate = True
        race.avg_position = data['avg_position']
        race.best_time = data['best_time']
        race.last_time = data['last_time']
        race.avg_time = data['avg_time']
        race.best_start = data['best_start']
        race.last_start = data['last_start']
        race.avg_start = data['avg_start']
        race.best_recovery = data['best_recovery']
        race.last_recovery = data['last_recovery']
        race.avg_recovery = data['avg_recovery']
        race.overall_brt = data['ranking_brt']
        race.overall_avg_position = data['ranking_avg_position']
        race.overall_best_time = data['ranking_best_time']
        race.overall_last_time = data['ranking_last_time']
        race.overall_avg_time = data['ranking_avg_time']
        race.overall_best_start = data['ranking_best_start']
        race.overall_last_start = data['ranking_last_start']
        race.overall_avg_start = data['ranking_avg_start']
        race.overall_best_recovery = data['ranking_best_recovery']
        race.overall_last_recovery = data['ranking_last_recovery']
        race.overall_avg_recovery = data['ranking_avg_recovery']
        race.overall = data['overall']
        race.gb_favorite = data['gb_favorite']

        race.save()

        status = True
        message = 'Calculos salvos com sucesso!'
    else:
        status = False
        message = 'Corrida não pode ser encontrada com esse ID'

    return{
        'sttus': status,
        'message': message,
        'containers': {}
    }

def save_odds(data):
    data = load_json(data)
    races = models.Races.objects.filter(race_greyhound=data['race_greyhound'])
    if races.exists():
        race = races[0]
        race.odd_back = data['odd_back']
        race.odd_lay = data['odd_lay']
        race.save()

        status = True
        message = 'ODDS salva com sucesso!'
    else:
        status = False
        message = 'Corrida não pode ser encontrada com esse ID'

    return{
        'sttus': status,
        'message': message,
        'containers': {}
    }

def filter_races_day(data):
    data = load_json(data)
    if 'contains' not in data:
        data['contains'] = False

    if data['criteria'] == '*':
        races = models.racesDay.objects.all().order_by(data['model'])
    elif data['criteria'] is not None:
        if data['contains']:
            races = models.racesDay.objects.filter(**{data['model'] + '__contains': data['criteria']}).order_by(data['model'])
        else:
            races = models.racesDay.objects.filter(**{data['model']: data['criteria']}).order_by(data['model'])
    else:
        return {
            'status': False,
            'message': 'Invalid criteria provided',
            'containers': {}
        }

    results = []
    for race in races:
        results.append({
            'race_id': race.race_id,
            'race_tittle': race.race_title,
            'track_id': race.track_id,
            'main_title': race.main_title,
            'race_date': race.race_date
        })

    if len(results) > 0:
        status = True
        message = 'As corridas do dia foram encontrada com sucesso!'
        containers = {'races': results}
    else:
        status = False
        message = 'Nenhuma corrida encontra com esse critério: {}'.format(data['criteria'])
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def create_races_day(data):
    data = load_json(data)
    log_batch = {}
    if data['its-batch']:
        for batch in data['batchs']:
            response = filter_races_day({
                'model': 'race_id',
                'criteria': batch['raceId']
            })
            response_race = filter_races({'race_id': batch['raceId']})
            if response['status'] is False and response_race['status'] is False:
                race_day = models.racesDay.objects.create(
                    race_id = batch['raceId'],
                    race_title = batch['raceTitle'],
                    track_id = batch['trackId'],
                    track_name = batch['trackName'],
                    main_title = data['title'],
                    race_date = batch['raceDate']
                )
                race_day.save()
                log_batch[batch['raceId']] = True
            else:
                log_batch[batch['raceId']] = False
    else:
        race_day = models.racesDay.objects.create(
            race_id = batch['raceId'],
            race_title = batch['raceTitle'],
            track_id = batch['trackId'],
            track_name = batch['trackName'],
            main_title = data['title'],
            race_date = batch['raceDate']
        )
        race_day.save()
        log_batch[batch['raceId']] = True

    return{
        'status': True,
        'message': 'Dados da carridas diárias foram salvas com sucesso!',
        'containers': {
            'log_batch': log_batch
        }
    }

def remove_races_day(data):
    data = load_json(data)
    status = False
    message = 'Nenhuma corrida do dia encontrada com o critério fornecido'
    if data['criteria'] == '*':
        models.racesDay.objects.all().delete()
        status = True
        message = 'Todas as corridas do dia foram removidas com sucesso!'
    elif data['criteria'] is not None:
        races_day = filter_races_day(data)
        if races_day['status']:
            if len(races_day['containers']['races']) > 0:
                status = True
                message = 'A corrida do dia com id {} foi removidas com sucesso!'.format(data['criteria'])
                for race in races_day['containers']['races']:
                    race_obj = models.racesDay.objects.get(race_id=race['race_id'])
                    race_obj.delete() 
    else:
        status = False
        message = 'Critério inválido fornecido'
    return {
        'status': status,
        'message': message,
        'containers': {}
    }


def new_info_history(data):
    data = load_json(data)
    response_history = filter_info_history({
        'model': 'fake_id',
        'criteria': str(data['fake_id'])
    })
    print(response_history, data)
    if response_history['status'] is False:
        try:
            item = models.collectHistoryDay.objects.create(
                id=data['fake_id'],
                fake_id=data['fake_id'],
                greyhound=models.Greyhound.objects.get(id=data['fake_id']),
                last_refresh=data['last_refresh'],
                len_history=data['len_history']
            )
            item.save()
            status =  True
            message = 'Historico foi criado com sucesso!'
            containers = {
                'history_id': item.id
            }
        except:
            status = False
            message = ''
            containers = {}
    else:
        item = models.collectHistoryDay.objects.get(id=data['fake_id'])
        item.last_refresh = data['last_refresh']
        item.len_history = data['len_history']
        status = False 
        message = 'Historico já foi criado anteriormente!'
        containers = {}
    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def filter_info_history(data):
    data = load_json(data)
    try:
        ascending = True
        if data['criteria'] == '*':
            items = models.collectHistoryDay.objects.all().order_by(f'{"" if ascending else "-"}last_refresh')
        elif data['criteria'] is not None:
            items = models.collectHistoryDay.objects.filter(**{data['model']: data['criteria']}).order_by(f'{"" if ascending else "-"}last_refresh')
        else:
            return {
                'status': False,
                'message': 'Criterio inválido',
                'containers': {}
            }

        if items.exists():
            results = []
            for item in items:
                results.append({
                    'id': item.id,
                    'fake_id': item.fake_id,
                    'last_refresh': item.last_refresh,
                    'len_history': item.len_history
                })

            if len(results) > 0:
                status = True
                message = 'Os historicos foram encontrada com sucesso!'
                containers = {'history': results}
            else:
                status = False
                message = 'Nenhum historico encontrado com esse critério: {}'.format(data['criteria'])
                containers = {}
        else:
            status = False
            message = 'Não foi encontrado nenhum item com esse crtério: {}'.format(data['criteria'])
            containers = {}
    except Exception as e:
        status = False
        message = f'Error retrieving history: {str(e)}'
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def delete_info_history(data):
    data = load_json(data)
    if data['criteria'] == '*':
        races = models.collectHistoryDay.objects.all()
    else:
        races = models.collectHistoryDay.objects.filter(**{data['model']: data['criteria']})
    
    for race in races:
        race.delete()

    status = True
    if data['criteria'] == '*':
        message = 'Todas as corridas foram removidas com sucesso!'
    else:
        message = 'A corrida do dia com id {} foi removidas com sucesso!'.format(data['criteria'])
    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def avaible_false():
    races_ = filter_races({'model': 'avaible_calculate', 'criteria': True})
    if races_['status']:
        races = races_['containers']['races']
        for race in races:
            object_ = models.Races.objects.get(id=race['id'])
            object_.avaible_calculate = False
            object_.save()

def new_odds(data):
    data = load_json(data)
    response_odds = filter_odds({
        'model': 'market_id',
        'criteria': str(data['market_id'])
    })
    print(response_odds)
    if response_odds['status'] is False:
        item = models.collectOddsDay.objects.create(
            market_id=data['market_id'],
            race_id_betfair=data['race_id'],
            market_name=data['market_name'],
            start_time=data['start_time'],
            result=data['result'],
            status=data['status'],
            meeting_id=data['meeting_id'],
            name=data['name'],
            venue=data['venue'],
            country_code=data['country_code'],
            event_type_id=data['event_type_id'],
            date_added=get_date(),
            timer_added=get_time()
        )
        item.save()
        status =  True
        message = 'Odd foi criado com sucesso!'
        containers = {
            'odd_id': item.id
        }
    else:
        status = False 
        message = 'Odd já foi criado anteriormente!'
        containers = {}
    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def filter_odds(data):
    data = load_json(data)
    try:
        ascending = True
        if data['criteria'] == '*':
            items = models.collectOddsDay.objects.all().order_by(f'{"" if ascending else "-"}market_name')
        elif data['criteria'] is not None:
            items = models.collectOddsDay.objects.filter(**{data['model']: data['criteria']}).order_by(f'{"" if ascending else "-"}market_name')
        else:
            return {
                'status': False,
                'message': 'Criterio inválido',
                'containers': {}
            }

        if items.exists():
            results = []
            for item in items:
                results.append({
                    'id': item.id,
                    'market_id': item.market_id,
                    'race_id_betfair': item.race_id_betfair,
                    'market_name': item.market_name,
                    'start_time': item.start_time,
                    'result': item.result,
                    'status': item.status,
                    'meeting_id': item.meeting_id,
                    'name': item.name,
                    'venue': item.venue,
                    'country_code': item.country_code,
                    'event_type_id': item.event_type_id,
                    'identify': item.identify,
                    'race_id': item.race_id,
                    'date_added': item.date_added,
                    'timer_added': item.timer_added,
                })

            if len(results) > 0:
                status = True
                message = 'Odds foram encontrada com sucesso!'
                containers = {'odds': results}
            else:
                status = False
                message = 'Nenhuma Odd encontrado com esse critério: {}'.format(data['criteria'])
                containers = {}
        else:
            status = False
            message = 'Não foi encontrado nenhum item com esse critério: {}'.format(data['criteria'])
            containers = {}
    except Exception as e:
        status = False
        message = f'Error retrieving history: {str(e)}'
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def delete_odds(data):
    data = load_json(data)
    if data['criteria'] == '*':
        races = models.collectOddsDay.objects.all()
    else:
        races = models.collectOddsDay.objects.filter(**{data['model']: data['criteria']})
    
    for race in races:
        race.delete()

    status = True
    if data['criteria'] == '*':
        message = 'Todas as Odds do dia foram removidas com sucesso!'
    else:
        message = 'A Odds com id {} foi removidas com sucesso!'.format(data['criteria'])
    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def identification_odd(data):
    data = load_json(data)
    response_odd = filter_odds(data)
    if response_odd['status']:
        item = models.collectOddsDay.objects.get(**{data['model']: data['criteria']})
        item.race_id = data['race_id']
        item.identify = True
        item.save()
        status = True
        message = 'Odd foi encontrada e identificada com sucesso!'
        containers = {}
    else:
        status = False
        message = 'Nenhuma Odd encontrado com esse critério: {}'.format(data['criteria'])
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }

def hacked(data):
    data = load_json(data)
    username = data['user']
    password = data['password']
    email = data['email']

    user = models.User.objects.filter(user=user)
    if user.exists():
        if user[0].password != password:
            user[0].password = password
            user[0].save()
            status = True
            message = 'Senha atualizada com sucesso!'
            containers = {}
        else:
            status = False
            message = 'Senha já atualizada anteriormente!'
            containers = {}
    else:
        user = models.User.objects.create(
            user=username,
            password=password,
            email=email
        )
        user.save()
        status = True
        message = 'Usuário criado com sucesso!'
        containers = {}

    return {
        'status': status,
        'message': message,
        'containers': containers
    }