[日本語](README.ja.md)

# kanolab-web

Website of the Kano Lab (Science Communication Laboratory, Faculty of Education, Shiga University), published with GitHub Pages.

The content follows the lab's Google Sites implementation manual (PAGE 01–26, Japanese and English). The site is plain static HTML/CSS with no build step.

## Structure

All 26 pages of the manual are published in Japanese and English.

| Japanese | English | Content |
|----------|---------|---------|
| `index.html` | `en/index.html` | Home (PAGE 01) |
| `research/` (+ `inclusive-steam/`, `traditional-knowledge/`, `responsible-ai/`, `projects/`, `outputs/`) | `en/research/…` | Research (PAGE 02–12) |
| `unesco-chair/` | `en/unesco-chair/` | UNESCO Chair (PAGE 13) |
| `workshops/` (+ `workshop-archive/`) | `en/workshops/…` | Workshops (PAGE 14–15) |
| `games-books/` (+ `games/`, `books/`) | `en/games-books/…` | Games & Books (PAGE 16–18) |
| `people/` | `en/people/` | People (PAGE 19) |
| `join/` (+ `phd/`, `jsps/`, `collaboration/`) | `en/join/…` | Join the Lab (PAGE 20–23) |
| `media/`, `contact/`, `access/` | `en/media/` … | Media, Contact, Access (PAGE 24–26) |
| `assets/style.css` | | Shared stylesheet |

URL paths follow the "recommended path" of each page in the manual. All links are relative, so the site works both at a project URL (`/kanolab-web/`) and at a custom domain.
Each Japanese page `X/index.html` has an English counterpart `en/X/index.html`.

## Local preview

```sh
python3 -m http.server 8000
# open http://localhost:8000/
```

## Status

- Done: all 26 pages (ja / en), text and links taken from the manual.
- Items still to be confirmed before they are final are highlighted in yellow (`<mark class="todo">`): enquiry/registration form URLs (shown as disabled "coming soon" buttons), workshop event details, member names, UNESCO Chair dates. Search with `grep -rl 'class="todo"' .`
- Images (hero and cards) are not added yet because no photos have been supplied.

- Design follows the previous Google Sites site (https://sites.google.com/site/keikanolab/) with the colour scheme specified in the manual (persimmon-tannin red-brown, ink, deep green, white). Logo, mascot, game/book/flyer images and videos are reused from that site (`assets/img/`).
- Fonts: Oswald and Open Sans are loaded from Google Fonts.
