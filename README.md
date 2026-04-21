# The 1%
### An Antarctic Soil Geochemistry Story
 
An interactive scrollytelling visualization exploring what machine learning can reveal about Antarctic soil geochemistry in the 1% of Antarctica that isn't covered in ice.
 
Built as a final project for DSPX315 (Data Storytelling & Visualization), Brigham Young University, Spring 2026.

View the full visualization at https://ansoildatavis.netlify.app/
  
---
 
## What This Is
 
Antarctica is almost entirely covered in ice, but in the small fractions of exposed, ice-free land, soil tells a story that matters for understanding climate change, ecosystem science, and the limits of life itself.
 
This project reflects preliminary results from ongoing research that I am conducting in accordance with the BYU LeMonte Lab of Environmental Geochemistry.
 
The underlying research predicts 67 soil chemical properties from 9 satellite-derived environmental features across 171 samples from 28 Antarctic locations. The strongest predicted target is δ¹⁵N (nitrogen isotopes), which traces penguin and seal colony influence on soil chemistry across the continent.
 
---
 
## Viewing the Project
 
**Option 1 — Live link** (recommended): Open the GitHub Pages link above in any modern browser.
 
**Option 2 — Local**: Download or clone this repo, then open `index_v15.html` directly in your browser.
 
```bash
git clone https://github.com/lilyeliason/ansoil-data-vis
cd ansoil-data-vis
open index_v15.html
```
 
Or serve it locally instead:
 
```bash
python -m http.server 8000
# then open http://localhost:8000 in your browser
```
 
> The lab data CSV (`lab_data.csv`) must be in the same folder as the HTML file for the download link in the Dig Deeper panel to work.
 
---
 
## File Structure
 
```
ansoil-data-vis/
├── index_v2.html           Main scrollytelling file (self-contained)
├── lab_data.csv            Cleaned geochemical dataset (171 samples, 80+ properties)
├── README.md               This file
│
└── assets/
    ├── video/
    │   ├── ant_sea_ice_globe.mp4     Rotating globe (Scene 1)
    │   └── ant_ice_change.mp4        GRACE ice mass change footage (Scene 3)
    │
    └── images/
        ├── ant_soil.jpg              Antarctic soil photo (Scene 2)
        ├── ant_geo.jpg               Coastal geology (Scene 2)
        ├── ant_coast.jpg             Coastline (Scene 7)
        ├── acbr_map.png              Antarctic Conservation Biogeographic Regions (Scene 4)
        ├── samples_real.svg          Sample location map (Scene 4)
        ├── sample_all.svg            All-region ACBR overview (Scene 4)
        ├── fieldwork.jpg             Field camp photograph (Scene 4)
        ├── clean_01_delta-15N.png    δ¹⁵N prediction map
        ├── clean_02_phosphorus.png   Phosphorus prediction map
        ├── clean_03_sodium.png       Sodium prediction map
        ├── clean_04_nickel.png       Nickel prediction map
        └── clean_05_titanium.png     Titanium prediction map
```
 
---
 
## Scene Structure
 
| Scene | Title | Content |
|-------|-------|---------|
| 1 | The 0.18% | Introduction to Antarctica |
| 2 | The Soils | Antarctic ecosystem pyramid, geochemical properties, the unmapped gap |
| 3 | A Changing Continent | GRACE ice mass change, why baselines matter |
| 4 | The Sampling Problem | ACBRs, why field work is limited, the 171 samples we have |
| 5 | Another Way | Satellite data inputs, machine learning equation |
| 6 | The Predictions | Interactive property maps (δ¹⁵N, P, Na, Ni, Ti) |
| 7 | Why It Matters | Climate science, smarter field work, life beyond Earth |
| 8 | Credits | Lab, data sources, satellite imagery attribution |
 
---
 
## Tech Stack
 
- Vanilla HTML, CSS, JavaScript (no build step)
- [D3.js v7](https://d3js.org/) — data visualization
- [Scrollama.js](https://github.com/russellsamora/scrollama) — scroll-driven interactions
- All assets are local; no backend required
---
 
## Data & Media Credits
 
**Soil data:** 
- LeMonte Lab of Environmental Geochemistry, Brigham Young University

**Satellite data:**
- Elevation/slope/aspect: Howat, I.M. et al. (2019). The Reference Elevation Model of Antarctica (REMA). *The Cryosphere*, 13(2), 665–674.
- Temperature/precipitation: Fick, S.E. & Hijmans, R.J. (2017). WorldClim 2. *Int. J. Climatol.*, 37, 4302–4315.
- Lithology: SCAR Antarctic Geological Map
- Coastline/ACBRs: Terauds, A. & Lee, J.R. (2016). *Diversity and Distributions*, 22(8), 836–840.

**Media:**
- Globe video: NASA Scientific Visualization Studio, AMSR-E instrument, Aqua satellite
- Ice mass change video: NASA GRACE/GRACE-FO, NASA/Goddard Space Flight Center SVS
---
 
## Related Repository
 
The machine learning pipeline (ANSOIL) that generated the prediction maps lives in a separate repo:
[github.com/lilyeliason/ansoil-spatial-prediction](https://github.com/lilyeliason/ansoil-spatial-prediction)
 
---
 
## About
 
Created by Lily Eliason  
DSPX315 Final Project, Spring 2025  
Brigham Young University















This project is for academic and educational purposes.
