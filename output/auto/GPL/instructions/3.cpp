#include "BioCoder.h"

int main()
{
    start_protocol("3");
    Fluid hypotonic_buffer = new_fluid("Hypotonic Buffer");
    Solid protein_A_beads = new_solid("Protein A Beads");

    Container centrifuge_tube = new_container(CENTRIFUGE_TUBE_15ML);

    // 1. Rinse Protein A beads in Hypotonic Buffer.
    first_step();
    wash_tissue(protein_A_beads, water, RINSING);

    // 2. Place on ice till ready for use.
    next_step();
    store(centrifuge_tube, ON_ICE);
}