PROJECT: The 0.18% — A scrollytelling essay on Antarctic ice-free 
regions and machine learning soil geochemistry prediction.

TECH STACK:
- Vanilla HTML, CSS, JavaScript only. No frameworks.
- Scrollama.js for scroll triggering 
  (CDN: https://unpkg.com/scrollama)
- D3 v7 for any data visualization 
  (CDN: https://cdn.jsdelivr.net/npm/d3@7)
- No jQuery, no React, no Vue.

FONTS:
- Primary: Suisse Int'l (self-hosted if available, 
  fallback: Helvetica Neue, Helvetica, Arial, sans-serif)

COLOR SYSTEM:
/* Base */
--color-bg: #0A1628;
--color-text-primary: #E8F4F8;
--color-text-secondary: #4A9ECA;
--color-dig-deeper: #2D6E7E;

/* Predictor layers (all same color) */
--color-predictor: #4A9ECA;

/* Sample regions */
--color-region-tm: #A34A2A;   /* Transantarctic Mountains */
--color-region-svl: #C49A5A;  /* South Victoria Land */
--color-region-nvl: #7A8F5A;  /* North Victoria Land */
--color-region-nwap: #8A5E4A; /* NW Antarctic Peninsula */

/* Target properties */
--color-nitrogen: #0E7A6E;
--color-potassium: #2E4FA8;
--color-sodium: #5A2E8A;
--color-phosphate: #8A1A4A;

ASSET PATHS (all assets live in /assets/images/):
- basemap.png
- elevation.png
- precipitation.png
- lithology.png
- contours.png (elevation contours, used as elevation 
  alt visualization)
- samples.png (sample locations map)
- 28_regions.png (zoomed regional map)
- ant_mass_change.png
- ant_field_work.png
- ant_dry_valley.jpeg
- marsdry_valley.png

GLOBAL UI ELEMENTS (present across all scenes):
- Fixed "Dig Deeper" button, bottom right corner, 
  color: #2D6E7E, appears from Scene 3 onward
- Fixed right-side scroll progress dots, 
  one per scene, highlight as reader advances
- On mobile: stack layouts vertically

---

SCENE 1 — TITLE / HOOK

Layout: Full-bleed, centered, dark background #0A1628

Elements (appear in this exact sequence):
1. Background: Globe video/image of Antarctica centered, 
   slowly rotating animation if possible, 
   else static globe image
2. Title fades in: "The 0.18%"
   Font: large, white, centered
3. Subtitle fades in below: 
   "Predicting Antarctic Soil Geochemistry"
   Font: small, #4A9ECA, centered
4. On first scroll step:
   Text appears: "Antarctica is 14.2 million square kilometers"
5. On second scroll step:
   Text appears: "Less than 0.18% of it is ice-free"
6. Animation: Small warm-toned amber/rust colored flecks 
   animate appearing along the ice free regions in Antarctica 
   (along the bottom left/center coasts)
7. On third scroll step:
   Text appears: "These tiny pockets of land contain almost 
   all of Antarctica's biodiversity, making them crucial for 
   understanding life in extreme environments"
8. Scroll cue: subtle animated down arrow appears

---

SCENE 2 — WHAT IS AN ICE-FREE REGION

Layout: Two-column split screen

LEFT COLUMN (black background, text/visuals):
Sequential scroll steps reveal the following one at a time:

Step 1: Title appears: "What exists in these regions?"

Step 2: First circle appears (image inside circle, 
        caption below):
  - Image: Adelie penguin (penguin.jpg)
  - Caption: "Macro-organisms"
  - Arrow pointing right toward map

Step 3: Second circle appears below first:
  - Image: Glacial lake with microorganisms
  - Caption: "Microorganisms" (microbe.jpg)
  - Arrow pointing right toward map

Step 4: Third circle appears below second:
  - Image: Rock and soil, Transantarctic Mountains (soil.jpg)
  - Caption: "Abiotic Factors"
  - Arrow pointing right toward map

Step 5: Top two circles + all arrows fade out. 
        Only bottom circle (Abiotic Factors) remains.
        Text block appears above it:
  "The soils in these regions are among the most extreme 
  on Earth: hyper-arid, UV-blasted, nutrient-poor, 
  wind-scoured, and very, very cold. Understanding their 
  geochemical makeup helps us understand how life persists 
  even in the most unforgiving circumstances."

Step 6: Bottom circle and text fade out. 
        Left side goes fully dark.
        New text block appears:
  "But actually getting there is incredibly difficult and 
  expensive. Our lab has analyzed only 171 soil samples 
  from across these regions.

  By pairing those samples with satellite-derived spatial 
  data and machine learning, we can predict soil chemistry 
  in areas that have never been sampled before."

Transition: Antarctica outline map fades in, anchoring 
the next several scenes.

RIGHT COLUMN:
- Zoomed photograph of western Antarctica coastline 
  showing ice-free region patches
- Stays fixed while left column text scrolls
- Use a real photograph here (placeholder: 
  /assets/images/icefree_photo.jpg)

---

SCENE 3 — THE PREDICTORS

Layout: Map takes 65% of screen width, centered. 
Tab controls on the right.

Title (above map): "The Predictors"

MAP COMPONENT:
- Base layer always visible: basemap.png
- One overlay layer visible at a time (default: elevation)
- All overlays stacked absolutely, same dimensions, 
  same position
- Layer transition: opacity fade 300ms

OVERLAY LAYERS (in tab order):
1. id="layer-elevation"     src="elevation.png"
2. id="layer-precipitation" src="precipitation.png"
3. id="layer-lithology"     src="lithology.png"
4. id="layer-contours"      src="contours.png"

TAB COMPONENT (right side, vertical stack):
- Tab style: pill shape, color #4A9ECA border, 
  muted fill when inactive, solid fill when active
- One tab per layer:
  [ Elevation ]
  [ Precipitation ]
  [ Lithology ]
  [ Distance to Coast ]

Clicking a tab:
  1. Active tab highlights
  2. Current layer fades out (opacity 1 to 0, 300ms)
  3. New layer fades in (opacity 0 to 1, 300ms)
  4. Annotation text below map updates

ANNOTATION TEXT (below map, updates per active tab):
- Elevation: "Elevation shapes temperature, weathering rate, 
  and soil development time across the continent, from the 
  low coastal margins to the high interior plateau."
- Precipitation: "Precipitation determines how much water 
  moves through Antarctic soils, controlling the leaching 
  of soluble ions and the distribution of pH across 
  ice-free regions."
- Lithology: "The underlying rock type sets the mineral 
  foundation of every soil, with volcanic, metamorphic, 
  and sedimentary substrates each producing distinct 
  geochemical signatures."
- Distance to Coast: "Distance to the coast captures the 
  gradient of marine influence, from nitrogen-rich soils 
  near penguin and seal colonies to the nutrient-depleted 
  interior."

DIG DEEPER PANEL CONTENT (Scene 3):
Title: "About these maps"
Body:
  "All maps were created in ArcGIS using publicly 
  available satellite data in the WGS 84 / Antarctic 
  Polar Stereographic projection.

  Sources:
  - Base map: Earthstar Geographics
  - Elevation: REMA (Reference Elevation Model 
    of Antarctica)
  - Precipitation: RACMO (Regional Atmospheric 
    Climate Model)
  - Distance to Coast: SCAR Antarctic Digital Database

  Note on Lithology:
  9 lithology codes classify rock type at each sample:
  a – Intermediate volcanic
  b – Mafic-ultramafic volcanic
  c – Cover sediments (glacial till)
  d – Mafic intrusive
  g – Felsic intrusive
  n – High-grade metamorphic
  p – Low-medium grade metamorphic
  s – Beacon Supergroup sedimentary
  w – Mixed sedimentary and volcanic"

---

SCENE 4 — THE 28 LOCATIONS, 171 SAMPLES

Layout: Full-width Antarctica map with sample dots overlay

MAP: samples.png displayed full width

SCROLL SEQUENCE:
Step 1: Map appears, no dots yet

Step 2: Colored outlined box appears around 
        Transantarctic Mountains cluster.
        Colored tab appears on right: 
        color #A34A2A, label "Transantarctic Mountains"
        Info panel shows:
          Name: "Transantarctic Mountains"
          Sample count: "107 samples"
          Description: "A 3,500 km mountain range dividing 
          East and West Antarctica, containing some of the 
          continent's largest and most geochemically diverse 
          ice-free valleys."

Step 3: Box + tab appear for South Victoria Land:
        color #C49A5A
          Name: "South Victoria Land"
          Sample count: "71 samples"
          Description: "A dense cluster of ice-free terrain 
          near McMurdo Station, characterized by cold desert 
          soils, glacial moraines, and strong marine nutrient 
          input from nearby penguin colonies."

Step 4: Box + tab appear for North Victoria Land:
        color #7A8F5A
          Name: "North Victoria Land"
          Sample count: "8 samples"
          Description: "A geologically complex coastal region 
          dominated by volcanic and metamorphic rock, with 
          sparse, nutrient-poor soils and limited 
          biological activity."

Step 5: Box + tab appear for NW Antarctic Peninsula:
        color #8A5E4A
          Name: "North-West Antarctic Peninsula"
          Sample count: "15 samples"
          Description: "The warmest and wettest part of 
          Antarctica, with relatively high biological 
          activity, greater organic matter accumulation, 
          and soils strongly influenced by marine fauna."

Step 6: Scroll past map. Dark background. 
        Image appears: 28_regions.png (centered)
        Caption below image:
        "Within these 4 regions, 171 samples were collected 
        across 28 sub-locations."

Step 7: New text appears below image:
        "This is a very limited dataset for understanding 
        Antarctic ice-free soils. Can we predict 
        geochemistry in regions we have never sampled?"

DIG DEEPER PANEL CONTENT (Scene 4):
  "Note on sample sizes: The sample sizes shown reflect 
  our original total of 201 samples. After cleaning the 
  dataset for missing values and errors, 171 samples 
  remained for analysis. Shackleton Glacier alone 
  contributes approximately 31% of the dataset, which 
  may have over-influenced the models."

---

SCENE 5 — WHAT WE WANT TO PREDICT

Layout: Dark background, centered cards

Title: "What we want to predict"

SCROLL SEQUENCE:
Cards appear one at a time, sliding up from below 
(transform: translateY 40px to 0, opacity 0 to 1, 
500ms ease).

Each card: horizontal layout, colored left border (6px), 
dark background #111827, rounded corners, padding 24px.

CARD FORMAT:
- Large element abbreviation (left, bold)
- Element name (below abbreviation)
- One-sentence description (right of abbreviation)
- Card accent color matches element color

CARD 1 — Nitrogen
  Abbreviation: N
  Name: Nitrogen
  Color: #0E7A6E
  Description: "The primary nutrient limiting biological 
  growth in polar soils, concentrated near coastal areas 
  where marine animals deposit organic matter."

CARD 2 — Potassium
  Abbreviation: K
  Name: Potassium
  Color: #2E4FA8
  Description: "Released slowly through rock weathering, 
  potassium levels in Antarctic soils reflect the age and 
  mineral composition of the underlying geology."

CARD 3 — Sodium
  Abbreviation: Na
  Name: Sodium
  Color: #5A2E8A
  Description: "Salt accumulates in Antarctic soils through 
  wind-blown sea spray and ancient marine deposits, with 
  high concentrations acting as a hard limit on 
  microbial survival."

CARD 4 — Phosphate
  Abbreviation: P
  Name: Phosphate
  Color: #8A1A4A
  Description: "A critical nutrient for biological activity, 
  phosphate in Antarctic soils comes almost entirely from 
  parent rock weathering and marine fauna inputs 
  near the coast."

After all 4 cards visible, text appears below:
"These are the four target elements we predict in 
unsampled regions using satellite-derived 
spatial variables."

DIG DEEPER PANEL CONTENT (Scene 5):
  "Note on targets: After processing all 171 samples, 
  we measured 58 total unique geochemical characteristics. 
  This visualization focuses on the top 4 by model 
  performance.

  More precise measurement names:
  - Nitrogen: Delta-15N (Nitrogen Isotope Ratio)
  - Potassium: K digest (Total Acid-Extractable Potassium)
  - Sodium: Na digest (Total Acid-Extractable Sodium)
  - Phosphate: PO4 total (Phosphate in Total Leachate)"

---

SCENE 6 — THE THREE MODELS

Layout: Dark background, three circular cards in 
a horizontal row

Title: "The Machine Learning Algorithms"

SCROLL SEQUENCE:
Cards appear left to right, one per scroll step.
Each card: circle shape, white fill #E8F4F8, 
dark text, centered content.

CARD FORMAT:
- Model abbreviation (large, bold, top)
- Full model name (smaller, below)
- SVG schematic illustration (center of circle)
- One-sentence description (below circle)

CARD 1 — KNN (leftmost)
  Abbreviation: KNN
  Full name: K-Nearest Neighbors
  Description: "Predicts a new location's soil chemistry 
  by finding the most similar sampled locations and 
  averaging their values."
  Schematic: 5 dots, with lines connecting 4 outer dots 
  to 1 central dot. Draw as inline SVG.

CARD 2 — RF (center)
  Abbreviation: RF
  Full name: Random Forest
  Description: "Builds hundreds of decision trees on 
  random subsets of the data and averages their 
  predictions to produce a more stable result."
  Schematic: Branching tree. 1 line splits into 2, 
  each splits into 2 more. Draw as inline SVG.

CARD 3 — XGB (rightmost)
  Abbreviation: XGB
  Full name: XGBoost
  Description: "Builds trees sequentially, where each 
  new tree corrects the errors of the previous one, 
  improving prediction accuracy with each step."
  Schematic: 3 stacked horizontal bars, each slightly 
  shorter than the one above. Draw as inline SVG.

Caption below all three cards:
"Each model performs differently depending on the target. 
Comparing all three gives important insight into the 
complex relationship between predictors and soil chemistry."

DIG DEEPER PANEL CONTENT (Scene 6):
  "How we evaluated the models:

  Cross-validation splits the dataset into training and 
  testing sets repeatedly so the model is always tested 
  on samples it has never seen.

  Leave-one-out validation is stricter: with only 171 
  samples, we trained on 170 and tested on 1, repeating 
  for every sample.

  RMSE measures average prediction error in the original 
  units of the data. Lower is better.

  R² measures how much variation in soil chemistry the 
  model explains. Our best targets reached around 0.40.

  Model selection matters because KNN, Random Forest, 
  and XGBoost each perform differently per target. 
  Predictions shown use the best-performing model 
  for each property.

  For full methodology: 
  https://github.com/lilyeliason/ansoil-spatial-prediction

  Learn more about each model:
  KNN: https://www.pinecone.io/learn/k-nearest-neighbor/
  RF: https://williamkoehrsen.medium.com/random-forest-simple-explanation-377895a60d2d
  XGB: https://medium.com/low-code-for-advanced-data-science/xgboost-explained-a-beginners-guide-095464ad418f"

---

SCENE 7 — THE PREDICTION MAPS

Layout: Close-up half view of Antarctica (left side 
of continent focused to show sample-dense regions).
Map takes full width.

ELEMENT SELECTOR:
4 colored rectangular buttons in 2x2 grid, 
top corners of the map:
  Top left:  [ Nitrogen ]  [ Potassium ]
  Top right: [ Sodium ]    [ Phosphate ]
Each button colored with its established element color.
Default active: Nitrogen.

MAP DISPLAY:
- Sample locations shown as small black squares
- Random grid prediction points shown as small circles
- When an element is selected, prediction grid points 
  for that element color according to its element color
- Points with no successful prediction remain gray

INFO PANEL (right side of map, updates per element):

NITROGEN (color: #0E7A6E)
  Standing: "Best-predicted target in the project."
  Results:
    Winner: XGB — R² = 0.416
    RF — R² = 0.383
    KNN — R² = 0.322
  Driven by: Distance to Coast, Lithology, Elevation
  Why: "Nitrogen isotopic signatures reflect marine aerosol 
  input near the coast, biological cycling rates, and 
  variation with rock substrate and elevation."

POTASSIUM (color: #2E4FA8)
  Standing: "Second best-predicted target, one of the 
  most stable across model runs."
  Results:
    Winner: XGB — R² = 0.396
    RF — R² = 0.359
    KNN — R² = 0.065
  Driven by: Lithology, Precipitation, Temperature
  Why: "Potassium is strongly tied to parent rock 
  mineralogy, particularly in sedimentary rock substrates."

SODIUM (color: #5A2E8A)
  Standing: "Third best-predicted target."
  Results:
    Winner: XGB — R² = 0.391
    RF — R² = 0.380
    KNN — R² = 0.318
  Driven by: Elevation, Lithology, Distance to Coast
  Why: "Sodium comes from two main sources: direct mineral 
  weathering from lithology, and marine aerosol deposition, 
  where lower-elevation coastal soils receive more 
  sea-spray sodium."

PHOSPHATE (color: #8A1A4A)
  Standing: "Fourth best-predicted target."
  Results:
    Winner: RF — R² = 0.367
    XGB — R² = 0.363
    KNN — R² = 0.168
  Driven by: Temperature, Elevation, Precipitation
  Why: "Phosphate availability appears strongly 
  temperature-controlled, possibly through weathering 
  rates or biological phosphorus cycling."

---

SCENE 8 — LIMITATIONS

Layout: Full-width Antarctica base map, 
dark background

Text above map (scroll step 1):
"This research is ongoing. Results and predictions 
are subject to change."

Text replaces it (scroll step 2):
"With that said, there are meaningful limitations 
to acknowledge."

BUBBLES: Appear one by one floating around the map, 
each on a scroll step. Style: rounded pill, 
white border, white text, semi-transparent dark fill.

If animated cloud overlay is feasible:
  Add a semi-transparent hazy animated layer slowly 
  rotating over the map to suggest uncertainty. 
  If not feasible, use a static blurred overlay.

Bubble 1: "Very limited and regionally unbalanced dataset"
Bubble 2: "Biological predictor variables were not included"
Bubble 3: "MAPE values are high even for strong predictions"
Bubble 4: "Seed variation between model runs"

DIG DEEPER PANEL CONTENT (Scene 8):
  "Bubble 1: With only 171 samples, machine learning is 
  difficult. Shackleton Glacier alone contributes 31% of 
  the dataset and may have over-influenced results.

  Bubble 2: Biological variables such as penguin colony 
  locations, vegetation maps, and microorganism data 
  could improve predictions meaningfully.

  Bubble 3: High MAPE (Mean Absolute Percentage Error) 
  means individual point predictions are unreliable. 
  The model's primary value is in identifying 
  spatial patterns, not precise point estimates.

  Bubble 4: RF and XGBoost were run with multiple random 
  seeds. Different seed combinations produced some 
  variation in reported values."

---

SCENE 9 — WHY ANY OF THIS MATTERS

Layout: Transitions from dark to white background 
as user scrolls through panels.

Title: "Why Any of This Matters"

Three panels, one per scroll beat. 
Each panel: image on one side, text on other.

PANEL 1 — Climate
  Image: ant_mass_change.png
  Text: "As the planet warms, Antarctic ice shelves are 
  melting and ice-free areas are expanding. These soils 
  act as delicate carbon sinks or sources. Understanding 
  their geochemical makeup helps predict permafrost 
  degradation, assess toxic trace element remobilization 
  risk, and understand how ecosystems adapt as 
  habitats expand."

PANEL 2 — Field Science
  Image: ant_field_work.png
  Text: "Predictive models do not replace field science, 
  they help inform it. Continent-wide prediction maps 
  can guide targeted field expeditions focused on 
  specific characteristics, saving significant time, 
  money, and resources."

PANEL 3 — Astrobiology
  Images side by side:
    Left: ant_dry_valley.jpeg 
          Caption: "Wright Valley, Antarctica"
    Right: marsdry_valley.png 
           Caption: "Ubajara, Mars"
  Text: "Antarctic ice-free soils are the closest analog 
  on Earth to the Martian surface and serve as crucial 
  terrestrial analogs for astrogeology, providing 
  accessible extreme-environment settings for testing 
  geological and biological processes."

DIG DEEPER PANEL CONTENT (Scene 9):
  Image Credits:
  - NASA ICESat and ICESat-2. (2020). A Satellite Lets 
    Scientists See Antarctica's Melting Like Never Before. 
    New York Times.
  - Unsworth, M. (2026). Cold outpost. 
    Encyclopaedia Britannica.
  - Arcus, C. (2002). View of the Wright Valley. 
    Antarctica New Zealand Pictorial Collection.
  - NASA/JPL-Caltech/MSSS. (2023). Curiosity Mars rover. 
    Universe Today.

---

SCENE 10 — CLOSING

Layout: Return to opening globe, full-bleed dark background

VISUAL: Same globe as Scene 1, slowly rotating.
Ice-free flecks now appear in multiple colors from 
the full color palette (nitrogen teal, potassium indigo, 
sodium violet, phosphate crimson, mixed).

CLOSING TEXT (centered, fades in line by line):
Line 1: "Antarctica is one of the most unique and complex 
         places on Earth."
Line 2: "These predictions are imperfect."
Line 3: "The uncertainty is real."
Line 4: "And the questions they raise — about what 
         survives here, what is changing, and what this 
         place has to teach us — are just beginning 
         to be asked."

CREDITS (appear below closing text):
"Research and Visualization by Lily Eliason"
"In collaboration with the LeMonte Lab of Geochemistry, 
Brigham Young University"

THREE BUTTONS (bottom of screen, colored rectangles):
  [ Explore the Data ]  → link to data CSV
  [ Learn More ]        → https://github.com/lilyeliason/ansoil-spatial-prediction
  [ Content References ] → link to references page

---

IMPLEMENTATION NOTES FOR CLAUDE CODE:

1. Build one scene at a time. Confirm each scene works 
   in the browser before moving to the next.

2. The Dig Deeper button is a fixed overlay present 
   from Scene 3 onward. It opens a slide-in panel 
   from the right. Panel content updates based on 
   which scene is currently active. Track active scene 
   with a global variable updated by Scrollama.

3. Scene 3 map component and Scene 7 map component 
   should share the same CSS class and base layout 
   so they look visually consistent.

4. All image overlays in Scene 3 must be exported 
   at identical pixel dimensions and positioned 
   identically so they register correctly when stacked.

5. Add a keyboard shortcut during development: 
   right arrow key advances to next scroll step. 
   Remove before final submission.

6. Test on both a wide desktop screen and a 
   narrow mobile screen after each scene is built.