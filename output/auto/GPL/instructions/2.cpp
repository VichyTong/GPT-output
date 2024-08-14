#include "BioCoder.h"

int main()
{
    start_protocol("2");

    Fluid dtt = new_fluid("DTT", "100mM in extraction buffer 2");
    Fluid tissue_lysate = new_fluid("tissue lysate");
    Fluid iaa = new_fluid("IAA", "550mM in extraction buffer");

    Container flask = new_container(FLASK, culture);

    // 1. Add 11ul of 100mM DTT in extraction buffer 2 to the tissue lysate.
    first_step();
    measure_fluid(tick_homogenate, vol(_, UL), flask);
    measure_fluid(dtt, vol(11, UL), flask);
    dissolve(flask)

    // 2. Incubate at 56°C for 1hr.
    next_step();
    incubate(flask, 56, time(1, HRS))

    // 3. Leave solution to cool to room temperature before adding 12μl of 550mM IAA in extraction buffer.
    next_step();
    store(flask, RT, COOLED)
    measure_fluid(iaa, vol(12, UL), flask);
    dissolve(flask)


    // 4. Incubate at room temperature for 30min in the dark.
    next_step();
    incubate(flask, RT, time(30, MINS))
}