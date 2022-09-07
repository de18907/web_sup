import webbrowser
urls =   [
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/A-Total-de-Activos-por-Entidad.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/B-Estados-Financieros.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/C-Indicadores-Financieros.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/D-Cartera-de-Creditos.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/E-Solvencia-y-sus-Componentes.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/F-numero-de-Empleados-Oficinas-y-Cajeros-Automatico.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/G-Reclamaciones-de-los-Usuarios-de-los-Servicios-Financieros.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/O-Otros-Indicadores-Financieros.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/D-Cartera-de-Cr%C3%A9ditos-2006-2015_1.xlsx',
            'https://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/R _Eventos_deprdidas_economicas_de_Riesgo_Operacional_Mensual.xlsx',
            'http://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/subagentes-por-entidad_2.xlsx',
            'http://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/subagentes-por-localidad-y-actividad_2.xlsx',
            'http://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/estadisticas/seriestiempo/subagentes-transacciones_2.xlsx',
            'http://stats0.sb.gob.do/sites/default/files/nuevosdocumentos/tasas-y-comisiones-de-tarjetas-de-credito_27.xlsx'
        ]
aux = 0
for x in urls:
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C://Program Files/Google/Chrome/Application//chrome.exe"))
    webbrowser.get('Chrome').open(urls[aux])
    aux += 1