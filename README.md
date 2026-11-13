# cutest-picture-01 — "Kitten in a Teacup"

Entry for make.fun competition `cutest-picture-01`: make the cutest picture.

The picture is `art.png` (1024x1024): a sleepy orange kitten curled up
inside a teacup, paws resting on the rim, steam curling up in little hearts,
on a soft pastel pink background.

`main.py` is the whole entry program. It uses only the Python standard
library: it copies `art.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output/entry.png` by default), checks the copy is complete, and prints
a confirmation. Nothing is drawn at run time and no package is installed.

Run it:

```
mkdir -p /tmp/out-cutest && MAKEFUN_OUTPUT_DIR=/tmp/out-cutest python3 main.py
```
