from pydantic import BaseModel, Field
from typing import Optional

class PatientInput(BaseModel):
    Horario_laboral: int = Field(..., alias="Horario laboral \n(Si = 1; No = 0)")
    Edad: float
    Tiempo_entre_creacion_cita_y_cita: int = Field(..., alias="Tiempo entre creación cita y cita")
    Confirmado_por_email: int = Field(..., alias="Confirmado por email")
    Paciente_NO_ubicado: int = Field(..., alias="Paciente NO ubicado")
    Confirmado_FAMILIAR: int = Field(..., alias="Confirmado FAMILIAR")
    Confirmado_PACIENTE: int = Field(..., alias="Confirmado PACIENTE")
    Confirmado: int
    Antecedente_No_Show: int = Field(..., alias="Antecedente No Show")
    Antecedente_Cita_Asistida: int = Field(..., alias="Antecedente Cita Asistida")
    Antecedente_Cita_Cancelada: int = Field(..., alias="Antecedente Cita Cancelada")
    Estudio_Simple: int = Field(..., alias="Estudio Simple")
    Anestesia: int
    Reprogramacion: int = Field(..., alias="Reprogramación")
    Reprogramacion_por_paciente: int = Field(..., alias="Reprogramación por paciente")
    Cita_adelantada: int = Field(..., alias="Cita adelantada")
    Estrato_socioeconomico: float = Field(..., alias="Estrato socioeconómico")
    Parte_del_Cuerpo_ABDOMEN: bool = Field(..., alias="Parte del Cuerpo_ABDOMEN")
    Parte_del_Cuerpo_CEREBRO: bool = Field(..., alias="Parte del Cuerpo_CEREBRO")
    Parte_del_Cuerpo_COLUMNA: bool = Field(..., alias="Parte del Cuerpo_COLUMNA")
    Parte_del_Cuerpo_CORAZON: bool = Field(..., alias="Parte del Cuerpo_CORAZON")
    Parte_del_Cuerpo_MAMA: bool = Field(..., alias="Parte del Cuerpo_MAMA")
    Parte_del_Cuerpo_MMII: bool = Field(..., alias="Parte del Cuerpo_MMII")
    Parte_del_Cuerpo_MMSS: bool = Field(..., alias="Parte del Cuerpo_MMSS")
    Parte_del_Cuerpo_OTRO: bool = Field(..., alias="Parte del Cuerpo_OTRO")
    Parte_del_Cuerpo_PELVIS: bool = Field(..., alias="Parte del Cuerpo_PELVIS")
    Parte_del_Cuerpo_PROSTATA: bool = Field(..., alias="Parte del Cuerpo_PROSTATA")
    Voluntario_Obligatorio: bool = Field(..., alias="Voluntario_Obligatorio")
    Voluntario_Voluntario: bool = Field(..., alias="Voluntario_Voluntario")
    RS_RC_OT: bool = Field(..., alias="RS / RC_OT")
    RS_RC_RC: bool = Field(..., alias="RS / RC_RC")
    RS_RC_RS: bool = Field(..., alias="RS / RC_RS")
    Sexo_Femenino: bool = Field(..., alias="Sexo_Femenino")
    Sexo_Masculino: bool = Field(..., alias="Sexo_Masculino")
    Grupo_etnico_Afroamericano: bool = Field(..., alias="Grupo étnico_Afroamericano")
    Grupo_etnico_Caucasico: bool = Field(..., alias="Grupo étnico_Caucásico")
    Grupo_etnico_Indigena: bool = Field(..., alias="Grupo étnico_Indígena")
    Grupo_etnico_Mestizo: bool = Field(..., alias="Grupo étnico_Mestizo")
    Grupo_etnico_Mulato: bool = Field(..., alias="Grupo étnico_Mulato")
    Grupo_etnico_Negro: bool = Field(..., alias="Grupo étnico_Negro")
    Grupo_etnico_NingunoAnterior: bool = Field(..., alias="Grupo étnico_NingunoAnterior")
    Grupo_etnico_Otro: bool = Field(..., alias="Grupo étnico_Otro")

    class Config:
        allow_population_by_field_name = True

