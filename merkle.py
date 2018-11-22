# Jinglan Wang

from hashlib import sha256

values = [str(i) for i in range(8)]
leaves = [hash(value) for value in values]
tree = {}
for i in range(len(leaves)):
	tree[leaves[i]] = values[i]

# Make a merkle tree
def merkle(leaves, tree):
	parents = []
	for i in range(0, len(leaves), 2):
		parent_hash = hash(str(leaves[i]) + str(leaves[i+1]))
		parents.append(parent_hash)
		tree[str(parent_hash)] = str(leaves[i]) + str(leaves[i+1])
	# if root node, return two children 
	if len(leaves) == 2:
		return parents
	else:
		return merkle(parents, tree)

# print(merkle(leaves, tree))
merkle(leaves, tree)
# print(tree)
