from validadorclave.errores import 
from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
  def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

  def _validar_longitud(self, clave):        return len(clave) > self._longitud_esperada
    

   def _contiene_mayuscula(self, clave):
        return any(char.isupper() for char in clave)

   def _contiene_minuscula(self, clave):
        return any(char.islower() for char in clave)

    def _contiene_numero(self, clave):
        return any(char.isdigit() for char in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave):
        especiales = 0
        return (char in especiales for char in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudError("La clave no tiene la longitud mínima requerida")
        if not self._contiene_mayuscula(clave):
            raise MayusculaError("La clave no contiene ninguna letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise MinusculaError("La clave no contiene ninguna letra minúscula")
        if not self._contiene_numero(clave):
            raise NumeroError("La clave no contiene ningún número")
        if not self.contiene_caracter_especial(clave):
            raise CaracterEspecialError("La clave no contiene un caracter especial permitido")
        
        return True

class ReglaValidacionCalisto(ReglaValidacion):
  def __init__(self):
        super().__init__(longitud_esperada=6)

   def contiene_calisto(self, clave):
        pos = clave.lower().find("calisto")
        if pos == -1:
            return False

        substring = clave[pos:pos + 7]
        mayusculas = sum(1 for char in substring if char.isupper())
        return 2 <= mayusculas < len(substring)

   def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudError("La clave no tiene la longitud mínima requerida")
        if not self._contiene_numero(clave):
            raise NumeroError("La clave no contiene ningún número")
        if not self.contiene_calisto(clave):
            raise PalabraCalistoError("La clave no contiene 'calisto' con al menos dos letras mayúsculas y no todas")

        return True


class Validador:
  def __init__(self, regla):
        self.regla = regla

   def es_valida(self, clave):
        return self.regla.es_valida(clave)
