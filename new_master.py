

class MasterClass:
    def __init__(self,file):
        self.content = open(file, "r").read()

        self.name = "name"
        self.text = '[vc_tta_section tab_id="'  +'" title="' + '"]'

    def __str__(self):
        return self.text

    # def get_content(self, file):
    #     self.content = open(file, "r").read()
    #     #print (self.content)

    def get_section(self,n):
        x = self.content.find("section_" + '{:02d}'.format(n))  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
        ini = self.content.rfind("[",0,x)       # Buscar el [ previo = inicio estructura
        x = self.content.find(" ",ini)          # Buscar tipo de estructrua
        struct_type = self.content[ini+1:x]     # La guardo en struct_type
        x = self.content.find(("/" + struct_type),ini)     # Buscar el fianl de la estructura
        end = self.content.find("]",x) + 1         # Buscarl el cierre
        self.section = self.content[ini:end] # Extraer la estructura entera

    def __get_num_sections(self):
        i = 0
        x = 0
        while x != -1:
            i += 1
            x = self.content.find("section_" + '{:02d}'.format(i),x+1)
        # self.num_sections = i-1

        # print(i-1)
        return(i-1)


    def get_inter_sections(self):
        array_inter_sections = []
        end = 0
        # print(self.__get_num_sections())
        for n in range(2,self.__get_num_sections()+1):
            # print(("section_" + '{:02d}'.format(n)))
            z = self.content.find(("section_" + '{:02d}'.format(n)),end)  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
            # print('z: ' +str (z))
            x = self.content.find("dish",z)  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
            temp = self.content.find("vc_separator",z)  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
            # print('x: ' +str (x))



            if x > temp: x = temp
            if x == -1: x = temp
            end = self.content.rfind("[",0,x+1)       # Buscar el [ previo = inicio estructura

            x = self.content.rfind("dish",0,end)  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones


            # print('x: ' +str (x))
            ini = self.content.rfind("[",0,x)       # Buscar el [ previo = inicio estructura
            x = self.content.find(" ",ini)          # Buscar tipo de estructrua
            struct_type = self.content[ini+1:x]     # La guardo en struct_type
            x = self.content.find(("/" + struct_type),ini)     # Buscar el fianl de la estructura
            ini = self.content.find("]",x) + 1         # Buscarl el cierre

            # print('ini: ' +str (ini)) # Extraer la estructura entera
            # print('end: ' +str (end)) # Extraer la estructura entera
            # print(self.content[ini:end]) # Extraer la estructura entera
            array_inter_sections.append(self.content[ini:end])


        print (array_inter_sections)
        #print(len(array_inter_sections))
        # print (array_inter_sections[0])
        # print (array_inter_sections[1])
        # print (array_inter_sections[2])
        return(array_inter_sections)


    def do_inter_sections(self,n):

        a = self.get_inter_sections()
        return(a[n-1])



    def get_separator(self):

        try:
            self.section
        except:
            # print ("It doesn't Exist!")
            exit()
        else:
            # print ("It exists!")
            pass
        # if 'self.section' in locals():
        #     print ("var2: variable exist")
        # else:
        #     print ("var2: variable does not exist")
        # if self.section:
        #     print ("AAAAAAAAAAAAAAAA")

        pos_ini = self.section.find("[vc_separator")
        pos_end = self.section.find("]",pos_ini) +1
        self.separator = self.section[pos_ini:pos_end]
        # print(self.separator)
        pass




    def get_dish(self):

        try:
            self.section
        except:
            # print ("It doesn't Exist!")
            exit()
        else:
            # print ("It exists!")
            pass
        x = self.section.find("dish")  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
        ini = self.section.rfind("[",0,x)       # Buscar el [ previo = inicio estructura
        x = self.section.find(" ",ini)          # Buscar tipo de estructrua
        struct_type = self.section[ini+1:x]     # La guardo en struct_type
        x = self.section.find(("/" + struct_type),ini)     # Buscar el fianl de la estructura
        end = self.section.find("]",x) + 1         # Buscarl el cierre
        self.dish = self.section[ini:end] # Extraer la estructura entera


    def do_intro(self):

        x = self.content.find("dish")  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
        temp = self.content.find("[vc_separator")  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones

        if x > temp: x = temp
        end = self.content.rfind("[",0,x+1)       # Buscar el [ previo = inicio estructura

        intro = self.content[0:end]
        # print(intro)
        return(intro)

    def do_outro(self):


        x = self.content.rfind("dish")  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
        ini = self.content.rfind("[",0,x)       # Buscar el [ previo = inicio estructura
        x = self.content.find(" ",ini)          # Buscar tipo de estructrua
        struct_type = self.content[ini+1:x]     # La guardo en struct_type
        x = self.content.find(("/" + struct_type),ini)     # Buscar el fianl de la estructura
        end = self.content.find("]",x) + 1         # Buscarl el cierre

        x = end

        temp = self.content.rfind("[vc_separator")  # Buscar el elemento objetivo -- esto vale para acordeones, columnas, filas, pero no para elementos internos como imagenes, titulos, descripciones
        temp = self.content.find("]",temp) +1
        if x < temp:
            x = temp
            print("BBBBBBBBB")
        # ini_out = self.content.find("]",x)      # Buscar el [ previo = inicio estructura
        ini_out = x
        outro = self.content[ini_out:]
        return(outro)
        # print(outro)

    def do_dish(self,new_dish,i):
        try:
            self.dish
        except:
            # print ("It doesn't Exist!")
            exit()
        else:
            # print ("It exists!")
            pass

        # c = self.dish.find("photo")
        # d = self.dish.rfind("image",0,c)
        # e = self.dish.find(" ",d)
        # actual_image =  self.dish[d:e]
        # new = self.dish[:d] + "image=\"" + str(int(df["imagen"][i])) + "\"" + self.dish[e:]
        # return(new)

        self.dish  = self.__add_name(i)
        self.dish  = self.__add_photo(i)
        self.dish  = self.__add_price(i)
        self.dish  = self.__add_description(i)

        new_dish = self.dish
        # print("AAAAAAAAAAA")
        # print(new_dish)
        if str(df["separador previo"][i]) != str("nan") :  # revisar esto, si es texto vacio me da que peta
            # print(df["separador previo"][i])
            # print("previo "+ str(i))
            new_dish  = self.separator + new_dish
        if str(df["separador posterior"][i]) != str("nan"):
            new_dish = new_dish + self.separator
            # print("posterior "+ str(i))
            # print(df["separador previo"][i])
            # print(type(df["separador previo"][i]))
        return(new_dish )

        # if (str(df["separador posterior"][i]) != str("nan")) or (str(df["separador posterior"][i]) != str("")):

    def __add_photo(self,i):
        c = self.dish.find("photo")
        if c == -1:
            return(self.dish)
        d = self.dish.rfind("image",0,c)
        e = self.dish.find(" ",d)
        new = self.dish[:d] + "image=\"" + str(int(df["imagen"][i])) + "\"" + self.dish[e:]
        return(new)

    def __add_name(self,i):
        c = self.dish.find("el_id=\"nombre\"")
        d = self.dish.rfind("vc_custom_heading text",0,c)
        e = self.dish.find("\" ",d) + 1
        new = self.dish[:d] + "vc_custom_heading text=\"" + str(df["nombre"][i]) + "\"" + self.dish[e:]
        return(new)

    def __add_price(self,i):
        c = self.dish.find("el_id=\"precio\"")
        d = self.dish.rfind("vc_custom_heading text",0,c)
        e = self.dish.find("\" ",d) + 1
        # print (df["precio"][i])
        a = df["precio"][i]
        # print (type(df["precio"][i]))
        # print(isinstance(df["precio"][i], str))
        if not (isinstance(df["precio"][i], str)):      # para prevenir que no sea str
            # print("NO LO ES")
            a = '{:.2f} €'.format(df["precio"][i])
        new = self.dish[:d] + "vc_custom_heading text=\"" + str(a) + "\"" + self.dish[e:]
        return(new)


    def __add_description(self,i):
        c = self.dish.find("el_id=\"descripcion\"")
        if c == -1:
            return(self.dish)
        pos = self.dish.find(">",c)  # esto esta cogido con pinzas, segunod >, pero esto será asi siempre???
        # print(pos)
        # pos = self.dish.find(">",pos+1) +1

        pos +=1
        # d = self.dish.rfind("vc_custom_heading text",0,c)
        e = self.dish.find("</p>",pos) #+ 1
        new = self.dish[:pos] + str(df["descripcion"][i]) + self.dish[e:]
        return(new)

