# 生生不息探險隊 · Sheng Sheng Expeditions

A bilingual Traditional Chinese and English travel journal organized into themes. Its U.S. National Parks theme combines Grand Canyon, Death Valley, Yellowstone, Grand Teton, and four Alaska national parks. Start with a park, follow a complete regional itinerary, or explore nearby destinations.

## AI-built project

This website was built with substantial AI assistance using ChatGPT and Codex. The author supplied travel experience, itinerary corrections, and editorial direction. AI assisted with implementation, layout, content organization, and explanatory writing. Personal experiences are distinguished from planning guidance; private flight dates, booking details, identities, and correspondence are excluded.

## Explore

- `dist/index.html`: theme homepage for U.S. National Parks, Nature & Outdoors, and Getting There & Travel Essentials.
- `dist/themes/us-national-parks/`: eight-park overview with an AI-generated illustrated map, approximate clickable park markers, and regional filters.
- `dist/en/`: complete English counterparts for all 19 pages, with matching section anchors.
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

## Illustrated map

`dist/assets/us-illustrated-map.webp` is an AI-generated editorial illustration made with the built-in image generation tool. The tool did not expose a model selector, so no specific model version is claimed. Accessible park links and approximate markers are implemented in HTML/SVG. The illustration is not a navigation map. The generation prompt is recorded in `dist/assets/us-illustrated-map.json`.
