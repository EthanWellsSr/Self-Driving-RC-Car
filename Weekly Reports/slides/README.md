# Presentation slides — one file per person

**Why:** a `.pptx` is a binary file, so git can't merge two people's edits to the
same deck — you get an unresolvable conflict. To avoid that, everyone edits their
**own** file here. Two people never touch the same file, so conflicts can't happen,
and you can all work at the same time.

## The rule

- **Edit only your own file** in this folder (e.g. Alexis edits `2-alexis-perez.pptx`).
  Edit it in PowerPoint like normal — text, images, whatever.
- **Do not hand-edit** `../Self-Driving-RC-Car.pptx`. It is generated and your changes
  there get overwritten.
- Pull, edit your file, commit, push — as usual. No coordination needed.

## Building the final deck

Whoever is assembling the deck (usually the group leader, before submission) runs,
from the `Weekly Reports` folder:

```
python3 assemble_deck.py
```

That stitches every `slides/*.pptx`, in filename order, into
`../Self-Driving-RC-Car.pptx`. Then commit that final deck alongside the slide files.

## Files / order

Slide order comes from the numeric prefix:

| File | Slide |
|---|---|
| `0-title.pptx` | Title / team |
| `1-ethan-wells.pptx` | Ethan Wells |
| `2-alexis-perez.pptx` | Alexis Perez |
| `3-ethan-bishop.pptx` | Ethan Bishop |
| `4-abigail-duran.pptx` | Abigail Duran |

Add a person by dropping a new `NN-name.pptx` here; remove one by deleting their file.
Each member's slide keeps the four sections: **Goals for the week**, **Progress for the
week**, **Goals for next week**, **Hours spent on progress**.
