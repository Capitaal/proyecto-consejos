from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import random
import os
import httpx


app = FastAPI()

#SE ECHA A ANDAR CON python -m uvicorn api_consejos:app --reload

# Lista de 100+ consejos filosóficos
consejos = [
    "Conócete a ti mismo. – Sócrates",
    "La vida no examinada no vale la pena vivirla. – Sócrates",
    "Pienso, luego existo. – Descartes",
    "La libertad es la obediencia a la ley que uno se ha trazado para sí mismo. – Rousseau",
    "El hombre está condenado a ser libre. – Sartre",
    "El deseo es la esencia del hombre. – Spinoza",
    "Lo que no me mata, me hace más fuerte. – Nietzsche",
    "El tiempo es la imagen móvil de la eternidad. – Platón",
    "Sólo sé que no sé nada. – Sócrates",
    "La felicidad depende de uno mismo. – Aristóteles",
    "La esperanza es el sueño del hombre despierto. – Aristóteles",
    "El hombre es la medida de todas las cosas. – Protágoras",
    "La vida es voluntad de poder. – Nietzsche",
    "No hay nada bueno ni malo, el pensamiento lo hace así. – Shakespeare",
    "Dios ha muerto. – Nietzsche",
    "La existencia precede a la esencia. – Sartre",
    "El infierno son los otros. – Sartre",
    "Vivimos en el mejor de los mundos posibles. – Leibniz",
    "El alma nunca piensa sin una imagen. – Aristóteles",
    "No hay hechos, sólo interpretaciones. – Nietzsche",
    "El conocimiento es poder. – Francis Bacon",
    "La mente es todo. En lo que piensas, te conviertes. – Buda",
    "Quien tiene un porqué para vivir puede soportar casi cualquier cómo. – Nietzsche",
    "El arte de ser sabio es el arte de saber qué pasar por alto. – William James",
    "La vida es como una obra de teatro: no es la duración sino la calidad lo que importa. – Séneca",
    "No hay camino hacia la felicidad, la felicidad es el camino. – Lao-Tse",
    "La filosofía es un combate contra el embrujo de nuestra inteligencia por el lenguaje. – Wittgenstein",
    "La razón no es la fuente del conocimiento, sino su límite. – Kant",
    "Somos lo que hacemos repetidamente. – Aristóteles",
    "Nadie puede herirte sin tu consentimiento. – Eleanor Roosevelt",
    "El sabio no dice todo lo que piensa, pero siempre piensa todo lo que dice. – Aristóteles",
    "No vemos las cosas como son, las vemos como somos. – Talmud",
    "Aquel que tiene imaginación, con qué facilidad saca de la nada un mundo. – Gustavo Adolfo Bécquer",
    "No se puede enseñar nada a un hombre; sólo se le puede ayudar a encontrar la respuesta dentro de sí mismo. – Galileo Galilei",
    "La educación es el encendido de una llama, no el llenado de un recipiente. – Plutarco",
    "La vida es breve, el arte largo, la ocasión fugaz, la experiencia engañosa, el juicio difícil. – Hipócrates",
    "El objetivo de la vida es la autorrealización. – Carl Jung",
    "El primer paso hacia la sabiduría es el silencio. – Pitágoras",
    "Quien no comprende una mirada, tampoco comprenderá una larga explicación. – Proverbio árabe",
    "Nada es permanente, excepto el cambio. – Heráclito",
    "El sabio puede cambiar de opinión. El necio, nunca. – Kant",
    "Tu visión se aclarará solamente cuando mires dentro de tu corazón. – Carl Jung",
    "Prefiero ser un hombre de paradojas que un hombre de prejuicios. – Rousseau",
    "Todo lo que escuchamos es una opinión, no un hecho. Todo lo que vemos es una perspectiva, no la verdad. – Marco Aurelio",
    "El conocimiento de uno mismo es el principio de toda sabiduría. – Aristóteles",
    "Donde hay amor, hay vida. – Mahatma Gandhi",
    "El alma se tiñe del color de sus pensamientos. – Marco Aurelio",
    "No busques el sentido de la vida. Da sentido a tu vida. – Viktor Frankl",
    "Aquel que tiene fe no necesita explicación; aquel que no la tiene, no la entenderá. – Tomás de Aquino",
    "La medida de la inteligencia es la capacidad de cambiar. – Einstein",
    # Añade más aquí si deseas...
]

