from datetime import datetime, timedelta

class CalendarioAzteca:
    """
    Simulador completo del calendario azteca con Xiuhpohualli (365 días) y Tonalpohualli (260 días)
    Incluye significados astrológicos, dioses patronos, características de personalidad, colores y direcciones
    Basado en la correlación de Alfonso Caso (12 de febrero = inicio del año azteca)
    """
    
    # Los 18 meses del Xiuhpohualli (veintenas)
    MESES_XIUHPOHUALLI = [
        "Atlcahualo",          # 1
        "Tlacaxipehualiztli",  # 2
        "Tozoztontli",         # 3
        "Huey Tozoztli",       # 4
        "Toxcatl",             # 5
        "Etzalcualiztli",      # 6
        "Tecuilhuitontli",     # 7
        "Huey Tecuilhuitl",    # 8
        "Tlaxochimaco",        # 9
        "Xocotl Huetzi",       # 10
        "Ochpaniztli",         # 11
        "Teotleco",            # 12
        "Tepeilhuitl",         # 13
        "Quecholli",           # 14
        "Panquetzaliztli",     # 15
        "Atemoztli",           # 16
        "Tititl",              # 17
        "Izcalli"              # 18
    ]
    
    # Los 20 signos del Tonalpohualli con información completa
    SIGNOS_TONALPOHUALLI = [
        {
            "nahuatl": "Cipactli",
            "español": "Cocodrilo/Caimán",
            "glifo": "🐊",
            "simbolo": "☰",
            "dios_patron": "Tonacatecuhtli",
            "dios_descripcion": "Señor de la Subsistencia",
            "significado": "Origen, creación, fertilidad, abundancia material",
            "augurio": "Muy favorable",
            "personalidad": "Personas creativas, fuertes, con gran capacidad para crear y nutrir. Tienen poder material pero deben evitar la codicia.",
            "direccion": "Este",
            "color": "Verde/Amarillo",
            "elemento": "Tierra/Agua"
        },
        {
            "nahuatl": "Ehecatl",
            "español": "Viento",
            "glifo": "💨",
            "simbolo": "≋",
            "dios_patron": "Quetzalcoatl",
            "dios_descripcion": "Serpiente Emplumada",
            "significado": "Aliento divino, cambio, comunicación, espiritualidad",
            "augurio": "Variable, depende de las circunstancias",
            "personalidad": "Personas inquietas, comunicativas, espirituales. Amantes del cambio y la libertad. Pueden ser inestables emocionalmente.",
            "direccion": "Norte",
            "color": "Blanco",
            "elemento": "Aire"
        },
        {
            "nahuatl": "Calli",
            "español": "Casa",
            "glifo": "🏠",
            "simbolo": "⌂",
            "dios_patron": "Tepeyollotl",
            "dios_descripcion": "Corazón de la Montaña",
            "significado": "Hogar, interior, introspección, seguridad",
            "augurio": "Favorable para asuntos domésticos",
            "personalidad": "Personas hogareñas, protectoras, introspectivas. Valoran la familia y la estabilidad. Pueden ser posesivas.",
            "direccion": "Oeste",
            "color": "Negro/Azul oscuro",
            "elemento": "Tierra"
        },
        {
            "nahuatl": "Cuetzpallin",
            "español": "Lagartija",
            "glifo": "🦎",
            "simbolo": "⥮",
            "dios_patron": "Huehuecoyotl",
            "dios_descripcion": "Coyote Viejo",
            "significado": "Agilidad, adaptación, regeneración, astucia",
            "augurio": "Neutro, requiere precaución",
            "personalidad": "Personas ágiles mentalmente, adaptables, astutas. Pueden ser engañosas o demasiado cambiantes.",
            "direccion": "Sur",
            "color": "Rojo",
            "elemento": "Fuego"
        },
        {
            "nahuatl": "Coatl",
            "español": "Serpiente",
            "glifo": "🐍",
            "simbolo": "∿",
            "dios_patron": "Chalchiuhtlicue",
            "dios_descripcion": "La de la Falda de Jade",
            "significado": "Transformación, sabiduría, sensualidad, poder",
            "augurio": "Poderoso pero peligroso",
            "personalidad": "Personas magnéticas, seductoras, sabias. Gran capacidad de transformación personal. Pueden ser vengativas.",
            "direccion": "Este",
            "color": "Verde jade",
            "elemento": "Agua/Tierra"
        },
        {
            "nahuatl": "Miquiztli",
            "español": "Muerte",
            "glifo": "💀",
            "simbolo": "☠",
            "dios_patron": "Tecciztecatl/Mictlantecuhtli",
            "dios_descripcion": "Señor del Inframundo",
            "significado": "Transformación profunda, fin de ciclos, renacimiento",
            "augurio": "Desfavorable para inicios, favorable para finales",
            "personalidad": "Personas profundas, místicas, comprenden los ciclos de vida. Pueden ser melancólicas o morbosas.",
            "direccion": "Norte",
            "color": "Blanco/Negro",
            "elemento": "Tierra"
        },
        {
            "nahuatl": "Mazatl",
            "español": "Venado",
            "glifo": "🦌",
            "simbolo": "⚶",
            "dios_patron": "Tlaloc",
            "dios_descripcion": "Dios de la Lluvia",
            "significado": "Rapidez, timidez, gracia, conexión con la naturaleza",
            "augurio": "Favorable, especialmente para viajes",
            "personalidad": "Personas rápidas, nerviosas, amantes de la libertad y naturaleza. Pueden ser tímidas o huidizas.",
            "direccion": "Oeste",
            "color": "Azul",
            "elemento": "Agua"
        },
        {
            "nahuatl": "Tochtli",
            "español": "Conejo",
            "glifo": "🐰",
            "simbolo": "⊕",
            "dios_patron": "Mayahuel",
            "dios_descripcion": "Diosa del Maguey y la Embriaguez",
            "significado": "Fertilidad, abundancia, exceso, embriaguez",
            "augurio": "Peligroso, asociado con el exceso",
            "personalidad": "Personas fértiles, abundantes, sociables. Tendencia a los excesos, especialmente alcohol. Pueden ser irresponsables.",
            "direccion": "Sur",
            "color": "Rojo/Púrpura",
            "elemento": "Fuego"
        },
        {
            "nahuatl": "Atl",
            "español": "Agua",
            "glifo": "💧",
            "simbolo": "≈",
            "dios_patron": "Xiuhtecuhtli",
            "dios_descripcion": "Señor del Fuego",
            "significado": "Fluir, emociones, purificación, dualidad",
            "augurio": "Neutro, fluido como el agua",
            "personalidad": "Personas emocionales, purificadoras, fluidas. Se adaptan como el agua. Pueden ser inestables emocionalmente.",
            "direccion": "Este",
            "color": "Turquesa/Verde agua",
            "elemento": "Agua"
        },
        {
            "nahuatl": "Itzcuintli",
            "español": "Perro",
            "glifo": "🐕",
            "simbolo": "⊗",
            "dios_patron": "Mictlantecuhtli",
            "dios_descripcion": "Señor de los Muertos",
            "significado": "Lealtad, guía espiritual, sexualidad, instinto",
            "augurio": "Variable, depende del contexto",
            "personalidad": "Personas leales, protectoras, con fuerte instinto. Guías naturales. Pueden ser obsesivas o celosas.",
            "direccion": "Norte",
            "color": "Rojo oscuro",
            "elemento": "Fuego/Tierra"
        },
        {
            "nahuatl": "Ozomatli",
            "español": "Mono",
            "glifo": "🐵",
            "simbolo": "◐",
            "dios_patron": "Xochipilli",
            "dios_descripcion": "Príncipe de las Flores",
            "significado": "Arte, alegría, juego, creatividad, exceso",
            "augurio": "Favorable para arte, peligroso para seriedad",
            "personalidad": "Personas artísticas, alegres, juguetonas. Grandes artistas pero pueden ser irresponsables o superficiales.",
            "direccion": "Oeste",
            "color": "Amarillo/Dorado",
            "elemento": "Aire"
        },
        {
            "nahuatl": "Malinalli",
            "español": "Hierba Torcida",
            "glifo": "🌿",
            "simbolo": "⚘",
            "dios_patron": "Patecatl",
            "dios_descripcion": "Señor de la Medicina",
            "significado": "Sanación, resistencia, flexibilidad, sacrificio",
            "augurio": "Desfavorable, requiere sacrificio",
            "personalidad": "Personas resilientes, sanadoras, flexibles. Sufren pero crecen. Pueden ser mártires o victimizarse.",
            "direccion": "Sur",
            "color": "Verde pasto",
            "elemento": "Tierra"
        },
        {
            "nahuatl": "Acatl",
            "español": "Caña/Carrizo",
            "glifo": "🎋",
            "simbolo": "⚏",
            "dios_patron": "Tezcatlipoca/Itztlacoliuhqui",
            "dios_descripcion": "Espejo Humeante",
            "significado": "Autoridad, dirección, liderazgo, rectitud",
            "augurio": "Muy favorable para líderes",
            "personalidad": "Personas autoritarias, directas, líderes naturales. Rectas y firmes. Pueden ser inflexibles o despóticas.",
            "direccion": "Este",
            "color": "Verde/Negro",
            "elemento": "Aire/Madera"
        },
        {
            "nahuatl": "Ocelotl",
            "español": "Jaguar/Ocelote",
            "glifo": "🐆",
            "simbolo": "◉",
            "dios_patron": "Tlazolteotl",
            "dios_descripcion": "Devoradora de Inmundicias",
            "significado": "Valor guerrero, noche, misterio, pasión",
            "augurio": "Poderoso para guerreros, peligroso para otros",
            "personalidad": "Personas valientes, misteriosas, apasionadas. Guerreros naturales. Pueden ser agresivas o destructivas.",
            "direccion": "Norte",
            "color": "Negro con manchas doradas",
            "elemento": "Tierra/Noche"
        },
        {
            "nahuatl": "Cuauhtli",
            "español": "Águila",
            "glifo": "🦅",
            "simbolo": "◈",
            "dios_patron": "Xipe Totec",
            "dios_descripcion": "Nuestro Señor el Desollado",
            "significado": "Visión superior, libertad, conexión con el sol",
            "augurio": "Muy favorable, especialmente para guerreros",
            "personalidad": "Personas visionarias, libres, nobles. Gran perspectiva. Pueden ser distantes o arrogantes.",
            "direccion": "Oeste",
            "color": "Azul cielo/Dorado",
            "elemento": "Aire/Fuego"
        },
        {
            "nahuatl": "Cozcacuauhtli",
            "español": "Buitre/Zopilote",
            "glifo": "🦅",
            "simbolo": "⊙",
            "dios_patron": "Itzpapalotl",
            "dios_descripcion": "Mariposa de Obsidiana",
            "significado": "Purificación, longevidad, sabiduría anciána",
            "augurio": "Favorable para ancianos, desfavorable para jóvenes",
            "personalidad": "Personas longevas, purificadoras, sabias. Ven lo esencial. Pueden parecer morbosas o negativas.",
            "direccion": "Sur",
            "color": "Rojo sangre",
            "elemento": "Aire/Muerte"
        },
        {
            "nahuatl": "Ollin",
            "español": "Movimiento/Temblor",
            "glifo": "🌀",
            "simbolo": "⊛",
            "dios_patron": "Xolotl",
            "dios_descripcion": "Gemelo de Quetzalcoatl",
            "significado": "Cambio constante, terremoto, transformación cósmica",
            "augurio": "Muy poderoso pero inestable",
            "personalidad": "Personas dinámicas, transformadoras, inquietas. Agentes de cambio. Pueden ser caóticas o destructivas.",
            "direccion": "Este",
            "color": "Todos los colores/Iridiscente",
            "elemento": "Todos/Movimiento puro"
        },
        {
            "nahuatl": "Tecpatl",
            "español": "Pedernal/Cuchillo",
            "glifo": "🔪",
            "simbolo": "⚔",
            "dios_patron": "Chalchiuhtotolin",
            "dios_descripcion": "Guajolote Precioso",
            "significado": "Sacrificio, corte quirúrgico, división, dolor necesario",
            "augurio": "Desfavorable, doloroso pero purificador",
            "personalidad": "Personas cortantes, decisivas, sacrificadas. Hacen cortes necesarios. Pueden ser crueles o hirientes.",
            "direccion": "Norte",
            "color": "Blanco/Plateado",
            "elemento": "Piedra/Metal"
        },
        {
            "nahuatl": "Quiauitl",
            "español": "Lluvia",
            "glifo": "🌧️",
            "simbolo": "☔",
            "dios_patron": "Tonatiuh",
            "dios_descripcion": "El Sol",
            "significado": "Renovación, fertilidad, bendición divina",
            "augurio": "Muy favorable, bendición del cielo",
            "personalidad": "Personas renovadoras, fértiles, bendecidas. Traen abundancia. Pueden ser abrumadoras o tormentosas.",
            "direccion": "Oeste",
            "color": "Azul lluvia/Plateado",
            "elemento": "Agua/Cielo"
        },
        {
            "nahuatl": "Xochitl",
            "español": "Flor",
            "glifo": "🌸",
            "simbolo": "✿",
            "dios_patron": "Xochiquetzal",
            "dios_descripcion": "Flor Preciosa Emplumada",
            "significado": "Belleza, arte, amor, placer, delicadeza",
            "augurio": "Muy favorable para amor y arte",
            "personalidad": "Personas bellas, artísticas, amorosas. Aprecian lo bello. Pueden ser vanidosas o superficiales.",
            "direccion": "Sur",
            "color": "Rosa/Multicolor",
            "elemento": "Aire/Flores"
        }
    ]
    
    # Los 4 portadores de año (signos que pueden ser años)
    PORTADORES_AÑO = ["Acatl", "Tecpatl", "Calli", "Tochtli"]
    
    def __init__(self, año_base=2024):
        """
        Inicializa el calendario azteca
        año_base: año gregoriano de referencia para cálculos
        """
        self.año_base = año_base
        # Fecha de inicio según correlación de Caso: 12 de febrero
        self.inicio_año_azteca = datetime(año_base, 2, 12)
        
    def es_bisiesto(self, año):
        """Verifica si un año gregoriano es bisiesto"""
        return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
    
    def dias_en_año(self, año):
        """Retorna el número de días en el año (365 o 366)"""
        return 366 if self.es_bisiesto(año) else 365
    
    def fecha_gregoriana_a_azteca(self, fecha_gregoriana):
        """
        Convierte una fecha gregoriana a fecha azteca
        Retorna un diccionario con información de ambos calendarios
        """
        # Determinar el año azteca al que pertenece la fecha
        año_greg = fecha_gregoriana.year
        
        # Si la fecha es antes del 12 de febrero, pertenece al año azteca anterior
        if fecha_gregoriana.month < 2 or (fecha_gregoriana.month == 2 and fecha_gregoriana.day < 12):
            año_azteca_actual = datetime(año_greg - 1, 2, 12)
            año_greg_para_calculo = año_greg - 1
        else:
            año_azteca_actual = datetime(año_greg, 2, 12)
            año_greg_para_calculo = año_greg
        
        # Normalizar las fechas para evitar problemas con zonas horarias
        fecha_greg_normalizada = datetime(fecha_gregoriana.year, fecha_gregoriana.month, fecha_gregoriana.day)
        año_azteca_normalizado = datetime(año_azteca_actual.year, año_azteca_actual.month, año_azteca_actual.day)
        
        dias_desde_inicio = (fecha_greg_normalizada - año_azteca_normalizado).days
        
        # Validar que dias_desde_inicio esté en el rango correcto
        if dias_desde_inicio < 0:
            # Retroceder un año azteca
            año_azteca_actual = datetime(año_greg - 1, 2, 12)
            año_greg_para_calculo = año_greg - 1
            año_azteca_normalizado = datetime(año_azteca_actual.year, año_azteca_actual.month, año_azteca_actual.day)
            dias_desde_inicio = (fecha_greg_normalizada - año_azteca_normalizado).days
        
        # XIUHPOHUALLI (365/366 días)
        xiuhpohualli = self._calcular_xiuhpohualli(dias_desde_inicio, año_greg_para_calculo)
        
        # TONALPOHUALLI (260 días - ciclo continuo)
        # Calculamos desde una fecha base conocida (asumimos que el 12 feb 2024 es 1-Cipactli)
        fecha_base_normalizada = datetime(2024, 2, 12)
        dias_totales_desde_base = (fecha_greg_normalizada - fecha_base_normalizada).days
        tonalpohualli = self._calcular_tonalpohualli(dias_totales_desde_base)
        
        # Calcular el año azteca (usando portadores de año)
        año_azteca = self._calcular_año_azteca(año_greg_para_calculo)
        
        return {
            'fecha_gregoriana': fecha_gregoriana.strftime('%d/%m/%Y'),
            'xiuhpohualli': xiuhpohualli,
            'tonalpohualli': tonalpohualli,
            'año_azteca': año_azteca,
            'dias_desde_inicio_año': dias_desde_inicio
        }
    
    def _calcular_xiuhpohualli(self, dias_desde_inicio, año):
        """Calcula la fecha en el Xiuhpohualli"""
        dias_en_año = self.dias_en_año(año)
        
        # Normalizar dias_desde_inicio para que esté dentro del rango del año
        dias_desde_inicio = dias_desde_inicio % dias_en_año
        
        # Cada mes tiene 20 días, son 18 meses = 360 días
        # Luego vienen los Nemontemi (5 días normales, 6 si es bisiesto)
        
        if dias_desde_inicio < 360:
            # Estamos en uno de los 18 meses
            mes_index = dias_desde_inicio // 20
            dia_del_mes = (dias_desde_inicio % 20) + 1
            
            return {
                'tipo': 'mes_regular',
                'mes': self.MESES_XIUHPOHUALLI[mes_index],
                'mes_numero': mes_index + 1,
                'dia': dia_del_mes,
                'representacion': f"Día {dia_del_mes} de {self.MESES_XIUHPOHUALLI[mes_index]}"
            }
        elif dias_desde_inicio < dias_en_año:
            # Estamos en los Nemontemi
            dia_nemontemi = dias_desde_inicio - 360 + 1
            dias_nemontemi = 6 if self.es_bisiesto(año) else 5
            
            return {
                'tipo': 'nemontemi',
                'mes': 'Nemontemi',
                'dia': dia_nemontemi,
                'total_nemontemi': dias_nemontemi,
                'representacion': f"Nemontemi día {dia_nemontemi} de {dias_nemontemi} (días aciagos)"
            }
        else:
            # El año ha terminado, nuevo año azteca (esto no debería ocurrir con la normalización)
            return {
                'tipo': 'nuevo_año',
                'mes': 'Nuevo Año',
                'representacion': 'Inicio del nuevo año azteca'
            }
    
    def _calcular_tonalpohualli(self, dias_totales):
        """Calcula la fecha en el Tonalpohualli (ciclo de 260 días)"""
        # El Tonalpohualli es un ciclo continuo de 260 días
        # Combina 13 números con 20 signos
        
        posicion_en_ciclo = dias_totales % 260
        
        # Número (del 1 al 13)
        numero = (posicion_en_ciclo % 13) + 1
        
        # Signo (de los 20 signos)
        signo_index = posicion_en_ciclo % 20
        signo_info = self.SIGNOS_TONALPOHUALLI[signo_index]
        
        # Calcular la trecena (grupo de 13 días)
        trecena = (posicion_en_ciclo // 13) + 1
        
        return {
            'numero': numero,
            'signo_nahuatl': signo_info['nahuatl'],
            'signo_español': signo_info['español'],
            'glifo': signo_info['glifo'],
            'simbolo': signo_info['simbolo'],
            'dios_patron': signo_info['dios_patron'],
            'dios_descripcion': signo_info['dios_descripcion'],
            'significado': signo_info['significado'],
            'augurio': signo_info['augurio'],
            'personalidad': signo_info['personalidad'],
            'direccion': signo_info['direccion'],
            'color': signo_info['color'],
            'elemento': signo_info['elemento'],
            'trecena': trecena,
            'dia_en_ciclo': posicion_en_ciclo + 1,
            'representacion': f"{numero}-{signo_info['nahuatl']}",
            'representacion_completa': f"{numero}-{signo_info['nahuatl']} ({signo_info['español']}) {signo_info['glifo']}"
        }
    
    def _calcular_año_azteca(self, año_gregoriano):
        """
        Calcula el nombre del año azteca usando los portadores de año
        Los portadores rotan: Acatl, Tecpatl, Calli, Tochtli
        """
        # Usamos una fecha base conocida y rotamos desde ahí
        # Asumimos que 2024 es un año "1-Acatl" (ajusta según necesites)
        años_desde_base = año_gregoriano - 2024
        
        # Ciclo de 52 años con 4 portadores rotando con 13 números
        posicion_en_ciclo = años_desde_base % 52
        
        # Determinar portador (rota cada año: Acatl → Tecpatl → Calli → Tochtli)
        portador_index = posicion_en_ciclo % 4
        portador = self.PORTADORES_AÑO[portador_index]
        
        # Determinar número (del 1 al 13, rota cada 13 años)
        numero = (posicion_en_ciclo % 13) + 1
        
        # Calcular posición en el ciclo de 52 años
        año_en_ciclo_52 = posicion_en_ciclo + 1
        
        return {
            'numero': numero,
            'portador': portador,
            'año_en_ciclo_52': año_en_ciclo_52,
            'representacion': f"{numero}-{portador}"
        }
    
    def generar_año_completo(self, año_gregoriano=None):
        """
        Genera el calendario azteca completo para un año
        """
        if año_gregoriano is None:
            año_gregoriano = self.año_base
        
        inicio = datetime(año_gregoriano, 2, 12)
        dias_en_año = self.dias_en_año(año_gregoriano)
        
        calendario_completo = []
        
        for i in range(dias_en_año):
            fecha_actual = inicio + timedelta(days=i)
            fecha_azteca = self.fecha_gregoriana_a_azteca(fecha_actual)
            calendario_completo.append(fecha_azteca)
        
        return calendario_completo
    
    def mostrar_fecha(self, fecha_gregoriana):
        """Muestra una fecha azteca de forma legible con toda la información"""
        resultado = self.fecha_gregoriana_a_azteca(fecha_gregoriana)
        
        print("=" * 90)
        print(f"FECHA GREGORIANA: {resultado['fecha_gregoriana']}")
        print("=" * 90)
        
        print(f"\n📅 AÑO AZTECA: {resultado['año_azteca']['representacion']}")
        print(f"   (Año {resultado['año_azteca']['año_en_ciclo_52']} del ciclo de 52 años)")
        
        print(f"\n☀️  XIUHPOHUALLI (Calendario Solar - 365 días):")
        print(f"   {resultado['xiuhpohualli']['representacion']}")
        
        print(f"\n🌙 TŌNALPŌHUALLI (Calendario Sagrado - 260 días):")
        print(f"   Náhuatl:     {resultado['tonalpohualli']['representacion']}")
        print(f"   Español:     {resultado['tonalpohualli']['numero']}-{resultado['tonalpohualli']['signo_español']}")
        print(f"   Glifo:       {resultado['tonalpohualli']['glifo']} {resultado['tonalpohualli']['simbolo']}")
        print(f"   Trecena:     {resultado['tonalpohualli']['trecena']} de 20")
        print(f"   Día:         {resultado['tonalpohualli']['dia_en_ciclo']} de 260")
        
        print(f"\n🎭 INFORMACIÓN ASTROLÓGICA:")
        print(f"   Dios Patrón:    {resultado['tonalpohualli']['dios_patron']} ({resultado['tonalpohualli']['dios_descripcion']})")
        print(f"   Significado:    {resultado['tonalpohualli']['significado']}")
        print(f"   Augurio:        {resultado['tonalpohualli']['augurio']}")
        print(f"   Dirección:      {resultado['tonalpohualli']['direccion']}")
        print(f"   Color:          {resultado['tonalpohualli']['color']}")
        print(f"   Elemento:       {resultado['tonalpohualli']['elemento']}")
        
        print(f"\n👤 PERSONALIDAD (para nacidos en este día):")
        print(f"   {resultado['tonalpohualli']['personalidad']}")
        
        print("=" * 90)
    
    def mostrar_signo_completo(self, nombre_signo):
        """Muestra información completa de un signo específico"""
        signo = None
        for s in self.SIGNOS_TONALPOHUALLI:
            if s['nahuatl'].lower() == nombre_signo.lower() or s['español'].lower() == nombre_signo.lower():
                signo = s
                break
        
        if not signo:
            print(f"No se encontró el signo: {nombre_signo}")
            return
        
        print("=" * 90)
        print(f"SIGNO: {signo['nahuatl']} ({signo['español']}) {signo['glifo']}")
        print("=" * 90)
        print(f"\n🎭 Dios Patrón:")
        print(f"   {signo['dios_patron']} - {signo['dios_descripcion']}")
        print(f"\n📜 Significado:")
        print(f"   {signo['significado']}")
        print(f"\n🔮 Augurio:")
        print(f"   {signo['augurio']}")
        print(f"\n🧭 Correspondencias:")
        print(f"   Dirección: {signo['direccion']}")
        print(f"   Color:     {signo['color']}")
        print(f"   Elemento:  {signo['elemento']}")
        print(f"\n👤 Personalidad:")
        print(f"   {signo['personalidad']}")
        print("=" * 90)


# EJEMPLOS DE USO
if __name__ == "__main__":
    # Crear el calendario
    calendario = CalendarioAzteca()
    
    # Ejemplo 1: Fecha de hoy (fecha actual)
    print("\n### FECHA DE HOY COMPLETA ###")
    hoy = datetime.now()  # Usar la fecha actual en lugar de una fecha hardcodeada
    calendario.mostrar_fecha(hoy)
    
    # Ejemplo 2: Inicio del año azteca (12 de febrero del año actual)
    print("\n\n### INICIO DEL AÑO AZTECA ###")
    año_actual = datetime.now().year
    inicio_año = datetime(año_actual, 2, 12)
    calendario.mostrar_fecha(inicio_año)
    
    # Ejemplo 3: Información de un signo específico
    print("\n\n### INFORMACIÓN COMPLETA DEL SIGNO CIPACTLI ###")
    calendario.mostrar_signo_completo("Cipactli")
    
    # Ejemplo 4: Información de otro signo
    print("\n\n### INFORMACIÓN COMPLETA DEL SIGNO CUAUHTLI (ÁGUILA) ###")
    calendario.mostrar_signo_completo("Cuauhtli")
    
    # Ejemplo 5: Secuencia de días con información básica
    print("\n\n### SECUENCIA DE 10 DÍAS DESDE HOY ###")
    print("-" * 120)
    print(f"{'Fecha':12} | {'Xiuhpohualli':30} | {'Tonalpohualli':25} | {'Dios Patrón':25} | {'Augurio':20}")
    print("-" * 120)
    for i in range(10):
        fecha = hoy + timedelta(days=i)
        resultado = calendario.fecha_gregoriana_a_azteca(fecha)
        print(f"{resultado['fecha_gregoriana']:12} | "
              f"{resultado['xiuhpohualli']['representacion'][:30]:30} | "
              f"{resultado['tonalpohualli']['representacion']:25} | "
              f"{resultado['tonalpohualli']['dios_patron'][:25]:25} | "
              f"{resultado['tonalpohualli']['augurio'][:20]:20}")
    
    # Ejemplo 6: Tabla completa de los 20 signos
    print("\n\n### LOS 20 SIGNOS DEL TŌNALPŌHUALLI - INFORMACIÓN COMPLETA ###")
    print("-" * 120)
    print(f"{'#':3} | {'Náhuatl':16} | {'Español':20} | {'Glifo':6} | {'Dios Patrón':25} | {'Elemento':15}")
    print("-" * 120)
    for i, signo in enumerate(calendario.SIGNOS_TONALPOHUALLI, 1):
        print(f"{i:3} | {signo['nahuatl']:16} | {signo['español']:20} | "
              f"{signo['glifo']:6} | {signo['dios_patron'][:25]:25} | {signo['elemento']:15}")
    
    # Ejemplo 7: Fechas importantes del calendario
    print("\n\n### INICIO DE CADA MES DEL XIUHPOHUALLI 2025 ###")
    print("-" * 120)
    print(f"{'Mes (Náhuatl)':22} | {'Fecha Greg.':12} | {'Tonalpohualli':30} | {'Dirección':12} | {'Color':15}")
    print("-" * 120)
    inicio = datetime(2025, 2, 12)
    for i, mes_nombre in enumerate(calendario.MESES_XIUHPOHUALLI):
        fecha_mes = inicio + timedelta(days=i*20)
        resultado = calendario.fecha_gregoriana_a_azteca(fecha_mes)
        print(f"{mes_nombre:22} | "
              f"{resultado['fecha_gregoriana']:12} | "
              f"{resultado['tonalpohualli']['representacion_completa'][:30]:30} | "
              f"{resultado['tonalpohualli']['direccion']:12} | "
              f"{resultado['tonalpohualli']['color']:15}")
    
    # Mostrar Nemontemi
    nemontemi_fecha = inicio + timedelta(days=360)
    resultado_nem = calendario.fecha_gregoriana_a_azteca(nemontemi_fecha)
    print(f"{'Nemontemi (aciagos)':22} | "
          f"{nemontemi_fecha.strftime('%d/%m/%Y'):12} | "
          f"{resultado_nem['tonalpohualli']['representacion_completa'][:30]:30}")
    
    # Ejemplo 8: Búsqueda de días favorables
    print("\n\n### DÍAS MUY FAVORABLES EN LOS PRÓXIMOS 30 DÍAS ###")
    print("-" * 100)
    print(f"{'Fecha':12} | {'Tonalpohualli':30} | {'Augurio':30} | {'Significado':25}")
    print("-" * 100)
    for i in range(30):
        fecha = hoy + timedelta(days=i)
        resultado = calendario.fecha_gregoriana_a_azteca(fecha)
        augurio = resultado['tonalpohualli']['augurio']
        if 'favorable' in augurio.lower() and 'desfavorable' not in augurio.lower():
            print(f"{resultado['fecha_gregoriana']:12} | "
                  f"{resultado['tonalpohualli']['representacion_completa'][:30]:30} | "
                  f"{augurio[:30]:30} | "
                  f"{resultado['tonalpohualli']['significado'][:25]:25}")
    
    # Ejemplo 9: Ejemplo de lectura de personalidad por fecha de nacimiento
    print("\n\n### EJEMPLO: LECTURA DE PERSONALIDAD POR FECHA DE NACIMIENTO ###")
    fecha_nacimiento = datetime(1990, 5, 15)
    print(f"\nFecha de nacimiento: {fecha_nacimiento.strftime('%d/%m/%Y')}")
    print("-" * 90)
    calendario.mostrar_fecha(fecha_nacimiento)
    
    # Ejemplo 10: Mostrar direcciones cardinales y elementos
    print("\n\n### DISTRIBUCIÓN DE SIGNOS POR DIRECCIÓN CARDINAL ###")
    print("-" * 90)
    direcciones = {}
    for signo in calendario.SIGNOS_TONALPOHUALLI:
        dir = signo['direccion']
        if dir not in direcciones:
            direcciones[dir] = []
        direcciones[dir].append(f"{signo['glifo']} {signo['nahuatl']}")
    
    for direccion, signos in sorted(direcciones.items()):
        print(f"\n🧭 {direccion}:")
        for signo in signos:
            print(f"   {signo}")
    
    print("\n\n### DISTRIBUCIÓN DE SIGNOS POR ELEMENTO ###")
    print("-" * 90)
    elementos = {}
    for signo in calendario.SIGNOS_TONALPOHUALLI:
        elem = signo['elemento']
        if elem not in elementos:
            elementos[elem] = []
        elementos[elem].append(f"{signo['glifo']} {signo['nahuatl']}")
    
    for elemento, signos in sorted(elementos.items()):
        print(f"\n🌟 {elemento}:")
        for signo in signos:
            print(f"   {signo}")