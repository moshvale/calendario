// Datos del calendario azteca (extraídos del código Python)
const SIGNOS_TONALPOHUALLI = [
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
];

// Meses del Xiuhpohualli
const MESES_XIUHPOHUALLI = [
    "Atlcahualo",          // 1
    "Tlacaxipehualiztli",  // 2
    "Tozoztontli",         // 3
    "Huey Tozoztli",       // 4
    "Toxcatl",             // 5
    "Etzalcualiztli",      // 6
    "Tecuilhuitontli",     // 7
    "Huey Tecuilhuitl",    // 8
    "Tlaxochimaco",        // 9
    "Xocotl Huetzi",       // 10
    "Ochpaniztli",         // 11
    "Teotleco",            // 12
    "Tepeilhuitl",         // 13
    "Quecholli",           // 14
    "Panquetzaliztli",     // 15
    "Atemoztli",           // 16
    "Tititl",              // 17
    "Izcalli"              // 18
];

// Portadores de año
const PORTADORES_AÑO = ["Acatl", "Tecpatl", "Calli", "Tochtli"];

// Elementos del DOM
const fechaInput = document.getElementById('fecha');
const calcularBtn = document.getElementById('calcular');
const hoyBtn = document.getElementById('hoy');
const resultadosDiv = document.getElementById('resultados');
const loadingDiv = document.getElementById('loading');
const errorDiv = document.getElementById('error');
const fechaGregorianaElem = document.getElementById('fecha-gregoriana');
const añoAztecaElem = document.getElementById('año-azteca');
const xiuhpohualliElem = document.getElementById('xiuhpohualli');
const tonalpohualliElem = document.getElementById('tonalpohualli');
const infoSignoElem = document.getElementById('info-signo');

// Añadir elementos decorativos
function addDecorativeElements() {
    const body = document.body;
    
    // Crear elemento de decoración izquierda
    const leftDecoration = document.createElement('div');
    leftDecoration.className = 'decoration-left';
    body.appendChild(leftDecoration);
    
    // Crear elemento de decoración derecha
    const rightDecoration = document.createElement('div');
    rightDecoration.className = 'decoration-right';
    body.appendChild(rightDecoration);
}

// Inicializar el banner dinámico de signos (UN SOLO SIGNO POR TURNO)
function inicializarBannerSignos() {
    const bannerContainer = document.getElementById('signos-banner-container');
    if (!bannerContainer) return;
    
    // Crear estructura del banner
    bannerContainer.innerHTML = `
        <h2 class="banner-title">📋 Los 20 Signos del Tonalpohualli</h2>
        <div class="banner-controls">
            <button class="banner-btn" id="banner-prev">← Anterior</button>
            <button class="banner-btn" id="banner-play">▶ Auto</button>
            <button class="banner-btn" id="banner-next">Siguiente →</button>
        </div>
        <div class="banner-content" id="banner-content">
            <!-- Las diapositivas se generarán dinámicamente -->
        </div>
        <div class="banner-indicators" id="banner-indicators">
            <!-- Los indicadores se generarán dinámicamente -->
        </div>
    `;
    
    // Generar diapositivas (UN SOLO SIGNO POR DIAPOSITIVA)
    const signosPorSlide = 1; // CAMBIO: Ahora solo 1 signo por diapositiva
    const totalSlides = SIGNOS_TONALPOHUALLI.length; // 20 diapositivas en total
    const bannerContent = document.getElementById('banner-content');
    const indicatorsContainer = document.getElementById('banner-indicators');
    
    for (let i = 0; i < totalSlides; i++) {
        const signo = SIGNOS_TONALPOHUALLI[i];
        
        // Crear tarjeta para este signo individual
        const slideDiv = document.createElement('div');
        slideDiv.className = `banner-slide ${i === 0 ? 'active' : ''}`;
        slideDiv.innerHTML = `
            <div class="signo-card">
                <div class="signo-header">
                    <div class="signo-glyph">${signo.glifo}</div>
                    <div class="signo-number">${i + 1}</div>
                </div>
                <div class="signo-main">
                    <h3 class="signo-name">${signo.nahuatl}</h3>
                    <p class="signo-spanish">${signo.español}</p>
                </div>
                <div class="signo-details">
                    <div class="detail-row">
                        <span class="detail-label">Dios:</span>
                        <span class="detail-value">${signo.dios_patron}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Elemento:</span>
                        <span class="detail-value">${signo.elemento}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Dirección:</span>
                        <span class="detail-value">${signo.direccion}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Color:</span>
                        <span class="detail-value">${signo.color}</span>
                    </div>
                </div>
            </div>
        `;
        bannerContent.appendChild(slideDiv);
        
        // Crear indicador
        const indicator = document.createElement('div');
        indicator.className = `indicator ${i === 0 ? 'active' : ''}`;
        indicator.dataset.slide = i;
        indicatorsContainer.appendChild(indicator);
    }
    
    // Configurar controles
    let currentSlide = 0;
    let autoPlayInterval = null;
    const slides = document.querySelectorAll('.banner-slide');
    const indicators = document.querySelectorAll('.indicator');
    
    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove('active'));
        indicators.forEach(indicator => indicator.classList.remove('active'));
        
        slides[index].classList.add('active');
        indicators[index].classList.add('active');
        currentSlide = index;
    }
    
    function nextSlide() {
        const nextIndex = (currentSlide + 1) % slides.length;
        showSlide(nextIndex);
    }
    
    function prevSlide() {
        const prevIndex = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(prevIndex);
    }
    
    function toggleAutoPlay() {
        const playBtn = document.getElementById('banner-play');
        if (autoPlayInterval) {
            clearInterval(autoPlayInterval);
            autoPlayInterval = null;
            playBtn.textContent = '▶ Auto';
            playBtn.classList.remove('active');
        } else {
            autoPlayInterval = setInterval(nextSlide, 3000);
            playBtn.textContent = '⏸ Pausar';
            playBtn.classList.add('active');
        }
    }
    
    // Event listeners
    document.getElementById('banner-prev').addEventListener('click', () => {
        prevSlide();
        if (autoPlayInterval) {
            clearInterval(autoPlayInterval);
            autoPlayInterval = setInterval(nextSlide, 3000);
        }
    });
    
    document.getElementById('banner-next').addEventListener('click', () => {
        nextSlide();
        if (autoPlayInterval) {
            clearInterval(autoPlayInterval);
            autoPlayInterval = setInterval(nextSlide, 3000);
        }
    });
    
    document.getElementById('banner-play').addEventListener('click', toggleAutoPlay);
    
    // Event listeners para indicadores
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            showSlide(index);
            if (autoPlayInterval) {
                clearInterval(autoPlayInterval);
                autoPlayInterval = setInterval(nextSlide, 3000);
            }
        });
    });
    
    // Iniciar autoplay automáticamente
    toggleAutoPlay();
}

