"""
AGENDA PERSONAL - Sistema de Gestión de Contactos
Programa que permite agregar, consultar, editar y eliminar registros de contactos personales.
Almacena los datos en un archivo JSON para persistencia.
"""

import json
import os
from datetime import datetime

# Ruta del archivo de datos
ARCHIVO_DATOS = "contactos.json"

# ============================================================================
# SISTEMA DE CACHÉ EN MEMORIA
# ============================================================================

# Caché global para almacenar contactos en memoria
_cache_contactos = None
_cache_cargado = False

def inicializar_cache():
    """Inicializa la caché cargando los contactos del archivo una sola vez"""
    global _cache_contactos, _cache_cargado
    
    if not _cache_cargado:
        _cache_contactos = _cargar_contactos_del_archivo()
        _cache_cargado = True
        print(f"✅ Caché inicializado con {len(_cache_contactos)} contacto(s)")
    
    return _cache_contactos

def obtener_contactos():
    """Retorna los contactos desde la caché"""
    global _cache_contactos, _cache_cargado
    
    if not _cache_cargado:
        inicializar_cache()
    
    return _cache_contactos

def actualizar_cache(contactos):
    """Actualiza la caché y sincroniza con el archivo"""
    global _cache_contactos
    _cache_contactos = contactos
    guardar_contactos(contactos)

# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================

