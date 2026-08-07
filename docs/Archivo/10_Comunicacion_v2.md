# Documento 10
# Módulo de Comunicación

**Proyecto:** TiempoGanado

**Estado:** En auditoría

**Versión:** 2.0

---

# 1. Objetivo

El módulo de Comunicación permite planificar, segmentar y ejecutar campañas de difusión de las actividades de 2Marcu.

Su propósito es reducir el tiempo dedicado a la gestión manual de comunicaciones, manteniendo el criterio de Claudia como máxima autoridad en todas las decisiones.

El sistema nunca reemplaza el criterio humano.

Su función es asistir en la selección de destinatarios, ejecutar los envíos y registrar automáticamente toda la información generada durante cada campaña.

---

# 2. Alcance

Este documento define el funcionamiento completo del módulo de Comunicación.

Comprende:

- construcción de segmentos;
- reglas de selección;
- campañas;
- ejecución de envíos;
- registro de resultados;
- trazabilidad.

No comprende:

- seguimiento posterior de contactos;
- automatizaciones de seguimiento;
- respuestas automáticas;
- CRM;
- generación de contenido;
- campañas de reactivación.

Estos procesos serán definidos en documentos independientes.

---

# 3. Principios de diseño

## 3.1 Claudia toma las decisiones.

TiempoGanado propone.

Claudia decide.

Todas las decisiones manuales poseen prioridad absoluta sobre cualquier regla automática.

---

## 3.2 Una campaña comunica una única actividad.

Cada campaña comunica solamente una actividad.

Ejemplos:

- Photoshop I
- Lightroom
- Jam Photoshop
- Curso autoral

Nunca varias simultáneamente.

---

## 3.3 Un único mensaje por campaña.

Todos los destinatarios reciben el mismo mensaje.

Una campaña puede contener:

- texto;
- imágenes;
- videos;
- enlaces.

La personalización individual del contenido no forma parte del MVP.

---

## 3.4 Guardar hechos. No conclusiones.

TiempoGanado registra únicamente hechos.

Ejemplos:

Correcto

- Realizó Photoshop I.
- Participó en la Jam de agosto 2026.
- Respondió una campaña.

Incorrecto

- Hace mucho que no participa.
- Es un alumno avanzado.
- Participó en la última Jam.

Las conclusiones siempre serán calculadas por el sistema.

---

## 3.5 Toda campaña deja trazabilidad.

Cada comunicación deberá poder reconstruirse completamente.

El sistema deberá conservar toda la información necesaria para conocer qué ocurrió con cada destinatario.

---

# 4. Conceptos

## Actividad

Toda propuesta organizada por 2Marcu susceptible de ser comunicada mediante una campaña.

Ejemplos:

- Curso
- Jam
- Workshop
- Tutoría
- Exposición

---

## Campaña

Una campaña es el envío de una única comunicación a un segmento determinado de contactos.

Toda campaña posee:

- actividad;
- segmento;
- mensaje;
- archivos adjuntos (opcionales);
- fecha;
- resultado.

---

## Contacto activo

Se considera contacto activo a toda persona que:

- posee un medio de contacto válido;
- no solicitó dejar de recibir comunicaciones;
- no fue archivada manualmente.

Solo los contactos activos podrán ser incorporados automáticamente a campañas.

# 5. Flujo general de una campaña

Toda campaña sigue el mismo flujo de trabajo.

1. Selección de la actividad.
2. Construcción automática del segmento.
3. Revisión del segmento.
4. Redacción del mensaje.
5. Incorporación de archivos adjuntos.
6. Confirmación.
7. Ejecución del envío.
8. Registro automático de resultados.

Ninguna campaña puede ejecutarse sin una confirmación explícita de Claudia.

---

# 6. Selección de la actividad

Toda comunicación comienza seleccionando una actividad.

Las actividades disponibles serán definidas por el sistema y podrán ampliarse en el futuro.

Inicialmente el sistema contempla las siguientes actividades:

- Photoshop I
- Photoshop II
- Photoshop III
- Lightroom
- Jam Photoshop
- Jam Lightroom
- Workshops presenciales
- Cursos autorales
- Tutorías individuales
- Exposiciones

