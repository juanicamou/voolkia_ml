import requests
import json
import sys

# Función que logea
def logger(seller_id):
    
    print('Logeando el usuario: ', seller_id)

    # Path API ML que retorna los items de un vendedor para un determinado site_id y un seller_id
    path_items = 'https://api.mercadolibre.com/sites/MLA/search?seller_id=' + seller_id

    # Llamada a la API de ML
    call_items = requests.get(path_items, 
                            headers={'Authorization': ''})

    # Contenido del response
    content_items = call_items.content

    # json.load devuelve objeto de tipo diccionario sobre el que se puede iterar
    json_items = json.loads(content_items)

    # Condición para logear = que existan items.
    if json_items['results']:
        
        # Iteración sobre el diccionario
        for i in json_items['results']:
            
            # Path API ML que retorna los items de un vendedor para un determinado site_id y un seller_id
            path_category = 'https://api.mercadolibre.com/categories/' + i['category_id']

            # Llamada a la API de ML
            call_category = requests.get(path_category, 
                                headers={'Authorization': ''})

            # Contenido del response
            content_category = call_category.content

            # json.load devuelve objeto de tipo diccionario sobre el que se puede iterar
            json_category = json.loads(content_category)

            # Write del log
            log_name = 'log' + seller_id + '.txt'
            with open(log_name, 'a') as log:
                print(i['id'], '|', i['title'], '|', i['category_id'], '|',json_category['name'], file = log)
                log.close()
    else:
        # Print en caso de que no haya items
        print('El usuario ', seller_id, ' no posee items o es incorrecto.')

    print('Fin del logeo del usuario: ', seller_id)

    
    
if __name__ == '__main__':
    
    # Lista a partir de los parametros ingresados
    parameters = sys.argv

    for i in range(1, len(parameters)):
        logger(parameters[i])