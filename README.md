# ClaudeCloud

## Alternative Beta Dictionary

`alt-beta-graph/` is an interactive glossary of alternative beta strategies. It shows 48 linked concepts as a slowly rotating 3D cloud of spheres. Clicking a term recolors the page in its section's color, pulls its linked terms into a cluster, and opens a detail panel with a definition and example usage.

The terms are grouped into six sections:

- Foundations
- Equity Factors
- Cross-Asset Premia
- Portfolio Construction
- Risks & Evaluation
- Vehicles & Products

The content is educational only and is not investment advice.

### Files

| File | Purpose |
|---|---|
| `data.json` | Terms, sections, section colors and links between terms |
| `template.html` | Page layout, styles and the Three.js / d3-force-3d graph code |
| `build.py` | Checks `data.json` and inserts it into the template |
| `index.html` | The built page (generated; don't edit by hand) |

### Viewing the page

Open `alt-beta-graph/index.html` in a browser, or serve the folder:

```sh
cd alt-beta-graph
python3 -m http.server 8000
# then visit http://localhost:8000
```

The page loads Three.js 0.170.0 and d3-force-3d 3.0.5 from cdn.jsdelivr.net and its fonts from Google Fonts, so it needs an internet connection.

### Controls

- Click a sphere to open that term. Click empty space or press `Esc` to close it.
- Press `/` to search. Press `Enter` to open the first match.
- With a term open, press `←` / `→` for the previous / next term.
- The palette button (bottom right) turns on section colors.
- The URL hash holds the open term, so links like `index.html#carry` open that term directly.
- Keyboard users can tab into a text list of all terms and open any of them with `Enter`.

### Editing the content

1. Edit `alt-beta-graph/data.json`. Each term needs a `slug`, `title`, `section` and `summary`. Optional fields are `body`, `usage` and `related`.
2. Link terms inside `body` with `[[slug]]` or `[[slug|shown text]]`. These links become the graph's edges. List any other connections in `related`. The same syntax works in `usage` lines, but there it only makes a clickable link in the panel and adds no edge.
3. Rebuild the page:

   ```sh
   cd alt-beta-graph
   python3 build.py template.html data.json index.html
   ```

   The build fails if a slug is duplicated, a term names an unknown section, or a term is missing its title or summary.

Term order within each section sets the "07 / 48" counter and the order of Prev / Next.
