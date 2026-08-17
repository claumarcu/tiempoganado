Documento 30 — Modelo de Datos
1. Objetivo

El modelo de datos de TiempoGanado debe representar los hechos, intereses y decisiones que necesita el sistema para construir segmentos, gestionar campañas y conservar el historial de las relaciones con los contactos.

El modelo debe permitir que TiempoGanado pase de la información almacenada sobre cada contacto a una selección de destinatarios para una comunicación, conservando posteriormente el resultado de esa comunicación.

El objetivo inicial es construir una estructura suficientemente sólida para el MVP, sin incorporar complejidad que corresponda a etapas posteriores.

2. Principios del modelo
2.1. Guardar hechos, no conclusiones cuando estas puedan derivarse

Cuando una información pueda obtenerse a partir de hechos registrados, no debería requerir mantenimiento manual.

Por ejemplo:

Alumno / no alumno.
Realizó alguna actividad / no.
Modalidad histórica.
Cantidad de actividades.
Cantidad de cursos.
Contacto valioso.
Última actividad.

El sistema debe conservar los hechos que permiten obtener estos datos y calcular las conclusiones cuando sean necesarias.

2.2. Separar hechos, intereses y decisiones

El modelo distingue:

Hechos: lo que ocurrió.

Intereses: lo que sabemos que le interesa a una persona.

Decisiones manuales: instrucciones explícitas de Claudia sobre cómo debe tratar el sistema a una persona.

Esta separación evita convertir una decisión o una interpretación en un supuesto hecho histórico.

2.3. Conservar el historial

Un contacto no desaparece porque:

deje de participar;
deje de recibir comunicaciones;
sea marcado como no elegible;
deje de estar activo.

Su historial debe conservarse para poder reconocerlo si vuelve a comunicarse.

2.4. No almacenar información innecesaria

TiempoGanado no necesita registrar información que no pueda utilizar de manera confiable.

Por ejemplo, no es necesario saber si una persona terminó de ver un curso grabado.

2.5. No duplicar información derivable

Los datos derivados deben obtenerse a partir de los hechos registrados siempre que sea posible.

Esto evita contradicciones y reduce la necesidad de mantenimiento manual.

3. Contacto

Un Contacto representa a una persona con la que TiempoGanado tiene o tuvo algún vínculo.

El contacto permanece en la base aunque deje de participar o tenga decisiones de exclusión.

3.1. Datos básicos

El contacto debe poder conservar, como mínimo:

nombre;
teléfono;
email;
origen;
estado operativo;
fecha de incorporación al sistema.

La estructura actual de la base ya contiene varios de estos datos.

3.2. Datos derivados

No es necesario mantener manualmente en el contacto:

Alumno / no alumno;
Realizó alguna actividad / no;
Modalidad histórica;
Cantidad de actividades;
Cantidad de cursos;
Contacto valioso.

Estos datos se obtienen del historial.

3.3. Ubicación

El contacto puede tener una ubicación estimada:

AMBA;
Fuera de AMBA;
Desconocida.

Inicialmente puede inferirse a partir del número telefónico.

La inferencia debe considerarse aproximada y no como una confirmación de domicilio.

Si posteriormente existe una ubicación confirmada, esta puede prevalecer sobre la estimación.

La ubicación se utilizará principalmente como criterio de segmentación.

3.4. Contacto activo

Se considera contacto activo a una persona que posee un medio de contacto válido, no solicitó dejar de recibir comunicaciones y no fue archivada manualmente.

4. Actividad

Una Actividad representa cualquier propuesta, evento o instancia de participación que TiempoGanado necesita registrar en relación con sus contactos.

Ejemplos:

Curso;
Jam;
Workshop;
Jornada;
Exposición;
otras actividades futuras.
4.1. Datos básicos

Toda actividad debe poder tener:

nombre;
tipo;
categoría;
modalidad;
estado;
fecha o período, cuando corresponda.
4.2. Tipo

El tipo indica qué clase de actividad es.

Por ejemplo:

Curso;
Jam;
Workshop;
Jornada;
Exposición.
4.3. Categoría

