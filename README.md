[日本語](README.ja.md)

# kanolab-web

Website of the Kano Lab (Science Communication Laboratory, Faculty of Education, Shiga University), published with GitHub Pages.

The content follows the lab's Google Sites implementation manual (PAGE 01–26, Japanese and English). The site is plain static HTML/CSS with no build step.

## Structure

| Path | Content |
|------|---------|
| `index.html` | Japanese home page (PAGE 01) |
| `en/index.html` | English home page (PAGE 01) |
| `assets/style.css` | Shared stylesheet |

All links are relative, so the site works both at a project URL (`/kanolab-web/`) and at a custom domain.
Each Japanese page `X/index.html` has an English counterpart `en/X/index.html`.

## Local preview

```sh
python3 -m http.server 8000
# open http://localhost:8000/
```

## Status

- Done: home page (ja / en)
- Not yet created: the other pages linked from the navigation (`research/`, `unesco-chair/`, `workshops/`, `games-books/`, `people/`, `join/`, `media/`, `contact/`, `access/` and their sub-pages)
- Images (hero and cards) are not added yet because no photos have been supplied.
