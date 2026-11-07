# El collar bomba

Página web educativa sobre el caso del collar bomba de Chiquinquirá (Boyacá), ocurrido el 15 de mayo de 2000, en el que murieron la campesina Elvia Cortés y el técnico antiexplosivos de la Policía Jairo Hernando López.

**Página publicada:** https://collar-bomba-usta.web.app

## Autores

- Juan Diego Velasco
- Juan Esteban Herrera
- Jhonatan Gil

Filosofía Política · Universidad Santo Tomás, Seccional Tunja · 2026

## Contenido de la página

- Un carrusel de fotos con el que empieza la historia.
- La cronología del día, hora por hora, desde las 4:00 a. m. hasta las 3:00 p. m.
- Un simulador ficticio, con cuatro collares y cuatro niveles de dificultad, que transmite la presión de aquel día sin enseñar nada sobre explosivos reales.
- Lo que pasó después: la acusación equivocada a las FARC y la conclusión de la justicia.
- Las fuentes consultadas, las diferencias entre ellas y el crédito de cada fotografía.

Al fondo hay un paisaje dibujado del altiplano boyacense, y el cielo cambia con la hora de cada sección.

## Estructura

| Archivo | Para qué sirve |
| --- | --- |
| `public/index.html` | La página completa: HTML, CSS y JavaScript en un solo archivo |
| `public/img/` | Las fotografías del carrusel |
| `app.py` | Servidor Flask para ver la página en el computador |
| `firebase.json`, `.firebaserc` | Configuración de Firebase Hosting |

## Verla en el computador

```bash
py -m pip install -r requirements.txt
py app.py
```

Luego se abre http://127.0.0.1:5000 en el navegador.

## Publicarla

Con la [CLI de Firebase](https://firebase.google.com/docs/cli) instalada y la sesión iniciada:

```bash
firebase deploy --only hosting
```

## Fuentes

- Associated Press, despacho desde Chiquinquirá, 15 de mayo de 2000.
- Tim Johnson, «They were waiting for her», *The Miami Herald*, 12 de junio de 2000.
- La Silla Vacía, «Collar bomba: la justicia probó que fueron delincuentes comunes, no las Farc».
- *Vanguardia*, «El collar bomba: la historia que destruyó la esperanza», 13 de marzo de 2026.
- Wikipedia (inglés), «Boyacá necklace bomb incident».

## Derechos

© 2026 Juan Diego Velasco, Juan Esteban Herrera y Jhonatan Gil. Todos los derechos reservados sobre los textos, el diseño y el simulador.

Las fotografías pertenecen a sus autores. Las tres del 15 de mayo de 2000 provienen de archivos de prensa (La Silla Vacía, Latin American Post y El Diario de Ecuador) y se usan con fines educativos. Las demás son de Wikimedia Commons, con las licencias que se indican en la sección de fuentes de la página.

En memoria de Ana Elvia Cortés de Pachón y de Jairo Hernando López.