section_dish = ""
import pandas as pd
MASTER_FILE = "./master/master_page.txt"
CARTA = "./carta/carta.xls"
master = MasterClass (MASTER_FILE)


# master.get_content(MASTER_FILE)

# num_sections = master.get_num_sections()
# print(num_sections)



# master.get_section(1)
# master.get_separator()
# master.get_dish()

df = pd.ExcelFile(CARTA)
secs = df.sheet_names

print(len(secs ))
# exit()

new_page = ""
new_page = new_page + master.do_intro()
cont = 1

for temp in secs:
    if (temp == "info_web"):
        break
    print(temp)

    master.get_section(cont)
    if cont == 1:
        master.get_separator()
        master.get_dish()
    df = pd.read_excel(CARTA, temp)
    section_dish = ""
    for i in range(len(df)):
        section_dish = section_dish + master.do_dish(df,i)
    new_page = new_page + section_dish
    if cont < len(secs )-1:
        new_page = new_page + str(master.do_inter_sections(cont))
    cont += 1

new_page = new_page + master.do_outro()

print(new_page)
exit()
exit()


# for i in range(1, num_sections+1):
#     print(i)
#     master.get_section(i)


df = pd.read_excel(CARTA, 'entrantes')
section_dish = ""
section_dish = section_dish + master.do_dish(df,0)
section_dish = section_dish + master.do_dish(df,1)
section_dish = section_dish + master.do_dish(df,2)
new_page = new_page + section_dish