# 🖼️ Lista de imágenes subidas a GitHub
imagenes = [
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/dog-9578735_1280.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/irish-setter-8203155_1280.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/mark-basarab-z8ct_Q3oCqM-unsplash.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/michael-DXQB5D1njMY-unsplash.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-14539927.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-14548786.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-30257381.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-32024499.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-32073454.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-32104960.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-32117735.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-32146385.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-042896ec25-32146401.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-alesiakozik-6023546.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-charlesdeluvio-1851164.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-cristian-villanueva-230972756-12106782.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-diesgomo-14596489.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-1699020.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-2098427.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-28765354.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-28871323.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-28871326.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-28871391.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-29006818.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-29325582.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-29358117.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-29404650.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-30060644.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-31595222.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-31612187.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-31612217.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-31612221.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-31612222.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-31979794.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-eberhardgross-826376.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31692408.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31722862.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31730032.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31785363.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31843955.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31843958.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31844470.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31861850.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31942114.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31957656.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-31975533.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32037340.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32059902.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32061462.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32078499.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32105399.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32126109.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-efrem-efre-2786187-32129618.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-fede-roveda-1461538-3600569.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-fotios-photos-1055068.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/LOTE1/pexels-fotios-photos-2873895.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-042896ec25-31828024.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-andre-ulysses-de-salis-2100065-3739624.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-eberhardgross-28871315.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-eberhardgross-29985442.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-efrem-efre-2786187-31678604.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-efrem-efre-2786187-31860472.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-efrem-efre-2786187-32075083.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-george-desipris-792381.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-jens-johnsson-14223-66092.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-laurathexplaura-3608263.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-leonardo-merlo-1124828-2124401.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-lukas-hartmann-304281-1624735.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-magdalenasukova-1535049.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-marek-piwnicki-3907296-25067987.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-marek-piwnicki-3907296-26755207.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-marek-piwnicki-3907296-29008783.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-marek-piwnicki-3907296-29451002.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-markb-106686.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mauroignaciotorres-17052535.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mauroignaciotorres-19724557.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mikebirdy-17417870.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mikebirdy-17590508.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mikebirdy-18054709.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mikebirdy-18404825.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mikebirdy-18671678.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mikebirdy-30735047.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-mohan-reddy-1263154-4388593.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-neale-lasalle-197020-631477.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-nien-tran-dinh-788736-1654748.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-osmanarabaciart-31494442.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-208821.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-258101.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-302304.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-50577.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-53153.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-54081.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-60023.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-pixabay-64287.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-rick98-3428278.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-rodrigo-a-36100054-12935282.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-rodrigo-a-36100054-14656946.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-rodrigo-a-36100054-14802257.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-sarmad-mughal-94606-305070.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-sascha-thiele-221815-747016.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-semws-2670898.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-shvetsa-4588065.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-tdcat-59523.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-tdcat-70912.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-thais-cordeiro-2213281-3874262.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-tobiasbjorkli-1819650.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-todd-trapani-488382-1405930.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-ton-souza-4613395.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-ton-souza-4613600.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-untal3d-23158189.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-vedran-miletic-1215404-2313396.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/pexels-william-jesus-casique-toro-110679-2744227.jpg",
  "https://raw.githubusercontent.com/Capitaal/api-consejos-imagenes/main/imagenes/lote2/tim-stief-YFFGkE3y4F8-unsplash.jpg",
]

# 🎨 Generador de color aleatorio
def generar_color_hex():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


# 📦 Ruta de API para obtener consejo, color y foto válida
@app.get("/consejo")
async def obtener_consejo():
    consejo = random.choice(consejos)
    color = generar_color_hex()

    imagen = ""
    for _ in range(5):  # Intenta máximo 5 veces
        posible = random.choice(imagenes)
        try:
            async with httpx.AsyncClient() as client:
                response = await client.head(posible)
                if response.status_code == 200:
                    imagen = posible
                    break
        except httpx.RequestError:
            continue

    return JSONResponse({
        "consejo": consejo,
        "color": color,
        "imagen": imagen
    })

# 🧩 Favicon para evitar error 404
@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")

# 🏠 Servir la página HTML principal
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")