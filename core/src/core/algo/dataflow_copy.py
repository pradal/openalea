# -*- python -*-
# -*- coding: latin-1 -*-
#
#       GraphCopy : openalea core package
#
#       Copyright or � or Copr. 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Jerome Chopard <jerome.chopard@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       VPlants WebSite : http://openalea.gforge.inria.fr
#

__doc__="""
This module provide an algorithm to create a factory from an instance of a dataflow
"""

__license__= "Cecill-C"
__revision__=" $Id: graph.py 116 2007-02-07 17:44:59Z tyvokka $ "

def structural_copy (dataflow_pattern, dataflow_copy) :
	"""
	make a copy of dataflow_pattern into dataflow_copy
	copy only structural informations and not informations
	related to vertices like actors
	"""
	dfp=dataflow_pattern
	dfc=dataflow_copy
	dfc.clear()
	#copie des vertices
	for vid in dfp.vertices() :
		dum=dfc.add_vertex(vid)
		for pid in dfp.out_ports(vid) :
			dum=dfc.add_out_port(vid,dfp.port(pid).local_pid,pid)
			dfc.set_capacity(pid,dfp.capacity(pid))
		for pid in dfp.in_ports(vid) :
			dum=dfc.add_in_port(vid,dfp.port(pid).local_pid,pid)
			dfc.set_capacity(pid,dfp.capacity(pid))
	#copie des liens
	for eid in dfp.edges() :
		dum=dfc.connect(dfp.source_port(eid),dfp.target_port(eid),eid)