// Verificar si un año es bisiesto
function esBisiesto(año) {
    return año % 4 === 0 && (año % 100 !== 0 || año % 400 === 0);
}

function calcularFechaAzteca(fecha) {
    try {
        // Mostrar indicador de carga
        loadingDiv.style.display = 'block';
        errorDiv.style.display = 'none';
        
        // Parsear la fecha en formato YYYY-MM-DD y crear un objeto Date sin componentes de tiempo
        const partesFecha = fecha.split('-');
        const año = parseInt(partesFecha[0]);
        const mes = parseInt(partesFecha[1]) - 1; // Los meses en JavaScript son 0-11
        const dia = parseInt(partesFecha[2]);
        
        const fechaObj = new Date(año, mes, dia);
        if (isNaN(fechaObj.getTime())) {
            throw new Error('Fecha inválida');
        }
        
        // Formatear fecha gregoriana
        const opciones = { year: 'numeric', month: 'long', day: 'numeric' };
        const fechaGregoriana = fechaObj.toLocaleDateString('es-ES', opciones);
        
        // Determinar el año azteca según la correlación de Caso (12 de febrero)
        let añoAztecaBase;
        let añoParaCalculo;
        
        if (mes < 1 || (mes === 1 && dia < 12)) { // mes+1 < 2
            añoAztecaBase = new Date(año - 1, 1, 12); // 12 de febrero del año anterior
            añoParaCalculo = año - 1;
        } else {
            añoAztecaBase = new Date(año, 1, 12); // 12 de febrero del mismo año
            añoParaCalculo = año;
        }
        
        // Calcular días desde el inicio del año azteca
        const unDiaEnMs = 1000 * 60 * 60 * 24;
        const diasDesdeInicio = Math.floor((fechaObj - añoAztecaBase) / unDiaEnMs);
        
        return calcularConDias(diasDesdeInicio, añoParaCalculo, fechaGregoriana);
    } catch (error) {
        mostrarError('Error al calcular la fecha: ' + error.message);
        return null;
    }
}

