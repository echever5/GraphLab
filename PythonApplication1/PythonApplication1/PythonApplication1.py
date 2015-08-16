#import graphlab as gl

#vertices = gl.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_vertices.csv')
#edges = gl.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_edges.csv')

#vertices.show()
#edges.show()

#g = gl.SGraph()
#g = g.add_vertices(vertices=vertices, vid_field='name')
#g = g.add_edges(edges=edges, src_field='src', dst_field='dst')
#g.get_vertices()

#pr = gl.pagerank.create(g)


#pr.get('pagerank').topk(column_name='pagerank')

#url = 'http://s3.amazonaws.com/dato-datasets/millionsong/song_data.csv'
#songs = gl.SFrame.read_csv(url)

#songs.show()

#songs['year'].mean()

#songs['num_words'] = songs['title'].apply(lambda x: len(x.split(' ')))
#songs.groupby('artist_name', {'total': graphlab.aggregate.COUNT})


#url = 'http://s3.amazonaws.com/dato-datasets/regression/Housing.csv'
#x = gl.SFrame.read_csv(url)
#m = gl.linear_regression.create(x, target='price')


#from graphlab import SGraph, Vertex, Edge
#g = SGraph()
#verts = [Vertex(0, attr={'breed': 'labrador'}),
#         Vertex(1, attr={'breed': 'labrador'}),
#         Vertex(2, attr={'breed': 'vizsla'})]
#g = g.add_vertices(verts)
#g = g.add_edges(Edge(1, 2))
#print g


#g = SGraph().add_vertices([Vertex(i) for i in range(10)]).add_edges(
#    [Edge(i, i+1) for i in range(9)])


#from graphlab import SFrame
#edge_data = SFrame.read_csv(
#    'http://s3.amazonaws.com/dato-datasets/bond/bond_edges.csv')

#g = SGraph()
#g = g.add_edges(edge_data, src_field='src', dst_field='dst')
#print g

#vertex_data = SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_vertices.csv')

#SFrame.show()

#g = SGraph(vertices=vertex_data, edges=edge_data, vid_field='name',
#           src_field='src', dst_field='dst')

#targets = ['James Bond', 'Moneypenny']
#subgraph = g.get_neighborhood(ids=targets, radius=1, full_subgraph=True)
#subgraph.show(vlabel='id', highlight=['James Bond', 'Moneypenny'], arrows=True)

#from graphlab import SGraph, Vertex, Edge

#g = SGraph()
#verts = [Vertex(0, attr={'breed': 'labrador'}),
#         Vertex(1, attr={'breed': 'labrador'}),
#         Vertex(2, attr={'breed': 'vizsla'})]

#g = g.add_vertices(verts)
#g = g.add_edges(Edge(1, 2))

#print g

from graphlab import SFrame, SGraph
edge_data = SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_edges.csv')
vertex_data = SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_vertices.csv')

g = SGraph(vertices=vertex_data, edges=edge_data, vid_field='name',src_field='src', dst_field='dst')
#print g

g.show()


