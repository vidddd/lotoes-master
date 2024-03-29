#!/usr/bin/python
from app.blueprints.importers.model_importer import Importer
from app.blueprints.sorteos.model_sorteo import Sorteo, LoteriaNacionalCombinacion, BonolotoCombinacion, PrimitivaCombinacion, EuromillonesCombinacion, GordoPrimitivaCombinacion, QuinielaPartidos, QuinigolPartidos, LototurfCombinacion, QuintupleplusCombinacion
from flask import current_app
from datetime import timedelta, datetime
from app import db
from sqlalchemy import exc, text
import requests,json,re
from pprint import pprint
from app.extensions import var_dump
from app.common.mail import send_email

"""
Importing Sorteos
"""

class ImportingSorteos():
    def __repr__(self):
        return "<ImportingSorteos>"
    
    def __init__(self, **kargs):
        self.today = datetime.today()
        
    def importingAll(self):
        importers = Importer.get_all_activos()
        for importer in importers:
            if(importer.parametro_fecha):
                fecha = (self.today + timedelta(importer.dias)).strftime('%Y%m%d')
            else:
                fecha = self.today.strftime('%Y%m%d')
            
            result = self.get_sorteos_fecha(importer.url, fecha)
            if type(result) is list:
                for sorteo in result:
                    sorteo_id = Sorteo.exists(sorteo.get('id_sorteo'))
                    if(sorteo_id): #ya existe
                        id_sorteo=sorteo.get('id_sorteo')
                        su = Sorteo.query.filter_by(id_sorteo=id_sorteo).first()
                        if su:
                            su.fecha_sorteo = sorteo.get('fecha_sorteo')
                            su.recaudacion=sorteo.get('recaudacion')
                            su.combinacion_json=json.dumps(sorteo.get('combinacion')),
                            su.premios=sorteo.get('premios')
                            su.fondo_bote=sorteo.get('fondo_bote')
                            su.escrutinio=sorteo.get('escrutinio')
                            su.apuestas=sorteo.get('apuestas')
                            if(su.game_id == 'LNAC'):
                                # solo guardamos cuando existen resultados y nos se han guardado antes
                                comb = sorteo.get('combinacion').get('primer_premio')
                                comb2 = LoteriaNacionalCombinacion.exists_by_sorteo_id(sorteo_id)
                                if comb is not None and comb2 is None:
                                    lnaccomb = LoteriaNacionalCombinacion(
                                        sorteo_id = sorteo_id,
                                        primer_premio = sorteo.get('combinacion').get('primer_premio'),
                                        segundo_premio = sorteo.get('combinacion').get('segundo_premio'),
                                        tercer_premio = sorteo.get('combinacion').get('tercer_premio'),
                                        fraccion = sorteo.get('combinacion').get('fraccion'),
                                        serie = sorteo.get('combinacion').get('serie'))
                                    db.session.add(lnaccomb)
                                    current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))

                           
                            if(su.game_id == 'BONO'):
                                combinacion = sorteo.get('combinacion')
                                if combinacion is not None: 
                                    ''' Formato en que viene: 12 - 21 - 27 - 36 - 43 - 49 C(01) R(4) '''
                                    comb = BonolotoCombinacion.exists_by_sorteo_id(sorteo_id)
                                    if comb is None:
                                        x = re.findall("[0-9]+", combinacion) 
                                        bonocomb = BonolotoCombinacion(
                                            sorteo_id = sorteo_id,
                                            bola_1 = x[0],
                                            bola_2 = x[1],
                                            bola_3 = x[2],
                                            bola_4 = x[3],
                                            bola_5 = x[4],
                                            bola_6 = x[5],
                                            reintegro = x[6],
                                            complementario = x[7])
                                        db.session.add(bonocomb)
                                        current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))
                                                            
                            if(su.game_id == 'LAPR'):
                                combinacion = sorteo.get('combinacion')
                                if combinacion is not None:
                                    comb = PrimitivaCombinacion.exists_by_sorteo_id(sorteo_id)
                                    if comb is None:
                                        x = re.findall("[0-9]+", combinacion) 
                                        primicomb = PrimitivaCombinacion(
                                            sorteo_id = sorteo_id,
                                            bola_1 = x[0],
                                            bola_2 = x[1],
                                            bola_3 = x[2],
                                            bola_4 = x[3],
                                            bola_5 = x[4],
                                            bola_6 = x[5],
                                            reintegro = x[6],
                                            complementario = x[7])
                                        db.session.add(primicomb)
                                        current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))                                    
                                
                            if(su.game_id == 'ELGR'):
                                combinacion = sorteo.get('combinacion')
                                if combinacion is not None:
                                    comb = GordoPrimitivaCombinacion.exists_by_sorteo_id(sorteo_id)
                                    if comb is None:
                                        x = re.findall("[0-9]+", combinacion) 
                                        gordocomb = GordoPrimitivaCombinacion(
                                            sorteo_id = sorteo_id,
                                            bola_1 = x[0],
                                            bola_2 = x[1],
                                            bola_3 = x[2],
                                            bola_4 = x[3],
                                            bola_5 = x[4],
                                            clave = x[5])
                                        db.session.add(gordocomb)
                                        current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))

                                
                            if(su.game_id == 'EMIL'):
                                combinacion = sorteo.get('combinacion')
                                if combinacion is not None:
                                    comb = EuromillonesCombinacion.exists_by_sorteo_id(sorteo_id)
                                    if comb is None:
                                        x = re.findall("[0-9]+", combinacion) 
                                        eurcomb = EuromillonesCombinacion(
                                            sorteo_id = sorteo_id,
                                            bola_1 = x[0],
                                            bola_2 = x[1],
                                            bola_3 = x[2],
                                            bola_4 = x[3],
                                            bola_5 = x[4],
                                            estrella_1 = x[5],
                                            estrella_2 = x[6])
                                        db.session.add(eurcomb)
                                        current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))
                                        
                                
                            if(su.game_id == 'LAQU'):
                                partidos = sorteo.get('partidos')
                                if partidos is not None:
                                    part = QuinielaPartidos.exists_by_sorteo_id(sorteo_id)
                                    if part is None:
                                        for partido in partidos:
                                            print('partido quiniela')
                                            print(partido)
                                            signo = partido.get('signo') if partido.get('signo') != None else ''
                                            marcador = partido.get('marcador') if partido.get('marcador') != None else ''
                                            fecha = partido.get('fecha') if partido.get('fecha') != None else ''
                                            
                                            quipar = QuinielaPartidos(
                                                sorteo_id = sorteo_id,
                                                local = partido.get('local'),
                                                visitante = partido.get('visitante'),
                                                signo = signo,
                                                marcador = marcador,
                                                fecha = fecha
                                                )
                                            db.session.add(quipar)
                                            current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))

                                        
                            if(su.game_id == 'QGOL'):
                                partidos = sorteo.get('partidos')
                                if partidos is not None:
                                    part = QuinigolPartidos.exists_by_sorteo_id(sorteo_id)
                                    if part is None:
                                        for partido in partidos:
                                            print('partido quinigol')
                                            print(partido)
                                            signo = partido.get('signo') if partido.get('signo') != None else ''
                                            marcador = partido.get('marcador') if partido.get('marcador') != None else ''
                                            fecha = partido.get('fecha') if partido.get('fecha') != None else ''
                                            quipar = QuinigolPartidos(
                                                sorteo_id = sorteo_id,
                                                local = partido.get('local'),
                                                visitante = partido.get('visitante'),
                                                signo = signo,
                                                marcador = marcador,
                                                fecha = fecha
                                                )
                                            db.session.add(quipar)
                                            current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))

                                           
                            if(su.game_id == 'LOTU'):
                                combinacion = sorteo.get('combinacion')
                                if combinacion is not None:
                                    comb = LototurfCombinacion.exists_by_sorteo_id(sorteo_id)
                                    if comb is None:
                                        x = re.findall("[0-9]+", combinacion) 
                                        lotucomb = LototurfCombinacion(
                                            sorteo_id = sorteo_id,
                                            bola_1 = x[0],
                                            bola_2 = x[1],
                                            bola_3 = x[2],
                                            bola_4 = x[3],
                                            bola_5 = x[4],
                                            bola_6 = x[5],
                                            caballo = x[6],
                                            reintegro = x[7])
                                        db.session.add(lotucomb)
                                        current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))

                                                                    
                            if(su.game_id == 'QUPL'):
                                combinacion = sorteo.get('combinacion')
                                if combinacion is not None:
                                    comb = QuintupleplusCombinacion.exists_by_sorteo_id(sorteo_id)
                                    if comb is None:
                                        x = re.findall("[0-9]+", combinacion) 
                                        qucomb = QuintupleplusCombinacion(
                                            sorteo_id = sorteo_id,
                                            bola_1 = x[0],
                                            bola_2 = x[1],
                                            bola_3 = x[2],
                                            bola_4 = x[3],
                                            bola_5 = x[4],
                                            bola_6 = x[5])
                                        db.session.add(qucomb)
                                        current_app.logger.info('Update sorteo %s - %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('dia_semana'), sorteo.get('fecha_sorteo'))
                                                       
                        try:
                            db.session.commit()
                            #send_email(subject='Lotoes Master - Update Sorteo', sender=current_app.config['LOTOES_MAIL_FROM'], recipients=[current_app.config['LOTOES_MAIL_SEND']],
                            #    text_body=f'update '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))

                        except exc.SQLAlchemyError as e:
                            send_email(subject='Error - Lotoes Master',
                                            sender=current_app.config['LOTOES_MAIL_FROM'], recipients=[current_app.config['LOTOES_MAIL_SEND']],
                                            text_body=f'Error - update '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                            print('Error - update '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                            print(str(e.__dict__['orig'])) 

                    else:  #nuevo sorteo
                        s = Sorteo(
                            nombre=sorteo.get('nombre'),
                            fecha_sorteo=sorteo.get('fecha_sorteo'), 
                            dia_semana=sorteo.get('dia_semana'), 
                            id_sorteo=sorteo.get('id_sorteo'),
                            game_id=sorteo.get('game_id'),
                            anyo=sorteo.get('anyo'),
                            numero_sorteo=sorteo.get('num_sorteo'),
                            lugar=sorteo.get('lugar'),
                            premio_bote=sorteo.get('premio_bote'),
                            cdc=sorteo.get('cdc'),
                            apuestas=sorteo.get('apuestas'),
                            recaudacion=sorteo.get('recaudacion'),
                            combinacion_json=json.dumps(sorteo.get('combinacion')),
                            premios=sorteo.get('premios'),
                            fondo_bote=sorteo.get('fondo_bote'),
                            escrutinio=sorteo.get('escrutinio'),
                        )
                        db.session.add(s)
                        try:
                            db.session.commit()
                            add = 'add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id')
                            print(add)
                            current_app.logger.info('Add sorteo %s - %s - %s', sorteo.get('id_sorteo'), sorteo.get('game_id'), sorteo.get('fecha_sorteo'))
                            send_email(subject='Lotoes Master - Add Sorteo', sender=current_app.config['LOTOES_MAIL_FROM'], recipients=[current_app.config['LOTOES_MAIL_SEND']],
                                        text_body=add)

                        except exc.SQLAlchemyError as e:
                            send_email(subject='Error - Lotoes Master',
                                sender=current_app.config['LOTOES_MAIL_FROM'], recipients=[current_app.config['LOTOES_MAIL_SEND']],
                                text_body=f'Error - add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'),
                                html_body=f'Error - add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'),)
                            print('Error - add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                            print(str(e.__dict__['orig']))

    def importingSorteo():
        importers = Importer.get_all_activos()


    def get_sorteos_fecha(self, url, fecha):
        url = url + "&fecha_sorteo=" + fecha
        response = requests.get(url)
        return response.json()
