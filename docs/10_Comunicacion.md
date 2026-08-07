# Documento 10
# Módulo de Comunicación

**Proyecto:** TiempoGanado

**Estado:** Cerrado

**Versión:** 1.0

---

# 1. Objetivo

El módulo de Comunicación permite planificar, segmentar y ejecutar campañas de difusión de las actividades de 2Marcu.

Su propósito es reducir al mínimo el tiempo dedicado a la gestión manual de comunicaciones, manteniendo siempre el criterio de Claudia como autoridad final en todas las decisiones.

TiempoGanado nunca decide qué comunicar ni a quién comunicar de manera autónoma.

Su función es asistir a Claudia proponiendo destinatarios, ejecutando campañas y registrando automáticamente toda la información generada durante el proceso.

---

# 2. Alcance

Este documento define el funcionamiento completo del módulo de Comunicación.

Comprende:

- creación de campañas;
- construcción automática de segmentos;
- revisión manual del segmento;
- reglas de negocio;
- ejecución de campañas;
- registro de resultados;
- trazabilidad.

No comprende:

- seguimiento posterior de contactos;
- campañas automáticas de reactivación;
- respuestas automáticas;
- CRM;
- automatizaciones de WhatsApp;
- generación de contenido.

Estos procesos serán definidos en documentos independientes.

---

# 3. Principios de diseño

## 3.1 Claudia toma las decisiones

TiempoGanado propone.

Claudia decide.

Toda decisión tomada manualmente por Claudia posee prioridad absoluta sobre cualquier regla automática.

---

## 3.2 Una campaña comunica una única actividad

Cada campaña comunica exclusivamente una actividad.

Ejemplos:

- Photoshop I
- Photoshop II
- Lightroom
- Jam Photoshop
- Workshop
- Curso autoral

Nunca varias actividades simultáneamente.

---

## 3.3 Un único mensaje por campaña

Todos los destinatarios de una campaña reciben el mismo mensaje.

Una campaña puede contener:

- texto;
- imágenes;
- videos;
- enlaces.

La personalización individual del contenido no forma parte del MVP.

---

## 3.4 Guardar hechos, no conclusiones

TiempoGanado registra únicamente hechos objetivos.

Ejemplos de hechos:

- realizó Photoshop I;
- participó en la Jam de agosto de 2026;
- respondió una campaña;
- asistió a una exposición.

No registra conclusiones.

Ejemplos de conclusiones:

- hace mucho que no participa;
- es un alumno avanzado;
- participó en la última Jam.

Todas las conclusiones serán calculadas automáticamente cuando el sistema las necesite.

---

## 3.5 Toda campaña deja trazabilidad

Cada campaña deberá poder reconstruirse completamente.

El sistema conservará toda la información necesaria para conocer qué ocurrió con cada destinatario.

---

# 4. Conceptos

## 4.1 Actividad

Toda propuesta organizada por 2Marcu susceptible de ser comunicada mediante una campaña.

Ejemplos:

- cursos;
- Jam;
- workshops;
- tutorías;
- exposiciones.

---

## 4.2 Campaña

Una campaña es una comunicación creada manualmente por Claudia para difundir una única actividad a un segmento determinado de contactos.

Toda campaña posee:

- actividad;
- segmento;
- mensaje;
- archivos adjuntos (opcionales);
- fecha de creación;
- fecha de envío;
- resultado final.

---

## 4.3 Decisiones permanentes

Las decisiones permanentes modifican el comportamiento futuro del sistema para un contacto determinado.

Ejemplos:

- avisar la próxima edición de Photoshop II;
- permitir comenzar directamente desde Photoshop III;
- no volver a ofrecer una actividad determinada;
- contacto prioritario.

Estas decisiones permanecen vigentes hasta que Claudia las modifique o elimine.

---

## 4.4 Modificaciones de campaña

Son cambios realizados por Claudia únicamente para la campaña que está preparando.

Ejemplos:

- agregar un contacto al segmento;
- excluir un contacto del segmento.

Estas modificaciones no alteran las reglas generales ni las decisiones permanentes.

# 5. Flujo general de una campaña

Toda campaña sigue el siguiente flujo.

1. Claudia crea una campaña.
2. Selecciona la actividad.
3. TiempoGanado construye automáticamente un segmento.
4. Claudia revisa el segmento.
5. Claudia redacta el mensaje.
6. Adjunta imágenes, videos o enlaces si corresponde.
7. Confirma el envío.
8. TiempoGanado ejecuta la campaña.
9. TiempoGanado registra automáticamente todos los resultados.

