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

#horascolaborador
anajuliaH = horascolaborador('anajulia')
antonionogueiraH = horascolaborador('antonionogueira')
bernardosouzaH = horascolaborador('bernardosouza')
carlosbatistaH = horascolaborador('carlosbatista')
ceciliamoreiraH = horascolaborador('ceciliamoreira')
celiaoliveiraH = horascolaborador('celiaoliveira')
davibatistaH = horascolaborador('davibatista')
elisioalbuquerqueH = horascolaborador('elisioalbuquerque')
elisiomartinsH = horascolaborador('elisiomartins')
enzogabrielH = horascolaborador('enzogabriel')
fabiosouzaH = horascolaborador('fabiosouza')
gabrielpereiraH = horascolaborador('gabrielpereira')
gustavosantosH = horascolaborador('gustavosantos')
kleberoliveiraH = horascolaborador('kleberoliveira')
luccameloH = horascolaborador('luccamelo')
matheusbarrosH = horascolaborador('matheusbarros')
pablomartinsH = horascolaborador('pablomartins')
rafaelxavierH = horascolaborador('rafaelxavier')
talitabragaH = horascolaborador('talitabraga')
vicentemoraesH = horascolaborador('vicentemoraes')

#taskcolaborador
anajuliaT = taskcolaborador('anajulia')
antonionogueiraT = taskcolaborador('antonionogueira')
bernardosouzaT = taskcolaborador('bernardosouza')
carlosbatistaT = taskcolaborador('carlosbatista')
ceciliamoreiraT = taskcolaborador('ceciliamoreira')
celiaoliveiraT = taskcolaborador('celiaoliveira')
davibatistaT = taskcolaborador('davibatista')
elisioalbuquerqueT = taskcolaborador('elisioalbuquerque')
elisiomartinsT = taskcolaborador('elisiomartins')
enzogabrielT = taskcolaborador('enzogabriel')
fabiosouzaT = taskcolaborador('fabiosouza')
gabrielpereiraT= taskcolaborador('gabrielpereira')
gustavosantosT = taskcolaborador('gustavosantos')
kleberoliveiraT = taskcolaborador('kleberoliveira')
luccameloT = taskcolaborador('luccamelo')
matheusbarrosT = taskcolaborador('matheusbarros')
pablomartinsT = taskcolaborador('pablomartins')
rafaelxavierT = taskcolaborador('rafaelxavier')
talitabragaT = taskcolaborador('talitabraga')
vicentemoraesT = taskcolaborador('vicentemoraes')


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
        elif opcao == 'taskcolaborador' and nome == 'anajulia':
            return jsonify(anajuliaT)
        elif opcao == 'taskcolaborador' and nome == 'antonionogueira':
            return jsonify(antonionogueiraT)
        elif opcao == 'taskcolaborador' and nome == 'bernardosouza':
            return jsonify(bernardosouzaT)
        elif opcao == 'taskcolaborador' and nome == 'carlosbatista':
            return jsonify(carlosbatistaT)
        elif opcao == 'taskcolaborador' and nome == 'ceciliamoreira':
            return jsonify(ceciliamoreiraT)
        elif opcao == 'taskcolaborador' and nome == 'celiaoliveira':
            return jsonify(celiaoliveiraT)
        elif opcao == 'taskcolaborador' and nome == 'davibatista':
            return jsonify(davibatistaT)
        elif opcao == 'taskcolaborador' and nome == 'elisioalbuquerque':
            return jsonify(elisioalbuquerqueT)
        elif opcao == 'taskcolaborador' and nome == 'elisiomartins':
            return jsonify(elisiomartinsT)
        elif opcao == 'taskcolaborador' and nome == 'enzogabriel':
            return jsonify(enzogabrielT)
        elif opcao == 'taskcolaborador' and nome == 'fabiosouza':
            return jsonify(fabiosouzaT)
        elif opcao == 'taskcolaborador' and nome == 'gabrielpereira':
            return jsonify(gabrielpereiraT)
        elif opcao == 'taskcolaborador' and nome == 'gustavosantos':
            return jsonify(gustavosantosT)
        elif opcao == 'taskcolaborador' and nome == 'kleberoliveira':
            return jsonify(kleberoliveiraT)
        elif opcao == 'taskcolaborador' and nome == 'luccamelo':
            return jsonify(luccameloT)
        elif opcao == 'taskcolaborador' and nome == 'matheusbarros':
            return jsonify(matheusbarrosT)
        elif opcao == 'taskcolaborador' and nome == 'pablomartins':
            return jsonify(pablomartinsT)
        elif opcao == 'taskcolaborador' and nome == 'rafaelxavier':
            return jsonify(rafaelxavierT)
        elif opcao == 'taskcolaborador' and nome == 'talitabraga':
            return jsonify(talitabragaT)
        elif opcao == 'taskcolaborador' and nome == 'vicentemoraes':
            return jsonify(vicentemoraesT)
        elif opcao == 'horascolaborador' and nome == 'anajulia':
            return jsonify(anajuliaH)
        elif opcao == 'horascolaborador' and nome == 'antonionogueira':
            return jsonify(antonionogueiraH)
        elif opcao == 'horascolaborador' and nome == 'bernardosouza':
            return jsonify(bernardosouzaH)
        elif opcao == 'horascolaborador' and nome == 'carlosbatista':
            return jsonify(carlosbatistaH)
        elif opcao == 'horascolaborador' and nome == 'ceciliamoreira':
            return jsonify(ceciliamoreiraH)
        elif opcao == 'horascolaborador' and nome == 'celiaoliveira':
            return jsonify(celiaoliveiraH)
        elif opcao == 'horascolaborador' and nome == 'davibatista':
            return jsonify(davibatistaH)
        elif opcao == 'horascolaborador' and nome == 'elisioalbuquerque':
            return jsonify(elisioalbuquerqueH)
        elif opcao == 'horascolaborador' and nome == 'elisiomartins':
            return jsonify(elisiomartinsH)
        elif opcao == 'horascolaborador' and nome == 'enzogabriel':
            return jsonify(enzogabrielH)
        elif opcao == 'horascolaborador' and nome == 'fabiosouza':
            return jsonify(fabiosouzaH)
        elif opcao == 'horascolaborador' and nome == 'gabrielpereira':
            return jsonify(gabrielpereiraH)
        elif opcao == 'horascolaborador' and nome == 'gustavosantos':
            return jsonify(gustavosantosH)
        elif opcao == 'horascolaborador' and nome == 'kleberoliveira':
            return jsonify(kleberoliveiraH)
        elif opcao == 'horascolaborador' and nome == 'luccamelo':
            return jsonify(luccameloH)
        elif opcao == 'horascolaborador' and nome == 'matheusbarros':
            return jsonify(matheusbarrosH)
        elif opcao == 'horascolaborador' and nome == 'pablomartins':
            return jsonify(pablomartinsH)
        elif opcao == 'horascolaborador' and nome == 'rafaelxavier':
            return jsonify(rafaelxavierH)
        elif opcao == 'horascolaborador' and nome == 'talitabraga':
            return jsonify(talitabragaH)
        elif opcao == 'horascolaborador' and nome == 'vicentemoraes':
            return jsonify(vicentemoraesH)
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