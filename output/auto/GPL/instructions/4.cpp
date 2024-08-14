#include "BioCoder.h"

int main()
{
    start_protocol("4");
    Fluid tris_edta = new_fluid("Tris-EDTA");

    Container tube = new_container(TUBE);

    // 1. Dissolve 15ul Tris-EDTA and store -20°C.
    first_step();
    measure_fluid(tris_edta, 15, UL);
    dissolve(tube)
    store_for(tube, -20);

}