Ninguna campaña puede ejecutarse sin una confirmación explícita de Claudia.

---

# 6. Construcción del segmento

Una vez seleccionada la actividad, TiempoGanado genera automáticamente una propuesta de destinatarios.

Su objetivo es reducir el trabajo manual sin reemplazar el criterio de Claudia.

Para construir el segmento el sistema utiliza cuatro tipos de información.

## 6.1 Hechos

Representan información objetiva registrada por el sistema.

Ejemplos:

- cursos realizados;
- Jam realizadas;
- workshops realizados;
- exposiciones en las que participó;
- ciudad de residencia.

Los hechos nunca se modifican automáticamente.

Constituyen el historial objetivo del contacto.

---

## 6.2 Intereses

Representan preferencias actuales del contacto.

Ejemplos:

- edición;
- fotografía autoral;
- actividades presenciales;
- actividades online.

Los intereses pueden registrarse mediante:

- campañas de segmentación;
- conversaciones;
- decisiones manuales.

Los intereses pueden modificarse con el tiempo.

---

## 6.3 Decisiones permanentes

Representan instrucciones dadas por Claudia que modifican el comportamiento futuro del sistema.

Ejemplos:

- avisar la próxima edición de Photoshop II;
- avisar la próxima Jam;
- permitir comenzar desde Photoshop III;
- contacto prioritario.

Las decisiones permanentes siempre tienen prioridad sobre cualquier regla automática.

---

## 6.4 Historial de comunicaciones

Registra todas las interacciones entre un contacto y 2Marcu.

Ejemplos:

- consultó por Photoshop;
- respondió una campaña;
- solicitó información;
- se inscribió;
- canceló una inscripción.

Este historial será la base del Documento 20 (Seguimiento de contactos).

---

## 6.5 Contacto activo

Se considera contacto activo a toda persona que:

- posee un medio de contacto válido;
- no solicitó dejar de recibir comunicaciones;
- no fue archivada manualmente.

Solo los contactos activos pueden ser incorporados automáticamente a campañas.

---

# 7. Revisión del segmento

Una vez construido el segmento, TiempoGanado presenta un resumen antes del envío.

El objetivo es permitir que Claudia valide la propuesta sin revisar contacto por contacto.

El sistema presenta grupos de destinatarios y la cantidad de personas incluida en cada uno.

Desde esta pantalla Claudia puede:

- aprobar el segmento;
- agregar contactos;
- excluir contactos;
- cancelar la campaña.

Las modificaciones realizadas durante esta etapa afectan únicamente a la campaña actual.

No modifican las reglas generales del sistema ni las decisiones permanentes.

---

# 8. Reglas generales de segmentación

Todas las campañas respetan las siguientes reglas.

## 8.1 Exclusión automática

Nunca podrán incorporarse automáticamente a una campaña las personas que:

- solicitaron dejar de recibir comunicaciones;
- no poseen un medio de contacto válido;
- fueron archivadas manualmente.

Solo podrán incorporarse mediante una decisión manual.

---

## 8.2 Prioridad

Cuando exista un conflicto entre:

- una regla automática;
- una decisión permanente;
- una modificación realizada durante la campaña,

el orden de prioridad será:

1. Modificación realizada durante la campaña.
2. Decisión permanente.
3. Regla automática.

---

## 8.3 Alcance de las modificaciones

Las modificaciones realizadas durante una campaña nunca alteran las reglas generales del sistema.

Solo afectan la campaña que se está preparando.

# 9. Reglas de negocio por actividad

Las siguientes reglas determinan qué contactos serán incorporados automáticamente al segmento de cada actividad.

Las reglas específicas se aplican siempre después de las reglas generales de segmentación.

---

## 9.1 Photoshop I

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

---

## 9.2 Photoshop II

### Objetivo

Continuar el recorrido de formación.

### Incluir automáticamente

- Personas que realizaron Photoshop I.

### Excluir

- Personas que realizaron Photoshop II.
- Personas que realizaron Photoshop III.

---

## 9.3 Photoshop III

### Objetivo

Completar el recorrido avanzado.

### Incluir automáticamente

- Personas que realizaron Photoshop II.

### Excluir

- Personas que realizaron Photoshop III.

---

## 9.4 Lightroom

### Objetivo

Difundir el curso de Lightroom.

### Incluir automáticamente

- Todos los contactos activos.

### Excluir

- Personas que realizaron Lightroom.

---

## 9.5 Jam Photoshop

