from pyld import jsonld
from rdflib import ConjunctiveGraph

def normalize(file_ttl):
    print("parsing")

    g = ConjunctiveGraph()
    g.get_context("http://example.org/graph").parse(file_ttl)

    nq = g.serialize(format="nquads")
    ld = jsonld.from_rdf(nq)
    print("normalizing")
    ldn = jsonld.normalize(ld)["http://example.org/graph"]
    # print(ldn)


# very quick
file1 = "perf_test1.ttl"
normalize(file1)

print()

# hangs (1 extra triple compared to perf_test1.ttl)
file2 = "perf_test2.ttl"
normalize(file2)