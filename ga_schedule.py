from transportnet import net
from transportnet import line
from transportnet import vehicle
from stochastic import stochastic
from genetics import ga


sim_time = 1.0 * 60
res_file = open('results.txt', 'w')
n = net.Net()
# define the network configuration
n.load_from_file('bochnia_net.txt')
# define a set of public transport lines
bochnia_lines = [line.Line(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 181, 10, 11, 12, 13, 14, 15, 16, 17,
                               17, 16, 15, 14, 13, 12, 11, 10, 181, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 17]),
                 line.Line(1, [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 10, 29, 30, 31, 32, 33, 34,
                              34, 33, 32, 31, 30, 29, 10, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18], [18, 34]),
                 line.Line(2n, [18, 19, 20, 21, 22, 23, 24, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                                49, 48, 47, 46, 45, 90, 43, 42, 41, 40, 39, 38, 37, 36, 35, 179, 180, 23, 22, 21, 20, 19, 18], [18, 49]),
                 line.Line(4n, [181, 9, 8, 40, 41, 42, 73, 74, 75, 53, 54, 78, 57,
                                57, 56, 55, 54, 53, 75, 74, 73, 42, 41, 40, 8, 9, 10, 181, 80, 81], [181, 57]),
                line.Line(5n, [60, 58, 37, 38, 39, 40, 41, 8, 9, 181, 10, 29, 30, 57, 56, 55, 53, 52, 51, 50,
                               50, 51, 52, 53, 55, 56, 57, 30, 29, 10, 181, 9, 8, 41, 40, 39, 38, 37, 58, 59, 60], [60, 50])]
                line.Line(7n, [61, 62, 39, 63, 64, 65, 26, 12, 66, 67, 68, 69, 70, 71, 72,
                               72, 71, 70, 69, 68, 67, 66, 12, 26, 65, 64, 6, 63, 39, 62, 61], [61, 72])]
                line.Line(8n, [60, 58, 37, 38, 39, 40, 41, 8, 9, 181, 10, 11, 66, 67, 68, 69, 70, 71, 72,
                               72, 71, 70, 69, 68, 67, 66, 11, 10, 181, 9, 8, 41, 40, 39, 38, 37, 58, 59, 60], [60, 72])]
                line.Line(9n, [18, 19, 20, 21, 22, 23, 24, 35, 36, 37, 38, 39, 40, 41, 42, 73, 74, 75, 53, 52, 51, 50,
                               50, 51, 52, 53, 75, 74, 73, 42, 41, 40, 39, 38, 37, 36, 35, 179, 180, 23, 22, 21, 20, 19, 18], [18, 50])]
                line.Line(10n, [50, 51, 52, 53, 75, 74, 73, 42, 87, 95, 39, 63, 64, 65, 26, 13, 14, 15, 16, 17,
                               17, 16, 15, 14, 13, 26, 65, 64, 6, 63, 39, 85, 86, 87, 42, 73, 74, 75, 53, 52, 51, 50], [50, 17])]
                line.Line(11n, [81, 80, 10, 181, 9, 8, 41, 40, 62, 61,
                               61, 62, 40, 41, 8 ,9, 181, 10, 80, 81], [81, 61])
                line.Line(12n, [181, 9, 8, 41, 42, 43, 44, 45,
                               45, 90, 43, 42, 41, 8, 9, 181], [181, 45])
                line.Line(14n, [60, 58, 37, 38, 63, 64, 65, 26, 12, 66, 67, 68, 69, 70, 71, 72,
                               72, 71, 70, 69, 68, 67, 66, 12, 26, 65, 64, 6, 63, 38, 37, 58, 59, 60], [60, 72])
                line.Line(17n, [91, 92, 61, 93, 94, 95, 85, 40, 41, 8, 9, 181, 10, 29, 30, 31, 32, 33, 34,
                               34, 33, 32, 31, 30, 29, 10, 10, 181, 9, 8, 41, 40, 85, 95, 94, 93, 61, 92, 91], [91, 34])
                line.Line(19n, [50, 51, 52, 53, 75, 74, 73, 42, 41, 40, 8, 9, 181, 10, 11, 66, 67, 68, 69, 70, 71, 72,
                               72, 71, 70, 69, 68, 67, 66, 11, 10, 181, 9, 8, 40, 41, 42, 73, 74, 75, 53, 52, 51, 50], [50, 72])
                line.Line(20n, [72, 71, 70, 69, 68, 67, 66, 11, 10, 181, 9, 8, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                               49, 48, 47, 46, 45, 90, 43, 42, 41, 8, 9, 181, 10, 11, 66, 67, 68, 69, 70, 71, 72], [72, 49])
                line.Line(21n, [45, 90, 43, 42, 41, 8, 9, 181, 10, 29, 30, 31, 104, 98, 99, 100, 101, 102, 103, 108, 105, 106, 107
                               107, 106, 105, 108, 103, 102, 101, 100, 99, 98, 104, 31, 30, 29, 10, 181, 9, 8, 41, 42, 43, 44, 45], [45, 107])
                line.Line(23n, [81, 80, 10, 181, 9, 8, 40, 41, 42, 73, 74, 75, 53, 52, 51, 50, 109, 110, 111, 112, 113,
                               113, 112, 111, 110, 109, 50, 51, 52, 53, 75, 74, 73, 42, 41, 40, 8, 9, 181, 10, 80, 81], [81, 113])
                line.Line(25n, [61, 93, 94, 95, 85, 40, 41, 8, 9, 181, 28, 27, 11, 66, 67, 68, 69, 114, 115, 116, 117, 118, 119, 121, 122,
                               122, 121, 119, 118, 117, 116, 115, 114, 69, 68, 67, 66, 11, 10, 181, 9, 8, 41, 40, 85, 95, 94, 93, 61], [61, 122])
                line.Line(26n, [45, 90, 43, 42, 41, 8, 9, 181, 28, 27, 11, 66, 67, 68, 69, 114, 115, 116, 117, 118, 125, 126, 127, 128, 129, 130,
                               130, 129, 128, 126, 125, 118, 117, 116, 115, 114, 69, 68, 67, 66, 11, 10, 181, 9, 8, 41, 42, 43, 44, 45], [45, 130])
                line.Line(27n, [181, 9, 8, 7, 6, 5, 4, 3, 2, 131, 132, 133, 134, 135,
                               135, 134, 133, 132, 131, 1, 2, 3, 4, 5, 6, 7, 8, 9, 181], [181, 135])
                line.Line(30n, [181, 9, 8, 7, 64, 65, 26, 13, 14, 15, 16, 17, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156,
                               156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 17, 16, 15, 14, 13, 26, 65, 64, 7, 8, 9, 181], [181, 156])
                line.Line(37n, [91, 92, 61, 93, 94, 95, 85, 40, 41, 8, 9, 181, 28, 27, 26, 25, 170, 171, 172,
                               172, 171, 170, 25, 26, 27, 28, 181, 9, 8, 41, 40, 85, 95, 94, 93, 61, 92, 91], [91, 172])
                line.Line(39n, [1, 2, 3, 37, 38, 39, 85, 86, 87, 42, 73, 74, 75, 53, 52, 51, 50,
                                50, 51, 52, 53, 75, 74, 73, 42, 87, 95, 39, 38, 37, 3, 2, 1], [1, 50])
                line.Line(44n, [50, 51, 52, 53, 55, 56, 57, 30, 29, 10, 181, 9, 8, 7, 63, 38, 37, 3, 2, 178, 177, 176, 175, 174, 173, 19, 18
                               18, 19, 173, 174, 175, 176, 177, 178, 1, 2, 3, 37, 38, 63, 7, 8, 9, 181, 10, 29, 30, 57, 56, 55, 53, 52, 51, 50], [50, 18])
                line.Line(80n, [1, 2, 3, 37, 38, 39, 40, 41, 8, 9, 181, 10, 11, 12, 13, 14, 15, 16, 17
                               17, 16, 15, 14, 13, 12, 11, 10, 181, 9, 8, 41, 40, 39, 38, 37, 3, 2, 1], [1, 50])
                line.Line(z19n, [182, 73, 77, 82, 183, 184, 79, 8,
                               8, 41, 42, 73, 182], [182, 8])
