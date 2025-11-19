import re

class Time:
    """Representa una hora con formato AM/PM o 24 horas."""

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HOURS"
        Time.time_count += 1

    # -------------------------------
    # Métodos privados y auxiliares
    # -------------------------------

    def __asign_format(self, pszFormat):
        """Asigna el formato si es válido (AM, PM o 24 HOURS)."""
        fmt = pszFormat.strip().upper()
        if fmt in Time.TIME_FORMATS:
            self.format = fmt
            return True
        return False

    def __is_24hour_format(self):
        """Devuelve True si el formato actual es de 24 horas."""
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        """Verifica si la hora, minutos y segundos están dentro de los rangos válidos."""
        if not (0 <= self.minutes <= 59 and 0 <= self.seconds <= 59):
            return False
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23
        else:
            return 1 <= self.hours <= 12

    # -------------------------------
    # Métodos públicos
    # -------------------------------

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        """Asigna una hora completa con validación de rango y formato."""
        if not self.__asign_format(pszFormato):
            return False

        self.hours = nHoras
        self.minutes = nMinutos
        self.seconds = nSegundos
        return self._is_valid_time()

    def get_time(self):
        """Devuelve la hora en formato de texto."""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """
        Crea un objeto Time a partir de una cadena.
        Acepta mayúsculas/minúsculas y espacios extra.
        Ejemplos válidos:
          - 02:30:00 PM
          - 14:00:00 24 HOURS
          - 7:05:02 am
          -  9:15:00   pM
        """
        # Eliminar espacios y normalizar mayúsculas
        time_string = time_string.strip().upper()

        # Expresión regular flexible
        pattern = r"^(\d{1,2}):(\d{2}):(\d{2})\s*(AM|PM|24 HOURS)$"
        match = re.match(pattern, time_string, re.IGNORECASE)

        if not match:
            print("❌ Formato de hora inválido. Usa HH:MM:SS FORMAT (por ejemplo 02:30:00 PM o 14:00:00 24 HOURS).")
            return None

        hours, minutes, seconds, fmt = match.groups()
        new_time = cls()
        if new_time.set_time(int(hours), int(minutes), int(seconds), fmt.upper()):
            return new_time
        else:
            print("❌ Hora fuera de rango. Revisa los valores de horas, minutos y segundos.")
            return None

    @staticmethod
    def is_valid_format(time_format):
        """Comprueba si el formato es válido."""
        return time_format.strip().upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """Devuelve cuántos objetos Time se han creado."""
        return cls.time_count


# ----------------------------------------
# FUNCIÓN EXTERNA PARA MOSTRAR LA HORA
# ----------------------------------------

def mostrar_hora(time_obj):
    """
    Devuelve una cadena con la hora formateada según el tipo (12h o 24h).
    """
    horas = time_obj.hours
    minutos = time_obj.minutes
    segundos = time_obj.seconds
    formato = time_obj.format

    if formato == "24 HOURS":
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    else:
        # Ajuste para formato 12 horas
        if horas == 0:
            horas = 12
        elif horas > 12:
            horas -= 12
        return f"{horas:02d}:{minutos:02d}:{segundos:02d} {formato}"