La actividad seleccionada determina automáticamente qué reglas de segmentación deberán aplicarse.

---

# 7. Construcción del segmento

Una vez seleccionada la actividad, TiempoGanado construye automáticamente un segmento de contactos.

El objetivo es evitar que Claudia tenga que seleccionar personas manualmente.

La construcción del segmento se realiza utilizando cuatro tipos de información.

## 7.1 Hechos

Los hechos representan información objetiva registrada por el sistema.

Ejemplos:

- cursos realizados;
- participación en Jam;
- participación en workshops;
- participación en exposiciones;
- ciudad de residencia.

Los hechos nunca se eliminan.

Constituyen el historial objetivo del contacto.

---

## 7.2 Intereses

Los intereses representan preferencias actuales del contacto.

Ejemplos:

- edición;
- fotografía autoral;
- actividades presenciales;
- actividades online.

Los intereses pueden obtenerse mediante:

- campañas de segmentación;
- conversaciones;
- decisiones manuales.

Los intereses pueden modificarse con el tiempo.

---

## 7.3 Decisiones manuales

Las decisiones manuales representan instrucciones dadas por Claudia que modifican el comportamiento automático del sistema.

Ejemplos:

- avisar próxima edición de Photoshop II;
- permitir comenzar directamente desde Photoshop III;
- incluir una persona en una campaña;
- excluir una persona de una campaña;
- contacto prioritario.

Las decisiones manuales poseen prioridad absoluta sobre cualquier regla automática.

---

## 7.4 Historial de comunicaciones

El historial registra todas las interacciones entre un contacto y 2Marcu.

Ejemplos:

- consultó por Photoshop;
- solicitó información;
- respondió una campaña;
- se inscribió;
- canceló una inscripción.

Este historial constituye la base para futuras campañas de seguimiento y reactivación.

---

# 8. Construcción y revisión del segmento

Una vez generado el segmento, TiempoGanado presenta un resumen antes del envío.

El objetivo es permitir una revisión rápida sin analizar contacto por contacto.

El sistema deberá mostrar grupos de personas.

Ejemplo:

- 84 realizaron Lightroom.
- 53 realizaron Photoshop I.
- 21 fueron agregados mediante decisiones manuales.
- 18 solicitaron recibir información sobre esta actividad.

Total del segmento: 176 contactos.

Desde esta pantalla Claudia podrá:

- aprobar el segmento;
- agregar contactos;
- excluir contactos;
- cancelar la campaña.

Toda modificación realizada en esta instancia tendrá prioridad sobre las reglas automáticas únicamente para esa campaña.

# 9. Reglas generales de segmentación

Todas las campañas respetan las siguientes reglas generales.

Estas reglas se aplican antes de evaluar la actividad específica.

## 9.1 Contactos excluidos

Nunca podrán incorporarse automáticamente a una campaña las personas que:

- solicitaron dejar de recibir comunicaciones;
- no poseen un medio de contacto válido;
- fueron archivadas manualmente.

Podrán ser incorporadas únicamente mediante una decisión manual.

---

## 9.2 Prioridad de decisiones

Cuando exista un conflicto entre una regla automática y una decisión manual, siempre prevalecerá la decisión manual.

Ejemplos:

- incluir una persona aunque normalmente quedaría excluida;
- excluir una persona aunque normalmente sería incluida;
- permitir comenzar un recorrido desde un curso avanzado;
- solicitar que una persona reciba nuevamente una actividad ya realizada.

---

## 9.3 Modificaciones del segmento

Toda modificación realizada manualmente durante la revisión del segmento afecta únicamente a la campaña en curso.

No modifica las reglas generales del sistema.

---

# 10. Reglas específicas por actividad

## 10.1 Photoshop I

### Objetivo

Incorporar nuevos alumnos al recorrido de Photoshop.

### Incluir automáticamente

- Contactos activos.

### Priorizar

- Personas que consultaron previamente por Photoshop.
- Personas que realizaron Lightroom.

### Excluir

- Personas que realizaron Photoshop I.
- Personas que realizaron Photoshop II.
- Personas que realizaron Photoshop III.

