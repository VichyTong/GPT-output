## 1. REMOVE

### Examples:
- [Remove]{operation} the [supernatant]{reagent1}.
- [Remove]{operation} [photoresist]{reagent1} with [acetone]{method}.
- [Remove]{operation} [3 mL albumen]{reagent1} with a [syringe]{device}.
- [Remove]{operation} [ethanol]{reagent1} after [30 seconds]{time} incubation [without destroying the bead pellet]{notice}.
- [Remove]{operation} [no more than two dishes]{reagent1} at a time from [incubator]{device}.
- [Remove]{operation} [all traces of fluid]{reagent1} by [aspiration]{method}.
- [Remove]{operation} [40 μL Washing solution]{reagent1}.
- [Remove]{operation} [the brain from the skull]{reagent1} [carefully]{notice}.
- [Discard]{operation} [supernatants]{reagent1}.
- [Discard]{operation} [the flow-through fraction]{reagent1}.
- [Discard]{operation} the [protein solution]]{reagent1}

### Notices:

### Synonyms:
- DISCARD

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The item to be removed |
| method | optional \| string | The method used to remove the item |
| device | optional \| string | The device used to remove the item |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 2. ADD

### Examples:
- [Add]{operation} [400 µl of methanol]{reagent1}, [300 µl of water]{reagent2} and [100 µl of chloroform]{reagent2} to the [protein solution]{reagent1}.
- [Add]{operation} [endoproteinase Lys-C]{reagent2} at an [enzyme:substrate ratio of 1:50]{ratio}.
- [Add]{operation} [hydrochloric acid]{reagent2} to a [final concentration of 200 mM]{concentration}.
- [Add]{operation} [1 µl lysis buffer (LB)]{reagent2} into each [PCR tube that contains samples and 1st NTC]{reagent1}.
- [Apply]{operation} [a drop of normal goat serum]{reagent2} to each [specimen]{reagent1}.
- [Apply]{operation} [ocular lubricant]{reagent2} to the [eyes of the mouse]{reagent1}.

### Notices:

### Synonyms:
- APPLY

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The primary reagent to which other reagents are added |
| reagent2 | optional \| reagent | Additional reagents to be added to the primary reagent |
| ratio | optional \| string | The ratio of reagents to be added, if applicable |
| concentration | optional \| concentration | The final concentration of the reagent to be added, if applicable |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 3. TRANSFER

### Examples:
- [Transfer]{operation} the [frozen samples]{reagent1} to a [storage box]{destination}.
- [Transfer]{operation} [10 ul]{volume} of the [culture]{reagent1} to a [tube]{destination}.
- [Transfer]{operation} the [supernatant]{reagent1} to a [fresh Eppendorf tube]{destination}.
- [Transfer]{operation} [1 µl]{volume} of [PBS with your target single cell]{reagent1} into the [bottom of a PCR tube]{destination}.
- [Transfer]{operation} the [cryovials]{reagent1} into a [laminar flow hood]{destination}.
- [Pour]{operation} out the unabsorbed PDDA from the [wells]{object}.
- [Pour]{operation} the [extract]{object} onto the [filter paper]{target}.
- [Pour]{operation} ~40 g PDMS to the [master]{object} in the [petri dish]{target} and degas PDMS in a [vacuum desiccator]{device}.
- [Pour]{operation} the [medium-Chiron mix]{object} into a [tray]{target} and add 150 μl of this mix to all wells using a [multichannel]{tool} and [DNA LoBind tips]{tool}.
- [Pour]{operation} the [PDMS pre-gel reagent]{object} on the [silicon master]{target} and incubate in oven at 85 °C for 1 hour for gelling.
- [Move]{operation} to the [next cross-linked peptides]{object} until going through all peptides in the ['target']{list} list.
- [Move]{operation} the [plate]{object} back and forth to plate the [cells and the drugs]{subject} evenly.
- [Move]{operation} all [media]{object} to [room temperature]{destination} to warm up [20 minutes]{time} before starting.
- [Move]{operation} the [needle tip]{object} to [the hole]{destination} and set it to the level of [skull surface]{position}.
- [Move]{operation} the [one-axis stage]{object} that holds the [MEMS]{object2} (the component 1 in Fig).
- [Decant]{operation} the [supernatant]{reagent1}.
- [Decant]{operation} [supernatant]{reagent1} and [resuspend SVF cell pellet in 2 ml RBC lysis buffer]{operation2}.
- [Decant]{operation} the [acetone]{reagent1}.
- [Decant]{operation} [the supernatant]{reagent1} [as soon as the rotor stops]{notice}.
- [Decant]{operation} [PFA]{reagent1} and [rinse with PBS]{operation2}.
- [Return]{operation} the [remaining blood]{item} to the [jugular vein]{location}.
- [Return]{operation} the [flask]{item} to [incubator]{location}.
- [Return]{operation} the [test mouse]{item} to its [home cage]{location}.
- [Return]{operation} the [plates]{item} to the [37<sup>0</sup>C 5% CO<sub>2</sub> tissue culture incubator]{location} for [48hours]{time}.
- [Return]{operation} the [constructs]{item} into an [incubator]{location} and left them at least [24 hours]{time} to allow for gel contraction.

### Notices:

### Synonyms:
- POUR
- MOVE
- DECANT
- RETURN

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| source | optional \| string | The source from where the sample is being transferred |
| destination | required \| string | The destination where the sample is being transferred |
| reagent1 | required \| reagent | The sample being transferred |
| volume | optional \| volume |  |
| equipment | optional \| string | Any equipment used during the transfer |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 4. INCUBATE

### Examples:
- [Incubate]{operation} [protein-DNA complexes]{reagent1} at [ambient temperature]{temperature} for [30 minutes]{time} [prior to measurements]{notice}.
- [Incubate]{operation} the [sample]{reagent1} at [37 ºC]{temperature} for [45 minutes]{time}.
- [Incubate]{operation} at [75 °C]{temperature} for [10min]{time}.
- [Incubate]{operation} for [30 minutes]{time} on [ice]{environment}, [protected from light]{notice}.
- [Incubate]{operation} the [muscularis pieces]{reagent1} with [100 U/ml collagenase D]{reagent2} and [30 µg/ml DNaseI in HBSS/20 % FCS]{reagent2} at [37 °C]{temperature} for [45 minutes]{time}.
- [Immerse]{operation} the [wafer]{object1} in [buffered oxide etch (6:1 NH4F:HF)]{reagent1} for [3 minutes]{time} at [ambient temperature]{temperature}.
- [Immerse]{operation} the [wafer]{object1} in [diluted hydrochloric acid solution (DI water: HCl = 1:1)]{reagent1} for [15 seconds]{time}.
- [Immerse]{operation} the [two pieces of PLNs]{object1} in [fluorescence mounting medium]{reagent1}.
- [Immerse]{operation} the [tissue blocks with the optic chiasma]{object1} into the [fixative]{reagent1} for [3 h]{time}.
- [Immerse]{operation} the [tissue]{object1} into [20% THF in water]{reagent1} in a [screw-capped glass bottle]{device} for at least [1 hour]{time} at [room temperature]{temperature}.

### Notices:

### Synonyms:
- IMMERSE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be incubated |
| reagent2 | optional \| reagent | Additional reagents added during incubation |
| temperature | required \| temperature | default=room temperature |
| time | required \| time | default=appropriate time |
| environment | optional \| string |  |
| device | optional \| string |  |
| thermoProgram | optional \| string | when "device"=thermocycler, this parameter should be changed to REQ |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 5. SUSPEND

