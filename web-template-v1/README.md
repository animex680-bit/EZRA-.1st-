# Web Template v1

Re-skin the car-shop landing page for a new brand / IG handle by editing **one JSON file** — no touching the HTML.

## What it does

The master build (`../360-remix/index.html`, aka the MEDO site) is the template. A brand config fills in
the swappable copy — name, IG handle, phone, hero line, the five "ways in" buttons, the AI copy, showroom,
reviews, transitions, nav/footer and the CORE chatbot — plus currency and any extra one-off swaps. The
generator stamps it all out into a standalone `index.html` that **shares the master's assets**
(images, 3D cars, video) via `../360-remix/assets/`, so nothing heavy is duplicated.

## Make a new brand (≈5 min)

1. Copy an existing config and rename it:
   ```bash
   cp brands/donk.json brands/yourbrand.json
   ```
2. Edit `brands/yourbrand.json` — change the words and buttons (see the field list below).
3. Generate:
   ```bash
   node generate.mjs brands/yourbrand.json ../yourbrand
   ```
   Writes `../yourbrand/index.html`. Put that folder next to `360-remix` (locally and when you deploy) so
   `../360-remix/assets/` resolves.
4. Preview: serve the site root and open `http://localhost:3000/Landing%20page%20prospects/yourbrand/index.html`.
5. Deploy: copy `yourbrand/index.html` into the Pages repo under `yourbrand/` (the repo already has
   `360-remix/` with the assets), commit and push → live at `…/yourbrand/`.

## Config fields

| key | what it is |
|---|---|
| `output` | default output folder name (overridden by the CLI arg) |
| `assetBase` | where assets live relative to the output (default `../360-remix/assets/`) |
| `lang`, `name`, `shortMark`, `wordmark`, `ig`, `phone`, `area`, `currency` | brand identity. `shortMark` = compact mark (favicon, pass codes, bot header); `wordmark` = logo HTML, one letter bold, e.g. `DO<b>N</b>K`; `currency` replaces every `£` |
| `titleTail`, `metaDesc`, `ogTitle`, `ogDesc`, `paintGold` | `<title>` tail, meta/OG text, the gold paint name |
| `hero` | `{kicker, h1, sub, cue}` — the first screen. `h1` may use `<br>` and `<em>…</em>`; its words animate in. |
| `ways` | the five buttons, in order **Buy, Sell, Finance, Build, Parts**: `{t: title, w: short word, s: subline}` |
| `omega` | the AI: `{kicker, h, sub, statCars, statParts, facts:[…8], aria}` |
| `scan`, `transitions`, `showroom`, `reviews`, `finance`, `booking`, `nav`, `core` | section copy (see donk.json) |
| `extra` | `[[find, replace], …]` — one-off literal swaps for anything not in the schema (e.g. the little floating pill labels) |
| `terminology` | `[[find, replace], …]` — global word swaps applied everywhere (e.g. `["restomod","donk build"]`) |

Anything you leave out keeps the master's (MEDO) wording.

## Notes / gotchas

- Strings that land inside the page's JavaScript (the `omega.facts`, `core.greeting/fallback/chips`) are
  wrapped automatically — write them with a curly `’` apostrophe, not a straight `'`, to be safe.
- `currency` does a blunt `£ → <symbol>` swap. The master's one price-matching regex is written `[£$]?`
  so this is safe; don't reintroduce a bare `£?` there.
- `terminology` is applied last and globally, so keep its pairs specific (e.g. `"on the floor"`, not `"floor"`).
- The generator prints any anchors it couldn't find — if several show up, the master build probably changed
  and the anchor strings in `generate.mjs` need re-syncing.
- The 3D showroom cars and the deep stock-gallery listings are **not** in the config yet — they stay as the
  master's cars. Swapping those needs new 3D models / stock data (a v2 job).

## Files

- `generate.mjs` — the generator (reads the live `../360-remix/index.html`, or `template.html` as a fallback)
- `template.html` — a snapshot of the master, used only if `../360-remix` isn't alongside
- `brands/donk.json` — a complete worked example (Donk Ryde or Die LLC)