### Objetivo

Sostener la continuidad del aprendizaje y desarrollar el criterio de edición.

### Incluir automáticamente

- Personas que realizaron al menos un módulo de Photoshop.
- Personas que participaron anteriormente en una Jam de Photoshop.

### Observaciones

Participar en una Jam nunca excluye futuras invitaciones.

Las promociones comerciales para participantes de la edición anterior no modifican estas reglas.

---

## 9.6 Jam Lightroom

### Objetivo

Sostener la continuidad del aprendizaje y desarrollar el criterio de edición.

### Incluir automáticamente

- Personas que realizaron Lightroom.
- Personas que participaron anteriormente en una Jam de Lightroom.

### Observaciones

Participar en una Jam nunca excluye futuras invitaciones.

---

## 9.7 Workshops presenciales

### Objetivo

Difundir actividades presenciales.

### Incluir automáticamente

- Personas residentes en Buenos Aires.
- Personas cuyo interés registrado incluya actividades presenciales.

---

## 9.8 Cursos autorales

### Objetivo

Invitar a personas con vínculo previo con 2Marcu a procesos de desarrollo autoral.

### Incluir automáticamente

- Personas que realizaron al menos un curso.

---

## 9.9 Tutorías individuales

### Objetivo

Ofrecer acompañamiento personalizado.

Las tutorías no poseen reglas automáticas de inclusión.

Su ofrecimiento depende del criterio de Claudia.

---

## 9.10 Exposiciones

### Objetivo

Invitar a la comunidad de alumnos.

### Incluir automáticamente

- Personas que realizaron al menos un curso.

---

## 9.11 Aplicación de decisiones manuales

En cualquiera de las actividades anteriores Claudia podrá:

- incorporar contactos al segmento;
- excluir contactos del segmento;
- registrar decisiones permanentes para campañas futuras.

Estas acciones siempre tendrán prioridad sobre las reglas automáticas.

# 10. Ejecución de la campaña

Una vez confirmada la campaña, TiempoGanado inicia automáticamente el proceso de envío.

Durante toda la ejecución el sistema deberá informar el estado de la campaña.

Como mínimo deberá mostrar:

- cantidad total de destinatarios;
- envíos realizados;
- envíos pendientes;
- envíos fallidos.

El objetivo es que Claudia pueda conocer el avance de la campaña en todo momento sin necesidad de intervenir.

---

# 11. Registro automático

Al finalizar la campaña, TiempoGanado registra automáticamente toda la información generada.

## Registro de la campaña

Cada campaña conservará:

- actividad comunicada;
- fecha y hora de creación;
- fecha y hora de envío;
- mensaje enviado;
- archivos adjuntos;
- cantidad de destinatarios;
- cantidad de envíos exitosos;
- cantidad de envíos fallidos.

## Registro por contacto

Para cada contacto el sistema registrará:

- campaña recibida;
- fecha de recepción;
- estado del envío;
- respuesta recibida (si existiera);
- fecha de la respuesta.

Toda esta información formará parte del historial del contacto.

---

# 12. Resultados de la campaña

Al finalizar una campaña el sistema generará un resumen.

Como mínimo deberá informar:

- cantidad total de destinatarios;
- envíos exitosos;
- envíos fallidos;
- respuestas recibidas;
- contactos sin respuesta.

En versiones futuras podrán incorporarse nuevos indicadores.

---

# 13. Índice de vínculo

TiempoGanado calculará automáticamente un índice de vínculo para cada contacto.

Este índice no representa una valoración personal.

Su objetivo es ayudar a Claudia a identificar las personas con mayor relación histórica con 2Marcu.

El cálculo podrá considerar, entre otros factores:

- cantidad de cursos realizados;
- participación en Jam;
- participación en workshops;
- participación en exposiciones;
- antigüedad como alumno.

La fórmula exacta será definida en un documento específico.

No forma parte del MVP.

---

# 14. Límites del módulo

El módulo de Comunicación finaliza cuando:

- la campaña fue ejecutada;
- todos los envíos quedaron registrados;
- las respuestas recibidas fueron incorporadas al historial.

Este documento no define qué hacer con esas respuestas.

Los procesos posteriores pertenecen al Documento 20 — Seguimiento de Contactos.

---

# 15. Estado del documento

Estado: En auditoría.

Este documento quedará oficialmente cerrado cuando la auditoría funcional confirme que un desarrollador puede implementar el módulo de Comunicación sin necesidad de realizar consultas funcionales adicionales.
