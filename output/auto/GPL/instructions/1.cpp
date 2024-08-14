#include "BioCoder.h"

int main()
{
    start_protocol("1");

    Fluid quick_extract = new_fluid("QuickExtract");
    Fluid tick_homogenate = new_fluid("tick homogenate");

    Container flask = new_container(FLASK, culture);

    // 1. Mix 50µl water with 50µl QuickExtract.
    first_step();
    measure_fluid(quick_extract, vol(50, UL), flask);
    measure_fluid(water, vol(50, UL), flask);
    dissolve(flask)

    // 2. Add to tick homogenate and mix well.
    next_step();
    measure_fluid(tick_homogenate, vol(_, UL), flask);
    vortex(flask)

    // 3. Incubate at 65°C for 6 minutes
    next_step();
    incubate(flask, 65, time(6, MINS))

    // 4. Incubate 95°C for 2 minutes.
    next_step();
    incubate(flask, 95, time(2, MINS))
}