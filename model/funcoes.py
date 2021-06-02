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
            './model/files/statusCountProject/status_count_[Albuquerque, Albuquerque and Carvalho Comercio] - Mandatory human-resource open architecture.json')
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
            './model/files/statusCountProject/status_count_[Costa Comercio Comercio] - Sharable non-volatile internet solution.json')
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
            './model/files/statusCountProject/status_count_[Pereira - Barros Comercio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/statusCountProject/status_count_[Santos - Batista Comercio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/statusCountProject/status_count_[Souza Comercio e Associados] - Innovative background implementation.json')
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
            './model/files/taskFinishedProject/taskfinished[Albuquerque, Albuquerque and Carvalho Comercio] - Mandatory human-resource open architecture.json')
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
            './model/files/taskFinishedProject/taskfinished[Costa Comercio Comercio] - Sharable non-volatile internet solution.json')
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
            './model/files/taskFinishedProject/taskfinished[Pereira - Barros Comercio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/taskFinishedProject/taskfinished[Santos - Batista Comercio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/taskFinishedProject/taskfinished[Souza Comercio e Associados] - Innovative background implementation.json')
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
            './model/files/nome-sobrenome-projeto/[Albuquerque, Albuquerque and Carvalho Comercio] - Mandatory human-resource open architecture.json')
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
            './model/files/nome-sobrenome-projeto/[Costa Comercio Comercio] - Sharable non-volatile internet solution.json')
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
            './model/files/nome-sobrenome-projeto/[Pereira - Barros Comercio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/nome-sobrenome-projeto/[Santos - Batista Comercio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/nome-sobrenome-projeto/[Souza Comercio e Associados] - Innovative background implementation.json')
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
            './model/files/horas-por-projeto/horas_projeto_[Albuquerque, Albuquerque and Carvalho Comercio] - Mandatory human-resource open architecture.json')
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
            './model/files/horas-por-projeto/horas_projeto_[Costa Comercio Comercio] - Sharable non-volatile internet solution.json')
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
            './model/files/horas-por-projeto/horas_projeto_[Pereira - Barros Comercio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/horas-por-projeto/horas_projeto_[Santos - Batista Comercio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Souza Comercio e Associados] - Innovative background implementation.json')
        return Souza
    elif projeto == 'xavier':
        Xavier = openfile(
            './model/files/horas-por-projeto/horas_projeto_[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')
        return Xavier

def mediahras(projeto):
    if projeto == 'mediahoras':
        mediahoras = openfile(
            './model/files/media-sum-horas/media_horas_total.json')
        return mediahoras
    elif projeto == 'albuquerque':
        Albuquerque = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Albuquerque, Albuquerque and Carvalho Comercio] - Mandatory human-resource open architecture.json')
        return Albuquerque
    elif projeto == 'batista':
        Batista = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Batista, Moreira and Pereira LTDA] - Monitored multi-state installation.json')
        return Batista
    elif projeto == 'carvalho':
        Carvalho = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Carvalho, Costa and Costa e Associados] - Ergonomic methodical methodology.json')
        return Carvalho
    elif projeto == 'costacomercio':
        Costa_Comercio = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Costa Comercio Comercio] - Sharable non-volatile internet solution.json')
        return Costa_Comercio
    elif projeto == 'costaltda':
        Costa_LTDA = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Costa LTDA S.A.] - Total asynchronous secured line.json')
        return Costa_LTDA
    elif projeto == 'melo':
        Melo = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Melo, Melo and Santos e Associados] - Organized impactful instruction set.json')
        return Melo
    elif projeto == 'pereira':
        Pereira = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Pereira - Barros Comercio] - Mandatory fault-tolerant Graphical User Interface.json')
        return Pereira
    elif projeto == 'santos':
        a = './model/files/media-horas-por-projeto/media_horas_projeto_[Santos - Batista Comercio] - Stand-alone well-modulated policy.json'
        Santos = openfile(a)
        return Santos
    elif projeto == 'souza':
        Souza = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Souza Comercio e Associados] - Innovative background implementation.json')
        return Souza
    elif projeto == 'xavier':
        Xavier = openfile(
            './model/files/media-horas-por-projeto/media_horas_projeto_[Xavier EIRELI S.A.] - Vision-oriented holistic architecture.json')
        return Xavier


