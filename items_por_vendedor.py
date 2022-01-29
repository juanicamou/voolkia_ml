import requests
import json
import sys

# Función llamada a la API
def call_api(path, token):
    
    # Llamada a la API de ML
    call_items = requests.get(path, headers={'Authorization': token})

    # json.load devuelve objeto de tipo diccionario sobre el que se puede iterar
    response = json.loads(call_items.content)

    return response

#Función imprimir log
def write_log(seller_id, item_id, item_name, category_id, category_name):

    log_name = 'log' + seller_id + '.txt'
    with open(log_name, 'a') as log:
        print(item_id, ',', item_name, ',', category_id, ',',category_name, file = log)
        log.close()

# Función que logea
def logger(seller_id):
    
    json_items = call_api('https://api.mercadolibre.com/sites/MLA/search?seller_id=' + seller_id, token)

    # Condición para logear = que existan items.
    if json_items['results']:

        print('Inicio del logeo del usuario: ', seller_id)

        # Iteración sobre el diccionario
        for i in json_items['results']:

            json_category = call_api('https://api.mercadolibre.com/categories/' + i['category_id'], token)

            # Write del log
            write_log(seller_id, i['id'], i['title'], i['category_id'], json_category['name'])
        
        print('Fin del logeo del usuario: ', seller_id)

    else:
        # Print en caso de que no haya items
        print('El usuario ', seller_id, ' no posee items o es incorrecto.')


if __name__ == '__main__':

    # Lista a partir de los parametros ingresados
    parameters = sys.argv

    # Token
    token = 'Bearer ' + parameters[1]

    # Sellers ID
    for i in range(2, len(parameters)):
        logger(parameters[i])