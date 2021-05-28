from model.funcoes import *

#! STATUS:
statustotal = status('statusall')
albu = status('albuquerque')
bati = status('batista')
carva = status('carvalho')
costacom = status('costacomercio')
costal = status('costaltda')
mel = status('melo')
pere = status('pereira')
san = status('santos')
sou = status('souza')
xav = status('xavier')

#! TASKS:
statustotalT = task('statusall')
albuT = task('albuquerque')
batiT = task('batista')
carvaT = task('carvalho')
costacomT = task('costacomercio')
costalT = task('costaltda')
melT = task('melo')
pereT = task('pereira')
sanT = task('santos')
souT = task('souza')
xavT = task('xavier')

#! Nome e sobrenome:
nomeall = nomesobrenome('nomeall')
albuN = nomesobrenome('albuquerque')
batiN = nomesobrenome('batista')
carvaN = nomesobrenome('carvalho')
costacomN = nomesobrenome('costacomercio')
costalN = nomesobrenome('costaltda')
melN = nomesobrenome('melo')
pereN = nomesobrenome('pereira')
sanN = nomesobrenome('santos')
souN = nomesobrenome('souza')
xavN = nomesobrenome('xavier')

#! horas:
horasall = horas('horastotal')
albuH = horas('albuquerque')
batiH = horas('batista')
carvaH = horas('carvalho')
costacomH = horas('costacomercio')
costalH = horas('costaltda')
melH = horas('melo')
pereH = horas('pereira')
sanH = horas('santos')
souH = horas('souza')
xavH = horas('xavier')

#mediahoras:
mediatotal = mediahras('mediahoras')
albuMH = mediahras('albuquerque')
batiMH = mediahras('batista')
carvaMH = mediahras('carvalho')
costacomMH = mediahras('costacomercio')
costalMH = mediahras('costaltda')
melMH = mediahras('melo')
pereMH = mediahras('pereira')
sanMH = mediahras('santos')
souMH = mediahras('souza')
xavMH = mediahras('xavier')

def projet(opcao, nome):
    if opcao and nome:
        if opcao == 'status' and nome == 'albuquerque':
            return jsonify(albu)
        elif opcao == 'status' and nome == 'batista':
            return jsonify(bati)
        elif opcao == 'status' and nome == 'carvalho':
            return jsonify(carva)
        elif opcao == 'status' and nome == 'costacomercio':
            return jsonify(costacom)
        elif opcao == 'status' and nome == 'costaltda':
            return jsonify(costal)
        elif opcao == 'status' and nome == 'melo':
            return jsonify(mel)
        elif opcao == 'status' and nome == 'pereira':
            return jsonify(pere)
        elif opcao == 'status' and nome == 'santos':
            return jsonify(san)
        elif opcao == 'status' and nome == 'souza':
            return jsonify(sou)
        elif opcao == 'status' and nome == 'xavier':
            return jsonify(xav)
        elif opcao == 'task' and nome == 'albuquerque':
            return jsonify(albuT)
        elif opcao == 'task' and nome == 'batista':
            return jsonify(batiT)
        elif opcao == 'task' and nome == 'carvalho':
            return jsonify(carvaT)
        elif opcao == 'task' and nome == 'costacomercio':
            return jsonify(costacomT)
        elif opcao == 'task' and nome == 'costaltda':
            return jsonify(costalT)
        elif opcao == 'task' and nome == 'melo':
            return jsonify(melT)
        elif opcao == 'task' and nome == 'pereira':
            return jsonify(pereT)
        elif opcao == 'task' and nome == 'santos':
            return jsonify(sanT)
        elif opcao == 'task' and nome == 'souza':
            return jsonify(souT)
        elif opcao == 'task' and nome == 'xavier':
            return jsonify(xavT)
        elif opcao == 'horas' and nome == 'albuquerque':
            return jsonify(albuH)
        elif opcao == 'horas' and nome == 'batista':
            return jsonify(batiH)
        elif opcao == 'horas' and nome == 'carvalho':
            return jsonify(carvaH)
        elif opcao == 'horas' and nome == 'costacomercio':
            return jsonify(costacomH)
        elif opcao == 'horas' and nome == 'costaltda':
            return jsonify(costalH)
        elif opcao == 'horas' and nome == 'melo':
            return jsonify(melH)
        elif opcao == 'horas' and nome == 'pereira':
            return jsonify(pereH)
        elif opcao == 'horas' and nome == 'santos':
            return jsonify(sanH)
        elif opcao == 'horas' and nome == 'souza':
            return jsonify(souH)
        elif opcao == 'horas' and nome == 'xavier':
            return jsonify(xavH)
        elif opcao == 'nome' and nome == 'albuquerque':
            return jsonify(albuN)
        elif opcao == 'nome' and nome == 'batista':
            return jsonify(batiN)
        elif opcao == 'nome' and nome == 'carvalho':
            return jsonify(carvaN)
        elif opcao == 'nome' and nome == 'costacomercio':
            return jsonify(costacomN)
        elif opcao == 'nome' and nome == 'costaltda':
            return jsonify(costalN)
        elif opcao == 'nome' and nome == 'melo':
            return jsonify(melN)
        elif opcao == 'nome' and nome == 'pereira':
            return jsonify(pereN)
        elif opcao == 'nome' and nome == 'santos':
            return jsonify(sanN)
        elif opcao == 'nome' and nome == 'souza':
            return jsonify(souN)
        elif opcao == 'nome' and nome == 'xavier':
            return jsonify(xavN)
        elif opcao == 'mediahoras' and nome == 'albuquerque':
            return jsonify(albuMH)
        elif opcao == 'mediahoras' and nome == 'batista':
            return jsonify(batiMH)
        elif opcao == 'mediahoras' and nome == 'carvalho':
            return jsonify(carvaMH)
        elif opcao == 'mediahoras' and nome == 'costacomercio':
            return jsonify(costacomMH)
        elif opcao == 'mediahoras' and nome == 'costaltda':
            return jsonify(costalMH)
        elif opcao == 'mediahoras' and nome == 'melo':
            return jsonify(melMH)
        elif opcao == 'mediahoras' and nome == 'pereira':
            return jsonify(pereMH)
        elif opcao == 'mediahoras' and nome == 'santos':
            return jsonify(sanMH)
        elif opcao == 'mediahoras' and nome == 'souza':
            return jsonify(souMH)
        elif opcao == 'mediahoras' and nome == 'xavier':
            return jsonify(xavMH)
        else:
            return "digite um projeto válido"
    elif opcao:
        if opcao == 'status':
            return jsonify(statustotal)
        elif opcao == 'task':
            return jsonify(statustotalT)
        elif opcao == 'horas':
            return jsonify(horasall)
        elif opcao == 'nome':
            return jsonify(nomeall)
        elif opcao == 'mediahoras':
            return jsonify(mediatotal)