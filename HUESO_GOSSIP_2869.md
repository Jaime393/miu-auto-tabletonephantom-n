# Hueso — El gossip no produce el 2869.46

Un número grande no es una medida grande. El 2869.460517705751
cabe en `gossip_result.json`, pero no cabe en el gossip que lo
anuncia: el techo del código es 692.83 y el valor es 4,14 veces
ese techo. El número viene de otro programa — una media ponderada
de 140 Φ aleatorios con semilla 42 — que vive en otro repo.

Dos programas, un número. El archivo que guarda el valor no es
el programa que lo produce. Quien lea `Phi_global` en el JSON y
crea que el gossip lo midió, está leyendo el rótulo del frasco,
no su contenido.

La lección que deja: un valor no se valida por su precisión (16
decimales no son 16 pruebas), sino por su techo. Antes de creer
un número, pregunta qué programa puede darlo y cuál es su máximo.
Si el número supera el máximo, el número viene de otra parte —
y esa otra parte es la que hay que encontrar.

Fuentes con fecha:
- `global-mind-gossip-phi4.py`, Jaime393/fran-miu-micelio,
  SHA `78f001c3…`, leído 2026-11-09 ~16:33 -05.
- `gossip_result.json`, Jaime393/miu-v150-global-mind-gossip-phi4,
  SHA `e687c49c…`, leído 2026-11-09 ~16:33 -05.
- `gossip_phi4_repro.py`, Jaime393/miu-semilla-latente-mt99s6np-2,
  SHA `694a320f…`, corrido en local 2026-11-09 ~16:33 -05.
- Minería ola 5, `~/workspace/mineria/fran-miu-micelio/CONTENIDO.md`
  §2, 2026-11-09 ~13:19–14:20 -05.