def validar_id(id_valor):
    """Valida que el ID sea un número entero positivo"""
    try:
        id_int = int(id_valor)
        if id_int > 0:
            return True, id_int
        else:
            return False, None
    except ValueError:
        return False, None

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío y contenga solo letras y espacios"""
    if not nombre or not nombre.strip():
        return False
    # Permitir letras, números, espacios y algunos caracteres comunes
    return True

def validar_telefono(telefono):
    """Valida que el teléfono tenga máximo 10 dígitos y solo contenga números"""
    telefono_limpio = telefono.replace(" ", "").replace("-", "").replace("+", "")
    
    if not telefono_limpio.isdigit():
        return False
    
    if len(telefono_limpio) > 10:
        return False
    
    if len(telefono_limpio) == 0:
        return False
    
    return True

def validar_correo(correo):
    """Valida que el correo tenga un formato básico válido"""
    if not correo or not correo.strip():
        return False
    
    # Validación básica de correo
    if "@" not in correo or "." not in correo:
        return False
    
    partes = correo.split("@")
    if len(partes) != 2 or not partes[0] or not partes[1]:
        return False
    
    if "." not in partes[1]:
        return False
    
    return True

def validar_direccion(direccion):
    """Valida que la dirección no esté vacía"""
    if not direccion or not direccion.strip():
        return False
    return True

# ============================================================================
# FUNCIONES DE MANEJO DE ARCHIVOS
# ============================================================================

def _cargar_contactos_del_archivo():
    """Carga los contactos desde el archivo JSON. Si no existe, retorna lista vacía"""
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                if contenido.strip():
                    return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error al leer el archivo. Se iniciará con una lista vacía.")
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}")
    
    return []

def guardar_contactos(contactos):
    """Guarda los contactos en el archivo JSON"""
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            json.dump(contactos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error al guardar los datos: {e}")
        return False

def obtener_proximo_id(contactos):
    """Obtiene el siguiente ID disponible"""
    if not contactos:
        return 1
    
    ids_existentes = [int(contacto['id']) for contacto in contactos if 'id' in contacto]
    return max(ids_existentes) + 1 if ids_existentes else 1

# ============================================================================
# FUNCIONES CRUD
# ============================================================================

def agregar_registro(contactos):
    """Agrega un nuevo contacto a la agenda"""
    print("\n" + "=" * 60)
    print("➕ AGREGAR NUEVO CONTACTO")
    print("=" * 60)
    
    # Capturar nombre
    while True:
        nombre = input("📝 Nombre completo: ").strip()
        if validar_nombre(nombre):
            break
        print("❌ El nombre no puede estar vacío.")
    
    # Verificar duplicados por nombre
    if any(contacto['nombre'].lower() == nombre.lower() for contacto in contactos):
        print("❌ Ya existe un contacto con este nombre.")
        return
    
    # Capturar teléfono
    while True:
        telefono = input("📱 Teléfono (máximo 10 dígitos): ").strip()
        if validar_telefono(telefono):
            break
        print("❌ El teléfono debe tener máximo 10 dígitos y solo números.")
    
    # Capturar correo
    while True:
        correo = input("📧 Correo electrónico: ").strip()
        if validar_correo(correo):
            break
        print("❌ El correo no es válido. Use formato: usuario@dominio.com")
    
    # Capturar dirección
    while True:
        direccion = input("🏠 Dirección: ").strip()
        if validar_direccion(direccion):
            break
        print("❌ La dirección no puede estar vacía.")
    
    # Crear nuevo contacto
    nuevo_id = obtener_proximo_id(contactos)
    nuevo_contacto = {
        'id': str(nuevo_id),
        'nombre': nombre,
        'telefono': telefono,
        'correo': correo,
        'direccion': direccion,
        'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    contactos.append(nuevo_contacto)
    
    # Actualizar caché y archivo
    actualizar_cache(contactos)
    print(f"\n✅ Contacto agregado exitosamente con ID: {nuevo_id}")

def consultar_registros(contactos):
    """Muestra todos los registros de manera ordenada"""
    print("\n" + "=" * 60)
    print("📋 CONSULTAR CONTACTOS")
    print("=" * 60)
    
    if not contactos:
        print("❌ No hay contactos registrados.")
        return
    
    print("\n1. Ver todos los contactos")
    print("2. Buscar por ID")
    print("3. Buscar por nombre")
    print("4. Volver al menú principal")
    
    opcion = input("\nElige una opción (1-4): ").strip()
    
    if opcion == "1":
        mostrar_tabla_contactos(contactos)
    
    elif opcion == "2":
        buscar_por_id(contactos)
    
    elif opcion == "3":
        buscar_por_nombre(contactos)
    
    elif opcion == "4":
        return
    
    else:
        print("❌ Opción no válida.")

def mostrar_tabla_contactos(contactos):
    """Muestra todos los contactos en formato tabla"""
    print("\n" + "-" * 120)
    print(f"{'ID':<5} | {'Nombre':<25} | {'Teléfono':<15} | {'Correo':<30} | {'Dirección':<35}")
    print("-" * 120)
    
    for contacto in contactos:
        id_val = contacto.get('id', 'N/A')
        nombre = contacto.get('nombre', 'N/A')[:25]
        telefono = contacto.get('telefono', 'N/A')[:15]
        correo = contacto.get('correo', 'N/A')[:30]
        direccion = contacto.get('direccion', 'N/A')[:35]
        
        print(f"{id_val:<5} | {nombre:<25} | {telefono:<15} | {correo:<30} | {direccion:<35}")
    
    print("-" * 120)

def buscar_por_id(contactos):
    """Busca un contacto por ID"""
    while True:
        id_busqueda = input("\n🔍 Ingresa el ID a buscar: ").strip()
        valido, id_int = validar_id(id_busqueda)
        if valido:
            break
        print("❌ ID inválido. Debe ser un número positivo.")
    
    id_str = str(id_int)
    contacto_encontrado = next((c for c in contactos if c.get('id') == id_str), None)
    
    if contacto_encontrado:
        print("\n" + "=" * 60)
        print("📌 CONTACTO ENCONTRADO")
        print("=" * 60)
        mostrar_contacto_detallado(contacto_encontrado)
    else:
        print(f"❌ No se encontró contacto con ID {id_int}.")

def buscar_por_nombre(contactos):
    """Busca contactos por nombre (búsqueda parcial)"""
    nombre_busqueda = input("\n🔍 Ingresa el nombre (o parte del nombre) a buscar: ").strip().lower()
    
    if not nombre_busqueda:
        print("❌ La búsqueda no puede estar vacía.")
        return
    
    resultados = [c for c in contactos if nombre_busqueda in c.get('nombre', '').lower()]
    
    if resultados:
        print("\n" + "=" * 60)
        print(f"📌 RESULTADOS DE LA BÚSQUEDA ({len(resultados)} encontrado(s))")
        print("=" * 60)
        
        for contacto in resultados:
            mostrar_contacto_detallado(contacto)
            print("-" * 60)
    else:
        print(f"❌ No se encontraron contactos con '{nombre_busqueda}' en el nombre.")

def mostrar_contacto_detallado(contacto):
    """Muestra los detalles completos de un contacto"""
    print(f"ID:                  {contacto.get('id', 'N/A')}")
    print(f"Nombre:              {contacto.get('nombre', 'N/A')}")
    print(f"Teléfono:            {contacto.get('telefono', 'N/A')}")
    print(f"Correo:              {contacto.get('correo', 'N/A')}")
    print(f"Dirección:           {contacto.get('direccion', 'N/A')}")
    print(f"Fecha de creación:   {contacto.get('fecha_creacion', 'N/A')}")

def editar_registro(contactos):
    """Edita un registro existente"""
    print("\n" + "=" * 60)
    print("✏️  EDITAR CONTACTO")
    print("=" * 60)
    
    if not contactos:
        print("❌ No hay contactos para editar.")
        return
    
    # Mostrar todos los contactos
    mostrar_tabla_contactos(contactos)
    
    # Solicitar ID del contacto a editar
    while True:
        id_editar = input("\n🔍 Ingresa el ID del contacto a editar: ").strip()
        valido, id_int = validar_id(id_editar)
        if valido:
            break
        print("❌ ID inválido. Debe ser un número positivo.")
    
    id_str = str(id_int)
    indice_contacto = next((i for i, c in enumerate(contactos) if c.get('id') == id_str), None)
    
    if indice_contacto is None:
        print(f"❌ No se encontró contacto con ID {id_int}.")
        return
    
    contacto = contactos[indice_contacto]
    
    print("\n" + "-" * 60)
    print("Contacto actual:")
    mostrar_contacto_detallado(contacto)
    print("-" * 60)
    
    # Mostrar opciones de edición
    print("\n¿Qué deseas editar?")
    print("1. Nombre")
    print("2. Teléfono")
    print("3. Correo")
    print("4. Dirección")
    print("5. Todos los campos")
    print("6. Cancelar")
    
    opcion = input("\nElige una opción (1-6): ").strip()
    
    cambios_realizados = False
    
    if opcion == "1":
        nuevo_nombre = input("📝 Nuevo nombre: ").strip()
        if validar_nombre(nuevo_nombre):
            if any(c['nombre'].lower() == nuevo_nombre.lower() and c.get('id') != id_str for c in contactos):
                print("❌ Ya existe otro contacto con este nombre.")
                return
            contacto['nombre'] = nuevo_nombre
            print("✅ Nombre actualizado.")
            cambios_realizados = True
        else:
            print("❌ Nombre inválido.")
            return
    
    elif opcion == "2":
        nuevo_telefono = input("📱 Nuevo teléfono (máximo 10 dígitos): ").strip()
        if validar_telefono(nuevo_telefono):
            contacto['telefono'] = nuevo_telefono
            print("✅ Teléfono actualizado.")
            cambios_realizados = True
        else:
            print("❌ Teléfono inválido.")
            return
    
    elif opcion == "3":
        nuevo_correo = input("📧 Nuevo correo: ").strip()
        if validar_correo(nuevo_correo):
            contacto['correo'] = nuevo_correo
            print("✅ Correo actualizado.")
            cambios_realizados = True
        else:
            print("❌ Correo inválido.")
            return
    
    elif opcion == "4":
        nueva_direccion = input("🏠 Nueva dirección: ").strip()
        if validar_direccion(nueva_direccion):
            contacto['direccion'] = nueva_direccion
            print("✅ Dirección actualizada.")
            cambios_realizados = True
        else:
            print("❌ Dirección inválida.")
            return
    
    elif opcion == "5":
        print("\n--- Editar todos los campos ---")
        
        nuevo_nombre = input("📝 Nuevo nombre: ").strip()
        if not validar_nombre(nuevo_nombre):
            print("❌ Nombre inválido.")
            return
        if any(c['nombre'].lower() == nuevo_nombre.lower() and c.get('id') != id_str for c in contactos):
            print("❌ Ya existe otro contacto con este nombre.")
            return
        
        nuevo_telefono = input("📱 Nuevo teléfono (máximo 10 dígitos): ").strip()
        if not validar_telefono(nuevo_telefono):
            print("❌ Teléfono inválido.")
            return
        
        nuevo_correo = input("📧 Nuevo correo: ").strip()
        if not validar_correo(nuevo_correo):
            print("❌ Correo inválido.")
            return
        
        nueva_direccion = input("🏠 Nueva dirección: ").strip()
        if not validar_direccion(nueva_direccion):
            print("❌ Dirección inválida.")
            return
        
        contacto['nombre'] = nuevo_nombre
        contacto['telefono'] = nuevo_telefono
        contacto['correo'] = nuevo_correo
        contacto['direccion'] = nueva_direccion
        print("✅ Todos los campos actualizados.")
        cambios_realizados = True
    
    elif opcion == "6":
        print("❌ Operación cancelada.")
        return
    
    else:
        print("❌ Opción no válida.")
        return
    
    # Actualizar caché y archivo si hay cambios
    if cambios_realizados:
        actualizar_cache(contactos)
        print("✅ Cambios guardados en el archivo.")

def eliminar_registro(contactos):
    """Elimina un registro existente"""
    print("\n" + "=" * 60)
    print("🗑️  ELIMINAR CONTACTO")
    print("=" * 60)
    
    if not contactos:
        print("❌ No hay contactos para eliminar.")
        return
    
    # Mostrar todos los contactos
    mostrar_tabla_contactos(contactos)
    
    # Solicitar ID del contacto a eliminar
    while True:
        id_eliminar = input("\n🔍 Ingresa el ID del contacto a eliminar: ").strip()
        valido, id_int = validar_id(id_eliminar)
        if valido:
            break
        print("❌ ID inválido. Debe ser un número positivo.")
    
    id_str = str(id_int)
    indice_contacto = next((i for i, c in enumerate(contactos) if c.get('id') == id_str), None)
    
    if indice_contacto is None:
        print(f"❌ No se encontró contacto con ID {id_int}.")
        return
    
    contacto = contactos[indice_contacto]
    
    # Mostrar contacto a eliminar
    print("\n" + "-" * 60)
    print("⚠️  Contacto a eliminar:")
    mostrar_contacto_detallado(contacto)
    print("-" * 60)
    
    # Confirmar eliminación
    confirmacion = input("\n¿Está seguro de que desea eliminar este contacto? (S/N): ").strip().upper()
    
    if confirmacion == "S":
        contactos.pop(indice_contacto)
        # Actualizar caché y archivo
        actualizar_cache(contactos)
        print("✅ Contacto eliminado exitosamente.")
    else:
        print("❌ Operación cancelada.")

# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("📞 AGENDA PERSONAL - SISTEMA DE GESTIÓN DE CONTACTOS")
    print("=" * 60)
    print("1. ➕ Agregar registro")
    print("2. 📋 Consultar registro")
    print("3. ✏️  Editar registro")
    print("4. 🗑️  Eliminar registro")
    print("5. 🚪 Salir")
    print("=" * 60)

def menu_principal():
    """Función principal que controla el flujo del programa"""
    print("\n🎉 Bienvenido a la Agenda Personal")
    
    # Inicializar caché (carga datos una sola vez)
    contactos = inicializar_cache()
    
    while True:
        mostrar_menu()
        
        opcion = input("\nElige una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_registro(contactos)
        
        elif opcion == "2":
            consultar_registros(contactos)
        
        elif opcion == "3":
            editar_registro(contactos)
        
        elif opcion == "4":
            eliminar_registro(contactos)
        
        elif opcion == "5":
            print("\n" + "=" * 60)
            print("👋 ¡Gracias por usar la Agenda Personal!")
            print(f"📁 Total de contactos guardados: {len(contactos)}")
            print("=" * 60 + "\n")
            break
        
        else:
            print("❌ Opción no válida. Intenta nuevamente.")
        
        input("\nPresiona Enter para continuar...")

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    menu_principal()




