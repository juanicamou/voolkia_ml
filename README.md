# Script Python - Ítems Vendedores Mercado Libre
### Script que retorna un log con los ítems de cada vendedor (id de vendedor) que se ingrese como parámetro para el site: MLA

##### Requerimientos
- `Python 3.9.7`
- Paquetes: `request` `json` `sys`

##### Instalación Python
https://www.python.org/downloads/release/python-3910/

##### Instalación de paquetes con PIP
La versión 3.9.7 de Python ya posee PIP por defecto, ante cualquier inconveniente consultar la documentación oficial de PIP: https://pip.pypa.io/en/stable/#

```
pip install requests
```

```
pip install json
```

```
pip install sys
```

##### Llamada al script
Se debe ejecutar el script como se muestra a continuación, siendo `$token` el token otorgado por la API de ML y `$seller_id_*` los id de vendedores que se desea consultar, todos los argumentos separados por un ´espacio´.

```
py items_por_vendedor.py $token $seller_id_1 $seller_id_2 $seller_id_*
```

En caso de que no funcione `py`, utilizar `python` o `python3`. 

##### Formato de salida
El script retorna un archivo txt por cada `seller_id` ingresado como parámetro con nombre `log$seller_id.txt` el cual posee el listado de ítems con el siguiente formato:

```
ID Ítem | Nombre Ítem | ID Categoría | Nombre Categoría
```
En caso de que algún `seller_id` ingresado como parámetro no exista, sea incorrecto o no posea ítems el script retorna un mensaje en por terminal indicándolo.
##### Token API Mercado Libre
Seguir el paso a paso de la documentación oficial de Mercado Libre: https://developers.mercadolibre.com.ar/es_ar/autenticacion-y-autorizacion
