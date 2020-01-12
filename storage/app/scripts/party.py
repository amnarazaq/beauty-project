# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:24:02 2019

@author: DELL
"""

from util import getProducts, getDefaultProducts

def party(conn, y_pred, colour):
    c=str(y_pred)
    if c == '[0]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for white_tan skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                        #same
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#A51C3B'   #red shade
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for white_tan skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '233374'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for white_tan skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#D98548'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for white_tan skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                 'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 27,
                     'color_code_hex': '#49989C'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for white_tan skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#5F1A25'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for white_tan skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#B6B6B9'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for white_tan skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#FF6647'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#F63E00'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for white_tan skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#E61A7D'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#D22262'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for white_tan skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#F34AD2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'D22262'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for white_tan skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 26,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '462724'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)  
    elif c == '[1]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for Extremely_fair skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A51C3B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '88151A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)    
            print("*************************************************************************")
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for Extremely_fair skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '233374'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '88151A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for Extremely_fair skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '5F1A25'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '88151A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for Extremely_fair skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'AE484B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for Extremely_fair skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for Extremely_fair skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B6B6B9'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'D22262'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for Extremelyfair skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'FF6647'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'F63E00'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for Extremely_fair skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 15,
                     'color_code_hex': 'F58AA8'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'D22262'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for Extremely_fair skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 2
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'F34AD2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '5D1E48'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for Extremely_fair skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 26,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '462724'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)
            print("*************************************************************************")
    if c == '[2]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for fair_redspot skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                        #same
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': 'A42028'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for fair_redspot skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#233374'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '681426'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for fair_redspot skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'DEB394'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for fair_redspot skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                 'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#01674F'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '6C2C32'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for fair_redspot skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A51C3B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '6C2C32'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for fair_redspot skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#B6B6B9'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '672B37'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for fair_redspot skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CE4B42'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#F63E00'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for fair_redspot skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 3
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#E7177D'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '681426'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for fair_redspot skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id':1 ,
                     'color_code_hex': '915584'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for fair_redspot skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 26,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '462724'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)
            print("*************************************************************************")
    if c == '[3]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for natural_redspot skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                        #same
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '##E9515A'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'DE373F'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for natural_redspot skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 7,
                     'color_code_hex': '1070A0'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'ba4a4b'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for natural_redspot skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '5F1A25'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for natural_redspot skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                 'e_shadow' : {
                     'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#01634A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#BC3B4F'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for natural_redspot skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '5F1A25'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#B10101'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for natural_redspot skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B6B6B9'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for natural_redspot skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 2,
                     'color_code_hex': 'd56e53'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'F15F47'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for natural_redspot skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 1
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 2,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for natural_redspot skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 2,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '932758'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for natural_redspot skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 26,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'E9515A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'DE373F'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getDefaultProducts(conn, defaultData) 
            
            print("*************************************************************************")
    elif c == '[4]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for natural skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'E9515A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'DE373F'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for natural skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 7,
                     'color_code_hex': '1070A0'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'DE373F'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for natural skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#954131'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '972427'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for natural skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'AA6441'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for natural skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 3,
                     'color_code_hex': '722731'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                     'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for natural skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': '432E2A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for natural skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'E7177B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B10101'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for natural skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for natural skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': '#F449D2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for natural skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 5
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#BA3941'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B10101'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getDefaultProducts(conn, defaultData)   
            print("*************************************************************************")
    elif c == '[5]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for black_brown skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CF0102'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A90F21'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for black_brown skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#1A2F63'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'C04246'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for black_brown skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                     'category_color_type_id': 28,
                     'color_code_hex': '#B58067'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A90F21'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }
            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for black_brown skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#B58067'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A90F21'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }
            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for black_brown skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_color_type_id': 6,
                     'color_code_hex': '#F449D2'
                },
                'e_shadow' : {
                    'category_id':22,
                     'category_color_type_id': 28,
                     'color_code_hex': '#5B1621'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A90F21'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for black_brown skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#877E8C'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '432E2A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)

        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for black_brown skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#DD765A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'F15F47'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for black_brown skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': '#EF4D77'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '862035'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for black_brown skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': '#F449D2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#F7348A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for black_brown skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#AB2837'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }
            responseData = getDefaultProducts(conn, defaultData)
            print("*************************************************************************")
    elif c == '[6]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for brown skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CF0102'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A90F21'
                },
                'blush': {
                    'category_id':6,
                   'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for brown skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '233374'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#9E513F'
                },
                'blush': {
                    'category_id':6,
                   'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for brown skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#BC724B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for brown skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#BC724B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for brown skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                    'color_code_hex': '#6C2C32'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '9D1A48'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for brown skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '877E8C'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '#624A57'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for brown skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#EF8644'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#F63E00'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for brown skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#D84B78'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#F42F86'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for brown skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                   'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': 'FA4189'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#F42F86'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for brown skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
'category_id':22,
                     'category_color_type_id': 7,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 7,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getDefaultProducts(conn, defaultData)
            print("*************************************************************************")
    elif c == '[7]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for dark_brown skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CF0102'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A90F21'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for dark_brown skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '233374'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#9E513F'
                },
                'blush': {
                    'category_id':6,
                   'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for dark_brown skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#BC724B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for dark_brown skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#BC724B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for dark_brown skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                    'color_code_hex': '#6C2C32'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '9D1A48'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for dark_brown skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '877E8C'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '#624A57'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for dark_brown skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#EF8644'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#F63E00'
                },
                'blush': {
                    'category_id':6,
                   'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for dark_brown skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': '#D84B78'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#F42F86'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for dark_brown skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                   'category_id':22,
                    'category_color_type_id': 28,
                    'color_code_hex': 'FA4189'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                    'color_code_hex': '#F42F86'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for dark_brown skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 8
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
'category_id':22,
                     'category_color_type_id': 7,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 7,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                   'category_color_type_id': 28,
                    'color_code_hex': 'D1B4A1'
                }
            }


            print("*************************************************************************")
    elif c == '[8]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for fair skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A51C3B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '88151A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)    
            print("*************************************************************************")
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for fair skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '233374'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '88151A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for fair skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '5F1A25'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '88151A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for fair skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'AE484B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for fair skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for fair skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B6B6B9'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'D22262'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for fair skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'FF6647'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'F63E00'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for fair skin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 15,
                     'color_code_hex': 'F58AA8'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'D22262'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for fair skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'F34AD2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '5D1E48'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for fair skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 9
                },
                'eyeliner' : {
                    'category_id' : 26,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#A42028'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '462724'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)
            print("*************************************************************************")
    elif c == '[9]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("party makeup for natural_white skin ON RED colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': 'E9515A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'DE373F'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("party makeup for natural_white skin ON Blue colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 7,
                     'color_code_hex': '1070A0'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'DE373F'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("party makeup for natural_white skin ON Golden colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#954131'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '972427'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("party makeup for natural_white skin ON Green colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'AA6441'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("party makeup for natural_white skin ON maroon colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 3,
                     'color_code_hex': '722731'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                     'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("party makeup for 722731 skin ON grey colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': '432E2A'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("party makeup for 722731 skin ON Orange colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'E7177B'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B10101'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("party makeup for natural_whiteskin ON pink colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("party makeup for naryeal_white skin ON purple colors!!")
            data = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': '#F449D2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getProducts(conn, data) 
               
        else:
            
            print ("party makeup for natural_white skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 10
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#BA3941'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': 'B10101'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }


            responseData = getDefaultProducts(conn, defaultData)   
            print("*************************************************************************")
 
          
    else:
            print("default party makeup ")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 6
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 23
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 28,
                     'color_code_hex': '#AB2837'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 28,
                     'color_code_hex': '#CC3838'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'FFCAD9'
                }
            }

            responseData = getDefaultProducts(conn, defaultData) 
    return responseData

              
   