### Decisiones manuales posibles

- Incluir una persona.
- Excluir una persona.
- Avisar próxima edición.

---

## 10.2 Photoshop II

### Objetivo

Continuar el recorrido de formación.

### Incluir automáticamente

- Personas que realizaron Photoshop I.

### Excluir

- Personas que realizaron Photoshop II.
- Personas que realizaron Photoshop III.

### Decisiones manuales posibles

- Habilitar ingreso directo.
- Avisar próxima edición.
- Incluir una persona.
- Excluir una persona.

---

## 10.3 Photoshop III

### Objetivo

Completar el recorrido avanzado.

### Incluir automáticamente

- Personas que realizaron Photoshop II.

### Excluir

- Personas que realizaron Photoshop III.

### Decisiones manuales posibles

- Habilitar ingreso directo.
- Avisar próxima edición.
- Incluir una persona.
- Excluir una persona.

---

## 10.4 Lightroom

### Objetivo

Difundir el curso de Lightroom.

### Incluir automáticamente

- Todos los contactos activos.

### Excluir

- Personas que realizaron Lightroom.

### Decisiones manuales posibles

- Avisar próxima edición.
- Incluir una persona.
- Excluir una persona.

## 10.5 Jam Photoshop

### Objetivo

Mantener la continuidad del aprendizaje y desarrollar el criterio de edición en Photoshop.

### Incluir automáticamente

- Personas que realizaron al menos un módulo de Photoshop.
- Personas que participaron anteriormente en una Jam de Photoshop.

### Excluir

- Personas excluidas por las reglas generales de segmentación.

### Observaciones

Participar en una Jam nunca excluye futuras invitaciones.

La participación previa constituye un indicador de continuidad.

Las promociones o descuentos para participantes de la edición inmediatamente anterior forman parte de la estrategia comercial y no modifican las reglas de segmentación.

### Decisiones manuales posibles

- Avisar próxima Jam.
- Incluir una persona.
- Excluir una persona.

---

## 10.6 Jam Lightroom

### Objetivo

Mantener la continuidad del aprendizaje y desarrollar el criterio de edición en Lightroom.

### Incluir automáticamente

- Personas que realizaron Lightroom.
- Personas que participaron anteriormente en una Jam de Lightroom.

### Excluir

- Personas excluidas por las reglas generales de segmentación.

### Observaciones

Participar en una Jam nunca excluye futuras invitaciones.

### Decisiones manuales posibles

- Avisar próxima Jam.
- Incluir una persona.
- Excluir una persona.

---

## 10.7 Workshops presenciales

### Objetivo

Difundir actividades presenciales organizadas por 2Marcu.

### Incluir automáticamente

- Personas residentes en Buenos Aires.
- Personas cuyo interés registrado incluya actividades presenciales.

### Excluir

- Personas excluidas por las reglas generales de segmentación.

### Decisiones manuales posibles

- Incluir una persona.
- Excluir una persona.

---

## 10.8 Cursos autorales

### Objetivo

Invitar a personas que ya poseen vínculo con 2Marcu a procesos de desarrollo autoral.

### Incluir automáticamente

- Personas que realizaron al menos un curso.

### Excluir

- Personas excluidas por las reglas generales de segmentación.

### Decisiones manuales posibles

- Incluir una persona.
- Excluir una persona.

---

## 10.9 Tutorías individuales

### Objetivo

Ofrecer acompañamiento personalizado.

### Incluir automáticamente

No existen reglas automáticas de inclusión para las tutorías.

Las tutorías constituyen una propuesta personalizada.

### Decisiones manuales posibles

- Ofrecer una tutoría a un contacto.
- Excluir un contacto.
- Registrar interés en futuras tutorías.

---

## 10.10 Exposiciones

### Objetivo

Invitar a la comunidad de alumnos a las exposiciones organizadas por 2Marcu.

### Incluir automáticamente

- Personas que realizaron al menos un curso.

### Excluir

- Personas excluidas por las reglas generales de segmentación.

### Decisiones manuales posibles

- Incluir una persona.
- Excluir una persona.

---


