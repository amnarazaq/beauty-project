import pymysql.cursors

def getProducts(conn, data):
    cursor=conn.cursor();

    response = {}

    queryTextWithID ="SELECT id, name, color_code_hex FROM products WHERE category_color_type_id={0} AND category_id={1}"
    queryTextWithHex = "SELECT id, name, color_code_hex FROM products WHERE category_id={0} AND category_color_type_id={1} AND  color_code_hex='{2}'"
    queryTextWithHexID = "SELECT id, name, color_code_hex FROM products WHERE category_id={0} AND category_color_type_id={1} AND  color_code_hex='{2}'"

    for key, category in data.items():
        if key == 'lipstick' or key == 'blush':
            query = queryTextWithHex.format(category['category_id'],category['category_color_type_id'], category['color_code_hex'])
        elif key == 'e_shadow':
            query = queryTextWithHexID.format(category['category_id'],category['category_color_type_id'], category['color_code_hex'])
        else:
            #foundation eyeliner
            query = queryTextWithID.format(category['category_color_type_id'], category['category_id'])
        cursor.execute(query)
        response[key] = cursor.fetchone()
    return response

def getDefaultProducts(conn, data):
    cursor=conn.cursor();

    response = {}

    # Fetch Foundation
    if 'foundation' in data:
        foundation = data.get('foundation')
        categoryColor = foundation.get('category_color_type_id')
        categoryId = foundation.get('category_id')
        query = "SELECT id, name, color_code_hex FROM products WHERE category_color_type_id={0} AND category_id={1}".format(categoryColor, categoryId)
        cursor.execute(query)
        response['foundation'] = cursor.fetchone()

    # Fetch Eyeliner
    if 'eyeliner' in data:
        eyeliner = data.get('eyeliner')
        categoryColor = eyeliner.get('category_color_type_id')
        categoryId = eyeliner.get('category_id')
        query = "SELECT id, name, color_code_hex FROM products WHERE category_color_type_id={0} AND category_id={1} ".format(categoryColor, categoryId)
        cursor.execute(query)
        response['eyeliner'] = cursor.fetchone()

    # Fetch Eye Shadow
    if 'e_shadow' in data:
        e_shadow = data.get('e_shadow')
        categoryId = e_shadow.get('category_id')
        colorCodeHex = e_shadow.get('color_code_hex')
        categoryColorType = e_shadow.get('category_color_type_id')
        query = "SELECT id, name, color_code_hex FROM products WHERE category_id={0} AND category_color_type_id={1} AND color_code_hex='{2}'".format(categoryId,categoryColorType, colorCodeHex)
        cursor.execute(query)
        response['e_shadow'] = cursor.fetchone()

    # Fetch lipstick
    if 'lipstick' in data:
        lipstick = data.get('lipstick')
        categoryId = lipstick.get('category_id')
        colorCodeHex = lipstick.get('color_code_hex')
        categoryColor = lipstick.get('category_color_type_id')
        query = "SELECT id, name, color_code_hex FROM products WHERE category_id={0} AND category_color_type_id={1} AND color_code_hex='{2}'".format(categoryId,categoryColor, colorCodeHex)
        cursor.execute(query)
        response['lipstick'] = cursor.fetchone()

    # Fetch blush
    if 'blush' in data:
        blush = data.get('blush')
        categoryId = blush.get('category_id')
        colorCodeHex = blush.get('color_code_hex')
        categoryColor = blush.get('category_color_type_id')
        query = "SELECT id, name, color_code_hex FROM products WHERE category_id={0} AND category_color_type_id={1} AND color_code_hex='{2}' ".format(categoryId,categoryColor, colorCodeHex)
        cursor.execute(query)
        response['blush'] = cursor.fetchone()

    return response