La categoría describe el área o temática de la actividad.

Por ejemplo:

Edición;
Autoral;
Iluminación.

No se establece en este documento una lista cerrada de categorías.

4.4. Modalidad

La modalidad pertenece a la actividad.

Puede ser:

Online;
Presencial;
eventualmente ambas.
4.5. Estado

Una actividad debe poder permanecer registrada aunque ya no esté disponible.

Una actividad finalizada no debe eliminarse porque continúa formando parte del historial de los contactos.

4.6. Requisitos de participación

Una actividad puede tener requisitos específicos para participar.

Los requisitos pertenecen a la actividad correspondiente y no deben confundirse con los criterios utilizados para segmentar la comunicación.

Por ejemplo, una actividad puede requerir haber realizado una actividad anterior.

La definición técnica de estos requisitos y su lógica de aplicación se desarrollará posteriormente.

5. Participación

Una Participación representa el hecho de que un contacto tuvo una relación efectiva con una actividad.

Es la relación entre:

Contacto ↔ Actividad

Una persona puede tener muchas participaciones y una actividad puede tener muchos participantes.

5.1. Qué significa participar

La participación no implica que la persona haya completado la actividad.

En un curso, el hecho relevante es que la persona se inscribió/adquirió el curso y obtuvo acceso.

No es necesario registrar si posteriormente terminó de verlo.

En otras actividades, la participación representa la relación correspondiente con esa actividad.

5.2. Datos mínimos

Una participación debe conservar:

contacto;
actividad;
tipo de participación;
fecha.

La estructura actual enrollments representa parcialmente esta relación para los cursos. Durante la implementación deberá evaluarse cómo integrar esa información al modelo general de Participación sin mantener dos sistemas paralelos.

5.3. Casos excepcionales

Una persona que reservó una actividad pero no pagó ni asistió no debe registrarse como una participación realizada.

Ese antecedente puede conservarse como observación asociada al contacto.

Si además Claudia toma una decisión respecto de esa persona, dicha decisión se registra por separado como decisión manual.

6. Intereses

Un Interés representa algo que sabemos que una persona quiere conocer, recibir o explorar dentro de la propuesta de TiempoGanado.

Los intereses son independientes de las actividades que la persona haya realizado.

Una persona puede tener intereses aunque nunca haya realizado una actividad.

6.1. Características

Los intereses:

pueden ser múltiples;
se registran principalmente de forma manual;
pueden modificarse con el tiempo;
funcionan como criterios de segmentación.
6.2. Intereses y comunicaciones

Un interés indica qué tipo de comunicación puede resultar pertinente para una persona.

No constituye por sí mismo una autorización de envío.

Si una persona tiene interés en Edición pero existe una decisión de No recibir mensajes, no debe ser incluida en campañas.

Los intereses no deben eliminarse automáticamente cuando una persona deja de recibir comunicaciones.

La posibilidad de actualizar intereses mediante una campaña específica queda fuera del alcance actual y se conserva en Parking.

7. Decisiones manuales

Una Decisión manual representa una decisión explícita de Claudia sobre cómo debe tratar TiempoGanado a un contacto.

Las decisiones manuales permiten que el criterio humano prevalezca sobre las reglas automáticas.

No modifican los hechos históricos.

7.1. No recibir mensajes

Indica que el contacto no debe ser incluido en campañas de comunicación.

Esta decisión:

prevalece sobre sus intereses;
prevalece sobre los criterios de segmentación;
no elimina al contacto;
no elimina sus intereses;
no elimina su historial.
7.2. No elegible para actividades

Indica que el contacto no debe ser incluido en propuestas o segmentos destinados a actividades.

Puede utilizarse, por ejemplo, ante:

deudas pendientes;
incumplimientos;
reservas no pagadas;
situaciones conflictivas;
otros casos excepcionales.

Puede conservarse el motivo de la decisión.

La persona permanece en la base y conserva su historial.

7.3. Habilitación para una actividad específica

Permite que Claudia habilite manualmente a una persona para una actividad aunque no cumpla el criterio automático correspondiente.

Por ejemplo:

Una persona no realizó Photoshop I, pero Claudia considera que tiene conocimientos suficientes y decide habilitarla para Photoshop II.

La habilitación:

corresponde a una actividad concreta;
no convierte a la persona en alumno;
no modifica el historial;
permite considerarla al construir el segmento correspondiente.

Una habilitación para una actividad no implica habilitación para otras.

8. Historial de comunicaciones

El historial de comunicaciones registra la relación entre TiempoGanado y cada contacto a través de las comunicaciones realizadas.

No es necesario almacenar dentro de TiempoGanado el contenido completo de las conversaciones de WhatsApp.

8.1. Información a conservar

Para cada comunicación asociada a un contacto:

contacto;
campaña;
fecha y hora;
estado del envío;
si hubo respuesta;
fecha de respuesta.
8.2. Estado del envío

Para el MVP:

Pendiente;
Enviado;
Fallido.
8.3. Respuesta

El sistema debe registrar si el contacto respondió a una comunicación y cuándo.

La interpretación de esa respuesta y las reglas de seguimiento pertenecen al Documento 20.

9. Campañas y destinatarios

Una Campaña representa una acción de comunicación concreta dirigida a un segmento.

Una campaña puede estar asociada a una actividad cuando corresponda, pero no es obligatorio que toda campaña comunique una actividad.

Una campaña debe poder conservar:

actividad asociada, cuando corresponda;
segmento utilizado;
mensaje;
adjuntos, cuando existan;
fecha y hora;
resultado general.
9.1. Destinatarios

Cada destinatario debe registrarse individualmente.

Esto permite conocer qué ocurrió con cada persona.

Por ejemplo:

Campaña Lightroom
│
├── Miguel → enviado → respondió
├── Laura → enviado → no respondió
├── Ana → fallido
└── Pedro → enviado → respondió
9.2. Resultados

Los resultados generales de una campaña deben poder calcularse a partir de los registros individuales:

enviados;
fallidos;
respondidos;
pendientes;
tasa de respuesta.

Estos valores no necesitan almacenarse como datos independientes.

10. Datos derivados

Los datos derivados son valores que TiempoGanado puede obtener automáticamente a partir de los hechos registrados.

10.1. Realizó alguna actividad

Sí cuando existe al menos una participación válida.

Puede incluir:

curso;
workshop;
jornada;
Jam;
exposición.
10.2. Alumno

Una persona es considerada alumno cuando realizó al menos una actividad formativa.

Actualmente se consideran formativas:

Curso;
Workshop;
Jornada.

Por ahora:

Jam → no;
Exposición → no.

Esta clasificación podrá revisarse en el futuro sin modificar el historial.

10.3. Modalidad histórica

Se obtiene a partir de las modalidades de las actividades realizadas:

Online;
Presencial;
Ambas;
Sin actividad registrada.

No representa dónde vive actualmente la persona.


10.4. Cantidad de actividades

El sistema debe poder calcular la cantidad total de actividades en las que participó cada contacto.

Este valor permite realizar estadísticas y segmentaciones según distintos niveles de participación.

Por ejemplo, puede consultarse cuántos contactos realizaron 4, 5, 7 o más actividades.

10.5. Cantidad de actividades relevantes

El sistema debe poder calcular la cantidad de actividades relevantes para el vínculo realizadas por cada contacto.

Para este indicador cuentan:

- Cursos;
- Workshops;
- Jornadas;
- Exposiciones.

Las Jams quedan fuera de este cálculo por ahora.

Este valor se utiliza, entre otras cosas, para determinar el criterio de Contacto valioso.

10.6. Contacto valioso

Un contacto es considerado valioso cuando realizó 4 o más actividades relevantes para el vínculo.

Para este cálculo cuentan por igual:

Cursos;
Workshops;
Jornadas;
Exposiciones.

Las Jams quedan fuera de este cálculo por ahora.

El valor del contacto se relaciona con la recurrencia de participación, no con el tipo o precio de una actividad determinada.

El umbral de 4 es configurable y puede modificarse en el futuro sin alterar los datos históricos.

10.7. Cantidad de cursos