new_page = new_page + str(master.do_inter_sections(1))

master.get_section(2)
df = pd.read_excel(CARTA, 'primeros')
section_dish = ""
section_dish = section_dish + master.do_dish(df,0)
section_dish = section_dish + master.do_dish(df,1)
section_dish = section_dish + master.do_dish(df,2)
new_page = new_page + section_dish

new_page = new_page + str(master.do_inter_sections(2))

master.get_section(3)
df = pd.read_excel(CARTA, 'segundos')
section_dish = ""
section_dish = section_dish + master.do_dish(df,0)
section_dish = section_dish + master.do_dish(df,1)
section_dish = section_dish + master.do_dish(df,2)
new_page = new_page + section_dish

new_page = new_page + str(master.do_inter_sections(3))

master.get_section(4)
df = pd.read_excel(CARTA, 'postres')
section_dish = ""
section_dish = section_dish + master.do_dish(df,0)
section_dish = section_dish + master.do_dish(df,1)
section_dish = section_dish + master.do_dish(df,2)
section_dish = section_dish + master.do_dish(df,3)
new_page = new_page + section_dish

new_page = new_page + master.do_outro()

print(new_page)
exit()





master.do_intro()
print("AAAAAAA")
master.do_outro()

master.get_inter_sections()
exit()

master.do_intro()
print("AAAAAAA")
master.do_outro()

master.get_section(1)
print("AAAAAAA")
master.get_separator()


master.get_dish()
df = pd.read_excel(CARTA, 'entrantes')

section_dish = section_dish + master.do_dish(df,0)
section_dish = section_dish + master.do_dish(df,1)
section_dish = section_dish + master.do_dish(df,2)

print(section_dish)

exit()

# print(df)
#
# print(df['nombre'][0])
# print(df['descripción'][0])
# print(df['precio'][0])
print(df['imagen'][0])
# print(df['alérgenos'][0])
#
# print(master.section)
# print("AAAAA")
# print(master.dish)


print(len(df))