### Examples:
- [Suspend]{operation} [2 million cells]{reagent1} in [150 µl of ice-cold lysis buffer]{reagent2}.
- [Suspend]{operation} [frozen yeast cell pellets]{reagent1} from [500-ml cultures in 5 ml lysis solution]{reagent2}.
- [Suspend]{operation} [the cell pellet]{reagent1} by adding [50 µl of 1X PBS]{reagent2} per ml of culture.
- [Suspend]{operation} [1-5 million cells]{reagent1} in the [labeling medium]{reagent2} for [10 min]{time} at [37 ˚C]{temperature}.
- [Suspend]{operation} [the cells]{reagent1} in [1 mL of PBS]{reagent2}.
- [Resuspend]{operation} in [2 ml PBS]{reagent1} and perform magnetic column enrichment using [LS columns]{device}, according to the manufacturers’ protocol.
- [Resuspend]{operation} cells in ~200 ul [PBS containing 1X PI]{reagent1}, transfer to a [FACS tube]{device}, and store at [4°C]{temperature} until analysis.
- [Resuspend]{operation} sperm pellet in [10 uL PBS]{reagent1}.
- [Resuspend]{operation} the pellet in [1 mL EGM-2 medium]{reagent1} and count the cells using a [hemocytometer]{device}.
- [Resuspend]{operation} the washed beads in [100µl 1x LysBB per reaction]{reagent1} and add of [2µl of CV2_btn (100 µM)and 2µl CV16_btn (100 µM) per reaction]{reagent2}, rotate tubes for [10min]{time} at [room temperature]{temperature} for binding of the oligonucleotides to the beads.
- [Resuspend]{operation} cells in [PBS containing PE-Sca1, APC-cKit, Streptavidin-APC/eFluor780 antibodies]{reagent1}.
- [Resuspend]{operation} cells thoroughly with[0.5mL 0.06M potassium chloride.]{reagent1}
- [Resuspend]{operation} RNA pellet with [200 μL of RNase-free water.]{reagent1}
- [Resuspend]{operation} the cell pellet in [10 ml of 106 medium (Gibco) supplemented with LSGS (Gibco)]{reagent1} and plated into a [T75 flask]{device} (one cryovial to one T75).
- [Resuspend]{operation} the bead in [10 μL of 2X Biotin Binding Buffer]{reagent1} and add to the samples.
- [Resuspend]{operation} beads in [50 μL of PCR master mix]{reagent1}: [25 μL Phusion HF 2X, 1 μL Nextera Ad1.1 (Universal) 12.5 uM, 1 μL Nextera Ad2.x (Barcoded) 12.5 uM, 23 μL Water]{reagent2}.
- [Resuspend]{operation} the cells to a final concentration of approximately [1x10<sup>7</sup> cells per ml in Dulbecco&#x2019;s calcium-magnesium free phosphate buffered saline]{reagent1}.
- [Resuspend]{operation} beads in [42 µl of H<sub>2</sub>O]{reagent1}, put on magnetic rack for [5 min]{time}.

### Notices:

### Synonyms:
- RESUSPEND

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be suspended |
| reagent2 | optional \| reagent | The medium or buffer in which the reagent is suspended |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 6. PLATE

### Examples:
- [Plate]{operation} [hOBs]{reagent1} at a density of [3000 cells/cm^2]{density} in [growth media]{reagent2}.
- [Plate]{operation} the [shocked cells]{reagent1} onto the [SD -Trp, -Leu selective media]{reagent2}.
- [Plate]{operation} [100 µl]{volume} onto [Cl-Phe/Kan 50 µg/ml plate]{reagent2}.
- [Plate]{operation} the [cells]{reagent1} on [LB agar plates]{reagent2} containing [appropriate combination of antibiotics]{additionalReagents}.
- [Plate]{operation} [75,000 4T1 cells]{reagent1} per well in a [6-well-plate]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The type of cells to be plated |
| reagent2 | optional \| reagent | The destination for plating |
| density | optional \| number | The density of cells to be plated per cm^2 or per well |
| reagent0 | required \| reagent |  |
## 7. COLLECT

### Examples:
- [Collect]{operation} all the [cell culture media]{reagent1} in the well into a [15 ml tube]{container} [using a pipette]{method}.
- [Collect]{operation} [cells]{reagent1} by [centrifugation (200 g, 5 min, room temperature)]{method}.
- [Collect]{operation} the [supernatant]{reagent1} from [the upper part of the incubation mixture in step 7]{source}.
- [Collect]{operation} [samples]{reagent1} under [sterile conditions]{environment}.
- [Collect]{operation} [blood]{reagent1} and [tissues]{reagent1} for [analysis when animals are culled and/or at the study end-point]{purpose}.
- [Obtain]{operation} the radial magnitude pattern at each longitudinal location by multiplying the normalized radial magnitude pattern by the measured displacement at the given longitudinal location.
- [Obtain]{operation} mature DCs by a 40-h stimulation of iDCs with CD40L-transfected J558L cells \(at a DC/J558L ratio of 1:1), as previously described, or with soluble r-CD40L molecules \(Alexis Biochemicals, Alexis Corporation).
- [Obtain]{operation} the brain from C57 Black/6 mice (16–21 days old for cerebellar slices, 6-8 weeks old for hippocampal slices), then place in ice-cold artificial cerebrospinal fluid (ACSF) cutting solution (in mM).
- [Obtain]{operation} B cells by CD43 negative purification using anti-CD43 magnetic beads.
- [Obtain]{operation} a new microcentrifuge tube if separating crystals from source.
- [Capture]{operation} biotinylated thrombin with streptavidin agarose.
- [Capture]{operation} each Z-stack at a minimum resolution of 512x512.
- [Capture]{operation} the image of the stapes footplate using a digital camera through a stereomicroscope.
- [Capture]{operation} images of stained slides by Pannoramic 250 Flash II slide scanner or other microscope.
- [Capture]{operation} Z-stacked images of randomly chosen HEK293T cells by confocal microscopy \(63 x objective), maintaining the same acquisition parameters throughout the acquisition.

### Notices:

### Synonyms:
- HARVEST
- OBTAIN
- CAPTURE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The item to be collected |
| container | required \| reagent | The container where the item will be collected |
| method | optional \| string | The method used to collect the item |
| environment | optional \| string | The condition under which the item is collected |
| purpose | optional \| string | The purpose of collection |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 8. MIX

### Examples:
- [Mix]{operation} [media]{reagent1} well by [inversion]{method} [before use]{notice}.
- [Mix]{operation} [1:1]{ratio} with [Trypan Blue]{reagent2}.
- [Mix]{operation} well by [vortexing]{method}.
- [Mix]{operation} by [pipetting]{method} [carefully to make the stock of the single cell suspension]{notice}.
- [Mix]{operation} well.
- [Mix]{operation} [10 μg total RNA]{reagent1} with [Loading Buffer]{reagent2} [1:1]{ratio}.
- [Combine]{operation} 20-100 μg of total [RNA]{reagent1}, 50 μL [MTSEA-biotin-XX]{reagent2}, 25 µL 10x [Biotinylation buffer]{reagent3} and sufficient [DEPC-treated water]{reagent4} to generate a 250 μL reaction.
- [Combine]{operation} [resin]{reagent1} and [hexylene glycol]{reagent2} at 1:2 ratio, add to dish, mix on rotor for 2 hours.
- [Combine]{operation} the topoisomerase I-relaxed circular [DNA (in tube B)]{reagent1} and core histones (in tube A) that were pre-incubated with, in our experiments, GST or GST-JDP2 in 50 µl of [assembly buffer]{reagent2}.
- [Combine]{operation} fractions which contain the product, and then remove the solvent under a rotary evaporator to yield the product as a yellowish solid.
- [Combine]{operation} the [water extracts]{reagent1}, wash the solution with [ethyl ether (2 × 30 mL)]{reagent2}.

### Notices:

### Synonyms:
- COMBINE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The main reagent to be mixed |
| reagent2 | optional \| reagent | Additional reagents to be mixed |
| ratio | optional \| string | The ratio of reagents to be mixed |
| method | optional \| string | The method of mixing, such as inversion, vortexing, pipetting, etc. |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 9. DILUTE

### Examples:
- [Dilute]{operation} the [Rhodamine fluorescently labelled Ultra-Magnetic Liposomes (UMLs)]{reagent1} in a [10mM Hepes pH 7.4, 20mM Na3Citrate, 108mM NaCl buffer solution]{reagent2} to a final concentration of [0.1M]{targetConcentration}.
- [Dilute]{operation} the [overnight culture]{reagent1} with [fresh]{reagent2} to [OD600 of 0.15]{targetConcentration}.
- [Dilute]{operation} [4 ug plasmid DNA]{reagent1} in [250 μl of Opti-MEM®]{reagent2}.
- [Dilute]{operation} [1000x rhIFN-γ solution]{reagent1} by [1:5]{targetConcentration} in [DPBS]{reagent2}.
- [Dissolve]{operation} the [solid]{reagent1} in a [minimal amount of boiling methanol]{reagent2}.
- [Dissolve]{operation} the [precipitate]{reagent1} in [50 mM Tris-HCl, pH 7.5, 0.15 M NaCl]{reagent2} at a concentration of [3 mg/ml]{concentration}.
- [Dissolve]{operation} [1 microlitre of the reconstituted dye (i.e in DMSO)]{reagent1} in [1ml of 1X PBS]{reagent2} to give a final concentration of [10uM]{concentration}.
- [Dissolve]{operation} [appropriate amount of streptozotocin]{reagent1} with [STZ/acetate buffer]{reagent2} and inject the mouse (i.p., 175-250 mg kg-1 body weight).
- [Dissolve]{operation} the [components of the coupled transcription-translation _E]{reagent1}.

### Notices:

### Synonyms:
- DISSOLVE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be diluted |
| reagent2 | optional \| reagent | The reagent used for dilution |
| targetConcentration | required \| concentration | The final concentration of the diluted reagent |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 10. SHAKE

### Examples:
- [Shake]{operation} at [4,800 rpm]{intensity} for [50 seconds]{time} by the [Mini Beadbeater]{device} to [remove epithelial cells]{purpose}.
- [Shake]{operation} the [dish]{reagent1} at [37ºC]{temperature} for [30 minutes]{time}.
- [Shake]{operation} the [sealed tubes]{reagent1} at [37 ºC]{temperature} for [15 minutes]{time}.
- [Shake]{operation} the [tube]{reagent1} [vigorously]{notice} for [15 sec]{time}.
- [Shake]{operation} the [PCR clean-up plate]{reagent1} using the [plate shaker]{device} at [1800 rpm]{intensity} for [2 minutes]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be shaken |
| temperature | optional \| temperature | default=room temperature |
| time | required \| time | default=appropriate time |
| intensity | optional \| intensity | The intensity of shaking |
| device | optional \| string |  |
| purpose | optional \| string | The purpose of shaking |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 11. CENTRIFUGE

### Examples:
- [Centrifuge]{operation} [sample]{reagent1} at [14,000 g]{intensity} for [1 minute]{time}.
- [Centrifuge]{operation} the [samples]{reagent1} at [2,000 rpm]{intensity} for [20 min]{time} at [room temperature]{temperature}.
- [Centrifuge]{operation} [cells]{reagent1} at [370g]{intensity} for [5min]{time} to collect cells.
- [Centrifuge]{operation} for [30 min]{time} at [12,000 rcf]{intensity} ([4°C]{temperature}).
- [Centrifuge]{operation} the [cell suspension]{reagent1} at approximately [100–200 × g]{intensity} for [5 to 10 minutes]{time}.
- [Concentrate]{operation} if necessary.
- [Concentrate]{operation} eluate in speedvac to [22.5 µL]{volume}.
- [Concentrate]{operation} the [chromatin]{reagent} to [0.3 mg/mL]{concentration} using a [concentrator]{device}.
- [Concentrate]{operation} the [commercial silver colloid 10 times]{reagent} by centrifugation and disperse in ultrapure water to give final concentration of [1.2 nM]{concentration}.
- [Concentrate]{operation} the [protein to 1 mg/mL or greater]{reagent}.
- [Concentrate]{operation} protein to ~ 10-15 mg ml.
- [Concentrate]{operation} the [sample]{reagent} at 16000xg for at 4˚C until the volume goes down to ~ 30 µL.
- [Concentrate]{operation} the [sample]{reagent} by the 0.5 mL Amicon 10K spin column at 16000xg for at 4˚C until the volume goes down to ~ 50 µL.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The sample to be centrifuged |
| intensity | required \| number | The intensity at which to centrifuge the sample, usually represented as rpm/xg/rcf |
| time | required \| time | The duration for which to centrifuge the sample |
| temperature | optional \| temperature | default=room temperature |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 12. PURIFY

### Examples:
- [Purify]{operation} [CD11c-positive cells]{reagent1} twice using [CD11c MicroBeads]{device} according to the manufacturer’s instructions.
- [Purify]{operation} the [pre-PCR product]{reagent1} as described in [Box1]{device}.
- [Purify]{operation} the [PCR products]{reagent1} by [QIAquick PCR purification column]{device}.
- [Purify]{operation} and concentrate [PCR product]{reagent1} using [DNA Clean and Concentrator 5 columns]{device}.
- [Purify]{operation} [RNA]{reagent1} using a [RNeasy Micro Kit]{device} (Qiagen).
- [Purify]{operation} the [DNA]{reagent1} from 50 µl of the digested chromatin fraction by [phenol-chloroform extraction]{method} followed by ethanol precipitation.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be purified |
| method | optional \| string | The method used to purify the reagent |
| device | optional \| string | The device used for purification |
| reagent0 | required \| reagent |  |
## 13. REPLACE

### Examples:
- [Replace]{operation} the [waste tube]{reagent1} with a [collection microcentrifuge tube]{reagent2}.
- [Replace]{operation} the [egg]{reagent1} in the [incubator]{reagent2} in a [horizontal]{position} position [without shaking]{notice}.
- [Replace]{operation} [ultrapure water \(1.8 mL)]{reagent1} in the recording chamber with an equivalent volume of [degassed 0.5 mM CaCl<sub>2</sub> BSS]{reagent2} at [18°C]{temperature} using [a long needle Hamilton syringe]{device}.
- [Replace]{operation} [media]{reagent1} with [primary antibodies dissolved in the block solution]{reagent2}.
- [Replace]{operation} the [medium]{reagent1} [every day]{frequency}.
- [Change]{operation} the [species parameter setting]{param1} to [_Mus musculus_]{value1}.
- [Change]{operation} [half of the culture medium]{param1} (iii) [every other day]{time}.
- [Change]{operation} the [oven temperature]{param1} to [45°C]{value1}.
- [Change]{operation} the [medium]{param1} [every 2 days, for 10 days]{time}.
- [Change]{operation} the [medium]{param1} [every other day]{time} until [cells reach approximately 70% confluence]{environment}.
- [Change]{operation} the [medium]{param1} with [20 mL of fresh complete DMEM]{value1} and then [infect the LLC-MK2 cells with 1x10<sup>8</sup> trypomastigotes/flask]{additional_action}.
- [Change]{operation} the [objectives]{param1} from [×5]{value1} to [×100]{value2} to [have a clear view of the TFP and particles]{notice}.
- [Change]{operation} the [medium]{param1} at [2 days of culture]{time}.
- [Change]{operation} the [input data]{param1} (especially [pressure and temperature]{param2}) and [observe how it affects the outcome]{additional_action}.
- [Change]{operation} [Method Parameters tab]{param1} to [Average for general projection view]{value1}.
- [Change]{operation} the [colormap]{param1} to [your preference]{value1}.

### Notices:

### Synonyms:
- CHANGE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The item to be replaced |
| reagent2 | required \| reagent | The item to replace with, defult = another brand new reagent |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| position | optional \| string |  |
| frequency | optional \| frequency |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 14. MEASURE

### Examples:
- [Measure]{operation} [anisotropy]{parameter} using a [Safire (Tecan Group Ltd.) fluorescent plate reader]{device}.
- [Measure]{operation} [protein concentration]{parameter} using [bicinchoninic acid assay kit]{device}.
- [Measure]{operation} the [luminescence]{parameter} for [10 s]{time} [with a delay of 2s between injection and measurement]{notice}.
- [Measure]{operation} [absorbance]{parameter} of the [sample]{reagent1} at [550 nm]{wavelength} for [2 min]{time}.
- [Measure]{operation} [RNA concentration]{parameter} using a [Nanodrop]{device}.
- [Determine]{operation} [G-factor]{arg1} by measuring [1:1 complexes of each protein bound to its respective fluorophore-labeled substrate at the highest protein concentration]{measurementDetails}.
- [Determine]{operation} if [need to do further purification on S75 or S200]{task}.
- [Determine]{operation} the [total number of cells]{measurement1} and [% viability]{measurement2} using a [hemacytometer]{device} or [cell counter]{device} and [Trypan Blue exclusion]{method}.
- [Determine]{operation} the [protein concentration]{measurement} with [Bradford microplate microassay]{method} (Bio-Rad).
- [Determine]{operation} the [DNA concentration]{measurement} using a [spectrophotometer]{device}.

### Notices:

### Synonyms:
- DETERMINE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| device | optional \| string | The device used for measurement |
| reagent1 | optional \| reagent | The reagent used for measurement |
| parameter | required \| string | The parameter to be measured |
| time | optional \| time |  |
| wavelength | optional \| number | Wavelength used for measurement if applicable |
| notice | optional \| string |  |
| data0 | required \| number |  |
## 15. ASPIRATE

### Examples:
- [Aspirate]{operation} the [aqueous phase]{reagent1} [above the interface layer]{notice}.
- [Aspirate]{operation} [culture medium]{reagent1}.
- [Aspirate]{operation} the [collagen type I solution]{reagent1}.
- [Aspirate]{operation} [medium]{reagent1}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be aspirated |
| reagent2 | optional \| reagent | Additional reagents to be aspirated if any |
| volume | optional \| volume |  |
| device | optional \| string | Device used for aspiration |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 16. COAT

### Examples:
- [Coat]{operation} [samples]{reagent1} with [gold]{reagent2} using [sputter coater]{device}.
- [Coat]{operation} [each well surface]{reagent1} by filling up the wells for [2 h]{time} with [1% poly(diallyl dimethylammonium chloride) (PDDA)]{reagent2}.
- [Coat]{operation} [new 6-well culture plates]{reagent1} with [LN511E8 at 0.5 µg/cm<sup>2</sup> in 1.5 ml PBS]{reagent2}.
- [Coat]{operation} [35-mm glass bottom dish]{reagent1} with [0.01% (w/v) poly-lysine]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be coated |
| reagent2 | required \| reagent | The material used for coating |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 17. RINSE

### Examples:
- [Rinse]{operation} the [wafer]{reagent1} in [DI water]{reagent2} for [10 seconds]{time}.
- [Rinse]{operation} [twice]{repeat} with [1 ml PBS]{volume}.
- [Rinse]{operation} [gently]{notice} with [0.5mM EDTA in PBS]{reagent2} \(5 ml/ 75 cm<sup>2</sup> culture flask).
- [Rinse]{operation} the [tip of the titration needle]{reagent1} by flushing with [BSS]{reagent2} using a [1 mL PIPETMAN]{device}.
- [Rinse]{operation} the [solid substrate \(e.g., glass, silicon wafer)]{reagent1} with [ethanol]{reagent2}.
- [Wash]{operation} the slides in [0.01M PBS]{solution} for [5 min]{time} [three times]{count}.
- [Wash]{operation} with [PBS]{solution} and remove the muscle layers by tweezers under stereomicroscope.
- [Wash]{operation} harvested cells [three times]{count} with [1 mL with cold phosphate–buffered saline solution]{solution} by centrifuging at [1500 g for 5 minutes]{rotation}.
- [Wash]{operation} the [cell pellet]{collect} with [200 µl Mcllvaine’s buffer]{solution}.
- [Wash]{operation} samples [once]{count} with [PBS]{solution}.
- [Wash]{operation} once with [PBS]{solution}.
- [Wash]{operation} in [1 ml PBS]{solution}.
- [Wash]{operation} the [beads]{collect} [once for 5 min]{count} in [300 mM ammonium acetate]{solution} and once for 5 min in 150 mM ammonium acetate.
- [Wash]{operation} the [column]{collect} three times with [100 µl of 0.5% formic acid in water]{solution} by centrifuging for 2 minutes at 220 g.
- [Wash]{operation} the [glass plate and scissors and forceps]{equipment} with [D.I.]{solution}.
- [Wash]{operation} another 2 times.
- [Wash]{operation} twice 50µL of [Dynabeads]{equipment} with [PBS containing Tween 0.02%]{solution}.
- [Wash]{operation} the cells by adding [3 mL of cold staining solution]{solution}.
- [Wash]{operation} the [nerve endings]{equipment} quickly [three times]{count} with 1 ml of Locke solution.
- [Wash]{operation} the [cells from step 27]{collect} by adding 2 mL of buffer per one million cells and centrifuge at 300g for 10 min and then aspirate the supernatant completely.
- [Wash]{operation} with [PBS]{solution} briefly.
- [Wash]{operation} the homogenizer probe with detergent solution, [D.I.]{solution}.
- [Wash]{operation} the precipitate was with [70% ethanol]{solution}

### Notices:

### Synonyms:
- WASH
- FLUSH

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The object to be rinsed |
| reagent2 | required \| reagent | The material used to rinse the object,defult = water |
| repeat | optional \| number | Number of times the object should be rinsed, default=1 |
| time | optional \| time |  |
| notice | optional \| string |  |
| reagent1 | required \| reagent | The object after rinsing |
## 18. ELUTE

### Examples:
- [Elute]{operation} [peptides]{component} from [column]{reagent1} with [80% acetonitrile, 0.5% formic acid]{reagent2} by [centrifuging]{method} at [110 g]{intensity} for [2 minutes]{time}.
- [Elute]{operation} [RNA]{component} from the [column]{reagent1} by adding [100 μL of freshly prepared 100 mM dithiothreitol (DTT)]{elutionBuffer}, followed by a second elution with another 100 µL 5 min later.
- [Elute]{operation} [purified RNA]{component} in [20 μL of DEPC-treated water]{reagent2}.
- [Elute]{operation} [DNA]{component} in [21 ul elution buffer]{reagent2}.
- [Elute]{operation} [DNA]{component} from [beads]{reagent1} by adding [50 μl above elution buffer]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be eluted |
| reagent2 | required \| reagent | The eluent |
| component | optional \| reagent | The part to be eluted from the reagent |
| method | optional \| string | Method used for elution, e.g., centrifugation, boiling, shaking |
| time | optional \| time |  |
| temperature | optional \| temperature |  |
| reagent0 | required \| reagent |  |
## 19. VORTEX

### Examples:
- [Vortex]{operation} the [mixture]{reagent1} for [30s]{time} at an [intermediate rate]{intensity}.
- [Vortex]{operation} [briefly]{time}.
- [Vortex]{operation} the [tube]{reagent1} [vigorously]{intensity} for [2 minutes]{time} with the [“vortex rack”]{device}.
- [Vortex]{operation} the [AMPure XP beads]{reagent1} for [30 seconds]{time} to [make sure that the beads are evenly dispersed]{purpose}.
- [Vortex]{operation} the [combined aqueous and oil phases]{reagent1} at [max speed (3,000 rpm)]{intensity} for [30 sec]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The mixture to be vortexed |
| time | optional \| time | default=briefly |
| intensity | optional \| string | default=intermediate intensity |
| frequency | optional \| number | default=1 time |
| device | optional \| string | default=standard vortexer |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 20. THAW

### Examples:
- [Thaw]{operation} [TRI reagent lysed cells]{reagent1} [on ice]{environment}.
- [Thaw]{operation} [frozen stocks]{reagent1}.
- [Thaw]{operation} [aliquots of laminin or collagen IV (1 mg/ml) prepared as described above]{reagent1}.
- [Thaw]{operation} [CSF supernatant]{reagent1} [on ice]{environment}.
- [Thaw]{operation} [urine samples]{reagent1} [to room temperature]{temperature}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be thawed |
| temperature | optional \| temperature |  |
| environment | optional \| STR |  |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 21. PASSAGE

### Examples:
- [Passage]{operation} to [new Gelatin-coated 150-mm culture dish]{reagent2} at [1:4]{ratio} with [0.25w/v% trypsin digestion]{reagent2}.
- [Passage]{operation} [hiPSCs]{reagent1} using [0.1% \(wt/vol) collagenase IV in DMEM-F12 medium]{reagent2} for [5–10 min]{time}.
- [Passage]{operation} the [cells]{reagent1} in [MEF media]{medium} [at least once]{frequency} \(P1) [before using them for experiments]{notice}.
- [Passage]{operation} the stem cells with [GCDR]{reagent2}: aspirate the cell culture medium, add 1 ml of GCDR to the well(s) to be passaged.
- [Passage]{operation} [xeno-free human EPS cells]{reagent1} every [3-4 days]{frequency}.
- [Passage]{operation} [1 well of hESCs]{reagent1} by treating with [1 ml collagenase IV]{reagent2} for [5 to 10 min]{time} followed by a DPBS rinse.
- [Passage]{operation} the [cells]{reagent1} [when they reach confluency]{timer}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The cells to be passaged |
| reagent2 | optional \| reagent | The medium used for passaging |
| reagent3 | optional \| reagent | The other reagent used for passaging |
| ratio | optional \| number |  |
| time | optional \| time |  |
| frequency | optional \| frequency |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 22. PELLET

### Examples:
- [Pellet]{operation} the [cells]{reagent1} at [2000 g]{intensity} for [5 min]{time} at [room temperature]{temperature}.
- [Pellet]{operation} [cells]{reagent1} by [centrifugation]{method} at [200 rcf]{intensity} for [5 min]{time}.
- [Pellet]{operation} [cells]{reagent1}.
- [Pellet]{operation} [cells]{reagent1} by [centrifugation]{method} at [4000xg]{intensity} at [4ºC]{temperature}.
- [Pellet]{operation} [cells]{reagent1} at [1500 rpm]{intensity} for [5 minutes]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be pelleted |
| intensity | optional \| number | The intensity of operation |
| time | optional \| time |  |
| temperature | optional \| temperature |  |
| device | optional \| string | The method used for this operation |
| reagent0 | required \| reagent |  |
## 23. DIGEST

### Examples:
- [Digest]{operation} [2 µg of vector]{reagent1} with [restriction enzymes]{reagent2}.
- [Digest]{operation} for [6hr]{time} [at room temperature]{temperature}.
- [Digest]{operation} the [cell wall]{reagent1} with [approx]{reagent2}.
- [Digest]{operation} the [sample]{reagent1} at [37°C]{temperature} in a [dry bath]{device} [overnight]{time}.
- [Digest]{operation} [proteins]{reagent1} with [recombinant trypsin (30:1 ratio protein/trypsin)]{reagent2} [over night]{time} at [37˚C]{temperature} [with shaking]{notice}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be digested |
| reagent2 | optional \| reagent | The digestive reagent |
| temperature | optional \| temperature | default=room temperature |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 24. EXTRACT

### Examples:
- [Extract]{operation} with [chloroform]{reagent2} [two to four times]{notice}.
- [Extract]{operation} the [plasmid DNA]{component} with [phenol]{reagent2}, [chloroform]{reagent2} and [isoamyl alcohol]{reagent2}.
- [Extract]{operation} [genomic DNA]{component} from [5 ml whole blood]{reagent1}.
- [Extract]{operation} [fecal DNA]{component} using the [QIAamp DNA Stool Mini Kit]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be extracted |
| reagent2 | optional \| reagent | The extractant |
| component | optional \| string | The part to be extracted from the reagent1 |
| device | optional \| string | The kit used for extraction |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 25. PIPETTE

### Examples:
- [Pipette]{operation} [900 µl]{volume} of [suspension]{reagent1} from top carefully with a [1000 µl tip]{tip}.
- [Pipette]{operation} [10 µl]{volume} stock of [single cell suspension]{reagent1} into the [dish]{destination}.
- [Pipette]{operation} [100 microL]{volume} of [standard diluent]{reagent1} into the [NSB (non-specific binding) and B0 (0 pg oxytocin/ml standard) wells]{destination} of a 96-well plate.
- [Pipette]{operation} [50 microL]{volume} of [the blue conjugate]{reagent1} into each well, except [TA (Total activity) and Blank wells]{destination}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| volume | optional \| volume | The volume to be pipetted |
| reagent1 | required \| reagent | The source from which the volume is pipetted |
| destination | optional \| reagent | The destination where the volume is pipetted to |
| repeat | optional \| number | The number of times the pipetting action is repeated |
| tip | optional \| string | The type of pipette tip used |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 26. CONCENTRATE

### Examples:
- [Concentrate]{operation} [eluate]{reagent1} in [speedvac]{device} to [22.5 µL]{targetVol}.
- [Concentrate]{operation} the [commercial silver colloid]{reagent1} [10 times]{repeat} by [centrifugation \(16,770 g, 15 min)]{method}.
- 

### Notices:
- Unlike DILUTE, CONCENTRATE mostly indicates the target volume rather than the target concentration.
- To accurately express the meaning, here use parameter "targetVol" instead of the old parameter "Volume", to avoid being mistaken for the volume of the reagent to be concentrated.
- Some protocols do not provide any parameters, such as "Concentrate if necessary"

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| REG | The reagent to be concentrated |
| targetVol | optional \| VOL |  |
| targetConcentration | optional \| CONC |  |
| method | optional \| STR |  |
| device | optional \| STR |  |
| reagent0 | required \| REG |  |
## 27. STERILIZE

### Examples:
- [Sterilize]{operation} the [medium]{reagent1} in an [autoclave]{device} at [110oC]{temperature} for [15 minutes]{time}.
- [Sterilize]{operation} the [dissection instruments]{reagent1} in an [antiseptic solution]{reagent2}.
- [Sterilize]{operation} the [MEA]{reagent1} with [70% ethanol]{reagent2} for [20 min]{time}.
- [Sterilize]{operation} the [scalp]{reagent1} with [povidone-iodine and 70% ethanol]{reagent2}.
- [Sterilize]{operation} a [metal spatula]{reagent1} by shortly heating it over a [Bunson burner]{device}.
- [Sterilize]{operation} [20-50 seeds]{reagent1} for [30 s]{time} with [20 ml of 75% ethanol]{reagent2} in [a sterile Petri dish with a lid]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The object to be sterilized |
| reagent2 | optional \| reagent | The sterilant |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| device | optional \| string |  |
| reagent0 | required \| string | The sterilized object |
## 28. PRECIPITATE

### Examples:
- [Precipitate]{operation} [RNA]{component} from [each fraction]{reagent1} by the addition of [30 µl of 3 M sodium acetate (pH 5.2) and 825 µl of 100% ethanol]{reagent2}.
- [Precipitate]{operation} the [DNA]{component} in [cold ethanol]{reagent2}.
- [Precipitate]{operation} [unbound proteins]{component} by adding [6 volumes of cold acetone with 10mM NaCl]{reagent2}.
- [Precipitate]{operation} the [DNA]{component} by [inverting the tube several times by hand]{method}.
- [Precipitate]{operation} the [RNA]{component} from the [aqueous phase]{reagent1} by mixing with [isopropyl alcohol]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be precipitated |
| reagent2 | optional \| reagent | The reagent used for precipitation |
| component | optional \| reagent | The portion of the reagent1 that needs to be precipitated |
| temperature | optional \| temperature | default=-20°C |
| time | optional \| time |  |
| method | optional \| string | Method of precipitation, e.g., shaking, spinning, etc. |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 29. QUENCH

### Examples:
- [Quench]{operation} [staining]{reagent1} by adding [150µL staining buffer]{reagent2}.
- [Quench]{operation} the crosslinking by [adding 10 mL of 2.5M Glycine]{method}.
- [Quench]{operation} with [NH4Cl 50mM]{reagent2} [15 min]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be quenched |
| reagent2 | required \| reagent | The quenching reagent |
| time | optional \| time |  |
| reagent0 | required \| reagent |  |
## 30. FLOW

### Examples:
- [Flow]{operation} the [worm suspension]{reagent1} through the [filtering device]{device} to [remove debris]{purpose}.
- [Flow]{operation} [PBS]{reagent1} into the [chamber]{device}.
- [Flow]{operation} the [imaging buffer]{reagent1} onto the [sample]{reagent2}.
- [Flow]{operation} rate: [2 μL/min]{flowRate}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | Flowing reagents |
| reagent2 | required \| reagent | Stationary reagent |
| device | optional \| string | The device used for flow(At least provide one of "device" or "reagent2") |
| flowRate | optional \| rate | The rate at which the reagent is flowed |
| time | optional \| time |  |
| method | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 31. NORMALIZE

### Examples:
- [Normalize]{operation} [samples]{reagent1} for protein concentration (recommended concentration: between [0.3 and 0.6 µg/µl]{concentration}).
- [Normalize]{operation} by the [mRNA quantification values of reference gene (_Gapdh_)]{method}.
- [Normalize]{operation} the [purified PCR product]{reagent1} to [0.2 ng/µl]{targetConcentration} with [MANTIS Liquid Handler]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The sample to be normalized |
| targetConcentration | optional \| concentration | The target concentration after normalization |
| device | optional \| string | The device used for normalization |
| method | optional \| string | The method used for normalization |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 32. DISPENSE

### Examples:
- [Dispense]{operation} [1 ml]{volume} of the [virus preparation]{reagent1} in a [pre-labeled TruCool cryovial]{container}.
- [Dispense]{operation} [100 μL]{volume} [ES cells suspension]{reagent1} to each [ultra-low attachment 96 well]{container}.
- [Dispense]{operation} [1 ml]{volume} of [stock]{reagent1} in a [pre-labeled TrueCool cryovial]{container}.
- [Dispense]{operation} [photoresist mixture solution]{reagent1} on the [center of the wafer]{container}.
- [Dispense]{operation} [SU-8 2025 (3 mL)]{reagent1} on the [wafer]{container} using the [mosquito®HTS]{device}.

### Notices:
- Be careful not to create bubbles when dispensing.
- Dispense medium on the inner wall of the well and not directly on the Matrigel droplet.

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be dispensed |
| volume | required \| volume | The volume of the reagent to be dispensed (Volume per serving) |
| container | required \| string | The container where the reagent will be dispensed |
| device | optional \| string | The device used to dispense the reagent |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 33. EVAPORATE

### Examples:
- [Evaporate]{operation} the [tube]{reagent1} under [N2]{environment} in a [water bath]{environment} with [30-40 C]{temperature}.
- [Evaporate]{operation} the [solvent]{reagent1} to [dryness]{termination} using a [rotary evaporator]{device}.
- [Evaporate]{operation} the [mixture]{reagent1} under a [gentle stream of N2]{environment} at [40 °C]{temperature}.
- [Evaporate]{operation} [>50 nm of Au]{reagent1} taking the crucible at a [temperature suitable for a rate <1 nm/min]{notice}.
- [Evaporate]{operation} the [separated organic solution]{reagent1} with a [rotary evaporator]{device} at [50℃]{temperature} for [4 minutes]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be evaporated |
| temperature | optional \| temperature | default=room temperature |
| time | optional \| time |  |
| termination | optional \| string | Reaction endpoint, such as "dryness" |
| environment | optional \| string | Operating environment, such as N2 or water bath |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 34. ALIQUOT

### Examples:
- [Aliquot]{operation} [23 µl]{volume} of [master mix]{reagent1} into each [PCR tube]{container} [on ice]{environment}.
- [Aliquot]{operation} [1ml]{volume} of [cell suspension in cryoprotective freezing medium]{reagent2} into each of the [cryovials]{container}.
- [Aliquot]{operation} the [samples]{reagent1} in [1.5ml Eppendorf tubes]{container}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be aliquoted |
| volume | required \| volume | The volume of each aliquot |
| container | required \| string | The container to aliquot into |
| reagent0 | required \| reagent |  |
## 35. PLACE

### Examples:
- [Place]{operation} the [cryo vials]{reagent1} directly in the wells of the [pre-equilibrated CoolRack CFT30]{destination} to [snap-freeze the samples]{purpose}.
- [Place]{operation} the [PCR tubes]{reagent1} into the [thermo cycler]{device} and [make sure the tubes are closed tightly]{notice}.
- [Place]{operation} all [PCR tubes]{reagent1} into the [thermo cycler]{device}.
- [Place]{operation} the [liver]{reagent1} into a [sterile organ bag filled with UW solution on ice]{destination}.
- [Place]{operation} [500 μL]{volume} of the [final extract]{reagent1} in a [chromatographic vial]{destination}.
- [Put]{operation} the slides in [0.3% H2O2/Methanol]{reagent} for [15 min]{time}.
- [Put]{operation} another [coverslip]{equipment} on top to seal the [tissue]{reagent}.
- [Put]{operation} [resected tumors]{reagent} to a [petri dish]{equipment} on ice and determine the size with [calipers]{equipment}.
- [Put]{operation} [samples]{reagent} on [magnet]{device} and transfer [supernatant]{reagent} into new tubes.
- [Put]{operation} the tube into the [thermocycler]{equipment} when it has reached the temperature of [98°C]{temperature}.
- ['Position]{operation} the recording electrodes with a stepping-motor microdrive
- ['Position]{operation} the chair so it is out of [the way]{location} but convenient to access when the step test is completed
- ['Position]{operation} the organoid fusion tissue in the center of the [agarose]{object}, at the bottom of the tissue embedding mold
- ['Position]{operation} the photoactivation ROI that was saved from the previous set of experiments
- ['Position]{operation} both ends of the artery over the opposing glass cannula in the bath chamber and secure with 10-0 [nylon suture]{object}

### Notices:

### Synonyms:
- PUT
- POSITION

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be placed |
| destination | required \| string | The location where the reagent1 is to be placed |
| temperature | optional \| temperature |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 36. CUT

### Examples:
- [Cut]{operation} into [5-µm]{size} sections on [a cryostat]{device}.
- [Cut]{operation} the [chest]{reagent1} [through the sternum]{direction}.
- [Cut]{operation} the [tissue]{reagent1} at [30 µm]{size} [in sets of 5]{notice}.
- [Cut]{operation} the [segments]{reagent1} into [smaller pieces]{size} with a [scalpel]{device} under [sterile conditions]{environment}.
- [Cut]{operation} each [hemisphere]{reagent1} [along the caudal to rostral]{direction} direction.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent | required \| reagent | The reagent to be cut |
| device | optional \| string | Device used to cut the object |
| size | optional \| number | Size of the sections to be cut |
| direction | optional \| string | Direction in which the object is cut, including preposition |
| environment | optional \| string | Any specific environment under which the object is cut |
| reagent0 | required \| reagent | The cut object |
## 37. FIX

### Examples:
- [Fix]{operation} the [sections]{reagent1} in [4% paraformaldehyde]{reagent2} for [10 min]{time}.
- [Fix]{operation} the [pellet]{reagent1} with [200 µl of 4% formaldehyde (prepared in Mcllvaine’s buffer)]{reagent2}.
- [Fix]{operation} the [ultrasonic probe]{reagent1} on [one side of the phantom]{reagent2}.
- [Fix]{operation} samples with [glutaraldehyde fixative]{reagent2} at [4°C]{temperature} [overnight]{time}.
- [Fix]{operation} the [mouse]{reagent1} with [its head away from the operator]{direction} by [taping its feet to the operating table]{method}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be fixed |
| reagent2 | required \| reagent | The fixative to be used, or The place to fix the reagent1 |
| temperature | required \| temperature | default=room temperature |
| time | required \| time |  |
| device | optional \| string |  |
| direction | optional \| string | Direction of fixed reagent1 |
| method | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 38. DRY

### Examples:
- [Dry]{operation} the [slides]{reagent1} at [room temperature]{temperature} [in the dark]{notice}.
- [Dry]{operation} the [pellet]{reagent1} under [nitrogen]{environment}.
- [Dry]{operation} the [product]{reagent1} in an [oven]{device} at [60 °C]{temperature} for [24 h]{time}.
- [Dry]{operation} the [sample]{reagent1} in [Speedvac]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The sample to be dried |
| device | optional \| string | Device used for drying |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| environment | optional \| string | Operating environment, such as vacuum or nitrogen |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 39. HEAT

### Examples:
- [Heat]{operation} the [tube containing RNA and adapter]{reagent1} to [70°C]{temperature} for [2 minutes]{time}.
- [Heat]{operation} the [reaction mixture]{reagent1} to [95 °C]{temperature}.
- [Heat]{operation} the [flask]{reagent1} at [100°C]{temperature} [overnight]{time}.
- [Heat]{operation} the [tubes]{reagent1} on a [Thermomixer]{device} at [55°C]{temperature} for [2 minutes]{time}.
- [Heat]{operation} [shock cells]{reagent1} at [42 °C]{temperature} for [30 seconds]{time} in a [PCR machine]{device}.

### Notices:

### Synonyms:
- WARM

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be heated |
| temperature | required \| temperature |  |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 40. PREPARE

### Examples:
- [Prepare]{operation} enough for [200 ul]{volume} per well.
- [Prepare]{operation} [1 ml of [PBS]{reagent1} in [1.5 ml Eppendorf tube]{container}.
- [Prepare]{operation} [5 series]{quantity} of standard [DNA]{reagent1} by [5-fold dilution with water]{method} in [1.5 ml Eppendorf tubes]{container}.
- [Prepare]{operation} a [glass slide]{reagent1} with [the dimension of 75 mm x 50 mm x 1.0mm]{notice}.
- [Prepare]{operation} [AlInGaP epitaxial layer stacks]{reagent1} by [MOCVD growth on a GaAs wafer]{method}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The main reagent to be prepared |
| container | optional \| string |  |
| concentration | optional \| concentration |  |
| temperature | optional \| temperature |  |
| device | optional \| string |  |
| method | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 41. PERFORM

### Examples:
- [Perform]{operation} all [anisotropy measurements]{procedure} in [triplicate]{repeat}.
- [Perform]{operation} [wet chemical etching]{procedure} using [Cr and Au etchant]{reagent1}.
- [Perform]{operation} [a second round]{time} of [purification]{procedure} with [Ni-nitrilotriacetic acid (NTA) agarose (Qiagen)]{reagent1}.
- [Perform]{operation} [all procedures]{procedure} under [sterile conditions]{environment}.
- [Perform]{operation} the [flat test]{procedure} by placing the [Hamilton syringe]{equipment}.
- [Perform]{operation} [three]{repeat}, [5 minute]{time} [washes]{procedure} in [1XPBS]{reagent1}.
- [Perform]{operation} a [cell count]{procedure} on the [collected cells]{reagent1}.
- [Perfuse]{operation} the [mice]{object1} systemically with [10 ml of HBSS containing 20 mM EDTA]{material1} via the [left ventricle]{location1} using [21-gauge butterfly needle]{tool1} connected to [Peristaltic pump P-1]{device}.
- [Perfuse]{operation} the [lungs]{object1} with [10mL cold PBS]{material1} through the [right ventricle]{location1}.
- [Perfuse]{operation} with [PBS]{material1} at a rate of [2 ml per minute]{rate} to remove [phages]{object2} that stayed in circulation but did not bind to blood vessels.
- [Perfuse]{operation} the [rats]{object1} [transcardially]{method} with [0.9% saline]{material1} and then with [4% paraformaldehyde in 0.1 M phosphate buffer (pH 7.3)]{material2}.
- [Perfuse]{operation} the [body]{object1} with [20 ml of saline]{material1}.
- [Process]{operation} each [24 well (or 6 well) dish]{object} separately.
- [Process]{operation} the [data]{object} with [NMRPipe]{tool}.
- [Process]{operation} [samples]{object} further with the [FL-Ovation cDNA Biotin Module (Nugen)]{tool}.
- [Process]{operation} the [lysate]{object} for [DNA isolation]{goal} by [phenol-chloroform extraction]{method1} followed by [ethanol precipitation]{method2}.
- [Process]{operation} [all the datasets]{object} using [HKL2000]{tool} and the [.sca files]{fileType} generated are used for locating heavy atom (Se) positions, phasing and density modification using [ShelxC/D/E]{method} from [CCP4]{source}.

### Notices:

### Synonyms:
- PERFUSE
- PROCESS
- CARRY

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| procedure | required \| string | The procedure to be performed |
| reagent1 | optional \| reagent | Reagents used in the procedure |
| equipment | optional \| string | Equipment used in the procedure |
| environment | optional \| string | Environment under which the procedure is performed |
| repeat | optional \| number | Number of times the procedure is repeated |
| time | optional \| time | Time of the procedure |
| reagent0 | required \| reagent |  |
## 42. SPIN

### Examples:
- [Spin]{operation} down cells at [440 g]{intensity} for [5 minutes]{time} at [4°C]{temperature}.
- [Spin]{operation} at [1200 rpm]{intensity} for [5 min]{time}.
- [Spin]{operation} [shortly]{time}.
- [Spin]{operation} for [5 min]{time} at [3000 rpm]{intensity}.
- [Spin]{operation} [cast poly(methylmethacrylate) (PMMA)]{reagent1} at [3000rpm]{intensity} for [30 seconds]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be spun down |
| intensity | required \| intensity | The intensity at which the spin should be performed, default=appropriate intensity |
| time | required \| time | The duration for which the spin should be performed, default=appropriate time |
| temperature | optional \| temperature | The temperature at which the spin should be performed, default=room temperature |
| device | optional \| string | The device to be used for spinning, default=centrifuge |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 43. TAKE

### Examples:
- [Take]{operation} out the [cell suspension]{reagent1} from [4°C]{temperature}.
- [Take]{operation} [4 tubes of single cell lysate]{reagent1}.
- [Take]{operation} [1 ml]{volume} of [microalgal and [cyanobacterial culture grown for 25 days]{reagent1} at [28°C]{temperature} in [BG-11 and BG-0]{source}.
- [Take]{operation} the [eggs]{reagent1} out of the [incubator]{source}.
- [Take]{operation} [100 µL]{volume} of the [bacterial culture]{reagent1}.
- [Take]{operation} [800 ml]{volume} of [distilled water]{reagent1} in a [beaker]{source}.
- [Bring]{operation} [pellet]{tissue} up to [880 μL]{volume} in [Nuclear Lysis Buffer]{solution}.
- [Bring]{operation} [500 ml]{volume} of [sodium citrate buffer (pH 6.0)]{solution} to a [rolling boil (95-100°C)]{environment} on a [hot plate]{device}.
- [Bring]{operation} [amplicon PCR plate and the NucleoMag beads]{item} to [room temperature]{environment}.
- [Bring]{operation} [the NucleoMag bead cleaned indexed cpn60 amplicon libraries from D]{item} to [room temperature]{environment}.
- [Bring]{operation} [the bacteria glycerol stock]{item} out of the [-80 °C freezer]{location}.

### Notices:

### Synonyms:
- BRING

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be taken out or used |
| reagent2 | optional \| reagent | Additional reagents to be used |
| volume | optional \| volume |  |
| temperature | optional \| temperature |  |
| device | optional \| string |  |
| source | optional \| string | The location from where the reagent is to be taken out |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 44. STORE

### Examples:
- [Store]{operation} at [4°C]{temperature}.
- [Store]{operation} [gold coated samples]{reagent1} in [desiccator]{container} [until analysis]{termination}.
- [Store]{operation} the [tissues]{reagent1} in [cyrotubes]{container} [on dry ice]{environment} and [at -80°C]{temperature}.
- [Store]{operation} [CoolCell container]{reagent1} in a [-­‐80oC freezer]{container} for [at least 4 hours and up to 24 hours]{time} prior to [transfer to an archive storage such as a freezer capable of continually maintaining temperature below -­‐130°C or a gaseous phase liquid nitrogen storage vessel]{purpose}.
- [Store]{operation} [it]{reagent1} at [-20℃]{temperature} [if not proceeding  to the next step immediately]{timer}.
- [Store]{operation} [on ice]{environment} with [no light]{environment} [until the analysis/sorting]{termination}.
- Keep the liquid filtrate.
- Keep this as clean as possible.
- Keep the abdomen open with 2 retractors and place sterile moist cotton pads around the incision.
- Keep tubes on ice.
- Keep flask level so media can cover all cells.

### Notices:

### Synonyms:
- KEEP

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The item to be stored |
| temperature | optional \| temperature | default=room temperature |
| time | optional \| time |  |
| environment | optional \| string |  |
| container | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 45. CHECK

### Examples:
- [Check]{operation} the [density]{attribute} of [single cell suspension]{reagent1} under a [dissecting microscope using 5X objective lens]{equipment}.
- [Check]{operation} the [Ct value]{attribute} of [2ndNTC]{reagent1}.
- [Check]{operation} the [real-time PCR efficiency]{attribute} of the [standard curves]{reagent1}.
- [Check]{operation} the [reproducibility]{attribute} of [triplicates]{reagent1} by [observing the CV]{method}.
- [Check]{operation} the [status]{attribute} of the [cultures]{reagent1} [microscopically]{method} at [intervals during the lysis]{timing} to [determine the extent of the cellular removal]{purpose}.
- [Check]{operation} the [coolant temperature]{attribute} at the [cooling inlet]{environment} using a [thermocouple]{equipment}.
- [Monitor]{operation} the [fluorescence emission at 440 nm]{measurement} upon [excitation at 380 nm]{environment}.
- [Monitor]{operation} [DP values]{measurement} on the [screen]{location}.
- [Monitor]{operation} [animals]{subject} at least [three times a day]{frequency} for a period of [10 days post infection]{timespan}.
- [Monitor]{operation} the [growth of the strain]{object} until [OD600 reaches a value 0.5 to 0.9]{outcome}.
- [Monitor]{operation} the [mouse]{subject} [directly post-surgery]{time} and over the [next three consecutive days]{timespan}.
- [Observe]{operation} under [fluorescence microscope]{device}.
- [Observe]{operation} the [slides]{sample} under [confocal microscope]{device} by setting the [excitation filter at 370 nm and emission filter at 526 nm]{setting}.
- [Observe]{operation} the [resulting embryos]{sample} for [toxicity]{test} by [physical examination]{method}.
- [Observe]{operation} the [cells]{sample} under a [fluorescence microscope]{device} to check for [fluorescence]{endpoint} and determine whether the [transfection]{procedure} was successful.
- [Observe]{operation} the [mice injected with Tomo LVs]{sample} until they show symptoms indicating [brain tumor formation]{observation} such as [walking disturbance and dehydration]{symptoms}.
- [Examine]{operation} whether there is [abnormal amplification plots]{object} or not.
- [Examine]{operation} the [morphological change of the hemocytes]{object} under [light microscopy]{device} for their inability to cause degranulation of the horseshoe crab hemocytes.
- [Examine]{operation} the [cells]{object} by [phase-confract microscopy]{device} to confirm that cell lysis has not occurred.
- [Examine]{operation} [proteins in the preparation]{object} by [SDS-PAGE (18% polyacrylamide)]{method}.
- [Examine]{operation} the [gel]{object} on a [transilluminator]{device} to visualize DNA.

### Notices:

### Synonyms:
- MONITOR
- OBSERVE
- EXAMINE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The item to be checked |
| attribute | required \| string | The attribute to be checked |
| method | optional \| string | The method used to check the item |
| environment | optional \| string | The condition to be checked |
| equipment | optional \| string | The equipment used to check the item |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 46. RUN

### Examples:
- [Run]{operation} [10 ul or 200 ng of ligation products]{reagent1} on [1% agarose gel with 0.5 ug/ml ethidium bromide in 1X TAE buffer]{reagent2}.
- [Run]{operation} at least [2-4 ul (250-500 ng) DNA]{reagent1} on [2% agarose gel with ethidium bromide]{reagent2} to [check peak sizes of fragmented DNA]{purpose}.
- [Run]{operation} the following PCR program{: [5 minutes at 72C, 1 minute at 98C, then cycle 15 seconds at 98C, 30 seconds at 63C, and 1 minute at 72C]{program}.
- [Run]{operation} [moFF (match-between-runs and apex)]{reagent1} using the following command.
- [Run]{operation} [gel]{reagent1} at [120 volts]{voltage} for [3 h]{time} with a [peristaltic pump that recirculates running buffer between the electrodes]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be run |
| reagent2 | optional \| reagent | Additional reagents used during the run, such as supporting medium |
| volume | optional \| volume |  |
| device | optional \| string |  |
| program | optional \| string | when "device"=PCR machine(thermocycler), this parameter should be changed to REQ |
| voltage | optional \| voltage | voltage of electrophoresis |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 47. LOAD

### Examples:
- [Load]{operation} [tryptic peptides]{reagent1} on the [column]{destination}.
- [Load]{operation} [images]{reagent1} on to [FIJI]{destination} using the [drag and drop]{method} method.
- [Load]{operation} an [aliquot of elution product]{reagent1} on [mini SDS-polyacrylamide gel along with bovine serum albumin]{destination}.
- [Load]{operation} [1 μg of RNA]{reagent1} in a [1% TAE agarose gel]{destination}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be loaded |
| destination | required \| string | The location where the reagent is to be loaded |
| volume | optional \| volume |  |
| method | optional \| string | The method used to load the reagent |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 48. CALCULATE

### Examples:
- [Calculate]{operation} the [Coefficient of Variation (CV)]{attribute} for each triplicate by the below formulation: [CV = Cq Std.]{formula}
- [Calculate]{operation} the [relative T/R ratio]{attribute} by [2-ΔΔCt method]{formula} if the standard curves of telomere and Alu show similar high amplification efficiency.
- [Calculate]{operation} the [total incorporation of [alpha-32P]dCTP]{attribute}.
- [Calculate]{operation} the [volume inserted for the indexing PCR (Step 27)]{attribute} as follows:
- [Calculate]{operation} [complex III specific activity]{attribute} using the [Beer-Lambert law equation (Fig.1)]{formula}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| attribute | required \| string | The attribute to be caculated |
| formula | optional \| string | The formula to be used for calculation |
| variables | optional \| string | The variables involved in the calculation |
| values | optional \| number | The values of the variables |
| units | optional \| string | The units of the variables |
| software | optional \| string | The software used for calculation if any |
| notice | optional \| string |  |
| result | required \| number |  |
## 49. SELECT

### Examples:
- [Select]{operation} the [gradient parameter]{parameter} according to the manufacturer’s instructions.
- [Select]{operation} [Mouse, 5 output, and don’t show unpicked]{value}.
- [Select]{operation} [linear profile]{parameter} to conclude the analysis.
- [Select]{operation} [follicles]{parameter} suitable for IVG.
- [Select]{operation} the [file(s)]{parameter} to be converted.
- [Select]{operation} the [output directory]{parameter}.
- [Select]{operation} [spectra libraries]{parameter} for quantitation.
- [Select]{operation} a proper [cut-off value]{parameter} for each PK.
- [Select]{operation} [Top 20 precursor ions]{parameter} for fragmentation.
- [Select]{operation} [amino-acid constraints]{parameter} from analysis of the crystal structure.
- [Select]{operation} the [equation ‘log(inhibitor) vs. response – Variable slope (four parameters)’]{parameter}.
- [Select]{operation} [APC-Cy7 vs. FSC]{parameter} for P2 to draw positive gate.
- [Select]{operation} [threshold, intensity]{parameter} then view tab and select analysis controls, automated measurement results.
- [Select]{operation} [wells]{parameter} for both the classification beads and reporter beads in the Setup XY menu.
- [Select]{operation} the [precursor ions]{parameter} using an isolation width of 3 Da.
- [Select]{operation} the [“measurement”]{parameter} command via the [“analyze”]{value} drop-down menu.
- [Select]{operation} a large calyx (aboout 1-2μm in thickness) on the surface of the slice.
- [Select]{operation} all elements of the pattern and start laser ablation.
- [Select]{operation} both sequences, right click and choose 'trim ends' and choose default values.
- [Select]{operation} trimmed sequences and click deNovo assembly option under 'assembly' menu.
- [Select]{operation} the sequence generated in step 4 and choose 'sequence search' option on the top menu.
- [Select]{operation} all sequences that need to be aligned and choose Ctrl+Shift+A.
- [Select]{operation} the final trimmed alignment and choose Ctrl+Shift+E.
- [Select]{operation} peaks for image generation.
- [Select]{operation} ‘Z-stack tool’ in the Multidimensional Acquisition tool group.
- [Select]{operation} the most appropriate solution provided by SpADS.
- [Select]{operation} healthy, well developed seedlings for root transformation.
- [Select]{operation} regions of interest (ROIs).
- [Select]{operation} nine tissue strips extending from the gray matter to the pial surface.
- [Select]{operation} for diploids by transferring colony material from the YEPD plate to –Leu–Trp omni tray plates.
- [Select]{operation} the colony with correct transposition.
- [Select]{operation} your tomograms in the **Raw Data** window.
- [Select]{operation} a suffix for the ROIs in the **Output Suffix** text box.
- [Select]{operation} the **Build training set** option in the project manager.
- [Select]{operation} the “measurement” command via the “analyze” drop-down menu.
- [Select]{operation} leaf sheaths with smooth surfaces and trim.
- [Select]{operation} transfected cells in the presence of 2 ug/ml puromycin.
- [Select]{operation} the samples and measurements that you want analyzed by choosing the appropriate Gates and Channels in cyt.
- [Select]{operation} desired flow rate.
- [Select]{operation} X–01 Nucleofector program.
- [Select]{operation} TMT10-plex in MS2 for peptide quantification.
- [Select]{operation} transfected parasites with 4 nM WR99210.
- [Select]{operation} parasites with 2 µg/ml Blasticidin S or 0.9 µM DSM1.
- [Select]{operation} datasets to be analysed.
- [Select]{operation} the type of visualization that you want to generate.
- [Select]{operation} the desired imaging setting.
- [Select]{operation} the cell you want to image.
- [Select]{operation} the set of thresholds that maximize this number.
- [Select]{operation} Chip type CM5.
- [Select]{operation} the channel to flow cell 2.
- [Select]{operation} the flow path and chip type.
- [Select]{operation} the best regeneration buffer from previous assay.
- [Select]{operation} the curves to fit.
- [Select]{operation} kinetics or affinity to fit the data.
- [Select]{operation} the model to fit.
- [Select]{operation} those sequences that render ratios equal or lower than 2%.
- [Select]{operation} isolated and properly spread cells.
- [Select]{operation} represent type of metabolite.
- [Select]{operation} the organisms in which you want to perform the metabolic route search.
- [Select]{operation} if you want to display the detailed information of the provided candidates of your input metabolites.
- [Select]{operation} the direction of the metabolic route design operation.
- [Select]{operation} the representation type of the metabolite.
- [Select]{operation} if you want to display the detailed information about the provided candidates of your inputted metabolites.
- [Select]{operation} the previous design result file and upload it to restart the design process.
- [Select]{operation} the laser objective and ensure the pronuclei are in focus.
- [Select]{operation} an ovariole that contains an appropriate staged egg chamber.
- [Select]{operation} the range of data (numbers only) without including the header row.
- [Select]{operation} a study site of field crops.
- [Select]{operation} the donor, acceptor and substrate combination to perform SRET2 or SRET1 experiments.
- [Select]{operation} a tube of F-actin stabilization buffer containing a gel lid.
- [Select]{operation} a CD-HIT threshold value for clustering the output from PSI-BLAST.
- [Select]{operation} all structures of MFSs that bind the metal cofactor of interest.
- [Select]{operation} ‘sampleZ_featureCsv_patchImg’ in the somMode drop-down list.
- [Select]{operation} only one representative indel according to their numbers of supporting reads in each 10bp window.
- [Select]{operation} only tissue pieces larger than 1 cm<sup>3</sup> which can be confidently identified as decidua compacta or decidua spongiosa.
- [Select]{operation} 60x Apochromat TIRF objective with 1.49NA and mount the sample by applying index matching oil between the objective and sample.
- [Select]{operation} cells using the microscope's eyepiece.
- [Select]{operation} cells using the microscope's eyepiece.
- [Select]{operation} the model by going to<em>Image > ML Super Resolution</em>in the application menu bar.
- [Select]{operation} 'Amino Acids' as the [input sequence type]{parameter}, 'gBlocks Gene Fragments' as the [Product Type]{parameter}, 'Homo sapiens (human)' as the [Organism]{parameter}, and enter a tab-delimited list of peptides on the 'Bulk Entry' page.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1/data1 | required \| reagent/data | The reagent/data to be selected |
| requirement | optional \| string | The requirement of the selected reagent or data |
| device | optional \| string | The device(usually tool) for selection |
| purpose | optional \| string | The purpose for selection |
| notice | optional \| string | Things to notice while selection |
| reagent0/data0 | required \| reagent/data |  |
## 50. COUNT

### Examples:
- [Count]{operation} [mouse bone marrow cells]{reagent1}.
- [Count]{operation} [live cells]{reagent1} using [cell counter]{device} and [trypan blue live dead stain]{reagent2}.
- [Count]{operation} the total number of [viable/fertilized eggs]{reagent1}, dividing them into the desired experimental groups with a minimum of 20 eggs per group.
- [Count]{operation} the number of [cells]{reagent1}.
- [Count]{operation} [cells that exclude trypan blue]{reagent1}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | reagent to be counted(usually cell), keep alive |
| method | optional \| string | Method used for counting cells, such as 'hemocytometer', 'cell counter', 'Trypan Blue method', etc. |
| reagent2 | optional \| reagent | Stain used for cell counting, if applicable |
| device | optional \| string | Device used for cell counting, such as 'Countess Machine', 'hemocytometer', etc. |
| data0 | required \| number |  |
## 51. ADJUST

### Examples:
- [Adjust]{operation} the [protein volume]{attribute} to [100 µl]{data1}.
- [Adjust]{operation} [direct halogen illumination]{reagent1} to [appropriate intensity]{data1} [for the operation]{purpose}.
- [Adjust]{operation} [Tn5 amount]{attribute} [linearly]{notice} [for different amounts of post-ChIP DNA]{purpose}, with a [maximum amount of 4 μL]{data1} of Tn5.
- [Adjust]{operation} the [pH]{attribute} using [Tris base]{method} until it stabilizes at [7.0]{data1}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be adjusted |
| attribute | required \| string | The attribute to be adjusted |
| data1 | required \| data | The value to adjust the attribute to |
| method | optional \| string | The method used to adjust, if applicable |
| reagent0 | required \| reagent |  |
## 52. INJECT

### Examples:
- [Inject]{operation} [50 µL Narcoren® of a [16 g/100 mL pentobarbital stock solution]]{reagent1} into a [CAM vessel]{reagent2}.
- [Inject]{operation} [5 µL]{reagent1} to the [LC/MS]{destination}.
- [Inject]{operation} [0.1 μl of virus]{reagent1} [per minute]{repeat} to [avoid tissue damage]{purpose}.
- [Inject]{operation} [worm suspension]{reagent1} into the [device]{destination} using [pressure driven flow]{method}.
- [Inject]{operation} [10 &#xB5;l of the sample]{reagent1} onto the [LC-MS/MS]{destination}.
- [Administer]{operation} [1000 IU of heparin]{dose} [intravenously]{route}.
- [Administer]{operation} the [anesthetic]{substance} via [intraperitoneal injection]{route}.
- [Administer]{operation} [1.5 g/kg urethane]{dose} for [analgesia]{purpose} initially and [0.5 g/kg/h urethane]{dose} throughout surgery and recording.
- [Administer]{operation} [atropine sulphate]{substance} [15 min]{time} before induction of anesthesia to [inhibit tracheal secretion]{purpose}.
- [Administer]{operation} [mouse infusions]{substance} prior to placing them into the center of a Plexiglas box in a brightly lit room.

### Notices:

### Synonyms:
- ADMINISTER

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be injected |
| reagent2/destination | required \| reagent/string | The destination where the reagent1 is injected |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 53. FILTER

### Examples:
- [Filter]{operation} the [pond water]{reagent1}.
- [Filter]{operation} the [10mL of DPBS containing cells]{reagent1} through the same [40 μm cell strainer]{filter}.
- [Filter]{operation} the [culture]{reagent1} under [reduced pressure]{environment} over a [GF/C grade microfiber filter]{filter} using the filtration unit.
- [Filter]{operation} the [supernatant]{reagent1} through a [0.45µm filter]{filter}.
- [Filter]{operation} the [solutions]{reagent1} using a [0.2-μm filter]{filter}.
- [Filter]{operation} [sterile]{purpose} the [medium]{reagent1}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be filtered |
| filter | required \| string | Type of filter to be used |
| container | optional \| string | Container to collect the filtered reagent |
| environment | optional \| string | The environment for operation |
| temperature | optional \| temperature | Temperature conditions if any |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Filtered reagent1 |
## 54. ANALYZE

### Examples:
- [Analyze]{operation} the [corresponding values for each cleavage stage]{data1} in [normal condition]{environment} as well as in [hypergravity conditions]{environment}.
- [Analyze]{operation} the [result]{data1} using [software]{software} with [default settings]{settings}.
- [Analyze]{operation} [each point of the calibration curve]{data1} using [RP-HPLC-DAD]{device}.
- [Analyze]{operation} [biosynthesis pathways for vitamins and amino acids]{data1}.
- [Analyze]{operation} the [PCR products]{reagent1} by [electrophoresis on a 1% (wt/vol) agarose gel]{method}.
- [Analyze]{operation} the [recovery and purity of the DNA]{data1} by [NanoDrop]{device} and [Qubit]{device}.
- [Evaluate]{operation} the SCATR-PCR system with amplifications of [controls]{object}.
- [Evaluate]{operation} concentrations of the [samples]{object} with [calibration standards \\(0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 30, 50 ng/ml)]{reference} using [Analyst software 1.4 \\(Applied Biosystems)]{device}.
- [Evaluate]{operation} the size of the [patches]{object} \\(number of cells belonging to the same patch).
- [Evaluate]{operation} the DNA concentration of the [extracted DNA]{object} by [UV absorption at 260nm]{method} and the purity by [A260/280nm ratio]{method2} using a [UV spectrophotometer \\(Spectronic Unicam, Genesys, USA)]{device}.
- [Evaluate]{operation} the pain by [McGill Pain questionnaire and visual analog scale \\(VAS)]{method}.

### Notices:

### Synonyms:
- EVALUATE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | optional \| data | The reagent to be analyzed |
| data1 | optional \| data | The data to be analyzed, a ANALYZE instruction can either has "reagent1" or "data1", but cannot have neither or both |
| environment | optional \| string | The condition under which the data was collected |
| software | optional \| string | The software used for analysis |
| settings | optional \| string | software setting, default=default settings |
| method | optional \| string | The method used for analysis |
| notice | optional \| string |  |
| data0 | required \| data |  |
## 55. LEAVE

### Examples:
- [Leave]{operation} [mice]{reagent1} to [recover from the anesthesia]{purpose}.
- [Leave]{operation} at [room temperature]{temperature} for [2 h]{time}.
- [Leave]{operation} [the plates]{reagent1} [untouched}{notice} for [15-20 minutes]{time}.
- [Leave]{operation} [the samples]{reagent1} at [room temperature]{temperature} for [30 minutes]{time}.
- [Leave]{operation} [the cells]{reagent1} in the [incubator]{device} [with a cover]{notice} for [30 min]{time}.
- [Leave]{operation} [the fish]{reagent1} in [this tank]{device} for [4 to 24 hours]{time}.
- [Leave]{operation} [the slides]{reagent1} [overnight]{time} at [room temperature]{temperature}, [in the dark]{environment}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be left |
| temperature | optional \| temperature | default=room temperature |
| time | optional \| time |  |
| environment | optional \| string |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 56. POOL

### Examples:
- [Pool]{operation} the [PCR reactions]{reagent1} and [PCR purify]{reagent1} using the [Qiagen® PCR Purification Kit]{reagent2}.
- [Pool]{operation} [liquid]{reagent1} in a [flask]{container}.
- [Pool]{operation} [all eluates]{reagent1} in a [protein low bind 1.5 ml microcentrifuge tube]{container}.
- [Pool]{operation} the [culture medium with the neurospheres]{reagent1} from [a 24 multi-well plate]{source} into a [15 ml conical tube]{container}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be pooled |
| reagent2 | optional \| reagent | Additional reagents to be pooled |
| container | optional \| string | The container where the pooling will take place |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 57. TURN

### Examples:
- [Turn]{operation} the [laser]{device} [off]{state}.
- [Turn]{operation} the [EVOM2 POWER switch]{device} to the [on (“I”) position]{setting}.
- [Turn]{operation} [on]{state} the [boiling water bath, the evaporator’s water bath, and the centrifuge]{device}.
- [Turn]{operation} [off]{state} the [green channel]{device} and [turn on]{state} the [cyan channel]{device}.
- [Turn]{operation} [on]{state} the [Luminex 100 instrument]{device} then [open the Luminex 100 data collection software]{setting}.
- [Turn]{operation} [on]{state} the [heater of the gel dryer]{device} [after flattening the gel]{notice}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| device | required \| string | The device to be turned on or off |
| state | required \| string | The state to which the device should be turned, either 'on' or 'off' |
| setting | optional \| string | Any additional settings or adjustments to be made to the device |
| notice | optional \| string |  |
## 58. SEPARATE

### Examples:
- [Separate]{operation} the [colon]{component} from the [jejunum/ileum]{reagent1}.
- [Separate]{operation} [embryos]{component} from [placenta]{reagent1} with [forceps]{device}.
- [Separate]{operation} the [amplified products]{component} by [2% agarose gel electrophoresis]{method}.
- [Separate]{operation} [cells]{component} from [the bottom of flasks]{reagent1} by [tapping the flasks with hand]{method} and [pour the 4 l of the culture into four centrifuge tubes]{method}.
- [Separate]{operation} [plasma]{component} by [centrifugation at 1300×g for 15 minutes at room temperature]{method}.
- [Isolate]{operation} a single [microglia]{reagent} by removing surrounding processes with the [eraser tool]{device}.
- [Isolate]{operation} the [hypothalamus]{reagent} near the optic chiasma, including the supraoptic and paraventricular nuclei.
- [Isolate]{operation} [PBMCs]{reagent} and generate T cell clones as previously described.
- [Isolate]{operation} [CD34+ cells]{reagent} from CBMCs with the [Miltenyi human CD34 Microbead Kit]{kit}.
- [Isolate]{operation} the gel slice containing [DNA fragments between 220 and 700bp]{reagent}.
- [Dissociate]{operation} the given cells when reaching 90 % confluences.
- [Dissociate]{operation} the tissue
- [Dissociate]{operation} lungs using the [Miltenyi lung dissociation kit and GentleMACS tissue dissociator]{reagent_kit}
- [Dissociate]{operation} for [30 min]{time} at [4 °C]{temperature}
- [Dissociate]{operation} human pluripotent stem cell (hPSC) into single cells by incubating with [Accutase]{reagent} at [37°C]{temperature} for [10 mins]{time}

### Notices:

### Synonyms:
- ISOLATE
- DISSOCIATE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| component | required \| reagent | The component to be separated |
| reagent1 | required \| reagent | The reagent from which "component" is to be separated, keep alive |
| method | optional \| string | The method used to separate the objects |
| device | optional \| string | The device used to separate the objects |
| environment | optional \| string | The condition under which the separation is performed |
| reagent1 | required \| reagent | The separated object |
## 59. GROW

### Examples:
- [Grow]{operation} at [37°C]{temperature} until [OD600 = 0.6-1.2]{termination}.
- [Grow]{operation} [hOBs]{reagent1} at [37°C]{temperature} in [5% CO2]{environment} until [confluent]{termination} with [media changes every 3-4 days]{notice}.
- [Grow]{operation} [D. melanogaster larvae]{reagent1} at [18°C]{temperature} in [fly bottles]{container} on [standard fly food]{medium}.
- [Grow]{operation} the [cells]{reagent1} in [complete RPMI 1640 medium]{medium} until [the control cultures reach confluence]{termination}.
- [Grow]{operation} [HeLa Kyoto cells]{reagent1} in [DMEM]{medium}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The cells or organism to be grown |
| medium | optional \| reagent | The medium in which the cells or organism are grown |
| temperature | required \| temperature | default=room temperature |
| time | optional \| time |  |
| termination | optional \| string | The sign of stopping cultivation |
| environment | optional \| string | Additional growth conditions, such as CO2 concentration or shaking speed |
| device | optional \| string | The device in which the cells or organism are grown |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 60. FILL

### Examples:
- [Fill]{operation} the [syringe]{container} with [1.0 μl of AAV-DIO-ChR2]{reagent1}.
- [Fill]{operation} [each well]{container} with [100 µL detection solution]{reagent1}.
- [Fill]{operation} the [slot]{container} [carefully]{notice} with [running buffer (1× MOPS buffer)]{reagent1} [only up to the top of the gel (but not over the sample slots)]{notice}.
- [Fill]{operation} the [tube]{container} up to [15 ml]{volume} with the [pre-warmed neuronal medium]{reagent1}.
- [Fill]{operation} [all the wells of a standard 96-well plate]{container} with [200 µL of water]{reagent1}.
- [Fill]{operation} the [electrodes]{container} with [internal solution]{reagent1}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be filled |
| volume | optional \| volume |  |
| container | optional \| string | Container for reagent loading |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 61. WEIGH

### Examples:
- [Weigh]{operation} [10 g]{weight} [fresh silage]{reagent1}.
- [Weigh]{operation} and obtain the mean weight of the [embryos from the different experimental groups]{reagent1}.
- [Weigh]{operation} the [total weight]{weight} of the [tissue]{reagent1} with [electric balance]{device}.
- [Weigh]{operation} [two aliquots of 10 mg]{weight} of [collagenase type 2 powder]{reagent1}.
- [Weigh]{operation} [0.5 g (0.3-0.7 g)]{weight} [soil]{reagent1} to a [silica beads tube]{container}.

### Notices:
- Weigh carefully when collecting tissues.

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be weighed, keep alive |
| weight | required \| weight | The weight of the reagent1 |
| container | optional \| string | The container to hold the reagent1 |
| device | optional \| string | The device used to weigh the reagent1, default=electric balance |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 62. SEAL

### Examples:
- [Seal]{operation} the [vial]{reagent1} with a [Teflon lined screw cap]{reagent2}.
- [Seal]{operation} the [PCR plate]{reagent1} with [foil]{reagent2}.
- [Seal]{operation} the [deepwell plate]{reagent1} with a [foil sealer]{reagent2}.
- [Seal]{operation} the [PCR clean-up plate]{reagent1} using a [foil plate sealer]{reagent2}.
- [Seal]{operation} the [plate]{reagent1} with [adhesive aluminum foil]{reagent2}.
- [Close]{operation} all [phrenic veins]{object} using [4-0 PROLENE stitches]{tool}.
- [Close]{operation} the [abdominal wall]{object} with [1-0 SILK]{tool}.
- [Close]{operation} the [stopcock]{object} as soon as the [filter]{related_object} is dry.
- [Close]{operation} the [lid]{object} and [centrifuge]{operation2} at [8,000 x g]{speed} for [1 min]{time} to bind DNA.
- [Close]{operation} the [chamber]{object} and gas the [chamber]{object} for [3min]{time} with a mixture of [1% O2, 3% CO2 and a balance of N2]{mixture}.

### Notices:

### Synonyms:
- CLOSE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The container to be sealed |
| reagent2 | optional \| reagent | The material used to seal the container |
| device | optional \| string | Device used for sealing if any |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| notice | optional \| string |  |
| reagent0 | required \| string |  |
## 63. SEED

### Examples:
- [Seed]{operation} [1 ml]{cellDensity} per [48-well plate well]{container}.
- [Seed]{operation} [2x10e5 cells/well]{cellDensity} (12well plate) on [vitronectin-coated plate]{container}.
- [Seed]{operation} the [healthy cells]{reagent1} on the coverslips in [each well]{wellCount} of [a 24-well plate]{container} at about [60% density]{cellDensity}.
- [Seed]{operation} [FACS-sorted SSEA-4+, CD104+, TRA-1-60- cells (hiCECs)]{reagent1} on [the 6-well UpCell® plate]{container} at [1.5-6.0 x 105 cells/well]{cellDensity}.
- [Seed]{operation} [1,000-5,000 ESCs]{cellDensity} in [200ml of FBS ES medium]{medium} onto [each well]{wellCount} of [a U-bottomed 96-well plate]]{container} by using [8-channel pipettor]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The type of cells to be seeded |
| cellDensity | required \| number | The density of cells to be seeded per unit area or volume |
| container | optional \| string | The type of well or plate to be used for seeding |
| wellCount | required \| number | Number of wells used for seeding |
| reagent2 | optional \| reagent | The medium in which cells are to be seeded |
| coating | optional \| reagent | The coating on the well or plate, if any |
| environment | optional \| string | The conditions under which the seeded cells are to be incubated |
| cellCulture | required \| reagent |  |
## 64. ASSEMBLE

### Examples:
- [Assemble]{operation} the [EndOhm cup]{reagent1} with a [representative cell culture insert]{reagent2} to [confirm that the height of the electrode is 1-2 mm above the surface of the insert membrane]{purpose}.
- [Assemble]{operation} a [MinElute spin column]{reagent1} in a [new collection tube]{reagent2}.
- [Assemble]{operation} [PCR reactions]{reagent1} to [generate amplicons]{purpose} according to those detailed in [Table 2]{instructions} \(for whole-genome sequencing).
- [Assemble]{operation} the [two plates]{reagent1} with [PMF sealing pad]{reagent2} and the [membrane]{reagent2} [sandwiched in between]{notice} by [fastening the four clamps on each side of the plates in place]{mothod}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The main component to be assembled |
| reagent2 | optional \| reagent | Additional components to be assembled with the main component |
| instructions | optional \| string | Specific instructions or manufacturer's instructions for assembly |
| device | optional \| string | Device or equipment used for assembly |
| reagent0 | required \| reagent | The object after assembling |
## 65. PROCEED

### Examples:
- [Proceed]{operation} to [“_qPCR amplification to determine additional cycles_”]{procedure} [immediately]{timer}.
- [Proceed]{operation} with [FISH or immunostaining]{procedure} if planned, as suggested<sup>1</sup>.
- [Proceed]{operation} to [snap freeze aliquots in liquid N<sub>2</sub>]{procedure} (keep a non-frozen control aliquot on ice to assess viability).
- [Proceed]{operation} [immediately]{timer} to [step 13]{procedure}.
- [Proceed]{operation} with [PCR setup]{procedure}.
- [Proceed]{operation} with [Trypsin digestion]{procedure} as previously described<sup>10,19</sup>.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| procedure | required \| string | The procedure to proceed to |
| environment | optional \| string | Conditions under which to proceed |
| notice | optional \| string |  |
| nextStep | required \| string |  |
## 66. WAIT

### Examples:
- [Wait]{operation} till [mouse finishes the jelly]{termination}.
- [Wait]{operation} until [the tissue residue dried]{termination}.
- [Wait]{operation} [3-4 days]{time} to [reach full adhesion and spreading of islets cells]{purpose} [before proceeding with experiments]{timining}.
- [Wait]{operation} [5 min]{time} until [enough cancer cells are trapped at the cell docking area]{termination}.
- [Wait]{operation} for [5 min]{time} so that [the mice do not respond to pinching with tweezers]{purpose}.
- [Wait]{operation} [30 seconds]{time}.
- [Wait]{operation} for [about 1-2 min]{time} to [allow the cells to settle down in the crypt-shaped cavities]{purpose}.
- [Wait]{operation} [until there are two clear layers]{termination}.
- [Wait]{operation} [5 min]{time} for [the tube to cool down to room temperature]{purpose}.
- [Wait]{operation} [until the mouse loses the pinch reflex to begin surgery]{termination}.
- [Wait]{operation} [until parasites re-emerge (usually 1-3 weeks)]{termination}.
- [Wait]{operation} [2h]{time}, [85°C]{temperature}.
- [Wait]{operation} [5 minutes]{time} in [room temperature]{temperature} [before mixing the contents of both vials together]{timing}.
- [Wait]{operation} [until there are distinct two layers (or centrifuge for 5 minutes)]{termination}.
- [Wait]{operation} [at least 3 minutes]{time}.
- [Wait]{operation} [for 1~2 mins]{time} until ]the adhesive fill the gap between the glass and the fiber]{termination}.
- [Wait]{operation} [until all the solution is eluted]{termination}.
- [Wait]{operation} [until the red light turns off at the front end which usually takes 60 to 90 seconds]{termination}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| time | optional \| time | The time to wait, if specified |
| termination | optional \| string | The timing to stop waiting, a WAIT instruction must has one of "time" or "termination" |
| timing | optional \| string | The timing to start waiting |
| environment | optional \| string | The condition to be met before proceeding |
| purpose | optional \| string |  |
| temperature | optional \| temperature |  |
| notice | optional \| string |  |
## 67. COOL

### Examples:
- [Cool]{operation} down under [constant stirring]{method} to [50°C]{temperature}.
- [Cool]{operation} the [sonicator tip]{reagent1} after each round with an [ice bath]{environment}.
- [Cool]{operation} down the [tube]{reagent1} [in ice]{environment} for [5 minutes]{time}.
- [Cool]{operation} your [fingertips]{reagent1} in the [12°C water]{environment}.
- [Cool]{operation} the [bonded microfluidic device]{reagent1} to [room temperature]{temperature}.
- [Cool]{operation} the [mixture]{reagent1} to [-10˚C]{temperature} by a [cryohydrate bathe]{environment}.
- [Cool]{operation} down the [sample]{reagent1} [in the dark]{environment} at [room temperature]{temperature} for [10 min]{time}.
- [Cool]{operation} the [flask]{reagent1} to [&#x2013;78 &#xBA;C]{temperature} in a [dry ice/acetone bath]{environment}.
- [Cool]{operation} [250 mL PBS]{reagent1} to [4&#xBA;C]{temperature} in a [500 mL Duran bottle]{container}.
- [Cool]{operation} the [slides]{reagent1} for [20 min]{time} at [room temperature]{temperature}.
- [Freeze]{operation} the [compound]{reagent1} in [cooled 2-methyl butane]{container} in a [liquid nitrogen bath]{device}.
- [Freeze]{operation} the [cells]{reagent1} at [a cooling rate of -1oC/min]{environment} using [CoolCell® alcohol-free cell freezing container]{device} in a [-80oC freezer]{storage} or [dry ice locker]{storageAlternative}.
- [Freeze]{operation} the [chromatin sample]{reagent1} rapidly and [store]{operation} at [-80 °C]{storage}.
- [Freeze]{operation} [cell stocks]{reagent1}: Prepare [cell freezing medium]{solution} as follows: [chilled FBS 90%, DMSO 10%, keep on ice]{solutionComposition}; [collect]{operation} all [cell clusters]{reagent2}; [centrifuge]{operation2} and [resuspend]{operation3} cells with [freezing medium]{solution}; [transfer]{operation4} cryogenic vials immediately to [Mr. Frosty™ Freezing Container]{container} and [keep]{operation5} in [-80 °C freezer]{storage} for [24 hours]{time}; [transfer]{operation5} cell vials to [liquid nitrogen tank]{storage2}.

### Notices:

### Synonyms:
- FREEZE

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be cooled |
| temperature | required \| temperature | default=room temperature |
| time | optional \| time |  |
| environment | optional \| string | The physical environment under which reagent1 is cooled, such as "ice bath" or "in the dark" |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 68. TREAT

### Examples:
- [Treat]{operation} for [30 minutes]{time} at [37°C]{temperature}.
- [Treat]{operation} [cloned CD8+CD95+ T cells]{reagent1} with [14 &#x3BC;g/ml of caspase 3 inhibitor]{reagent2}.
- [Treat]{operation} the [cells]{reagent1} with [either control medium or the cytokines mentioned above]{reagent2} for [4 - 5 d]{time}.
- [Treat]{operation} the [PDMS replica and glass slide]{reagent1} by [plasma]{reagent2} for [1-2 minutes]{time}.
- [Treat]{operation} the [exposed coronal and radicular dentin surfaces]{reagent1} with [2% chlorohexidine]{reagent2}.
- [Treat]{operation} [iPS cells]{reagent1} with [0.5 ml Accutase]{reagent2} [briefly]{notice} and bring it up with [1 ml hES media]{reagent2}.
- [Treat]{operation} [ES cells grown on mEF]{reagent1} with [4 µg/ml cyt-B]{reagent2} for [14 hours]{time}.
- [Treat]{operation} [cells]{reagent1} with [cold methanol]{reagent2} at [-20 °C]{temperature} for [10 min]{time}.
- [Treat]{operation} the [sample]{reagent1} with [a solution of 0,5% KOH]{reagent2} for [one day]{time}.
- [Treat]{operation} the [sample]{reagent1} with [100% Glycerol]{reagent2} for [one day]{time}.
- [Treat]{operation} [i-motif DNA-immobilized chip]{reagent1} with [40 μL of hybridization solution]{reagent2} and agitate gently the slide for [3 h]{time}.
- [Treat]{operation} [both cell lines]{reagent1} with [4 nM calcein-AM in DPBS]{reagent2} for [15 min]{time}.
- [Treat]{operation} the [cells]{reagent1} with [Trypsin]{reagent2} for [5 min]{time} to [detach the cell from the culture flask]{purpose}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be treated |
| reagent2 | required \| reagent | Additional reagents used for treatment |
| temperature | required \| temperature | default=room temperature |
| time | optional \| time |  |
| environment | optional \| string |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 69. BLOCK

### Examples:
- [Block]{operation} [Fc receptors]{reagent1} by adding [ChromePure Rabbit IgG]{reagent2} [(final concentration 200 µg/mL)]{targetConcentration}.
- [Block]{operation} for [2 hours]{time} at [room temperature]{temperature} in [5% normal chicken serum]{reagent2}.
- [Block]{operation} with [2% BSA and 0.1% Tween in 0.02M TBS]{reagent2}; [1h at room temperature]{time}.
- [Block]{operation} the [membrane]{reagent1} with [10% fat-free skim milk in TBST buffer]{reagent2} for [1hr]{time} at [room temperature]{temperature}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be blocked |
| reagent2 | required \| reagent | The reagent(usually solution) used for blocking |
| temperature | optional \| temperature | default=room temperature |
| time | required \| time | default=1 hour |
| reagent0 | required \| reagent |  |
## 70. QUANTIFY

### Examples:
- [Quantify]{operation} the [DNA]{reagent1} using [Qubit]{device}.
- [Quantify]{operation} the [protein contents]{reagent1}.
- [Quantify]{operation} the [DNA concentration]{reagent1} of the extracted DNA by [UV absorption at 260nm]{method}.
- [Quantify]{operation} the [libraries]{reagent1} by [qPCR against Illumina primers and/or Bioanalyzer]{method}.
- [Quantify]{operation} the [RNA expression]{reagent1} by [ΔΔCt]{method}, with normalization based on expression of [glyceraldehyde 3-phosphate dehydrogenase]{standard}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be quantified |
| method | optional \| string | The method used for quantification |
| standard | optional \| reagent | The standard used for quantification |
| device | optional \| string | The device used for quantification |
| notice | optional \| string |  |
| data0 | required \| data |  |
## 71. STAIN

### Examples:
- [Stain]{operation} [cells]{reagent1} at [4°C]{temperature} for [30 minutes]{time}.
- [Stain]{operation} [aliquots of the cell fractions]{reagent1} with a [fluorochrome-conjugated antibody]{reagent2}.
- [Stain]{operation} the [membranes]{reagent1} with [Ponceau S solution]{reagent2}.
- [Stain]{operation} the [eluted CD34+ positive fraction]{reagent1} with [anti-CD34 and anti-CD3 antibodies and DAPI]{reagent2}.
- [Stain]{operation} the [transverse thalamic sections of 50 micro m thickness]{reagent1} using the [Nissl method]{method}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be stained |
| reagent2 | optional \| reagent | Additional reagents used for staining(usually staining agent) |
| temperature | required \| temperature | default=room temperature |
| time | optional \| time |  |
| method | optional \| string | Specific staining method if applicable |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 72. RECORD

### Examples:
- [Record]{operation} the [appropriate information about the cells]{information} in your cell repository.
- [Record]{operation} [3D TROSY-HNCA, 3D MQ-CCH-TOCSY and 4D 13C, 15N-edited NOESY]{information} for [resonance assignment]{purpose}.
- [Record]{operation} the [baseline]{information} for [2 min]{time}.
- [Record]{operation} [pre-infection body weights]{information}.
- [Record]{operation} [cell migration images]{information} at [6 frames/min]{frequency} for [15 min]{time}.
- [Record]{operation} the [distance moved and time spent in the entire open field or in a 25cm X 25cm center area]{information} using the [EthoVision pro video tracking system and software (Noldus Inc,]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| information | required \| string | The information to be recorded |
| time | optional \| time |  |
| device | optional \| string |  |
| software | optional \| string |  |
| notice | optional \| string |  |
| data0 | required \| data |  |
## 73. ENSURE

### Examples:
- [Ensure]{operation} that the [laser]{device} is [on]{state} during these [2.5 minutes]{time}.
- [Ensure]{operation} that the [EVOM2 unit]{device} is [fully charged]{state}.
- [Ensure]{operation} [enough wells]{state} for [all test samples]{reagent1}.
- [Ensure]{operation} that [no air bubbles]{state} are present [after centrifugation]{timing}.
- [Ensure]{operation} that the [cells seeded into the Aggrewell]{reagent1} are [evenly distributed]{state}.
- [Ensure]{operation} [data]{data1} is [being collected and recorded]{state}.
- [Ensure]{operation} to [minimize bubbling]{state}.
- [Ensure]{operation} the [valves]{device} are [closed]{state} [before dispensing the premix solution into the gradient maker]{timing}.
- [Maintain]{operation} sterile conditions for steps 10 and 11.
- [Maintain]{operation} virulent stocks by performing _in vivo_ passage every [6-12 months]{time}.
- [Maintain]{operation} a healthy cell culture on [T-25 flask]{device}.
- [Maintain]{operation} and [expand]{operation} MS5-hDLL1 cells in standard [T75 or T150 tissue culture-treated flasks]{device} in DMEM/10% FBS, passaging them [twice a week]{time} by trypsinization for [5 min]{time}.
- [Maintain]{operation} the [temperature]{environment} at [10 °C]{temperature} using a [recycling thermostatic water bath]{device}.
- [Confirm]{operation} the presence or absence of aberrant left hepatic artery in small omentum or right hepatic artery which is located dorsal to portal vein.
- [Confirm]{operation} the phenotype of BMDM by flow cytometry.
- [Confirm]{operation} the final pH of the resulting solution.
- [Confirm]{operation} that it is capable of building a typical nest and the pups are in the nest and being nurtured by the dam.
- [Confirm]{operation} the quality of the conjugation using native gel, Mini-PROTEAN TGX gels (Bio-rad, 456-1093) in 1x Tris/Glycine Buffer at 100 V.

### Notices:

### Synonyms:
- MAINTAIN
- CONFIRM

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1/data1/device | required \| reagent/data/string | The reagent/data/device to be checked or ensured |
| state | required \| string | The state needs to be ensured |
| timing | optional \| string | The timing of ENSURE operation |
| notice | optional \| string |  |
## 74. COVER

### Examples:
- [Cover]{operation} the [slides]{reagent1} to [block out ambient light]{purpose}.
- [Cover]{operation} [stained cells]{reagent1}.
- [Cover]{operation} the [plate]{reagent1} with [foil]{reagent2} to [protect it from light]{purpose}.
- [Cover]{operation} the [sample]{reagent1} with [90 &#x3BC;l of mineral oil]{reagent2}.
- [Cover]{operation} the [gel]{reagent1} with [another plastic wrap]{reagent2}.
- [Cover]{operation} the [top]{reagent1} with [a square of aluminum foil]{reagent2} so that [the lid and mesh are entirely covered]{purpose}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The object to be covered |
| reagent2 | required \| string | The material used to cover the object |
| purpsoe | optional \| string | The purpose of covering |
| notice | optional \| string |  |
| reagent0 | required \| string |  |
## 75. EQUILIBRATE

### Examples:
- [Equilibrate]{operation} [NEST MicroSpin C18 reverse phase column]{reagent1} with [100 µl of methanol]{reagent2} by [centrifuging at 110 g for 1 minute]{method}.
- [Equilibrate]{operation} the [column]{reagent1} twice with [50 ml PSG]{reagent2}, by [passing the buffer by gravity]{method}.
- [Equilibrate]{operation} [HiTrap Phenyl HP 5 ml]{reagent1} with [binding buffer]{reagent2}.
- [Equilibrate]{operation} the [column]{reagent1} with [PBS]{reagent2}.
- [Equilibrate]{operation} the [column]{reagent1} with [borate buffer pH 8.0 + 1 mM EDTA]{reagent2}, [flow rate 2.5 ml/min]{flowRate}.
- [Equilibrate]{operation} the [column]{reagent1} at [4 &#xB0;C]{temperature}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The column or device to be equilibrated |
| reagent2 | required \| reagent | The buffer or solution used for equilibration |
| volume | optional \| volume |  |
| time | optional \| time |  |
| temperature | optional \| temperature |  |
| device | optional \| string |  |
| flowRate | optional \| rate |  |
| notice | optional \| string |  |
| column | required \| reagent |  |
## 76. INOCULATE

### Examples:
- [Inoculate]{operation} [10 ml of YPAD medium]{reagent2} with a [single fresh AH109 colony]{reagent1}.
- [Inoculate]{operation} [5 ml of LB medium]{reagent2} with a [single colony of _E]{reagent1}.
- [Inoculate]{operation} [50 ml of LB medium in 250 ml E-flask]{reagent2} with [500 µl of culture]{reagent1}.
- [Inoculate]{operation} a [single colony]{reagent1} into a [50-ml sterile tube]{container} containing [10 ml of LB supplemented with 100 μg/ml ampicillin and 2% (wt/vol) glucose]{reagent2}.
- [Inoculate]{operation} [COS-1 cells]{reagent1} in a [75 cm2 cell culture flask]{container}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be inoculated |
| reagent2 | optional \| reagent | The reagent where reagent1 needs to be inoculated(usually medium) |
| container | optional \| string | The container where reagent1 needs to be inoculated,a INOCULATE instruction must has one of "reagent2" or "container" |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 77. SAVE

### Examples:
- [Save]{operation} [10µl]{volume} [for SDS-PAGE]{purpose}.
- [Save]{operation} [some supernatant and pellet]{reagent1} [for gel]{purpose}.
- [Save]{operation} [10µl]{volume} [for running on gel]{purpose}.
- [Save]{operation} [the selected ROI]{reagent1} [for use in all future experiments]{purpose}.
- [Save]{operation} [at -20°C freezer]{device}.
- [Save]{operation} [this tree]{reagent1} [in a vector format and export as .nexus for uploading to TreeBASE]{format}.
- [Save]{operation} [the samples]{reagent1} [at -20°C]{temperature} [for future use]{purpose}.
- [Save]{operation} [the probability map image]{data1} [using the ImageJ menu “File-Save”]{format}.
- [Save]{operation} [24 μl of cell lysate from each sample]{reagent1} [as input]{notice}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| volume | optional \| volume | The volume of the sample to be saved |
| reagent1/data1 | required \| reagent/data | The reagent/data to be saved |
| purpose | optional \| string | The purpose for saving the sample |
| device | optional \| string | The storage condition for the saved sample |
| format | optional \| string | The format in which the sample/data is to be saved |
| reagent0 | required \| reagent | Saved reagent |
## 78. GENERATE

### Examples:
- [Generate]{operation} a [phylogenetic tree]{target}.
- [Generate]{operation} [mutations in the siRNA target region of each cDNA]{target} using [QuickChange Site-Directed Mutagenesis Kit]{method}.
- [Generate]{operation} [cell lines stably expressing membrane receptors of interest and cells expressing monomeric or dimeric forms of the fluorescent marker protein]{target}.
- [Generate]{operation} [a continuous 1 kHz signal]{target} with the [function generator]{method}.
- [Generate]{operation} [all amino acid substitutions]{target} by [site-directed mutagenesis of the wild type AtAMT1;1 sequence]{method}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| target | required \| string | The target to be generated |
| method | optional \| string | The method or kit used to generate the target |
| parameters | optional \| string | Additional parameters or conditions for the operation |
| data0 | required \| data | The result of the operation |
## 79. AMPLIFY

### Examples:
- [Amplify]{operation} [inserts]{reagent1} using [Taq DNA polymerase]{reagent2}.
- [Amplify]{operation} for [4]{cycle} cycles using the following [program]{program}.
- [Amplify]{operation} electrical signals with a [MultiClamp 700B amplifier]{device}.
- [Amplify]{operation} the [T7 phages]{reagent1} bound to tumors.
- [Amplify]{operation} the [TOC1(At5g61380.1) promoter fragment]{reagent1} from _A.
- [Amplify]{operation} the [signal recorded by the microelectrode, together with the acoustic stimulus signal]{reagent1}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1/data1 | required \| reagent/data | The reagent/data to be amplified |
| reagent2 | optional \| reagent | Additional reagents used in the amplification process |
| device | optional \| string |  |
| cycle | optional \| number |  |
| program | optional \| string | PCR program to be used for amplification |
| notice | optional \| string |  |
| reagent0/data0 | required \| reagent/data |  |
## 80. SONICATE

### Examples:
- [Sonicate]{operation} [on ice]{environment} [in short bursts]{notice} to [disrupt the cells]{purpose} [until a partial clearing of the suspension is observed]{termination}.
- [Sonicate]{operation} [chromatin solution]{reagent1} [4 times]{repeat} for [10 seconds]{time} (continuous) with [power output setting at 10]{notice} using [Fisher sonic 60 dismembrator]{device}.
- [Sonicate]{operation} until [cells]{reagent1} have lysed ([3x20sec]{time}, [on ice 20sec in between]{notice}).
- [Sonicate]{operation} [suspension]{reagent1} in [Covaris Adaptive focused ultrasonicator]{device} with the following program: [Time 5min]{program}.
- [Sonicate]{operation} the [tube]{reagent1} for [90 min]{time} at [60 °C]{temperature} and [60 W]{power} power.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be sonicated |
| time | required \| time | default=2 min |
| temperature | optional \| temperature | default=room temperature |
| power | optional \| watt |  |
| device | optional \| string |  |
| program | optional \| string | when device=Covaris Adaptive focused ultrasonicator, this parameter should be changed to REQ |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 81. ANESTHETIZE

### Examples:
- [Anesthetize]{operation} [mice]{reagent1} with [ketamine \(100mg/kg)/xylaxine \(10mg/kg) mixture]{reagent2}.
- [Anesthetize]{operation} the [mouse]{reagent1} with [Nembutal \(i.p., ～0.05ml per mouse)]{reagent2}.
- [Anesthetize]{operation} the [rat]{reagent1} with [ketamine and xylazine \(80 and 10 mg/kg, intraperitonially)]{reagent2} for [a deep anesthesia in approximately 10 mins]{purpose}.
- [Anesthetize]{operation} [male C57BL/6 \(8 - 12 week old) mice]{reagent1} with [intraperitoneal injection of pentobarbital \(30 - 40 mg/kg)]{reagent2}.
- [Anesthetize]{operation} the [mouse]{reagent1} with [5% isoflurane]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The animal to be anesthetized |
| reagent2 | required \| reagent | The anesthetic to be used |
| dosage | optional \| string | The dosage of the anesthetic |
| method | optional \| string | The method of administration of the anesthetic |
| reagent0 | required \| reagent | The anesthetized animal |
## 82. ATTACH

### Examples:
- [Attach]{operation} [water soluble tape]{reagent1} on the [surface of fabricated system]{reagent2}.
- [Attach]{operation} the [tape]{reagent1} on the [Silbione/textile substrate]{reagent2}.
- [Attach]{operation} both [Hamilton syringes with 26 gauge needles]{reagent1} to the [stereotaxic apparatus]{reagent2}.
- [Attach]{operation} the [other end of the optical fibers, with a ferrule attached]{reagent1}, to the [two implanted optical fibers in the test mouse]{reagent2} using [ferrule sleeves]{device}.
- [Attach]{operation} [clear cap strips]{reagent1}.
- [Attach]{operation} a [floater]{reagent1} to the [top side of the tubing (the side with the light clamp)]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be attached |
| reagent2 | required \| reagent | The object to which the first object is attached |
| method | optional \| string | The method used to attach |
| device | optional \| string | The tool used to attach |
| position | optional \| string | The position where the object is attached |
| time | optional \| time |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Products after connecting reagent1 and reagent2 |
## 83. CLEAN

### Examples:
- [Clean]{operation} [the incubator]{object}.
- [Clean]{operation} [dissection equipment and scissors]{object} [between each mouse]{notice}.
- [Clean]{operation} [a 3-inch silicon wafer]{object}.
- [Clean]{operation} [all surfaces and centrifuges]{object} with [an RNase eliminating solution]{cleaningAgent}.
- [Clean]{operation} [the PCR products]{object} using [PureLink&#x2122; PCR Purification Kit (Invitrogen)]{cleaningKit}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1/object1 | required \| reagent/string | The reagent or object to be cleaned |
| reagent2 | required \| reagent | Detergent |
| device | optional \| reagent | Specific cleaning kit if used |
| method | optional \| string |  |
| notice | optional \| string |  |
| reagent0/object0 | required \| reagent/string | Cleaned reagent or object |
## 84. STIR

### Examples:
- [Stir]{operation} the [solution]{mixture} for [5 minutes]{time}.
- [Stir]{operation} the [mixture]{mixture} [continuously]{intensity} to dissolve amino acids.
- [Stir]{operation} at [190 rpm]{speed} for [15 hours]{time} at [35°C]{temperature}.
- [Stir]{operation} the [mixture]{mixture} using a [magnetic stir bar]{device}.
- [Stir]{operation} [drastically]{intensity}.
- [Stir]{operation} the [mixture]{mixture} under [UV light (365 nm)]{notice} using [UVP Blak-Ray® XX-15 L UV bench lamp]{device} for [2 h]{time}.
- [Swirl]{operation} flask around to [mix]{purpose}.
- [Swirl]{operation} this [solution]{material} around the [plate]{object} to complete [cell lysis]{purpose}.
- [Swirl]{operation} the [dish]{object} to ensure distribution over the [entire plate surface]{area}.
- [Swirl]{operation} the [plates]{object} briefly and [incubate]{next_operation} at [room temperature]{environment} for [15 minutes]{time}.
- [Swirl]{operation} [mastermix bottle]{object} gently to [mix]{purpose}.

### Notices:

### Synonyms:
- SWIRL

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be stirred |
| time | optional \| time |  |
| temperature | optional \| temperature |  |
| device | optional \| string | default=magnetic stir bar |
| intensity | optional \| string | The intensity at which to centrifuge the sample, usually represented as rpm/xg/rcf |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 85. DISSECT

### Examples:
- [Dissect]{operation} the [infrarenal aorta]{tissue} and surround the distal and proximal IRA with a [1-0 SILK]{tool}.
- [Dissect]{operation} the [hepatoduodenal ligament]{tissue} and identify each vascular channel such as the common bile duct, the hepatic artery, the gastroduodenal artery, and the portal vein (PV).
- [Dissect]{operation} [SHIVC]{tissue} and ligate the diaphragmatic vein that flowed into the SHIVC.
- [Dissect]{operation} out [mouse embryos]{tissue} in [DMEM + 25 mM HEPES]{reagent}
- [Dissect]{operation} and harvest only [spheroids]{tissue} carefully by [autoclaved-forceps]{tool}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The tissue to be dissected |
| reagent2 | optional \| reagent | Any reagents used during dissection |
| device | optional \| string | Any tools used during dissection |
| location | optional \| string | The location where the dissection is performed |
| notice | optional \| string |  |
| tissue0 | required \| reagent |  |
## 86. PASS

### Examples:
- [Pass]{operation} the [collected mesenteric lymph nodes]{reagent1} through a [100 nm nylon mesh]{device} into a [15 ml tube filled with CMF/20 % FCS]{reagent2} by disrupting them mechanically on the mesh with a straight forceps.
- [Pass]{operation} the [supernatant]{reagent1} through a [100 nm Nylon mesh]{device} into a [50 ml tube]{reagent2}.
- [Pass]{operation} the [resuspended cells]{reagent1} through a [30 µm filter]{device}.
- [Pass]{operation} the [cell suspensions]{reagent1} through [70 μm filter]{device} into a new [50 ml falcon tube]{reagent2}.
- [Pass]{operation} the [cell suspension]{reagent1} [10 times]{times} through an [uncut p1000 tip]{device}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be passed through |
| device | required \| string | The device or material to pass the reagent through |
| reagent2 | optional \| reagent | Additional reagents used during the process |
| volume | optional \| volume |  |
| repeat | optional \| number | Number of times the process is repeated |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Reagent1 after passing |
## 87. DRAW

### Examples:
- [Draw]{operation} up in a [3ml]{volume} syringe and pass through a [0.22-micron]{filter} syringe filter to sterilize.
- [Draw]{operation} up [5 μL]{volume} of the [cell slurry]{reagent1} for a single ATO using a [10 or 20 μL pipette tip]{device}.
- [Draw]{operation} and discard [50μL]{volume} of [culture supernatant]{reagent1} from each of the 18 wells labeled A1 to F3.
- [Draw]{operation} [25μL]{volume} from each of the 18 wells of the plate containing the [stained cells]{reagent1} of the invasion assay, and add this to the corresponding wells on the new plate containing only PBS.
- [Draw]{operation} the required dose of [18F]FHBG (100 μCi), and top the dose with sterile saline for a constant injection volume of [0.5 mL]{volume}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be drawn |
| volume | required \| volume | The volume of the reagent to be drawn |
| device | optional \| string | The device used to draw the reagent, such as a syringe or pipette |
| destination | optional \| string | The destination of the drawn reagent, if applicable |
| reagent0 | required \| reagent |  |
## 88. SORT

### Examples:
- [Sort]{operation} [cells]{cells} into a [5ml tube containing cold PBS/10% FBS]{tube}.
- [Sort]{operation} [mature populations]{population} into [500 µL collection buffer]{buffer} using unenriched sample.
- [Sort]{operation} [neuronal response data]{cells} for each paradigm using a [homemade program]{program}.
- [Sort]{operation} the [SSEA-4+, CD104+, and TRA-1-60- population]{population}.
- [Sort]{operation} [cells]{cells} into a [5mL tube containing cold PBS/10% FBS]{tube}.
- [Sort]{operation} and count debris items based on categories listed on the data sheet.
- [Sort]{operation} the [SP]{population} with a [FACS Vantage SE]{device} or equivalent sorter.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be sorted(usually cells) |
| container | optional \| reagent | The container to collect sorted cells(usually tube) |
| reagent2 | optional \| reagent | The buffer to be used during sorting |
| device | optional \| string | The device used for sorting, default=FACS |
| program | optional \| string | The program used for sorting data |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Sorted cells |
## 89. ROTATE

### Examples:
- [Rotate]{operation} [forty-five degree]{angle} to the [right]{direction}.
- [Rotate]{operation} the [trays]{object} [clockwise]{direction} every [two minutes]{time} to prevent settling of DAB precipitate onto the underlying cross-sections.
- [Rotate]{operation} at [20 rpm]{speed} for [60 min]{time} in a cold room \(4 &#xB0;C).
- [Rotate]{operation} the [tube]{object} for [10 min]{time} at [room T]{temperature}.
- [Rotate]{operation} the [fluorescence image]{object} using the ImageJ menu “Plugins-kbi-Kbi_registration \(mode: horizoner)” \(**Figure 2c**).

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be rotated |
| direction | optional \| string | The direction of rotation |
| angle | optional \| number | The angle of rotation in degrees |
| intensity | optional \| number | The intensity of rotation |
| time | optional \| time |  |
| temperature | optional \| temperature | default=room temperature |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 90. CONNECT

### Examples:
- [Connect]{operation} each [cannulation tube of IRA and IRIVC]{device1} with [perfusion tube and urine-collecting bag]{device2}.
- [Connect]{operation} [MPSC of the splenic vein and the IVC graft]{device1} to [circulation circuit of the active shunt system]{device2}.
- [Connect]{operation} [optical fibers]{device1} via a [FC/PC adaptor]{connector} to a [473 nm blue or 561 nm yellow laser diode and stimulator]{device2} to generate blue or yellow light pulses.
- [Connect]{operation} the [pressure chamber]{device1} to the [pressure source]{device2}.
- [Connect]{operation} the [Zinc-plated slotted angles]{device1} first and then the [aluminum bars]{device2}{sequence}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| device1 | required \| string | The first device to be connected |
| device2 | required \| string | The second device to be connected |
| connector | optional \| string | The connector used to connect the devices |
| sequence | optional \| string | The sequence of connecting the devices if it matters |
| device | required \| string | Products after connecting device1 and device2 |
## 91. SPLIT

### Examples:
- [Split]{operation} [cells]{object} into [6 well plates]{destination}.
- [Split]{operation} the [remaining chromatin solution]{object} \(450 &#x3BC;l) into [3 tubes]{destination} with [150 &#x3BC;l]{volume} each.
- [Split]{operation} the [culture]{object} in [10 tubes]{destination}, (each with [20mL]{volume}).
- [Split]{operation} [animals]{object} into [experimental groups]{destination}.
- [Split]{operation} [cells]{object} between [1:3 to 1:5]{ratio} and add the cells into a [pre-coated Primaria vessel]{destination}.
- [Split]{operation} [cells]{object} with a [1:3]{ratio} split ratio when reaching [80% of confluence]{environment}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be split |
| destination | required \| reagent | The destination where the object will be split into |
| ratio | optional \| number | The ratio for splitting the object |
| volume | optional \| volume | The volume of each split part |
| number | optional \| number | The number of parts to split the object into |
| environment | optional \| string | The condition under which the object should be split |
| reagent0 | required \| reagent | Reagent after splitting |
## 92. PULL

### Examples:
- [Pull]{operation} the [stitches of the back wall]{object} [cephalad]{direction}.
- [Pull]{operation} [up to 2.0 μl]{volume} [with air]{notice}.
- [Pull]{operation} the [silica capillary]{object} using the [following program]{settings}.
- [Pull]{operation} the [glass capillaries]{object} at the [adequate magnet and heater strength]{position}.
- [Pull]{operation} the [needle]{object} [out]{direction} [carefully]{notice}.
- [Pull]{operation} the [plunger]{object} to the [1 mL]{position} [position].

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be pulled |
| direction | optional \| string | The direction in which the object is pulled |
| volume | optional \| volume |  |
| device | optional \| string | The device used to pull the object |
| settings | optional \| string | The settings used on the device |
| position | optional \| string | The position to which the object is pulled |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 93. ACQUIRE

### Examples:
- [Acquire]{operation} [spectra]{data_type}.
- [Acquire]{operation} the [plate containing the diluted cell suspension]{data_type} on a [flow cytometer]{device} fitted with the appropriate laser lines for the fluorescent cell label and DNA dye chosen.
- [Acquire]{operation} [data]{data_type} with [Analyst 1.6.3]{device}.
- [Acquire]{operation} [images]{data_type} using a [HCX APO L20x objective]{device} with a 1.0 numerical aperture.
- [Acquire]{operation} [at least 30,000 CD4+ or CD8+ T cells]{quantity}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1/data1 | required \| reagent/data | The reagent/data to be acquired |
| device | required \| string | The device or software used to acquire the data |
| settings | optional \| string | Any specific settings or conditions for the acquisition |
| quantity | optional \| number | The quantity of reagent or data to be acquired |
| data | required \| string |  |
## 94. SWITCH

### Examples:
- [Switch]{operation} back to the [LSM mode]{mode}.
- [Switch]{operation} [medium]{device} to the [N3/basal medium]{medium}.
- [Switch]{operation} on the [magnetic stirrer and heater]{device}.
- [Switch]{operation} the [objective lens]{device} to [40x one]{mode}.
- [Switch]{operation} on the [pressure regulator]{device} on the [oxygen tank]{notice}.
- [Switch]{operation} the [perfusion]{device} to [CS]{medium} at [3ml/min]{flowRate} for additional [3 minutes]{time}.
- [Switch]{operation} on the [laser]{device}.
- [Switch]{operation} on the [pressure control]{device}.
- [Switch]{operation} the [EVOM2]{device} off and return the [EndOhm-12]{notice} to the [BSC]{notice}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| device | required \| string | The device to be switched |
| mode | optional \| string | The mode to be switched to |
| flowRate | optional \| volume |  |
| time | optional \| time |  |
| notice | optional \| string |  |
| device | required \| string |  |
## 95. SEE

### Examples:
- [See]{operation} [Table 2]{referenceType, referenceID}.
- [See]{operation} [Figure 3]{referenceType, referenceID} for an example of the UV absorbance profile.
- [See]{operation} [troubleshooting]{referenceType}, if segmentation is inaccurate.
- [See]{operation} [sequence of insert]{referenceType} below.
- [See]{operation} [Step 2]{referenceType} in <em>Prior to Arrival</em> according to Farrens et al.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| referenceType | required \| string | The type of reference to be seen (e.g., table, figure, step, troubleshooting, etc.) |
| referenceID | required \| string | The ID or name of the reference |
## 96. TRANSFORM

### Examples:
- [Transform]{operation} [protease-deficient _E.]{reagent1}.
- [Transform]{operation} [competent _E.]{reagent1}.
- [Transform]{operation} [1 l]{volume} into [20 l ElectroMAX DH10B cells]{reagent2}.
- [Transform]{operation} the [entire 6 μL reaction product]{reagent1} into a [high-efficiency cloning strain]{reagent2} following [standard transformation protocols]{protocol}.
- [Transform]{operation} the [data]{reagent1} into [patch size]{scale}.
- [Transform]{operation} [inhibitor concentrations]{reagent1} into [logarithms]{scale}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be transformed |
| reagent2 | optional \| reagent | The reagent into which transformation is to be done |
| volume | optional \| volume |  |
| protocol | optional \| string | Standard transformation protocols to be followed |
| scale | optional \| string | Scale to which data is to be transformed |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 97. TRANSFECT

### Examples:
- [Transfect]{operation} the [HeLa cells]{cellType} at [50-60% confluency]{confluency} with [CD63-pHluorin plasmid DNA]{plasmid}.
- [Transfect]{operation} [GFP-STIM1-APEX2]{plasmid} using [Lipofactamine 3000]{method} (500 ng plasmid) following the manufacturer’s instructions (Life technologies)
- [Transfect]{operation} [50 µg of plasmid DNA]{amount} using [standard procedures]{method} (alternatively transfection can be carried out with an Amaxa machine as described<sup>8</sup>)
- [Transfect]{operation} [cultured neurons]{cellType} with a form of [NGL-2]{plasmid} in which EGFP was tagged to the N terminus (EGFP-NGL-2) at DIV 14.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The reagent to be transfected(usually cells) |
| reagent2 | required \| reagent | The plasmid to be transfected into the cells |
| reagent3 | required \| reagent | The other reagent used for transfection(usually transfectant) |
| method | optional \| string | The method used for transfection, default=standard procedures |
| reagent0 | required \| string | Transfected cells |
## 98. FIT

### Examples:
- [Fit]{operation} [binding curves of anisotropy versus protein concentration]{object1} to a [single-ligand binding model]{model} and determine Kd.
- [Fit]{operation} the [individual brightness spectrogram]{object1} for a single concentration range with an [array of Gaussian functions]{model}.
- [Fit]{operation} the [flask]{object1} with a [water condenser]{object2} in the main neck and also a [rubber septum]{object2} in the second neck.
- [Fit]{operation} a [nose cone]{object1} over the face to maintain isoflurane anesthesia throughout the [scanning procedure]{procedure}.
- [Fit]{operation} the [window frame]{object1} into the space with [ribs/muscle]{object2} fitting snuggly within the grooved edge of the window frame.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| device1 | required \| string | The object to be fitted |
| device2 | required \| string | The object to fit into object1 |
| model | optional \| string | The model to fit the data to |
| notice | optional \| string |  |
| object0 | required \| string |  |
## 99. EXPOSE

### Examples:
- [Expose]{operation} the [hilum of the spleen]{object}.
- [Expose]{operation} the [wet membrane]{object} to [UV stratalinker]{exposureDevice} at [120 mJ/cm<sup>2</sup>]{exposureIntensity} for [1 minute]{exposureTime} to fix the RNA to the blot.
- [Expose]{operation} the [sealed envelope (containing the membrane)]{object} at room temperature to [Lumi-Film X-ray film]{exposureDevice} for [15 – 25 min]{exposureTime} and adjust the exposure time to get a darker or lighter band pattern.
- [Expose]{operation} the [kidney]{object} outside the body using [two saline-wetted cotton-tipped applicators]{exposureMethod}.
- [Expose]{operation} the [wafer]{object} to [UV]{exposureMethod} for [6 sec]{exposureTime} using the [thin layer photomask]{exposureDevice}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be exposed |
| method | required \| string | The method of exposure |
| time | optional \| time |  |
| intensity | optional \| number |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 100. DIVIDE

### Examples:
- [Divide]{operation} the [falciform ligament]{object1}.
- [Divide]{operation} the [left coronary and triangular ligament]{object1} using a [cautery]{method}.
- [Divide]{operation} the [resulting solution]{object1} to [5 aliquots]{quantity} in [200-μl PCR tubes]{container}.
- [Divide]{operation} the [total number of cells]{object1} by the [number of aggregates]{object2} used to determine an [average value]{calculation} at this stage.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be divided |
| method | optional \| string | Method used to divide the object |
| quantity | optional \| number | Number of parts to divide the object into |
| container | optional \| string | Container to place the divided parts into |
| object0 | required \| reagent |  |
## 101. DIALYZE

### Examples:
- [Dialyze]{operation} the [mixture]{mixture} against [0.1 M Tris-HCl, pH 7.5, 0.15 M NaCl, 0.02% (wt/vol) NaN3]{against} at [4°C]{temperature}.
- [Dialyze]{operation} [sample]{mixture} against [6 M Urea]{against} in rehydrated D-tubeTM Dialyzer Mini tubes for [2 h]{time} on a stirrer at [room temperature]{temperature}.
- [Dialyze]{operation} the [H1-depleted chromatin]{mixture} against [TEP buffer]{against} [overnight]{time}.
- [Dialyze]{operation} the [protofilaments]{mixture} for [1 h]{time} against [100 ml of 1x BRB80 supplemented with 0.5 μM taxol]{against}.
- [Dialyze]{operation} for [4 d]{time} at [4°C]{temperature} with stirring, changing the water three times per day (morning, noon, evening) to remove unreacted peptides and TEA.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The mixture to be dialyzed |
| reagent2 | required \| reagent | The solution to dialyze against |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Dialyzed mixture |
## 102. PICK

### Examples:
- [Pick]{operation} peaks in [4D <sup>13</sup>C,<sup>15</sup>N-edited NOESY]{object1} manually or automatically.
- [Pick]{operation} up individual [adult animals expressing Raichu-Ras probe]{object1} to a [bacteria-free NGM plate]{location} to remove bacteria.
- [Pick]{operation} [colonies]{object1} into [200 μL per well of 1x SC –Leu or 1x SC –Trp liquid media]{medium} and grow to saturation for 2 to 3 days with shaking at 30 °C.
- [Pick]{operation} the [pellet]{object1} up by using a [P1000 or P200 wide bore tip]{device}.
- [Pick]{operation} a [single colony]{object1} (or from glycerol stock) into [25 ml TB + salts + 0.4% glucose + antibiotic]{medium}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be picked |
| reagent2 | optional \| reagent | Medium in which the object is picked |
| quantity | optional \| number |  |
| device | optional \| string |  |
| location | optional \| string |  |
| notice | optional \| string |  |
| object0 | required \| reagent |  |
## 103. DROP

### Examples:
- [Drop]{operation} [1 μL]{volume} of [50% glycerol PBS solution]{reagent1} on a [glass slide]{target}.
- [Drop]{operation} [30 μL]{volume} [fixed cells]{reagent1} onto [pre-cleaned and wet slides]{target} tilted at a [45 degree]{angle} angle.
- [Drop]{operation} the needed volume of [cell suspension]{reagent1} onto the [laminin spot]{target} to achieve the desired cell density ([3000 cells/mm^2]{density}).
- [Drop]{operation} [3 ml]{volume} of the [dissociation solution]{reagent1} in the [lid of a small culture dish]{target}.
- [Drop]{operation} a [25 μL]{volume} solution of [LgtD (4 mU), UDP-Gal (10 mM), Tris-HCl (100 mM; pH 7.0), and MgCl_2 (10 mM)]{reagent1} into [three of four Gb4 tetrasaccharide-synthesized blocks]{target}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be dropped |
| volume | required \| volume | The volume of the reagent to be dropped |
| destination | required \| string | The target where the reagent is dropped |
| angle | optional \| number | The angle at which the target is tilted |
| density | optional \| number | The desired cell density if dropping cell suspension |
| reagent0 | required \| reagent |  |
## 104. ASSESS

### Examples:
- [Assess]{operation} [stocks]{sample} for viable CFU counts and homogeneity by [plating out serial dilutions]{method} of three frozen samples and [1 non-frozen control sample]{controlSample} on blood agar plates.
- [Assess]{operation} [35 mm dish]{sample} as lower wall of the flow chamber and [mount on a microscope stage]{method}.
- [Assess]{operation} [cell phenotype]{sample} by [flow cytometry]{method}.
- [Assess]{operation} the quality of [these PCR-libraries]{sample} by [analyzing 1 µL on a High Sensitivity DNA chip]{method} on a [2100 Bioanalyzer system]{device}.
- [Assess]{operation} [sgRNA yield]{sample} using the [One Drop OD-1000+ Spectrophotometer]{device} and sgRNA quality by [gel electrophoresis]{method}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be assessed |
| method | required \| string | The method used to assess the sample |
| device | optional \| string | The device used for assessment |
| notice | optional \| string |  |
| reagent0 | required \| string | Reagent after assessing |
## 105. RECOVER

### Examples:
- [Recover]{operation} a portion of the [liquid phase]{sample} after centrifugation using a [plastic syringe]{tool}.
- [Recover]{operation} [mononuclear cells]{sample} from interface using a [10 ml serological pipette]{tool}.
- [Recover]{operation} [supernatant]{sample} to [new 1.5ml tube]{destination}.
- [Recover]{operation} the [RNA]{sample} by centrifugation at [12,000 x g for 30 min at 4° C]{centrifugeCondition}.
- [Recover]{operation} [10 ml]{volume} of the [supernatant]{sample}.
- [Recover]{operation} [DNA]{sample} by placing inverted column into [new tube]{destination} and spinning at [1,000 x g for 2 minutes]{centrifugeCondition}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The sample to be recovered |
| device | optional \| string | Device used for recovery |
| volume | optional \| volume |  |
| destination | optional \| string | Where the recovered sample is placed |
| method | optional \| string | Method used for recovery |
| reagent0 | required \| reagent |  |
## 106. INCLUDE

### Examples:
- [Include]{operation} a [PBS treated vehicle control]{item} group.
- [Include]{operation} [enzyme restriction sites]{item} at 5’ ends of both oligonucleotides for vector cloning in the designed/intended orientation.
- [Include]{operation} a [negative control]{item} where no template DNA is added \(optional) and positive control with known genotype.
- [Include]{operation} [six animals]{quantity} in each group.
- [Include]{operation} a [100bp ladder DNA marker]{item}.
- [Include]{operation} [dead live staining]{item}, if possible, especially with extended cell extraction procedures.
- [Include]{operation} [wash step with buffer PB]{item}, and pre-heat buffer EB to 70 °C prior to eluting DNA from the QIAprep membrane.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be included |
| group | optional \| string | The group in which the item is included |
| control | optional \| bool | Whether the item is a control |
| quantity | optional \| number | The quantity of the item to be included |
| location | optional \| string | The location of the item |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 107. HOLD

### Examples:
- [Hold]{operation} each [embryo]{object} so that the polar bodies are located either at the [6 or 12 o'clock]{position} position.
- [Hold]{operation} the [mouse]{object} in a [supine]{position} position, allowing the head to tilt slightly backwards.
- [Hold]{operation} [tube]{object} in fist until thawed.
- [Hold]{operation} the [LRS chamber]{object} with the [conical point downwards]{direction}.
- [Hold]{operation} [it]{object} in place for [10 seconds]{time}.
- [Hold]{operation} the [pipette]{object} at an angle, push the pipette tips to the side of the wells and pipette the medium out with [some force]{force} (without spilling over) to dislodge the gastruloids from the plate.
- [Hold]{operation} potential at [-60 mV]{position} after sealing is successful (>3 GΩ).
- [Hold]{operation} temperature at [50°C]{temperature} for [1 min]{time}, then ramp to 320°C at a rate of 11°C/min, then hold at 320°C for 4.40 min.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The object to be held |
| position | optional \| string | The position in which the object should be held |
| time | optional \| time |  |
| temperature | optional \| temperature |  |
| direction | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| string |  |
## 108. WIPE

### Examples:
- [Wipe]{operation} [colons]{target} with [paper towel]{material}.
- [Wipe]{operation} off the [blood]{target}.
- [Wipe]{operation} down [mouse container]{target} from irradiator with [antiseptic]{reagent}.
- [Wipe]{operation} [injection site]{target} with [alcohol]{reagent}.
- [Wipe]{operation} [blood]{target} from the wound with [clean cotton tips]{material}.
- [Wipe]{operation} dry [excess water]{target}.
- [Wipe]{operation} the entire [dissection area]{target} with [70% ethanol]{reagent}.
- [Wipe]{operation} [femur and tibia]{target} by rubbing with [low-lint tissues]{material}.
- [Wipe]{operation} carefully in the [same]{direction} direction.
- [Wipe]{operation} either [outer or inner gel plate]{target} with [Sigmacote]{reagent}.
- [Wipe]{operation} off [excess ethanol]{target}.
- [Wipe]{operation} away [excess antibody cocktail]{target}.
- [Wipe]{operation} away the [excess PBS]{target}.
- [Wipe]{operation} away the [excess 75% ethanol]{target}.
- [Wipe]{operation} away the [excess ethanol]{target}.
- [Wipe]{operation} out the [cup surface]{target} with a [wet Kim Wipe]{material}.
- [Wipe]{operation} the [biosafety cabinet]{target} thoroughly with [70% ethanol]{reagent}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| location | required \| string | The areato be wiped |
| reagent2 | optional \| reagent | The other reagent used to wipe |
| notice | optional \| string |  |
## 109. REDUCE

### Examples:
- [Reduce]{operation} disulfide bonds by adding [DTT]{reagent2} to a final concentration of [10 mM]{concentration} and incubating at [56 ºC]{temperature} for [45 minutes]{time}.
- [Reduce]{operation} [cytochrome _c_]{reagent1} by adding tiny amounts of [sodium dithionite]{reagent2} until the absorbance at 550 nm of 100 µl of cytochrome _c_ in 1 ml of H<sub>2</sub>O is between 1.8 and 1.9.
- [Reduce]{operation} [human transferrin (Tf)]{reagent1} (20 mg) by incubation with [20 mM dithiothreitol]{reagent2} in 20 ml of 0.2 M Tris-HCl, pH 8.6 containing 8 M urea for [4 h at 37°C]{time}.
- [Reduce]{operation} the [volume]{volume} to [0.2 mL]{volume} by extracting with [n-butanol]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be reduced |
| reagent2 | required \| reagent | The reducing agent |
| targetConcentration/volume | required \| concentration | The final concentration or volume of the reagent1 |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 110. INCREASE

### Examples:
- [Increase]{operation} [temperature]{parameter} to [67]{value} and [incubate]{operation} for at least [1.5 hours]{time} with shaking.
- [Increase]{operation} the [volume]{parameter} to [500 μL]{value} of buffer.
- [Increase]{operation} the [speed]{parameter} of the shaker such that the solution is vigorously mixing.
- [Increase]{operation} [speed]{parameter} and centrifuge at [13,000 rpm]{value} for [1 min]{time} at room temperature.
- [Increase]{operation} [pressure]{parameter} to [1500 psi]{value}.
- [Increase]{operation} the [Morph value]{parameter} in order to erase small objects that is to be disregarded.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| attribute | required \| string | The attribute to be increased |
| value | required \| number | The value to which the parameter is increased |
| time | optional \| time |  |
| environment | optional \| string |  |
| device | optional \| string |  |
| notice | optional \| string |  |
## 111. DEHYDRATE

### Examples:
- [Dehydrate]{operation} the [slides]{reagent1} in [70%, 95% and 100% (vol/vol) ethanol]{reagent2} for [30 s each]{time}.
- [Dehydrate]{operation} [gels]{reagent1} with [100 μl acetonitrile]{reagent2} for [10 min]{time}.
- [Dehydrate]{operation} [sample]{reagent1} by [10min]{time} incubations in [50% (once), 70% (once), 90% (once) and 100% (3 times)]{reagent2}, at [room temperature]{temperature}.
- [Dehydrate]{operation} the [sections]{reagent1} in [graded ethanol and clear the sections in toluene]{reagent2}.
- [Dehydrate]{operation} [larvae]{reagent1} stepwise with [increasing concentrations of methanol (5 min washing steps each of 25%, 50%, 75% MeOH in PBST and 100% MeOH)]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The sample to be dehydrated |
| reagent2 | optional \| reagent | Dehydrating agents |
| time | optional \| time | Time for dehydration |
| temperature | optional \| temperature |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Dehydrated sample |
## 112. SEQUENCE

### Examples:
- [Sequence]{operation} [purified DNA plasmids]{sample} using [primers listed in Table 2]{primers}.
- [Sequence]{operation} the [purified bulk PCR amplicons]{sample} directly.
- [Sequence]{operation} with [Illumina Nextera read primer and read 2 primer and Nextera Index Read Primer for i5 and i7 indexes]{primers}.
- [Sequence]{operation} [cells]{sample} at [~200000]{reads} reads per cell.
- [Sequence]{operation} the [libraries]{sample} with [paired-end 150-bp]{mode} reads on [Hiseq X-ten or Novaseq 6000]{platform} platform.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The sample to be sequenced |
| reagent2 | optional \| reagent | Primers used for sequencing |
| frequency | optional \| frequency | Number of reads per sample/cell |
| mode | optional \| string | Sequencing mode, e.g. single-end or paired-end |
| device | optional \| string | Sequencing device used |
| protocol | optional \| string | Specific protocol followed for sequencing |
| sequence | required \| string |  |
## 113. INDUCE

### Examples:
- [Induce]{operation} and maintain anesthesia using [isoflurane]{reagent1} in oxygen.
- [Induce]{operation} anaesthesia in [mice]{reagent1} by inhalation of [3% isoflurane]{concentration} for [2-3min]{time} and maintain with [2% isoflurane]{concentration} for up to [6min]{time}.
- [Induce]{operation} apoptosis of [T cell clones]{reagent1} by the addition of [500 ng/ml anti-Fas]{reagent2}.
- [Induce]{operation} [megabody expression]{reagent1} with [1 mM IPTG]{reagent2} and grow overnight at [28 °C]{temperature} and [170 r.p.m]{method}.
- [Induce]{operation} protein expression by adding [IPTG]{reagent2} to a final concentration of [1 mM]{concentration}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent or subject to be induced |
| reagent2 | optional \| reagent | Additional reagents used for induction |
| temperature | optional \| temperature |  |
| time | optional \| time |  |
| method | optional \| string | Specific method or protocol for induction |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 114. DESIGN

### Examples:
- [Design]{operation} single-stranded DNA (ssDNA) [custom primer sequences]{designType} complementary to [regions of interest]{regionOfInterest} with [5’ phosphate modification]{modification} added.
- [Design]{operation} the [masks]{designType} by [CAD or other vectorial graphic software]{software}.
- [Design]{operation} of [paired sgRNA oligos]{designType}.
- [Design]{operation} the layout of your [Q-PCR 96 well plate or strips]{designType}, and determine the amounts necessary to assemble the following per-well Q-PCR reaction.
- [Design]{operation} [specific primers]{designType} flanking the [Cas9•sgRNA cutsite (target amplicon)]{regionOfInterest}.
- [Design]{operation} your [experiment]{experimentDetails}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| designType | required \| string | The type of design to be made |
| software | optional \| string | Software used for design |
| regionOfInterest | optional \| string | Region of interest for primer design |
| modification | optional \| string | Any modifications to be made to the design |
| primerType | optional \| string | Type of primers to be designed |
| notice | optional \| string |  |
| design | required \| string |  |
## 115. DEPOSIT

### Examples:
- [Deposit]{operation} metals \(Cr/Au, 15/100 nm) on the [prepared substrate]{substrate} using [electron beam evaporator]{method}.
- [Deposit]{operation} copper \(Cu, 3 µm) on the [substrate]{substrate} using [electron beam evaporation]{method}.
- [Deposit]{operation} silicon dioxide \(600nm) on the [wafer]{substrate} using [PECVD]{method}.
- [Deposit]{operation} PDMS \(10:1) on the [prepared surface]{substrate} and [cure for 1 day at ambient temperature]{notice}.
- [Deposit]{operation} 20 µL of [HepaRG cells \(7,000 cells)]{material} in the centre of each well of a [collagen I-coated 48 wells plate format \(P48)]{substrate}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be deposited |
| thickness | optional \| number | Thickness of the material to be deposited, default=0 |
| reagent2 | required \| reagent | The substrate on which the material is deposited |
| method | optional \| string | The method used for deposition |
| time | optional \| time |  |
| temperature | optional \| temperature |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 116. COMPARE

### Examples:
- [Compare]{operation} [spin-system types of a connectivity fragment]{item1} with [the protein sequence]{item2}.
- [Compare]{operation} [MGB neuronal responses to the sound stimulus under the LS paradigm]{item1} and [S paradigm]{item2}.
- [Compare]{operation} [the above results]{item1} with [that before the TRN inactivation]{item2}.
- [Compare]{operation} [drinking latencies between home cage]{item1} and [novel cage]{item2}.
- [Compare]{operation} [the amount of integrin tail binding between F2F3]{item1} and [F2F3 mutants]{item2}.
- [Compare]{operation} [the signal from your unknown sample]{item1} to [that of standard]{item2} and estimate the concentration.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The first item to be compared |
| reagent2 | required \| reagent | The second item to be compared |
| environment | optional \| string | The environment under which reagent is observed |
| notice | optional \| string |  |
## 117. ALIGN

### Examples:
- [Align]{operation} the [samples]{object1} to the [genome]{object2} using [‘STAR.’]{method}.
- [Align]{operation} the [combined PDMS layer]{object1} and bond it onto the [flipped PDMS layer 2]{object2} using [oxygen plasma treatment]{method}.
- [Align]{operation} the [pre-soaked membrane]{object1} on top of the [wet filter papers]{object2}.
- [Align]{operation} [reads]{object1} to the [genome]{object2}.
- [Align]{operation} first by [Geneious alignment]{method}, with [default parameters]{parameters}.
- [Align]{operation} once again using [MUSCLE alignment]{method} with [8]{iterations} iterations.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The object to be aligned |
| reagent2 | optional \| reagent | The object to which object1 is aligned, keep alive |
| method | optional \| string | The method or tool used for alignment |
| repeat | optional \| number |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 118. WRAP

### Examples:
- [Wrap]{operation} the [tube]{item} with [PTFE tape]{material}.
- [Wrap]{operation} the [cap]{item} with [Teflon tape]{material}.
- [Wrap]{operation} the [box]{item} with [aluminum foil]{material}.
- [Wrap]{operation} [tightly]{tightness} with [Parafilm]{material} if [desired]{additional_protection} for further protection.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The item to be wrapped |
| reagent2 | required \| reagent | The material used to wrap the item |
| notice | optional \| string |  |
| reagent0 | required \| string | Wrapped reagent |
## 119. SACRIFICE

### Examples:
- [Sacrifice]{operation} the [mice]{animal}.
- [Sacrifice]{operation} [two 8-16 week old reprogrammable mice/Oct4GFP mice]{animal} by [ventilating them with CO2]{method}.
- [Sacrifice]{operation} the [pregnant mother]{animal} by [cervical dislocation]{method}.
- [Sacrifice]{operation} [mouse]{animal} by [cervical dislocation method]{method} and [immerse whole body thoroughly with 75% ethanol solution 10min]{procedure}.
- [Sacrifice]{operation} [E17 rat]{animal} according to [institutional ethically approved procedures]{notice}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| string | The animal to be sacrificed |
| method | optional \| string | The method used to sacrifice the animal |
| age | optional \| number | The age of the animal to be sacrificed |
| notice | optional \| string | Any additional information or precautions |
| reagent0 | required \| reagent | Dead animal |
## 120. READ

### Examples:
- [Read]{operation} the [Tergazyme SDS sheet]{target} prior to cleaning the [EndOhm chamber]{device}.
- [Read]{operation} the [optical density]{target} at [405 nm]{parameter} with a [plate reader]{device}.
- [Read]{operation} the [data]{target} into [R]{device} by typing on the [command line]{method}.
- [Read]{operation} the [absorbance]{target} at [660 nm]{parameter}.
- [Read]{operation} the [README file]{target} in the [AlignDB package root directory]{device}.
- [Read]{operation} in [qPCR machine]{device} (use [FAM/SYBR channel]{parameter}).

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| device | required \| string | The device used to read |
| data1 | required \| data | The target to be read(usually file) |
| parameter | optional \| string | Additional parameters for reading, such as wavelength, channel, etc. |
| method | optional \| string | The method used to read, such as command line, setting, etc. |
| notice | optional \| string |  |
| data0 | required \| data |  |
## 121. SETUP

### Examples:
- [Setup]{operation} controls for pre-amplification in [PCR tube strips]{container} as described below.
- [Setup]{operation} pre-PCR master mixes in a [1.5 ml Eppendorf tube]{container} on ice by mixing the following components.
- [Setup]{operation} the real-time PCR master mix in a [2 ml of Eppendorf tube]{container} with [Telomere primers]{reagent1} according to the following recipe.
- [Setup]{operation} a [hotplate]{container} at approximately [85°C]{temperature}
- [Setup]{operation} and activate a new [virtual environment]{container}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| container | required \| string | The container to setup, e.g., PCR tube, Eppendorf tube, PCR plate, glass plates, hotplate, perfusion station, culture dishes, manipulation dish |
| reagent1 | optional \| reagent | The main reagent to be setup |
| reagent2 | optional \| reagent | Additional reagents added during setup |
| volume | optional \| volume |  |
| temperature | optional \| temperature |  |
| environment | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 122. PACK

### Examples:
- [Pack]{operation} the [resin composite]{reagent1} inside [Tygon tubes]{container} placed perpendicularly onto the flat coronal dentin surface.
- [Pack]{operation} a [chromatography column \(2.8 × 40 cm)]{container} with a slurry of [silica gel]{reagent1} in [EtOAc : PE = 1 : 2]{reagent2}.
- [Pack]{operation} [NeutrAvidin Agarose Resin]{reagent1} into a [1.5 ml tube]{container} and wash with [RIPA buffer]{reagent2}, centrifuge at 2,000 ×g for 1 min to remove storage solution, repeat wash step twice.
- [Pack]{operation} approximately [6-7cm]{volume} of [packing material]{reagent1} behind the bottleneck.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be packed |
| container | required \| string | The container where the reagent is packed |
| volume | optional \| volume |  |
| device | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 123. IMPORT

### Examples:
- [Import]{operation} [mass spectrometry raw data]{file} for [quantitation]{purpose}.
- [Import]{operation} the [images]{file} to [“ImageJ”]{software} to [track cells]{purpose}.
- [Import]{operation} the [VM]{file} into the player following the [step-by-step instructions provided in the manual on the website]{instruction}.
- [Import]{operation} the [resulting files from GenePix 4.0 (Axon Instruments) analysis]{file} into [Genespring 5.0 (Silicon Genetics)]{software} for [additional visualization and data mining]{purpose}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| data1 | required \| data | The file to be imported |
| software | required \| string | The software where the file will be imported |
| purpose | optional \| string | The purpose of importing the file |
| reference | optional \| string | Additional reference for importing the file |
| data0 | required \| data |  |
## 124. HOMOGENIZE

### Examples:
- [Homogenize]{operation} [cells]{reagent1} by passing them twice through a [25-gauge needle]{device}.
- [Homogenize]{operation} [tissue]{reagent1} with [reusable pellet pestles and motor]{device} for [45 s]{time} with at least [10]{strokes} strokes.
- [Homogenize]{operation} [mouse liver tissue]{reagent1} to a cell suspension in [ice-cold PBS]{reagent2} by using a [dounce homogenizer or a pellet pestle]{device}.
- [Homogenize]{operation} [frozen tissue]{reagent1} with [ice-cold 10 mM Tris-HCl buffer containing 250 mM sucrose at pH 7.4]{reagent2}.
- [Homogenize]{operation} the [swollen cells]{reagent1} on ice with [15]{strokes} strokes of a [Dounce homogenizer]{device} on ice.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be homogenized |
| reagent2 | optional \| reagent | Additional reagents added during homogenization |
| device | optional \| string | The device used for homogenization |
| time | optional \| time |  |
| strokes | optional \| number | Number of strokes used during homogenization |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 125. GIVE

### Examples:
- [Give]{operation} [1 piece of vehicle jelly]{quantity} to [each mouse]{recipient} in the morning of the following 3 days.
- [Give]{operation} [about 1/8th of vehicle jelly or treatment jelly]{quantity} to [mice in the control or treatment group]{recipient} respectively.
- [Give]{operation} the [glucose piece jelly]{reagent1} to [corresponding mouse]{recipient}.
- [Give]{operation} [all treatments]{reagent1} [once a day]{frequency} for [5 consecutive days]{time}.
- [Give]{operation} [anesthesia intra-peritoneally]{method} to the [male mice]{recipient} (100µl/20g of body weight).

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be given |
| reagent2 | required \| reagent | The recipient(usually mouse) of the reagent |
| quantity | required \| volume | default=1 piece |
| repeat | optional \| number |  |
| frequency | optional \| number |  |
| method | optional \| string |  |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 126. DENATURE

### Examples:
- [Denature]{operation} [RNA]{reagent1} at [65°C]{temperature} for [10 min]{time} followed by rapid cooling on ice for [5 min]{coolingTime}.
- [Denature]{operation} the [probe]{reagent1} by placing it in a boiling water bath for [5 min]{time} followed by snap cooling on ice.
- [Denature]{operation} the [DNA]{reagent1} for [5 min]{time} at [95°C]{temperature}.
- [Denature]{operation} [streptavidin]{reagent1} in the pellets with [10 μl 10 mM EDTA, 95% formamide]{reagent2} at [90°C]{temperature} for [3 min]{time}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be denatured |
| temperature | required \| temperature |  |
| time | required \| time | default=5 min |
| notice | optional \| string |  |
| reagent0 | required \| reagent | Denatured reagent |
## 127. TRIM

### Examples:
- [Trim]{operation} the [diaphragmatic patch]{object} to a [decent size]{size}.
- [Trim]{operation} the [tissue]{object} to cut off non-tissue stuff and get rid off the blood on the tissue with [Kimwipers]{method}.
- [Trim]{operation} the [floor plate]{object} gently to flatten the tissue.
- [Trim]{operation} [reads]{object} to remove adapter sequences.
- [Trim]{operation} the [V/1 tip]{object} to [8 mm]{size}.
- [Trim]{operation} [alignment]{object} [to only epitope region]{termination}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be trimmed |
| size | optional \| number | The size to which the object should be trimmed |
| method | optional \| string | The method or tool used to trim the object |
| purpose | optional \| string | The purpose of trimming |
| notice | optional \| string |  |
| reagent0 | required \| reagent |  |
## 128. SUPPLEMENT

### Examples:
- [Supplement]{operation} [1 ml of viral supernatant]{reagent1} with [8µg/mL polybrene]{reagent2}.
- [Supplement]{operation} [E8 medium]{reagent1} with the [ROCK inhibitor Y-27632 (1:1000)]{reagent2} to a final concentration of [10 μM]{concentration}.
- [Supplement]{operation} [nuclei suspension]{reagent1} with [1 mM CaCl2]{reagent2}.
- [Supplement]{operation} [with fresh media plus IL-2]{reagent2} [daily starting two days after stimulation]{timing}.
- [Supplement]{operation} [the media]{reagent1} with [amphotericin B (2.5 mg/l), trimethoprim (5 mg/l), polymyxin B (1250 IU/l), and vancomycin (10 mg/l)]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be supplemented |
| reagent2 | required \| reagent | The other reagent(s) to be added |
| volume | optional \| volume |  |
| targetConcentration | optional \| concentration |  |
| timing | optional \| string | When to supplement, if necessary |
| reagent0 | required \| reagent |  |
## 129. RECONSTITUTE

### Examples:
- [Reconstitute]{operation} [dye]{reagent1} right after dissection and immediately before use in [anhydrous DMSO]{reagent2}.
- [Reconstitute]{operation} the [residue]{reagent1} with [200 &#xB5;l water/0.002% formic acid]{volume reagent2}.
- [Reconstitute]{operation} [40 &#xB5;g of trypsin]{reagent1} with [20 &#xB5;l dissolution buffer]{volume reagent2}.
- [Reconstitute]{operation} the [Vn96 peptide]{reagent1} to 2.5 µg/µL by adding [200 µL ME-buffer]{volume reagent2}.
- [Reconstitute]{operation} the [pellet]{reagent1} in [100 μl MEM]{volume reagent2}.
- [Reconstitute]{operation} [sample]{reagent1} in [20% acetonitrile/2% formic acid]{volume reagent2}.
- [Reconstitute]{operation} [tryptic peptide digests]{reagent1} in [25 µL 5% acetonitrile containing 0.1% trifluoroacetic acid]{volume reagent2}.
- [Reconstitute]{operation} and store the [luciferase substrate stock solution containing coelenterazine h or DeepBlueC]{reagent1} with [anhydrous ethanol]{reagent2}.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| reagent1 | required \| reagent | The reagent to be reconstituted |
| reagent2 | required \| reagent | The reagent used for reconstitution |
| timing | optional \| string | When the reconstitution should be done, if applicable |
| reagent0 | required \| reagent | The reconstituted reagent |
## 130. EXPORT

### Examples:
- [Export]{operation} the [data]{data} to a [Microsoft Excel]{format} spreadsheet.
- [Export]{operation} the [automated quantitation result]{data} following [Step 11 and 12]{step} with [two additional data columns]{additionalColumns}.
- [Export]{operation} [manually corrected quantitation results]{data} following [Step 11 and 12]{step}.
- [Export]{operation} the [image]{data} in [proper format]{imageFormat}.
- [Export]{operation} [images]{data} in [.tif]{imageFormat} format.

### Notices:

### Synonyms:

Arguments:

| Argument | Type | Comment |
| --- | --- | --- |
| data1 | required \| data | The data to be exported |
| format | optional \| string | The format to export the data in |
| step | optional \| number | The step in the process where the data is exported |
| data0 | required \| string | Exported data |