Cantidad de cursos realizados por el contacto.

10.8. Última actividad

Permite conocer cuál fue la actividad más reciente registrada y cuándo ocurrió.

Este dato permitirá posteriormente construir segmentos basados en recencia.

10.9. Ubicación estimada

La ubicación puede inferirse inicialmente a partir del número telefónico:

AMBA;
fuera de AMBA;
desconocida.

La inferencia es aproximada.

Una ubicación confirmada puede prevalecer sobre la estimación.

11. Segmentación

La segmentación es el proceso mediante el cual TiempoGanado determina qué contactos pueden formar parte de una campaña.

Para construir un segmento consulta:

hechos;
intereses;
decisiones manuales;
datos derivados;
historial de comunicaciones cuando sea relevante.

La segmentación no modifica los datos del contacto. Produce una selección de destinatarios.

11.1. Criterios

Los criterios pueden combinarse.

Por ejemplo:

Personas que realizaron Photoshop I + contactos activos + ubicación AMBA.

O:

Personas interesadas en Edición + que nunca realizaron una actividad.

O:

Alumnos + modalidad histórica Online.

11.2. Requisitos, segmentación y decisiones

Son conceptos diferentes.

Requisito: define una condición de participación de una actividad.

Segmentación: define a quién se desea comunicar una actividad o campaña.

Decisión manual: permite modificar el resultado automático para un contacto determinado.

11.3. Aplicación de decisiones manuales

El proceso conceptual es:

Criterios automáticos
        ↓
Segmento propuesto
        ↓
Aplicar decisiones manuales
        ↓
Segmento final
        ↓
Campaña

Las exclusiones deben prevalecer sobre la selección automática.

Una habilitación específica puede incorporar una persona que no hubiera sido seleccionada automáticamente.

11.4. Ubicación y segmentación

Para actividades presenciales, AMBA puede utilizarse como criterio de segmentación.

No constituye por sí mismo un requisito de participación.

Una persona de fuera de AMBA puede ser incluida manualmente si Claudia decide hacerlo.

12. Observaciones y antecedentes

TiempoGanado debe poder conservar información relevante sobre un contacto que no constituye:

una participación;
un interés;
una decisión manual.

Por ejemplo:

"Reservó una jornada, no pagó y no asistió."

Una observación:

no cuenta como actividad;
no convierte al contacto en alumno;
no modifica sus intereses;
no genera por sí misma una acción automática.

Si ese antecedente genera una instrucción para el sistema, esa instrucción debe registrarse como decisión manual.

Las observaciones permiten conservar situaciones particulares sin convertir cada excepción en una categoría del modelo.

13. Relaciones entre entidades

Las principales relaciones conceptuales son:

CONTACTO
   │
   ├──────── INTERESES
   │
   ├──────── DECISIONES MANUALES
   │
   ├──────── OBSERVACIONES
   │
   ├──────── PARTICIPACIONES ───── ACTIVIDAD
   │
   └──────── DESTINATARIOS ─────── CAMPAÑA

Una actividad puede tener muchas participaciones.

Un contacto puede tener muchas participaciones.

Una campaña puede tener muchos destinatarios.

Un contacto puede recibir muchas campañas.

Por lo tanto:

Contacto ↔ Participación ↔ Actividad


Contacto ↔ Destinatario ↔ Campaña

Estas relaciones deberán representarse mediante estructuras intermedias adecuadas durante la implementación.

14. Modelo actual vs. modelo requerido

La base SQLite existente contiene actualmente:

contactos
mensajes
courses
enrollments

Además existe sqlite_sequence, que corresponde al funcionamiento interno de SQLite y no forma parte del modelo funcional.

contactos

Ya conserva:

identificador;
nombre;
teléfono;
email;
etiquetas;
estado;
origen;
fecha de incorporación.

Constituye la base del modelo de Contacto.

courses

Ya conserva:

nombre;
categoría;
modalidad;
área.

Constituye una primera versión del concepto de Actividad, aunque deberá ampliarse para representar otros tipos.

enrollments

Ya relaciona:

contacto;
curso;
fecha;
evento;
fuente.

