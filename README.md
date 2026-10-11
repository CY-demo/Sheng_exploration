# National Park Field Guide · 公園隨行

A bilingual Traditional Chinese and English travel website combining Grand Canyon, Death Valley, Yellowstone, Grand Teton, and four Alaska national parks. Start with a park, follow a complete regional itinerary, or explore nearby destinations.

## AI-built project

This website was built with substantial AI assistance using ChatGPT and Codex. The author supplied travel experience, itinerary corrections, and editorial direction. AI assisted with implementation, layout, content organization, and explanatory writing. Personal experiences are distinguished from planning guidance; private flight dates, booking details, identities, and correspondence are excluded.

## Explore

- `dist/index.html`: eight-park overview with a geographic U.S. map and regional filters.
- `dist/en/`: complete English counterparts for all 16 pages, with matching section anchors.
- `dist/parks/`: Grand Canyon, Death Valley, Kenai Fjords, Denali, Katmai, Wrangell–St. Elias, Yellowstone, and Grand Teton.
- `dist/routes/alaska/`: detailed nine-day itinerary.
- `dist/routes/southwest/`: Las Vegas, Death Valley, Grand Canyon, and Page route.
- `dist/nearby/page/`: Antelope Canyon, Horseshoe Bend, and surrounding stops.
- `dist/travel/airports/`: expandable SJC and LAS lounge locations and eligible cards.

- `dist/routes/yellowstone-grand-teton/`: actual compact four-day route, planning time bands, and an optional full-day Teton extension.

## Build and validation

Run `python3 build.py` to regenerate pages, then `python3 verify.py`. The build uses Python standard libraries only. `node verify.mjs` runs the same validation for GitHub Pages deployment.

The `dist/` directory is a complete static site with relative links, usable under a GitHub repository path or a standalone domain. Existing `#death`, `#grand`, `#page`, and `#airport` bookmarks redirect to their new pages. Source modules: `itinerary.py`, `experience_days.py`, `actual_rides.py`, `hub.py`, `park_notes.py`, `extensions.py`, and `canyon-content.json`. `bilingual.py` builds static English counterparts from the reviewed `english.json` catalog; missing translations fail the build.

## Offline reading and images

Use the offline download button while online to save both language editions and photos on that device. Language links preserve section anchors; English links stay within the English edition. No external translation service is used. External references require internet access. Image credits and source URLs are retained in `dist/assets/credits.json`, `dist/assets/spots/manifest.json`, and the linked official references. Third-party image rights remain with their respective owners; see individual attribution and license information.

## Privacy

No personal dates, hotel bookings, reservation IDs, traveler names, analytics, or login logic are included. Alaska and the Yellowstone–Grand Teton routing follow the recorded journeys; times not recorded are described by part of the day. Alternative trips and the upcoming Southwest itinerary remain clearly marked as plans. The repository is public; local private notes are not included.
