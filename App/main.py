from modulos.vistas import componentes as cmp

def main():
    cmp.configurar_pagina()
    pagina = cmp.menu_principal()
    cmp.actualizar_pagina(pagina)


#main()

import modulos.procesos.notas as notas

notas.cargar_estudiantes()