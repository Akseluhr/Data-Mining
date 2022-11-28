import osimport sysimport matplotlib.pyplot as pltimport timeimport random# Given a tuple, e.g. ['2', '3'], we create the edges between them# If frm is smaller than to, we do nothing, if the opposite, we change places # Not sure why we do thisclass Edge:    def __init__(self, frm, to) -> None:        # the smaller edge is always 'from', while the greater is always 'to'        self.frm, self.to = (frm, to) if frm < to else (to, frm)class TRIEST_base:    # edge sample S (default 100) with M edges    # Assume M >= 6.     def __init__(self, m: int = 7) -> None:        if m < 6:            raise Exception('M is <6')        self.t = 0        self.tau = 0        self.edge_sample = set()        self.m = m        self.counters = {}    # Reservoir sampling.    # If t < m , put it into the stream and we update counter    # If not (e.g. if the memory space /sampling is full), flip a coin and see whether     def sample_edge(self, edge):        def flip_biased_coin() -> bool:            # Random random generates a float between 0-1                    return random.random() <= (self.m / self.t)        # when t < than m, return true all the time        # this means that we put the edges into the sample        # if m = 100, we take the first 100 edges into the sample        # Whenever this is filled, we flip a coin        # With a probability of m / t, e.g. for the 101 edge,         # there will be a 100/101 probability that we remove a random edge and        # insert this new incoming edge.,        # This means that the more data coming, the probability of replacing an element increases        if self.t < self.m:            return True        elif flip_biased_coin():            unlucky_element = random.sample(self.edge_sample, 1)[0]            self.edge_sample.remove(unlucky_element)            self.update_counters('remove', unlucky_element)            return True        # If we the flipping returns false, this function returns false.        # This means that the current edge will not be inserted in the sample and the count will not update        return False    # Calculates the global and local number of triangles (I think global = ALL triangles and local = in our sample)    # Input: incoming edge from stream    def update_counters(self, operation, edge: Edge):        s1 = set()        s2 = set()        # Iterate over all edges in our sample.        # and compare it with the incoming edges from the stream.        for element in self.edge_sample:            # print("element", element)            # print("hej", element.frm, element.to)            if element.frm == edge.frm:  # same value ? add to set.                s1.add(element.to)            #  print('s1', s1)            #  print("hejdå", element.frm, element.to)            #     print("s1, element frm = edge frm ", s1)            if element.to == edge.frm:                s1.add(element.frm)            #  print("s1, element to = edge frm ", s1)            if element.frm == edge.to:                s2.add(element.to)            # print("s2, element frm = edge frm ", s2)            if element.to == edge.to:                s2.add(element.frm)                # print("s2, element to = edge frm ", s2)        # vertex is the overlap between s1 and s2        #         for vertex in (s1 & s2):  # <-- finds intersection between s1 and s2"            print("vertexy", vertex)            if operation == 'add':                self.tau += 1                print(self.tau)                self.counters[vertex] = self.counters.get(vertex, 0) + 1                self.counters[edge.frm] = self.counters.get(edge.frm, 0) + 1                self.counters[edge.to] = self.counters.get(edge.to, 0) + 1            elif operation == 'remove':                self.tau -= 1                self.counters[vertex] = self.counters.get(vertex, 0) - 1                self.counters[edge.frm] = self.counters.get(edge.frm, 0) - 1                self.counters[edge.to] = self.counters.get(edge.to, 0) - 1                if self.counters[vertex] <= 0:                    del self.counters[vertex]                    del self.counters[edge.frm]                    del self.counters[edge.to]        print(self.counters)    def algo_start(self, edge_stream):        #  print(edge_strea)        for edge in edge_stream:            self.t += 1            if self.sample_edge(edge):                # if self.sample_edge():                self.edge_sample.add(edge)                # Keyword add determines that we update the counter                #  print("iter:", self.t)                self.update_counters('add', edge)        est = max([1, (self.t * (self.t - 1) * (self.t - 2)) / (self.m * (self.m - 1) * (self.m - 2))])        return self.tau * estdef read_data(file):    data = set()    curr_dir = os.path.dirname(__file__)    sys.path.append(curr_dir)    with open(curr_dir + '/data/' + file) as f:        for line in f:            #   print(line)            content = line.split()  # from e.g. 2 3 --> ['2', '3']            # print(content)            # get rid of duplicates            if content[0] != content[1]:                e = Edge(content[0], content[1])                print("hi", e)                data.add(Edge(content[0], content[1]))    return datadef main():    data = read_data('dummy_data.txt')    print(data)    # TRIEST base    print('Testing TRIEST base:')    sample_size = 14    print('test_set length:', len(data))    expected = TRIEST_base(sample_size).algo_start(data)    print('Expected value:', expected)    start = time.time()    true = TRIEST_base(len(data)).algo_start(data)    exec_time = time.time() - start    print('True value:', true)    print('Difference:', round(abs(expected - true) / true * 100), '%')    sizes = [300, 600, 900, 1200, 1500, 1800, 2100]    values = []    times = []    true_values = [true for _ in range(len(sizes))]    true_times = [exec_time for _ in range(len(sizes))]    for size in sizes:        start = time.time()        expected = TRIEST_base(size).algo_start(data)        end = time.time()        times.append(end - start)        values.append(round(expected))    plt.title('TRIEST basic')    plt.plot(sizes, values)    # plt.plot(sizes, true_values)    plt.ylabel('Number of triangles')    plt.xticks(sizes)    plt.grid(True)    plt.savefig('base_number_of_triangles.png')    plt.clf()    plt.title('TRIEST basic')    plt.plot(sizes, times)    # plt.plot(sizes, true_times)    plt.ylabel('Time (seconds)')    plt.xticks(sizes)    plt.grid(True)main()