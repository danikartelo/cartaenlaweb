
a = "das,cru,   soj   "
a = a.strip()
print(a)
b= a.split(',')

for i in range(len(b)):
    b[i] = b[i].strip()
print(b)



def glu():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/gluten.png"'
            'alt="gluten" width="32" height="32" /></div>')
def soj():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/soja.png"'
            'alt="soja" width="32" height="32" /></div>')
def hue():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/huevos.png"'
            'alt="huevos" width="32" height="32" /></div>')
def pes():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/pescado.png"'
            'alt="pescado" width="32" height="32" /></div>')
def lac():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/lacteos.png"'
            'alt="lacteos" width="32" height="32" /></div>')
def cru():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/crustaceos.png"'
            'alt="crustaceos" width="32" height="32" /></div>')
def mol():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/moluscos.png"'
            'alt="moluscos" width="32" height="32" /></div>')
def sds():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/sesamo.png"'
            'alt="sesamo" width="32" height="32" /></div>')
def das():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/dioxido_de_azufre_y_sulfitos.png"'
            'alt="dioxido de azufre" width="32" height="32" /></div>')
def mos():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/mostaza.png"'
            'alt="mostaza" width="32" height="32" /></div>')
def fdc():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/frutos_de_cascara.png"'
            'alt="frutos de cascara" width="32" height="32" /></div>')
def cac():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/cacahuetes.png"'
            'alt="cacahuetes" width="32" height="32" /></div>')
def alt():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/altramuces.png"'
            'alt="altramuces" width="32" height="32" /></div>')
def api():
    return( 'src="https://cartaenlaweb.com/sites/elmonje/wp-content/uploads/2020/07/apio.png"'
            'alt="apio" width="32" height="32" /></div>')

allegern = {'glu':glu,
            'soj':soj,
            'hue':hue,
            'pes':pes,
            'lac':lac,
            'cru':cru,
            'mol':mol,
            'sds':sds,
            'das':das,
            'mos':mos,
            'fdc':fdc,
            'cac':cac,
            'alt':alt,
            'api':api
            }


def do_allergens(array_allegerns):

    dish_allergen = ('<div class="wpb_single_image wpb_content_element vc_align_center">'
                    '<figure class="wpb_wrapper vc_figure">')

    for element in array_allegerns:
         # print(allegern[element]())
         dish_allergen = dish_allergen + ('<div class="vc_single_image-wrapper vc_box_border_grey">'
                        '<img class="vc_single_image-img"')
         dish_allergen = dish_allergen + str(allegern[element]())

    dish_allergen = dish_allergen + ('</figure></div>')
    return(dish_allergen)


# dish_alergen = ('<div class="wpb_single_image wpb_content_element vc_align_center">'
#                 '<figure class="wpb_wrapper vc_figure">')
# dish_alergen = dish_alergen + str(add_allergens(b))
# dish_alergen = dish_alergen + ('</figure></div>')

print(str(do_allergens(b)))


# for element in b:
#      print(element)
#      dish_alergen = dish_alergen + str(element)



# print(allegern['glu']())
