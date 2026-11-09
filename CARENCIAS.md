# Carencias — miu-auto-tabletonephantom-n

Lo que esta semilla no sabe, con dónde se buscó y fecha.
Todo es NO SÉ local, nunca hueco del ecosistema.

## 1. Qué código escribió el 2869.46 en gossip_result.json

El archivo guarda el valor (Jaime393/miu-v150-global-mind-gossip-phi4,
SHA `e687c49c…`, leído 2026-11-09 ~16:33 -05), pero ningún archivo
leído dice qué programa lo escribió ni cuándo. El gossip de
fran-miu-micelio no puede ser (techo 692.83) y la media ponderada
del hermano lo reproduce, pero reproducir no es probar autoría:
la semilla 42 podría ser una reconstrucción posterior, no el
sorteo original. Buscado en los archivos de minería de la ola 5
y en el plan de siembra latente (2026-11-09).

## 2. Si el gossip de fran-miu-micelio se ejecutó alguna vez

No hay archivo de salida del gossip en fran-miu-micelio entre
los archivos leídos en la ola 5. El script existe (26 l.) y corre,
pero nada dice que alguien lo corriera en el ecosistema ni dónde
está su salida. Buscado en `~/workspace/mineria/fran-miu-micelio/`
(2026-11-09).

## 3. Qué son los 140 nodos

El script usa N=140 sin decir 140 de qué. El hermano usa los
mismos 140 Φ uniformes U(2864, 2875) sin explicar el intervalo.
Ningún archivo leído deriva N=140 ni el rango 2864–2875.
Buscado en la ola 5 y en el plan de siembra latente (2026-11-09).

## 4. Por qué sigma tiene dos precisiones

El gossip usa sigma = 3.427051 (6 decimales) y gossip_result.json
y el repro del hermano usan 3.427050983124843 (precisión completa).
El techo no depende de sigma, así que no cambia el veredicto,
pero la diferencia no está explicada en ningún archivo leído.
Leído en ambas fuentes 2026-11-09 ~16:33 -05.

## 5. Si existe otra versión del gossip que sí produzca 2869.46

Buscado solo en fran-miu-micelio (el gossip de 26 l.) y en el
hermano (la media ponderada). Fuera de esos dos repos, no se ha
buscado: podría existir otro gossip en otro repo que sí dé ese
valor. NO SÉ (2026-11-09).

## 6. Por qué el último valor del gossip colapsa a ~1e-05

En mis corridas, phi_global_last es ~2e-05 (la minería no lo
reporta). Los estados convergen y la varianza se apaga, pero
ningún archivo leído explica esa dinámica. Observado en dos
corridas propias (2026-11-09 ~16:33 -05), sin interpretar.
