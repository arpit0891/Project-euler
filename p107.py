# 
# Solution to Project Euler problem 107
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 


# 
# This problem involves constructing a minimum spanning tree of the graph.
# 0. First we sum all the undirected edge weights of the original graph, which are given in the form of an adjacency matrix.
# 1. Next we compute a minimum spanning tree from scratch, taking note of the total weight of the spanning tree.
# 2. Finally we subtract the spanning tree weight from the original total weight to get the final answer.
# 
# Because the graph is small, the minimum spanning tree algorithm chosen is slower but simpler:
# 0. We start with one node that forms the connected set.
# 1. In each loop iteration, we look at all the nodes that are not in
#    the connected set but are adjacent to some node in the connected set.
# 2. Among these unexplored nodes, we pick the one that has the shortest edge to a connected node.
# 3. Then we mark this new node as connected and repeat the loop.
# This procedure can be thought of as a pessimized version of Prim's algorithm -
# with the same kind of frontier exploration, but without the priority queue.
# 
def compute():
	# Number of nodes/vertices in the matrix
	numnodes = len(WEIGHTS)
	
	# Check that the matrix is well-behaved
	if any((len(row) != numnodes) for row in WEIGHTS):
		raise AssertionError("Matrix not square")
	if any(WEIGHTS[i][i] != -1 for i in range(numnodes)):
		raise AssertionError("Self edge")
	if any(WEIGHTS[i][j] != WEIGHTS[j][i] for i in range(numnodes) for j in range(numnodes)):
		raise AssertionError("Matrix not symmetric")
	
	# Add up all undirected edge weights
	oldweight = sum(WEIGHTS[i][j]
		for i in range(numnodes)
		for j in range(i + 1, numnodes)
		if WEIGHTS[i][j] != -1)
	
	# Inefficient minimum spanning tree algorithm
	connected = set([0])  # Node indexes
	newweight = 0  # Total of edge weights used in spanning tree
	for _ in range(numnodes - 1):  # One new node is connected per iteration
		lowestweight, newnode = min((WEIGHTS[j][k], k)
			for j in connected
			for k in range(numnodes)
			if k not in connected and WEIGHTS[j][k] != -1)
		connected.add(newnode)
		newweight += lowestweight
	
	ans = oldweight - newweight
	return str(ans)