def taskcolaborador (projeto):
    if projeto == "anajulia":
        anajulia = openfile('./model/files/tasks-por-colaborador/Ana Julia_Franco.json')
        return anajulia
    elif projeto == "antonionogueira":
        antonionogueira = openfile('./model/files/tasks-por-colaborador/Antonio_Nogueira.json')
        return antonionogueira
    elif projeto == "bernardosouza":
        bernardosouza = openfile('./model/files/tasks-por-colaborador/Bernardo_Souza.json')
        return bernardosouza
    elif projeto == "carlosbatista":
        carlosbatista = openfile('./model/files/tasks-por-colaborador/Carlos_Batista.json')
        return carlosbatista
    elif projeto == "ceciliamoreira":
        ceciliamoreira = openfile('./model/files/tasks-por-colaborador/Cecilia_Moreira.json')
        return ceciliamoreira
    elif projeto == "davibatista":
        davibatista = openfile('./model/files/tasks-por-colaborador/Davi_Batista.json')
        return davibatista
    elif projeto == "elisioalbuquerque":
        elisioalbuquerque = openfile('./model/files/tasks-por-colaborador/Elisio_Albuquerque.json')
        return elisioalbuquerque
    elif projeto == "elisiomartins":
        elisiomartins = openfile('./model/files/tasks-por-colaborador/Elisio_Martins.json')
        return elisiomartins
    elif projeto == "enzogabriel":
        enzogabriel = openfile('./model/files/tasks-por-colaborador/Enzo Gabriel_Saraiva.json')
        return enzogabriel
    elif projeto == "fabiosouza":
        fabiosouza = openfile('./model/files/tasks-por-colaborador/Fabio_Souza.json')
        return fabiosouza
    elif projeto == "gabrielpereira":
        gabrielpereira = openfile('./model/files/tasks-por-colaborador/Gabriel_Pereira.json')
        return gabrielpereira
    elif projeto == "gustavosantos":
        gustavosantos = openfile('./model/files/tasks-por-colaborador/Gustavo_Santos.json')
        return gustavosantos
    elif projeto == "kleberoliveira":
        kleberoliveira = openfile('./model/files/tasks-por-colaborador/Kleber_Oliveira.json')
        return kleberoliveira
    elif projeto == "luccamelo":
        luccamelo = openfile('./model/files/tasks-por-colaborador/Lucca_Melo.json')
        return luccamelo
    elif projeto == "matheusbarros":
        matheusbarros = openfile('./model/files/tasks-por-colaborador/Matheus_Barros.json')
        return matheusbarros
    elif projeto == "pablomartins":
        pablomartins = openfile('./model/files/tasks-por-colaborador/Pablo_Martins.json')
        return pablomartins
    elif projeto == "rafaelxavier":
        rafaelxavier = openfile('./model/files/tasks-por-colaborador/Rafael_Xavier.json')
        return rafaelxavier
    elif projeto == "talitabraga":
        talitabraga = openfile('./model/files/tasks-por-colaborador/Talita_Braga.json')
        return talitabraga
    elif projeto == "vicentemoraes":
        vicentemoraes = openfile('./model/files/tasks-por-colaborador/Vicente_Moraes.json')
        return vicentemoraes


def horascolaborador (projeto):
        if projeto == "anajulia":
            anajulia = openfile('./model/files/horas-por-colaborador/Ana Julia_Franco.json')
            return anajulia
        elif projeto == "antonionogueira":
            antonionogueira = openfile('./model/files/horas-por-colaborador/Antonio_Nogueira.json')
            return antonionogueira
        elif projeto == "bernardosouza":
            bernardosouza = openfile('./model/files/horas-por-colaborador/Bernardo_Souza.json')
            return bernardosouza
        elif projeto == "carlosbatista":
            carlosbatista = openfile('./model/files/horas-por-colaborador/Carlos_Batista.json')
            return carlosbatista
        elif projeto == "ceciliamoreira":
            ceciliamoreira = openfile('./model/files/horas-por-colaborador/Cecilia_Moreira.json')
            return ceciliamoreira
        elif projeto == "davibatista":
            davibatista = openfile('./model/files/horas-por-colaborador/Davi_Batista.json')
            return davibatista
        elif projeto == "elisioalbuquerque":
            elisioalbuquerque = openfile('./model/files/horas-por-colaborador/Elisio_Albuquerque.json')
            return elisioalbuquerque
        elif projeto == "elisiomartins":
            elisiomartins = openfile('./model/files/horas-por-colaborador/Elisio_Martins.json')
            return elisiomartins
        elif projeto == "enzogabriel":
            enzogabriel = openfile('./model/files/horas-por-colaborador/Enzo Gabriel_Saraiva.json')
            return enzogabriel
        elif projeto == "fabiosouza":
            fabiosouza = openfile('./model/files/horas-por-colaborador/Fabio_Souza.json')
            return fabiosouza
        elif projeto == "gabrielpereira":
            gabrielpereira = openfile('./model/files/horas-por-colaborador/Gabriel_Pereira.json')
            return gabrielpereira
        elif projeto == "gustavosantos":
            gustavosantos = openfile('./model/files/horas-por-colaborador/Gustavo_Santos.json')
            return gustavosantos
        elif projeto == "kleberoliveira":
            kleberoliveira = openfile('./model/files/horas-por-colaborador/Kleber_Oliveira.json')
            return kleberoliveira
        elif projeto == "luccamelo":
            luccamelo = openfile('./model/files/horas-por-colaborador/Lucca_Melo.json')
            return luccamelo
        elif projeto == "matheusbarros":
            matheusbarros = openfile('./model/files/horas-por-colaborador/Matheus_Barros.json')
            return matheusbarros
        elif projeto == "pablomartins":
            pablomartins = openfile('./model/files/horas-por-colaborador/Pablo_Martins.json')
            return pablomartins
        elif projeto == "rafaelxavier":
            rafaelxavier = openfile('./model/files/horas-por-colaborador/Rafael_Xavier.json')
            return rafaelxavier
        elif projeto == "talitabraga":
            talitabraga = openfile('./model/files/horas-por-colaborador/Talita_Braga.json')
            return talitabraga
        elif projeto == "vicentemoraes":
            vicentemoraes = openfile('./model/files/horas-por-colaborador/Vicente_Moraes.json')
            return vicentemoraes