for ln in bochnia_lines:
    ln.add_vehicles([vehicle.Vehicle(45) for _ in range(2)])
n.lines.extend(bochnia_lines)

for sn in range(100):
    # n = net.Net()
    # # define the network configuration
    # n.load_from_file('bochnia_net.txt')
    # # conf #1
    # # n.add_link(1, 2, 1.0)
    # # n.add_link(3, 2, 2.0)
    # # n.add_link(2, 4, 2.0)
    # # n.add_link(5, 4, 3.0)
    # # n.add_link(4, 6, 1.0)
    # # n.add_link(2, 7, 1.0)
    # # n.add_link(4, 8, 2.0)
    # # n.add_link(9, 7, 1.0)
    # # n.add_link(7, 8, 3.0)
    # # n.add_link(8, 10, 2.0)
    # # n.add_link(7, 11, 3.0)
    # # n.add_link(8, 12, 2.0)
    # #
    # # conf #2
    # # s_weight = stochastic.Stochastic(0, 0.9, 1.1)
    # # n.add_link(1, 3, s_weight.get_value())
    # # n.add_link(3, 4, s_weight.get_value())
    # # n.add_link(2, 4, s_weight.get_value())
    # # n.add_link(4, 5, s_weight.get_value())
    # # n.add_link(4, 6, s_weight.get_value())
    # # n.add_link(5, 8, s_weight.get_value())
    # # n.add_link(6, 9, s_weight.get_value())
    # # n.add_link(7, 8, s_weight.get_value())
    # # n.add_link(8, 9, s_weight.get_value())
    # # n.add_link(9, 10, s_weight.get_value())
    # # n.add_link(8, 11, s_weight.get_value())
    # # n.add_link(9, 12, s_weight.get_value())
    # # n.add_link(11, 13, s_weight.get_value())
    # # n.add_link(12, 14, s_weight.get_value())
    # #
    # # conf #3
    # # n.add_link(1, 2, s_weight.get_value())
    # # n.add_link(2, 3, s_weight.get_value())
    # # n.add_link(3, 4, s_weight.get_value())
    # # n.add_link(4, 5, s_weight.get_value())
    # # n.add_link(5, 6, s_weight.get_value())
    # # n.add_link(6, 7, s_weight.get_value())
    # # n.add_link(8, 3, s_weight.get_value())
    # # n.add_link(3, 9, s_weight.get_value())
    # # n.add_link(9, 10, s_weight.get_value())
    # # n.add_link(10, 11, s_weight.get_value())
    # # n.add_link(11, 12, s_weight.get_value())
    # # n.add_link(13, 14, s_weight.get_value())
    # # n.add_link(14, 10, s_weight.get_value())
    # # n.add_link(10, 15, s_weight.get_value())
    # # n.add_link(15, 16, s_weight.get_value())
    # # n.add_link(16, 17, s_weight.get_value())
    # # n.add_link(17, 18, s_weight.get_value())
    # # n.add_link(18, 19, s_weight.get_value())
    # # n.add_link(20, 21, s_weight.get_value())
    # # n.add_link(21, 10, s_weight.get_value())
    # # n.add_link(10, 22, s_weight.get_value())
    # # n.add_link(22, 23, s_weight.get_value())
    # # n.add_link(23, 5, s_weight.get_value())
    # # n.add_link(5, 24, s_weight.get_value())
    # # n.add_link(25, 5, s_weight.get_value())
    # # n.add_link(5, 26, s_weight.get_value())
    # # n.add_link(26, 27, s_weight.get_value())
    # # n.add_link(27, 17, s_weight.get_value())
    # # n.add_link(17, 28, s_weight.get_value())
    # # n.add_link(28, 29, s_weight.get_value())
    # # n.add_link(29, 30, s_weight.get_value())

    s_mean_interval = stochastic.Stochastic(law=0, location=1, scale=4)
    for nd in n.nodes:
        nd.s_interval = stochastic.Stochastic(law=2, scale=s_mean_interval.get_value())

    # # define a set of public transport lines
    # bochnia_lines = [line.Line(n, [27, 28, 39, 18, 23, 26, 15, 31, 32,
    #                                31, 15, 26, 23, 18, 35, 25, 27], [27, 32]),
    #                  line.Line(n, [27, 28, 39, 18, 9, 11, 7, 8, 10, 4, 5, 6,
    #                                5, 4, 10, 8, 7, 11, 9, 18, 35, 25, 27], [27, 6]),
    #                  line.Line(n, [18, 35, 20, 21, 22, 19, 14, 12, 13,
    #                                12, 14, 19, 22, 21, 20, 35, 18], [18, 13]),
    #                  line.Line(n, [27, 28, 39, 18, 23, 24, 17, 16, 40, 41, 30, 42, 43, 2, 3, 33, 34, 29,
    #                                34, 1, 2, 36, 37, 38, 37, 36, 43, 42, 30, 41, 40, 16, 17, 24, 23, 18, 35, 25, 27], [27, 29])]
    # # conf #2
    # # lines = [line.Line(n, [1, 3, 4, 6, 9, 12, 14]),
    # #          line.Line(n, [2, 4, 5, 8, 11, 13]),
    # #          line.Line(n, [7, 8, 9, 10])]
    # # conf #3
    # # lines = [line.Line(n, [1, 2, 3, 4, 5, 6, 7]),
    # #          line.Line(n, [8, 3, 9, 10, 11, 12]),
    # #          line.Line(n, [13, 14, 10, 15, 16, 17, 18, 19]),
    # #          line.Line(n, [20, 21, 10, 22, 23, 5, 24]),
    # #          line.Line(n, [25, 5, 26, 27, 17, 28, 29, 30])]

    # for ln in bochnia_lines:
    #     ln.add_vehicles([vehicle.Vehicle(45) for _ in range(2)])
    # n.lines.extend(bochnia_lines)

    # generate demand for sim_time hours
    n.gen_demand(sim_time)
    # n.print_od_matrix()
    # print


    def fitness_function(shifts):
        n.reset()
        for idx in range(len(n.lines)):
            n.lines[idx].schedule_shift = shifts[idx]
        return n.simulate(sim_time)

    # print 'population #', sn
    # g = ga.GA()
    # # 5 bits per a time shift value: in range between 0 and 31
    # g.chromosome_size = len(n.lines), 5
    # g.population_size = 50
    # g.generations = 30
    # g.fitness_function = fitness_function
    # winner = g.run()
    # for w in winner[0]:
    #     res_file.write(str(w) + '\t')
    # for w in winner[1]:
    #     res_file.write(str(w) + '\t')

    for res in fitness_function([5, 8, 0, 1]):
        print(res, end="\n")
        res_file.write(str(res) + '\t')
    res_file.write('\n')
    print

res_file.close()

