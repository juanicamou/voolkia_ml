# Script Python - Items Vendedores 
### Script que retorna un log con los items de cada vendedor (id de vendedor) que se ingrese como parametro para el site: MLA

##### Requerimientos
- `Python 3.9.7`
- Paquetes: `request` `json` `sys`

##### Instalación Python
https://www.python.org/downloads/release/python-3910/

##### Instalación de paquetes con PIP

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

```
py items_por_vendedor.py <arg_1> <arg_2> <arg_n>
```

En caso de que no funcione `py`, utilizar `python` o `python3`. 

Luego `items_por_vendedor.py` agregar los seller_id separados por un `espacio`.

##### Formato de salida

```
ID Ítem | Nombre Ítem | ID Categoría | Nombre Categoría
```