// Función auxiliar para calcular con días ya determinados
function calcularConDias(diasDesdeInicio, año, fechaGregoriana) {
    const diasEnAño = esBisiesto(año) ? 366 : 365;
    let xiuhpohualli;
    
    if (diasDesdeInicio < 360) {
        const mesIndex = Math.floor(diasDesdeInicio / 20);
        const diaDelMes = (diasDesdeInicio % 20) + 1;
        xiuhpohualli = `Día ${diaDelMes} de ${MESES_XIUHPOHUALLI[mesIndex]}`;
    } else {
        const diaNemontemi = diasDesdeInicio - 360 + 1;
        const diasNemontemi = esBisiesto(año) ? 6 : 5;
        xiuhpohualli = `Nemontemi día ${diaNemontemi} de ${diasNemontemi} (días aciagos)`;
    }
    
    // TONALPOHUALLI (calendario sagrado - ciclo de 260 días)
    // Fecha base conocida: 12 de febrero de 2024 = 1-Cipactli
    const fechaBase = new Date(2024, 1, 12); // 12 de febrero de 2024
    
    // Calcular la fecha actual sumando los días desde el inicio del año azteca
    const fechaActual = new Date(año, 1, 12); // 12 de febrero del año actual
    fechaActual.setDate(fechaActual.getDate() + diasDesdeInicio);
    
    const unDiaEnMs = 1000 * 60 * 60 * 24;
    const diasTotalesDesdeBase = Math.floor((fechaActual - fechaBase) / unDiaEnMs);
    const posicionEnCiclo = ((diasTotalesDesdeBase % 260) + 260) % 260; // Asegurar valor positivo
    
    const numero = (posicionEnCiclo % 13) + 1;
    const signoIndex = posicionEnCiclo % 20;
    const signo = SIGNOS_TONALPOHUALLI[signoIndex];
    const tonalpohualli = `${numero}-${signo.nahuatl} (${signo.español}) ${signo.glifo}`;
    
    // AÑO AZTECA
    const añosDesdeBase = año - 2024;
    const posicionEnCicloAño = ((añosDesdeBase % 52) + 52) % 52; // Asegurar valor positivo
    const portadorIndex = posicionEnCicloAño % 4;
    const portador = PORTADORES_AÑO[portadorIndex];
    const numeroAño = (posicionEnCicloAño % 13) + 1;
    const añoAzteca = `${numeroAño}-${portador}`;
    const añoEnCiclo = posicionEnCicloAño + 1;
    
    // Ocultar indicador de carga
    loadingDiv.style.display = 'none';
    
    return {
        fechaGregoriana: fechaGregoriana,
        añoAzteca: `${añoAzteca} (Año ${añoEnCiclo} del ciclo de 52 años)`,
        xiuhpohualli: xiuhpohualli,
        tonalpohualli: tonalpohualli,
        signo: signo,
        numero: numero,
        diaEnCiclo: posicionEnCiclo + 1,
        trecena: Math.floor(posicionEnCiclo / 13) + 1
    };
}

// Mostrar resultados - MODIFICADO
function mostrarResultados(resultado) {
    if (!resultado) return;
    
    fechaGregorianaElem.textContent = resultado.fechaGregoriana;
    añoAztecaElem.textContent = resultado.añoAzteca;
    xiuhpohualliElem.textContent = resultado.xiuhpohualli;
    tonalpohualliElem.textContent = `${resultado.tonalpohualli} - Trecena ${resultado.trecena} de 20 - Día ${resultado.diaEnCiclo} de 260`;
    
    // Mostrar información del signo con estructura modificada
    const signo = resultado.signo;
    infoSignoElem.innerHTML = `
        <div class="info-item">
            <span class="info-label">Dios Patrón:</span>
            <span class="info-value">${signo.dios_patron} (${signo.dios_descripcion})</span>
        </div>
        <div class="info-item">
            <span class="info-label">Significado:</span>
            <span class="info-value">${signo.significado}</span>
        </div>
        <div class="info-item">
            <span class="info-label">Augurio:</span>
            <span class="info-value">${signo.augurio}</span>
        </div>
        <div class="info-item">
            <span class="info-label">Dirección:</span>
            <span class="info-value">${signo.direccion}</span>
        </div>
        <div class="info-item">
            <span class="info-label">Color:</span>
            <span class="info-value">${signo.color}</span>
        </div>
        <div class="info-item">
            <span class="info-label">Elemento:</span>
            <span class="info-value">${signo.elemento}</span>
        </div>
        <div class="info-item personality">
            <div>
                <span class="info-label">Personalidad:</span>
            </div>
            <span class="info-value">${signo.personalidad}</span>
        </div>
    `;
    
    resultadosDiv.style.display = 'block';
}

// Mostrar error
function mostrarError(mensaje) {
    loadingDiv.style.display = 'none';
    errorDiv.textContent = mensaje;
    errorDiv.style.display = 'block';
}

// Establecer fecha de hoy en el input
function establecerFechaHoy() {
    const hoy = new Date();
    // Ajustar para obtener la fecha local correcta
    const año = hoy.getFullYear();
    const mes = String(hoy.getMonth() + 1).padStart(2, '0');
    const dia = String(hoy.getDate()).padStart(2, '0');
    const fechaHoy = `${año}-${mes}-${dia}`;
    fechaInput.value = fechaHoy;
    return fechaHoy;
}

// Event Listeners
calcularBtn.addEventListener('click', () => {
    const fecha = fechaInput.value;
    if (fecha) {
        const resultado = calcularFechaAzteca(fecha);
        mostrarResultados(resultado);
    } else {
        mostrarError('Por favor, selecciona una fecha');
    }
});

hoyBtn.addEventListener('click', () => {
    const fechaHoy = establecerFechaHoy();
    const resultado = calcularFechaAzteca(fechaHoy);
    mostrarResultados(resultado);
});

// Inicializar la página
document.addEventListener('DOMContentLoaded', () => {
    addDecorativeElements();
    
    // Inicializar banner de signos con un solo signo por turno
    inicializarBannerSignos();
    
    // Establecer y calcular la fecha de hoy por defecto
    const fechaHoy = establecerFechaHoy();
    const resultado = calcularFechaAzteca(fechaHoy);
    mostrarResultados(resultado);
});