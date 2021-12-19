#include "wscp.h"

int main(int argc, char *argv[])
{
    int time_limit = atoi(argv[2]);
    WSCP wscp_solver(time_limit);
    int seed = atoi(argv[3]);
    srand(seed);

    int new_weight = atoi(argv[4]);
    int tabu_len = atoi(argv[5]);
    double novelty_p = atof(argv[6]);

    /*
    int tabu_len = atoi(argv[4]);
    double novelty_p = atof(argv[5]);
    double explore_p = atof(argv[6]);
    int t = atoi(argv[7]);
    */

    /*
    int w1 = atoi(argv[4]);
    int w2 = atoi(argv[5]);
    int w3 = atoi(argv[6]);
    int w4 = atoi(argv[7]);
    */

    wscp_solver.build_instance(argv[1]);
    //cout << "Finish instance construction!" << endl;
    wscp_solver.reduce_instance();
    //cout << "Finish instance reduction!" << endl;
    //wscp_solver.set_param(tabu_len, novelty_p, explore_p, t);
    wscp_solver.set_param(new_weight, tabu_len, novelty_p);
    //cout << "Finish parameters setting!" << endl;
    //wscp_solver.set_param(w1, w2, w3, w4);
    //wscp_solver.set_tabu_len(tabu_len);
    start_timing();
    wscp_solver.init();
    //cout << "Finish initialization!" << endl;
    wscp_solver.local_search();
    //cout << "Finish local search!" << endl;
    wscp_solver.check_solu();
    //cout << wscp_solver.best_cost << " " << wscp_solver.best_time << endl;
    cout << "v ";
    for (int i = 0; i < wscp_solver.set_num; ++i)
        cout << wscp_solver.best_solu[i] << " ";
    cout << endl;
    wscp_solver.free_memory();
}
