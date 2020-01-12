# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:24:02 2019

@author: DELL
"""

from util import getProducts, getDefaultProducts

def casual(conn, y_pred, colour):
    c=str(y_pred)
    if c == '[0]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for white_tan skin ON RED colors!!")
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
                    'category_color_type_id': 1,
                    'color_code_hex': 'AD2A3F'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                    'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for white_tan skin ON Blue colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for white_tan skin ON Golden colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': '8E693E'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for white_tan skin ON Green colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'DE8549'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for white_tan skin ON maroon colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'BD6C76'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '972427'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for white_tan skin ON grey colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': '84727D'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '624A57'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for white_tan skin ON Orange colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'd56e53'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'F15F47'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for white_tan skin ON pink colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'e97451'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for white_tan skin ON purple colors!!")
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
                    'category_color_type_id': 1,
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
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for white_tan skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'DE6452'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)  
    elif c == '[1]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for Extremely_fair skin ON RED colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for Extremely_fair skin ON Blue colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for Extremely_fair skin ON Golden colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for Extremely_fair skin ON Green colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for Extremely_fair skin ON maroon colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for Extremely_fair skin ON grey colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for Extremelyfair skin ON Orange colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for Extremely_fair skin ON pink colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for Extremely_fair skin ON purple colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for Extremely_fair skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
                'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)
    if c == '[2]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for fair_redspot skin ON RED colors!!")
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
                    'category_color_type_id': 1,
                    'color_code_hex': 'A22630'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for fair_redspot skin ON Blue colors!!")
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
                    'category_color_type_id': 3,
                     'color_code_hex': '737199'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                     'color_code_hex': 'ad6356'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for fair_redspot skin ON Golden colors!!")
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
                    'category_color_type_id': 3,
                     'color_code_hex': '8E693E'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for fair_redspot skin ON Green colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'DE8549'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for fair_redspot skin ON maroon colors!!")
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
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for fair_redspot skin ON grey colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': '323e31'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A16167'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for fair_redspot skin ON Orange colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A16167'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for fair_redspot skin ON pink colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'e97451'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for fair_redspot skin ON purple colors!!")
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
                    'category_color_type_id': 1,
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
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for fair_redspot skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'DE6452'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A16167'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)
    if c == '[3]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for natural_redspot skin ON RED colors!!")
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
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for natural_redspot skin ON Blue colors!!")
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
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A16167'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for natural_redspot skin ON Golden colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'A38462'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '391118'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for natural_redspot skin ON Green colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'A55C40'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for natural_redspot skin ON maroon colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'AA6441'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for natural_redspot skin ON grey colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': '84727D'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A16167'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for natural_redspot skin ON Orange colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'd56e53'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'F15F47'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for natural_redspot skin ON pink colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '915584'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for natural_redspot skin ON purple colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'AA88CC'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '391118'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for natural_redspot skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                    'category_id':22,
                    'category_color_type_id': 26,
                     'color_code_hex': 'DE6452'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '391118'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData) 
    elif c == '[4]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for natural skin ON RED colors!!")
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
                     'color_code_hex': 'AD2A3F'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for natural skin ON Blue colors!!")
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
                     'color_code_hex': 'CC8A73'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for natural skin ON Golden colors!!")
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
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': '972427'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for natural skin ON Green colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for natural skin ON maroon colors!!")
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
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for natural skin ON grey colors!!")
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
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for natural skin ON Orange colors!!")
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
                    'category_color_type_id': 3,
                     'color_code_hex': 'ad6356'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for natural skin ON pink colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '915584'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                     'color_code_hex': 'ad6356'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for natural skin ON purple colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for natural skin without colour!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': 'CC8A73'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'A1A3AF'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getDefaultProducts(conn, defaultData)   
    
    elif c == '[5]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for black_brown skin ON RED colors!!")
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
                     'color_code_hex': '#ba4a4b'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'ba4a4b'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for black_brown skin ON Blue colors!!")
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
                    'category_color_type_id': 6,
                     'color_code_hex': '#'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '920F41'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for black_brown skin ON Golden colors!!")
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
                    'category_color_type_id': 6,
                     'color_code_hex': '#F449D2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': 'ba4a4b'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for black_brown skin ON Green colors!!")
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
                    'category_color_type_id': 6,
                     'color_code_hex': '#F449D2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '#AE484B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for black_brown skin ON maroon colors!!")
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
                     'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '#681426'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for black_brown skin ON grey colors!!")
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
                    'category_color_type_id': 2,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '432E2A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for black_brown skin ON Orange colors!!")
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
                     'color_code_hex': '#A0799E'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                     'color_code_hex': 'F15F47'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for black_brown skin ON pink colors!!")
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
                    'category_color_type_id': 6,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for black_brown skin ON purple colors!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': '#E8426E'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for black_brown skin without colour!!")
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
                    'category_color_type_id': 26,
                     'color_code_hex': '#F449D2'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                     'color_code_hex': '#ba4a4b'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getDefaultProducts(conn, defaultData)
    elif c == '[6]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for brown skin ON RED colors!!")
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
                    'category_color_type_id': 7,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 7,
                    'color_code_hex': '#9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for brown skin ON Blue colors!!")
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
                    'category_color_type_id': 7,
                    'color_code_hex': '1070A0'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 21,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for brown skin ON Golden colors!!")
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
                    'category_color_type_id': 7,
                    'color_code_hex': '#986276'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 7,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for brown skin ON Green colors!!")
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
                    'category_color_type_id': 7,
                    'color_code_hex': '#986276'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': 'ad6356'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for brown skin ON maroon colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': '#6C2C32'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '920F41'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for brown skin ON grey colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': '#624A57'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '#624A57'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for brown skin ON Orange colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': '#A0799E'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '#AE484B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for brown skin ON pink colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                    'color_code_hex': '#915584'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 2,
                    'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for brown skin ON purple colors!!")
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
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for brown skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 7
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
                'e_shadow' : {

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
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }


            responseData = getDefaultProducts(conn, defaultData) 
    elif c == '[7]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for dark_brown skin ON RED colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 8,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 8,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for dark_brown skin ON Blue colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for dark_brown skin ON Golden colors!!")
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
                   
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for dark_brown skin ON Green colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for dark_brown skin ON maroon colors!!")
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
                
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for dark_brown skin ON grey colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for dark_brown skin ON Orange colors!!")
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
                   
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for dark_brown skin ON pink colors!!")
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
                   
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for dark_brown skin ON purple colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 26,
                    'color_code_hex': '9E273A'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for dark_brown skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                        #same
                    'category_id' : 21,
                    'category_color_type_id': 26
                },
                'e_shadow' : {
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData)

    elif c == '[8]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for fair skin ON RED colors!!")
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
                    'category_color_type_id': 2,
                    'color_code_hex': 'AD2A3F'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                    'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            print("casual makeup for fair skin ON Blue colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                     'color_code_hex': '405E87'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            print("casual makeup for fair skin ON Golden colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                     'color_code_hex': '8E693E'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'D15F54'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            print("casual makeup for fair skin ON Green colors!!")
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
                    'category_color_type_id': 1,
                     'color_code_hex': 'DE8549'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'C1212B'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            print("casual makeup for fair skin ON maroon colors!!")
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
                   'category_id' : 22, 
                    'category_color_type_id': 1,
                     'color_code_hex': 'BD6C76'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '972427'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            print("casual makeup for fair skin ON grey colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                     'color_code_hex': '84727D'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '624A57'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for fair skin ON Orange colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                     'color_code_hex': 'd56e53'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'F15F47'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for far skin ON pink colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'e97451'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for fair skin ON purple colors!!")
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
                    'category_id' : 22,
                    'category_color_type_id': 1,
                     'color_code_hex': '915584'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': '6E2747'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for fair skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
               'e_shadow' : {
                   'category_id': 22, 
                    'category_color_type_id': 26,
                     'color_code_hex': 'DE6452'
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                     'color_code_hex': 'B87889'
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData) 
    elif c == '[9]':
        if colour == "#FFA07A" or colour == "#FA8072"  or colour=="#E9967A" or  colour=="#F08080" or colour=="#CD5C5C" or colour == "#DC143C" or colour == "#B22222"  or colour=="#FF0000" or  colour=="#8B0000"or colour=="#800000" or colour=="#FF6347" or  colour=="#FF4500"or colour=="#DB7093":#red shades
            print("casual makeup for natural_white skin ON RED colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)     
        elif colour == "0000FF" or colour == "#0000CC"  or colour=="#000099" or  colour=="#000066" or colour=="#000033"  or colour == "#0033FF" or colour == "#0033FF"  or colour=="#003399" or  colour=="#003366"or colour=="#006699" or colour == "#0066CC" or colour == "#0066FF"  or colour=="#0099CC" or  colour=="#0099FF"or colour=="#00CCCC" or colour == "#00CCFF" or colour == "#330099"  or colour=="#3300CC" or  colour=="#3300FF"or colour=="#333399" or colour == "#3333CC" or colour == "#3333FF"  :
            
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)   
        elif colour == "#ffe866" or colour == "#ffe44d"  or colour=="#ffe033" or  colour=="#ffe033" or colour=="#ffd700"  or colour == "#e6c300" or colour == "#ccad00"  or colour=="#b39800"  or colour == "#998200" or colour == "#CFB53B"  or colour=="#806c00" or colour == "#C5B358"  or colour=="#D4AF37" :#golden shades
            
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#001a00" or colour == "#003300"  or colour=="#004d00" or  colour=="#006600" or colour=="#008000"  or colour == "#009900" or colour == "#00b300"  or colour=="#00cc00" or colour=="#00cc00"   :#green shades
            
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#300000 " or colour == "#380000 "  or colour=="#400000 " or  colour=="#480000" or colour=="#500000 "  or colour == "#580000 " or colour == "#600000 "  or colour=="#680000 " or colour=="#700000 " or colour=="#780000 "   :#maroon shades
            
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#585858	" or colour == "#606060	"  or colour=="#686868" or  colour=="#696969"   or colour == "#707070" or colour == "#585858	" or colour == "#787878	"  or colour=="#888888	" or  colour=="#909090	"   or colour == "#989898	" or colour=="#A0A0A0" or  colour=="##A8A8A8"   or colour == "#B0B0B0" :#gray colors
            
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
        elif colour == "#FF7F50" or colour == "#FF6347"  or colour=="#FF4500" or  colour=="#FF8C00" or colour == "#ff6600" or colour == "#ff751a"  or colour=="#ff8533" or  colour=="#e65c00":#orange shades
            print("casual makeup for natural_white skin ON Orange colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }
            responseData = getProducts(conn, data)  
        elif colour == "#ff3399" or colour == "#ff99cc"  or colour=="#ff80bf" or  colour=="#ff66b3" or  colour=="#ff4da6" or  colour=="#ff1a8c" or  colour == "#ff0080" or colour == "#e60073"  or colour=="#ffcce6":#pink shades
            print("casual makeup for natural_white skin ON pink colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data)  
        elif colour == "#4B0082" or colour == "#800080"  or colour=="#8B008B" or  colour=="#9932CC"or colour=="#9400D3"  or colour == "#8A2BE2" or colour == "#9370DB"  or colour=="#BA55D3" or colour=="#FF00FF" or colour=="#FF00FF" or colour == "#DA70D6"  or colour=="#EE82EE" or colour=="#DDA0DD" or colour=="#D8BFD8" or  colour=="#E6E6FA"   :#purple shades
            print("casual makeup for natural_white skin ON purple colors!!")
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
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getProducts(conn, data) 
               
        else:
            
            print ("casual makeup for natural_white skin without colour!!")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 4
                },
                'eyeliner' : {
                        #same
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
                'e_shadow' : {
                    'category_id': 22,
                    'category_color_type_id': 26,
                    'color_code_hex': 'BF4C45'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 3,
                    'color_code_hex': '642226'
                },
                'blush': {
                    'category_id':6,
                        #same
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData) 
    else:
            print("default casual makeup ")
            defaultData = {
                'foundation' : {
                    'category_id' : 3,
                    'category_color_type_id': 26
                },
                'eyeliner' : {
                    'category_id' : 21,
                    'category_color_type_id': 21
                },
                'e_shadow' : {
                    'category_id' : 22,
                    'category_color_type_id': 1,
                    'color_code_hex': 'AD2A3F'
                        
                },
                'lipstick' : {
                    'category_id':23,
                    'category_color_type_id': 1,
                    'color_code_hex': 'C1212B'
                
                },
                'blush': {
                    'category_id':6,
                    'category_color_type_id': 15,
                    'color_code_hex': 'F58AA8'
                }
            }

            responseData = getDefaultProducts(conn, defaultData) 
    return responseData

              
   