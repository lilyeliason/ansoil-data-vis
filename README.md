# AnSoil-Data-Vis
An interactive scrollytelling visualization exploring what machine learning can reveal about soil geochemistry in Antarctica's ice-free regions.
Built as a final project for DSPX315.

---

## About
Antarctica is almost entirely ice. But in the narrow strip of exposed, ice-free land that makes up just 0.4% of the continent tells a story that matters for understanding Earth's past, present, and future.
This project translates research that I've done through the BYU LeMonte Lab of Environmental Geochemistry into a visual story for a general audience. Using machine learning predictions of soil geochemistry across 28 Antarctic sampling locations, it walks through why these soils matter, what's at stake as ice recedes, and how scientists are working to understand them before it's too late.

---

## Running Locally

No setup required. Just open 'index_v2.html' in a browser.
If you run into video autoplay issues, serve it locally instead:
```bash
python -m http.server 8000
# then open http://localhost:8000
```

---

## File Structure

```
the-018-percent/
├── index_v2.html           Main scrollytelling file (self-contained)
├── README.md
├── spec.md                 Scene-by-scene design specification
├── ASSETS.md               Full asset inventory
│
└── assets/
    ├── video/
    │   ├── ant_sea_ice_globe.mp4     Rotating globe (Scene 1)
    │   └── ant_ice_change.mp4        Ice retreat footage (Scene 3)
    │
    └── images/
        ├── [scene photos & maps]     See ASSETS.md for full list
        ├── clean_01_delta-15N.png    }
        ├── clean_02_phosphorus.png   } ML prediction maps
        ├── clean_03_sodium.png       } (Scene 6 map explorer)
        ├── clean_04_nickel.png       }
        └── clean_10_titanium.png     }
```
 
---

## Narrative Arc

The visualization moves through 7 scenes:
 
**Scene 1 — The 0.18%**
- A rotating globe establishes Antarctica. The 0.18% of ice-free land is revealed, with pulsing blobs marking where life and soil exist.
 
**Scene 2 — Why soils matter**
- An ecosystem pyramid builds from the ground up, showing soil chemistry as the foundation for all Antarctic biodiversity. The scene transitions into what geochemistry actually measures and why the data gap is so significant.
 
**Scene 3 — Conditions are changing**
- Ice retreat footage establishes the urgency: as the climate warms, soils that have been frozen for thousands of years are being exposed — with no chemical baseline to track what's being lost.
 
**Scene 4 — The sampling problem**
- The ideal coverage (all 28 biogeographic regions) is set against the reality: 171 samples from just 4 regions. Field costs, logistics, and remoteness make comprehensive sampling impossible.
 
**Scene 5 — The approach**
- Satellite-derived environmental layers (elevation, precipitation, slope, lithology) are introduced as a continent-wide data source. A machine learning equation — samples + satellite data + ML models = predicted geochemistry — frames the solution.
 
**Scene 6 — Explore the predictions**
- An interactive map explorer lets users browse ML-predicted soil properties across the continent. Five properties are selectable, each with a plain-language explanation of what the spatial pattern reveals.
 
**Scene 7 — Why it matters**
- Three panels lay out the downstream significance: tracking a changing climate, guiding smarter field expeditions, and understanding Antarctic soils as an analogue for life on Mars.

**Scene 8 — Credits & Acknowledgements**
- Links to further reading and credits for resources used. 
 
---

## The Science Behind It

The underlying research predicts 67 soil chemical properties from 22 environmental features across Antarctic ice-free soils. 

Strongest predicted targets include delta-15N, weight percent nitrogen, potassium digest, sodium digest, and CLR phosphate. 

The prediction maps used in this visualization reflects **very preliminary results from our Random Forest and XGBoost models**. 
To see updated progress in this research, please review my ansoil-spatial-prediction repository. 

---
 
## Built With
 
- [D3.js v7](https://d3js.org/) for data-driven visuals
- [Scrollama.js](https://github.com/russellsamora/scrollama) for scroll-driven scene transitions
- Vanilla HTML/CSS/JS — no build tools, no dependencies to install
---

## Credits
- Author & Lead Researcher: Lily Eliason
- Data Credits: BYU LeMonte Lab of Environmental Geochemistry
- Course: DSPX315
















This project is for academic and educational purposes.