WEIGHTS = (
	(-1,-1,-1,427,668,495,377,678,-1,177,-1,-1,870,-1,869,624,300,609,131,-1,251,-1,-1,-1,856,221,514,-1,591,762,182,56,-1,884,412,273,636,-1,-1,774),
	(-1,-1,262,-1,-1,508,472,799,-1,956,578,363,940,143,-1,162,122,910,-1,729,802,941,922,573,531,539,667,607,-1,920,-1,-1,315,649,937,-1,185,102,636,289),
	(-1,262,-1,-1,926,-1,958,158,647,47,621,264,81,-1,402,813,649,386,252,391,264,637,349,-1,-1,-1,108,-1,727,225,578,699,-1,898,294,-1,575,168,432,833),
	(427,-1,-1,-1,366,-1,-1,635,-1,32,962,468,893,854,718,427,448,916,258,-1,760,909,529,311,404,-1,-1,588,680,875,-1,615,-1,409,758,221,-1,-1,76,257),
	(668,-1,926,366,-1,-1,-1,250,268,-1,503,944,-1,677,-1,727,793,457,981,191,-1,-1,-1,351,969,925,987,328,282,589,-1,873,477,-1,-1,19,450,-1,-1,-1),
	(495,508,-1,-1,-1,-1,-1,765,711,819,305,302,926,-1,-1,582,-1,861,-1,683,293,-1,-1,66,-1,27,-1,-1,290,-1,786,-1,554,817,33,-1,54,506,386,381),
	(377,472,958,-1,-1,-1,-1,-1,-1,120,42,-1,134,219,457,639,538,374,-1,-1,-1,966,-1,-1,-1,-1,-1,449,120,797,358,232,550,-1,305,997,662,744,686,239),
	(678,799,158,635,250,765,-1,-1,-1,35,-1,106,385,652,160,-1,890,812,605,953,-1,-1,-1,79,-1,712,613,312,452,-1,978,900,-1,901,-1,-1,225,533,770,722),
	(-1,-1,647,-1,268,711,-1,-1,-1,283,-1,172,-1,663,236,36,403,286,986,-1,-1,810,761,574,53,793,-1,-1,777,330,936,883,286,-1,174,-1,-1,-1,828,711),
	(177,956,47,32,-1,819,120,35,283,-1,50,-1,565,36,767,684,344,489,565,-1,-1,103,810,463,733,665,494,644,863,25,385,-1,342,470,-1,-1,-1,730,582,468),
	(-1,578,621,962,503,305,42,-1,-1,50,-1,155,519,-1,-1,256,990,801,154,53,474,650,402,-1,-1,-1,966,-1,-1,406,989,772,932,7,-1,823,391,-1,-1,933),
	(-1,363,264,468,944,302,-1,106,172,-1,155,-1,-1,-1,380,438,-1,41,266,-1,-1,104,867,609,-1,270,861,-1,-1,165,-1,675,250,686,995,366,191,-1,433,-1),
	(870,940,81,893,-1,926,134,385,-1,565,519,-1,-1,313,851,-1,-1,-1,248,220,-1,826,359,829,-1,234,198,145,409,68,359,-1,814,218,186,-1,-1,929,203,-1),
	(-1,143,-1,854,677,-1,219,652,663,36,-1,-1,313,-1,132,-1,433,598,-1,-1,168,870,-1,-1,-1,128,437,-1,383,364,966,227,-1,-1,807,993,-1,-1,526,17),
	(869,-1,402,718,-1,-1,457,160,236,767,-1,380,851,132,-1,-1,596,903,613,730,-1,261,-1,142,379,885,89,-1,848,258,112,-1,900,-1,-1,818,639,268,600,-1),
	(624,162,813,427,727,582,639,-1,36,684,256,438,-1,-1,-1,-1,539,379,664,561,542,-1,999,585,-1,-1,321,398,-1,-1,950,68,193,-1,697,-1,390,588,848,-1),
	(300,122,649,448,793,-1,538,890,403,344,990,-1,-1,433,596,539,-1,-1,73,-1,318,-1,-1,500,-1,968,-1,291,-1,-1,765,196,504,757,-1,542,-1,395,227,148),
	(609,910,386,916,457,861,374,812,286,489,801,41,-1,598,903,379,-1,-1,-1,946,136,399,-1,941,707,156,757,258,251,-1,807,-1,-1,-1,461,501,-1,-1,616,-1),
	(131,-1,252,258,981,-1,-1,605,986,565,154,266,248,-1,613,664,73,-1,-1,686,-1,-1,575,627,817,282,-1,698,398,222,-1,649,-1,-1,-1,-1,-1,654,-1,-1),
	(-1,729,391,-1,191,683,-1,953,-1,-1,53,-1,220,-1,730,561,-1,946,686,-1,-1,389,729,553,304,703,455,857,260,-1,991,182,351,477,867,-1,-1,889,217,853),
	(251,802,264,760,-1,293,-1,-1,-1,-1,474,-1,-1,168,-1,542,318,136,-1,-1,-1,-1,392,-1,-1,-1,267,407,27,651,80,927,-1,974,977,-1,-1,457,117,-1),
	(-1,941,637,909,-1,-1,966,-1,810,103,650,104,826,870,261,-1,-1,399,-1,389,-1,-1,-1,202,-1,-1,-1,-1,867,140,403,962,785,-1,511,-1,1,-1,707,-1),
	(-1,922,349,529,-1,-1,-1,-1,761,810,402,867,359,-1,-1,999,-1,-1,575,729,392,-1,-1,388,939,-1,959,-1,83,463,361,-1,-1,512,931,-1,224,690,369,-1),
	(-1,573,-1,311,351,66,-1,79,574,463,-1,609,829,-1,142,585,500,941,627,553,-1,202,388,-1,164,829,-1,620,523,639,936,-1,-1,490,-1,695,-1,505,109,-1),
	(856,531,-1,404,969,-1,-1,-1,53,733,-1,-1,-1,-1,379,-1,-1,707,817,304,-1,-1,939,164,-1,-1,616,716,728,-1,889,349,-1,963,150,447,-1,292,586,264),
	(221,539,-1,-1,925,27,-1,712,793,665,-1,270,234,128,885,-1,968,156,282,703,-1,-1,-1,829,-1,-1,-1,822,-1,-1,-1,736,576,-1,697,946,443,-1,205,194),
	(514,667,108,-1,987,-1,-1,613,-1,494,966,861,198,437,89,321,-1,757,-1,455,267,-1,959,-1,616,-1,-1,-1,349,156,339,-1,102,790,359,-1,439,938,809,260),
	(-1,607,-1,588,328,-1,449,312,-1,644,-1,-1,145,-1,-1,398,291,258,698,857,407,-1,-1,620,716,822,-1,-1,293,486,943,-1,779,-1,6,880,116,775,-1,947),
	(591,-1,727,680,282,290,120,452,777,863,-1,-1,409,383,848,-1,-1,251,398,260,27,867,83,523,728,-1,349,293,-1,212,684,505,341,384,9,992,507,48,-1,-1),
	(762,920,225,875,589,-1,797,-1,330,25,406,165,68,364,258,-1,-1,-1,222,-1,651,140,463,639,-1,-1,156,486,212,-1,-1,349,723,-1,-1,186,-1,36,240,752),
	(182,-1,578,-1,-1,786,358,978,936,385,989,-1,359,966,112,950,765,807,-1,991,80,403,361,936,889,-1,339,943,684,-1,-1,965,302,676,725,-1,327,134,-1,147),
	(56,-1,699,615,873,-1,232,900,883,-1,772,675,-1,227,-1,68,196,-1,649,182,927,962,-1,-1,349,736,-1,-1,505,349,965,-1,474,178,833,-1,-1,555,853,-1),
	(-1,315,-1,-1,477,554,550,-1,286,342,932,250,814,-1,900,193,504,-1,-1,351,-1,785,-1,-1,-1,576,102,779,341,723,302,474,-1,689,-1,-1,-1,451,-1,-1),
	(884,649,898,409,-1,817,-1,901,-1,470,7,686,218,-1,-1,-1,757,-1,-1,477,974,-1,512,490,963,-1,790,-1,384,-1,676,178,689,-1,245,596,445,-1,-1,343),
	(412,937,294,758,-1,33,305,-1,174,-1,-1,995,186,807,-1,697,-1,461,-1,867,977,511,931,-1,150,697,359,6,9,-1,725,833,-1,245,-1,949,-1,270,-1,112),
	(273,-1,-1,221,19,-1,997,-1,-1,-1,823,366,-1,993,818,-1,542,501,-1,-1,-1,-1,-1,695,447,946,-1,880,992,186,-1,-1,-1,596,949,-1,91,-1,768,273),
	(636,185,575,-1,450,54,662,225,-1,-1,391,191,-1,-1,639,390,-1,-1,-1,-1,-1,1,224,-1,-1,443,439,116,507,-1,327,-1,-1,445,-1,91,-1,248,-1,344),
	(-1,102,168,-1,-1,506,744,533,-1,730,-1,-1,929,-1,268,588,395,-1,654,889,457,-1,690,505,292,-1,938,775,48,36,134,555,451,-1,270,-1,248,-1,371,680),
	(-1,636,432,76,-1,386,686,770,828,582,-1,433,203,526,600,848,227,616,-1,217,117,707,369,109,586,205,809,-1,-1,240,-1,853,-1,-1,-1,768,-1,371,-1,540),
	(774,289,833,257,-1,381,239,722,711,468,933,-1,-1,17,-1,-1,148,-1,-1,853,-1,-1,-1,-1,264,194,260,947,-1,752,147,-1,-1,343,112,273,344,680,540,-1),
)


if __name__ == "__main__":
	print(compute())
