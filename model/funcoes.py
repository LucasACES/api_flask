from flask import Flask, jsonify, request
import json


def openfile(arq):
    json_file = open(file=f'{arq}')
    arquivoo = json.load(json_file)
    json_file.close()
    return arquivoo


def status(projeto):
    if projeto == 'statusall':
        status_all = openfile('./model/files/statusCount/status_count.json')
        return status_all
    elif projeto == 'albuquerque':
        Albuquerque = openfile(
            './model/files/statusCountProject/status_count_[Albuquerque, Albuquerque and Carvalho Comércio] - Mandatory human-resource open architecture.json')
        return Albuquerque
    elif projeto == 'batista':
        Batista = openfile(
            './model/files/statusCountProject/status_count_[Batista, Moreira and Pereira LTDA] - Monitored multi-state installation.json')
        return Batista
    elif projeto == 'carvalho':
        Carvalho = openfile(
            './model/files/statusCountProject/status_count_[Carvalho, Costa and Costa e Associados] - Ergonomic methodical methodology.json')
        return Carvalho
    elif projeto == 'costacomercio':
        Costa_Comercio = openfile(
            './model/files/statusCountProject/status_count_[Costa Comércio Comércio] - Sharable non-volatile internet solution.json')
        return Costa_Comercio
    elif projeto == 'costaltda':
        Costa_LTDA = openfile(
            './model/files/statusCountProject/status_count_[Costa LTDA S.A.] - Total asynchronous secured line.json')
        return Costa_LTDA
    elif projeto == 'melo':
        Melo = openfile(
            './model/files/statusCountProject/status_count_[Melo, Melo and Santos e Associados] - Organized impactful instruction set.json')
        return Melo
    elif projeto == 'pereira':
        Pereira = openfile(
            './model/files/statusCountProject/status_count_[Pereira - Barros Comércio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/statusCountProject/status_count_[Santos - Batista Comércio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/statusCountProject/status_count_[Souza Comércio e Associados] - Innovative background implementation.json')
        return Souza
    elif projeto == 'xavier':
        Xavier = openfile(
            './model/files/statusCountProject/status_count_[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')
        return Xavier


def task(projeto):
    if projeto == 'statusall':
        status_all = openfile(
            './model/files/taskFinished/tasksfinishedAll.json')
        return status_all
    elif projeto == 'albuquerque':
        Albuquerque = openfile(
            './model/files/taskFinishedProject/taskfinished[Albuquerque, Albuquerque and Carvalho Comércio] - Mandatory human-resource open architecture.json')
        return Albuquerque
    elif projeto == 'batista':
        Batista = openfile(
            './model/files/taskFinishedProject/taskfinished[Batista, Moreira and Pereira LTDA] - Monitored multi-state installation.json')
        return Batista
    elif projeto == 'carvalho':
        Carvalho = openfile(
            './model/files/taskFinishedProject/taskfinished[Carvalho, Costa and Costa e Associados] - Ergonomic methodical methodology.json')
        return Carvalho
    elif projeto == 'costacomercio':
        Costa_Comercio = openfile(
            './model/files/taskFinishedProject/taskfinished[Costa Comércio Comércio] - Sharable non-volatile internet solution.json')
        return Costa_Comercio
    elif projeto == 'costaltda':
        Costa_LTDA = openfile(
            './model/files/taskFinishedProject/taskfinished[Costa LTDA S.A.] - Total asynchronous secured line.json')
        return Costa_LTDA
    elif projeto == 'melo':
        Melo = openfile(
            './model/files/taskFinishedProject/taskfinished[Melo, Melo and Santos e Associados] - Organized impactful instruction set.json')
        return Melo
    elif projeto == 'pereira':
        Pereira = openfile(
            './model/files/taskFinishedProject/taskfinished[Pereira - Barros Comércio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/taskFinishedProject/taskfinished[Santos - Batista Comércio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/taskFinishedProject/taskfinished[Souza Comércio e Associados] - Innovative background implementation.json')
        return Souza
    elif projeto == 'xavier':
        Xavier = openfile(
            './model/files/taskFinishedProject/taskfinished[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')
        return Xavier


def nomesobrenome(projeto):
    if projeto == 'nomeall':
        nomeall = openfile(
            './model/files/nome-sobrenome/nomeAll.json')
        return nomeall
    elif projeto == 'albuquerque':
        Albuquerque = openfile(
            './model/files/nome-sobrenome-projeto/[Albuquerque, Albuquerque and Carvalho Comércio] - Mandatory human-resource open architecture.json')
        return Albuquerque
    elif projeto == 'batista':
        Batista = openfile(
            './model/files/nome-sobrenome-projeto/[Batista, Moreira and Pereira LTDA] - Monitored multi-state installation.json')
        return Batista
    elif projeto == 'carvalho':
        Carvalho = openfile(
            './model/files/nome-sobrenome-projeto/[Carvalho, Costa and Costa e Associados] - Ergonomic methodical methodology.json')
        return Carvalho
    elif projeto == 'costacomercio':
        Costa_Comercio = openfile(
            './model/files/nome-sobrenome-projeto/[Costa Comércio Comércio] - Sharable non-volatile internet solution.json')
        return Costa_Comercio
    elif projeto == 'costaltda':
        Costa_LTDA = openfile(
            './model/files/nome-sobrenome-projeto/[Costa LTDA S.A.] - Total asynchronous secured line.json')
        return Costa_LTDA
    elif projeto == 'melo':
        Melo = openfile(
            './model/files/nome-sobrenome-projeto/[Melo, Melo and Santos e Associados] - Organized impactful instruction set.json')
        return Melo
    elif projeto == 'pereira':
        Pereira = openfile(
            './model/files/nome-sobrenome-projeto/[Pereira - Barros Comércio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/nome-sobrenome-projeto/[Santos - Batista Comércio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/nome-sobrenome-projeto/[Souza Comércio e Associados] - Innovative background implementation.json')
        return Souza
    elif projeto == 'xavier':
        Xavier = openfile(
            './model/files/nome-sobrenome-projeto/[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')
        return Xavier


def horas(projeto):
    if projeto == 'horastotal':
        horastotal = openfile(
            './model/files/sum-horas/horastotal.json')
        return horastotal
    elif projeto == 'albuquerque':
        Albuquerque = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Albuquerque, Albuquerque and Carvalho Comércio] - Mandatory human-resource open architecture.json')
        return Albuquerque
    elif projeto == 'batista':
        Batista = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Batista, Moreira and Pereira LTDA] - Monitored multi-state installation.json')
        return Batista
    elif projeto == 'carvalho':
        Carvalho = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Carvalho, Costa and Costa e Associados] - Ergonomic methodical methodology.json')
        return Carvalho
    elif projeto == 'costacomercio':
        Costa_Comercio = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Costa Comércio Comércio] - Sharable non-volatile internet solution.json')
        return Costa_Comercio
    elif projeto == 'costaltda':
        Costa_LTDA = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Costa LTDA S.A.] - Total asynchronous secured line.json')
        return Costa_LTDA
    elif projeto == 'melo':
        Melo = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Melo, Melo and Santos e Associados] - Organized impactful instruction set.json')
        return Melo
    elif projeto == 'pereira':
        Pereira = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Pereira - Barros Comércio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/horas-por-projeto/horas_projeto_[Santos - Batista Comércio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Souza Comércio e Associados] - Innovative background implementation.json')
        return Souza
    elif projeto == 'xavier':
        Xavier = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')
        return Xavier
