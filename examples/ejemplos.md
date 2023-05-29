<h1>Ejemplos para otras facultades</h1>

# Uso

Se puede modificar la configuración del programa para que reciba noticias de páginas de otras facultades
1. Abre la configuración con el ícono del sistema (botón "Abrir configuración").
2. Cambia el contenido de la configuración por el contenido de algún archivo de [ejemplo](#plantillas-de-configuración).
3. Recargar las noticias en el ícono de la bandeja del sistema (botón "Recargar Noticias"). 

# Plantillas de configuración

- [fisi](fisi.json)
- [figmmg](figmmg.json)

# Agregar nuevas configuraciones

- Se utiliza la notación de query selectors de BeautifulSoup.
- Se tienen 3 configuraciones:
    - cards: El contenedor que envuelve a los títulos, descripciones y enlaces(links) de las noticias.
    - titles: Queryselector para todos los títulos.
    - descriptions: Queryselector para las descripciones, para este caso se toma todo el texto dentro de la etiqueta.
    - links: Queryselector para las etiquetas "a" de los enlaces.

## Solución de problemas

- Se pueden generar errores en caso de que los queryselectors no tengan elementos, para solucionarlos verificar en el navegador que el queryselector devuelva los elementos solicitados correctamente con la funcion:
```javascript
document.querySelectorAll(".tu-query-selector")
```