Constituye una primera versión de Participación.

Deberá evaluarse cómo integrar esta información al modelo general sin mantener dos estructuras paralelas.

mensajes

Ya conserva:

contacto;
mensaje;
fecha.

Constituye una primera versión del historial de comunicaciones.

Deberá evaluarse cómo conservar esta información al incorporar campañas, destinatarios, estados de envío y respuestas.

Información que todavía no tiene estructura específica

El modelo requerido necesita representar explícitamente:

intereses;
decisiones manuales;
actividades generales;
participaciones generales;
campañas;
destinatarios;
resultados de envíos;
respuestas;
observaciones;
ubicación.

La implementación deberá determinar la estructura técnica necesaria para cada caso.

15. Alcance del MVP

El MVP debe permitir:

conservar contactos;
conservar historial de actividades;
registrar intereses;
registrar decisiones manuales;
construir segmentos;
crear campañas;
determinar destinatarios;
enviar mensajes;
registrar resultados de envío;
registrar si hubo respuesta y cuándo.
Datos derivados necesarios

El MVP debe poder obtener:

realizó alguna actividad;
alumno/no alumno;
modalidad histórica;
cantidad de actividades;
cantidad de cursos;
contacto valioso;
última actividad;
ubicación estimada.
Fuera del MVP

No es necesario implementar inicialmente:

interpretación automática de conversaciones;
seguimiento comercial automatizado;
reglas de seguimiento;
análisis semántico de respuestas;
actualización automática de intereses mediante conversaciones;
funciones avanzadas de recomendación.

Estas funcionalidades quedan fuera de alcance y, cuando corresponda, se conservan en Parking o se desarrollan en documentos posteriores.

Ciclo mínimo
CONTACTOS
    ↓
DATOS + HISTORIAL
    ↓
SEGMENTACIÓN
    ↓
CAMPAÑA
    ↓
DESTINATARIOS
    ↓
ENVÍO
    ↓
RESULTADO
    ↓
RESPUESTA
16. Reglas de integridad y consistencia
16.1. No duplicar información derivable

Los datos que puedan calcularse a partir de hechos no deben requerir mantenimiento manual.

16.2. No borrar historial por cambios de estado

Las decisiones de exclusión o cambios de actividad no eliminan el historial.

16.3. No registrar como participación una actividad no realizada

Una reserva no pagada o una ausencia no constituye una participación realizada.

16.4. Las decisiones manuales no modifican los hechos

Una habilitación para Photoshop II no significa que la persona haya realizado Photoshop I.

16.5. Las exclusiones prevalecen

Las decisiones de no recibir mensajes y no elegibilidad deben aplicarse antes de producir el conjunto final de destinatarios.

16.6. No convertir excepciones en reglas generales

Una condición específica de una actividad no debe convertirse automáticamente en una regla permanente del sistema.

17. Evolución del modelo

El modelo definido constituye la estructura conceptual necesaria para evolucionar desde la base existente hacia un sistema de segmentación y comunicación.

La implementación debe avanzar de manera incremental.

Primero debe funcionar el ciclo:

CONTACTOS
   ↓
DATOS + HISTORIAL
   ↓
SEGMENTACIÓN
   ↓
CAMPAÑA
   ↓
ENVÍO
   ↓
RESULTADO

Sobre esta estructura podrán incorporarse posteriormente funciones de:

seguimiento comercial;
interpretación de respuestas;
automatización;
actualización de intereses;
análisis de comportamiento;
otras funciones registradas en Parking.

La incorporación de nuevas funciones no debe romper el historial existente ni obligar a reconstruir la información ya registrada.

18. Estado del documento

El modelo conceptual queda definido en este documento.

La siguiente etapa consiste en traducirlo a un modelo técnico de datos, comparando cada entidad conceptual con la estructura actual de alumnos.db y determinando:

qué tablas pueden conservarse;
cuáles deben modificarse;
cuáles deben incorporarse;
cómo conservar los datos existentes;
qué cambios son necesarios para el MVP.

Este documento no define todavía el código de implementación ni el esquema SQL definitivo.