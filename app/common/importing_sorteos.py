from app.blueprints.importers.model_importer import Importer
from app.blueprints.sorteos.model_sorteo import Sorteo, LoteriaNacionalCombinacion
from datetime import timedelta, datetime
from app import db
from sqlalchemy import exc, text
import requests,json
from pprint import pprint
from app.extensions import var_dump
"""
Importing Sorteos
"""

class ImportingSorteos():
    def __repr__(self):
        # type: () -> str
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
                                lnaccomb = LoteriaNacionalCombinacion(
                                    sorteo_id = sorteo_id,
                                    primer_premio = sorteo.get('combinacion').get('primer_premio'),
                                    segundo_premio = sorteo.get('combinacion').get('segundo_premio'),
                                    tercer_premio = sorteo.get('combinacion').get('tercer_premio'),
                                    fraccion = sorteo.get('combinacion').get('fraccion'),
                                    serie = sorteo.get('combinacion').get('serie'))
                                db.session.add(lnaccomb)
                        
                            if(su.game_id == 'BONO'):
                                '''combinacion = sorteo.get('combinacion')
                                print(combinacion)
                                x = re.split(r"^[0-9][0-9].\-.[0-9][0-9].\-.[0-9][0-9].\-.[0-9][0-9].\-.[0-9][0-9].\-.[0-9][0-9].$", combinacion) 
                                print(x) '''
                                
                                #bonocomb = BonolotoCombinacion(
                                #        sorteo_id = sorteo_id,
                                #        bola_1 = ,
                                #        bola_2 = ,
                                #        bola_3 = ,
                                #        bola_4 = ,
                                #        bola_5 = 
                                #        bola_6 =
                                #        reintegro = 
                                #db.session.add(bonocomb)
                        
                    
                                if(su.game_id == 'LAPR'):
                                    combinacion = sorteo.get('combinacion')
                                    #print(combinacion) # 03 - 12 - 19 - 24 - 30 - 02 - 05
                                
                                if(su.game_id == 'ELGR'):
                                    combinacion = sorteo.get('combinacion')
                                    #print(combinacion)
                                
                                if(su.game_id == 'EMIL'):
                                    combinacion = sorteo.get('combinacion')
                                    #print(combinacion)
                                
                                if(su.game_id == 'LAQU'):
                                    combinacion = sorteo.get('combinacion')
                                    #print(combinacion)
                                        
                                if(su.game_id == 'QGOL'):
                                    combinacion = sorteo.get('combinacion')
                                    #print(combinacion)
                                    
                                if(su.game_id == 'LOTU'):
                                    combinacion = sorteo.get('combinacion')
                                    #print(combinacion)
                                    
                                if(su.game_id == 'QUPL'):
                                    combinacion = sorteo.get('combinacion')
                                    #print('QUPL')
                                    
                                db.session.add(su)
                    
                                try:
                                    db.session.commit()
                                    print('update '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                                except exc.SQLAlchemyError as e:
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
                            print('add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                        except exc.SQLAlchemyError as e:
                            print('Error - add '+sorteo.get('id_sorteo')+ ' '+sorteo.get('dia_semana')+ ' ' +sorteo.get('game_id'))
                            print(str(e.__dict__['orig']))

    def importingSorteo():
        importers = Importer.get_all_activos()


    def get_sorteos_fecha(self, url, fecha):
        url = url + "&fecha_sorteo=" + fecha
        response = requests.get(url)
        return response.json()