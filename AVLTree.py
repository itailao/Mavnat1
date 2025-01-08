#id1:
#name1:
#username1:
#id2:
#name2:
#username2:


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key is not None 

	#connects between self/parent and kid accourding to key
	def connect(self, kid):
                kid.parent = self
                if self.key < kid.key:
                        self.right = kid
                else:
                        self.left = kid
                        
                        
"""
A class implementing an AVL tree.
"""

class AVLTree(object):
	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None
		self.max_node = None
		self.size = 0 
	
	@staticmethod
	def help_search(node,key):
		i = 1
		while (node.is_real_node() and node.key != key):
			if node.key > key:
				node = node.left
			else:
				node = node.right
			i += 1
		return node,i
	
	@staticmethod
	def rotation(node,isright):
		kid = node
		father = node.parent
		grandpa = father.parent
		if (isright):
			tmp = kid.right
			kid.connect(father)
			if tmp:
				father.connect(tmp)
		else:
			tmp = kid.left
			kid.connect(father)
			if tmp:
				father.connect(tmp)
		if grandpa:
			grandpa.connect(kid)
		else:
			kid.parent = None
		return kid

	#starts from kid of suspicious arch,verify insert, returns promCount
def newBalance(self, node):
    father = node.parent
    if father.height - node.height == 1:
        return 0
    isCorrect = False
    PromCount = 0
    while not isCorrect:
        father.height += 1
        PromCount += 1
        if father.parent and (father.parent.height - father.height == 1):
            isCorrect = True
        else:
            if not father.parent:
                break
            father = father.parent
            left_height = father.left.height if father.left else 0
            right_height = father.right.height if father.right else 0
            if abs(left_height - right_height) <= 1:
                father.height = max(left_height, right_height) + 1
                PromCount += 1
                father = father.parent
            else:
                isRightSon = father.key > father.parent.key
                if (not isRightSon and right_height + 2 == father.height) or \
                   (isRightSon and left_height + 2 == father.height):
                    AVLTree.rotation(father, not isRightSon)
                    isCorrect = True
                else:
                    if right_height + 1 == father.height:
                        tmp = father.right
                        AVLTree.rotation(tmp, False)
                    else:
                        tmp = father.left
                        AVLTree.rotation(tmp, True)

                    if father.parent and father.parent.key < father.parent.parent.key:
                        AVLTree.rotation(father.parent, True)
                    else:
                        AVLTree.rotation(father.parent, False)

                    isCorrect = True

    return PromCount

	
			
	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
def search(self, key):
	tup = AVLTree.help_search(self.root,key)
	if tup[0].is_real_node == False:
		return None,-1
	return tup
	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
def finger_search(self, key):
	node = self.max_node
	i = 1
	while (node.key >= key and node.parent.key >= key):
		if (node.key == key):
			return node,i
		node = node.parent
		i += 1
		tmp = AVLTree.help_search(node.left,key)
		return tmp[0],tmp[1] + i -1



	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	
@staticmethod
def help_insert(key, val, virt):
	virt.height = 0
	rightVirt = AVLNode(None,None)
	leftVirt = AVLNode(None,None)
	virt.right = rightVirt
	virt.left = leftVirt
	virt.key = key
	virt.val = val
	return virt

def insert(self,key,value):
	node = node(key,value)
	if self.root == None:
		self.root = node
		self.max_node = node
		return node, 1, 0
	tup = self.help_search(self.root,node)
	virt = tup[0]
	e = tup[1]
	retNode = self.help_insert(key, value ,virt)
	self.size+=1
	if value> self.max_node.value:
		self.max_node = virt
	Prom = newBalance(retNode)
	return retNode,e,Prom


	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
def finger_insert(self, key, val):
	tup = self.finger_search(key)
	virt = tup[0]
	e = tup[1]
	retNode = self.help_insert(key, val ,virt)
	self.size+=1
	if val > self.max_node.value:
		self.max_value = val
	Prom = newBalance(retNode)
	return retNode,tup[1],Prom


	


	"""deletes node from the dictionary
	#לאתחל מקסימום
	#להקטין גודל
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""

	def delete(self, node):
		return	

	
	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
def join(self, tree2, key, val):
    glueNode = AVLNode(key, val)
    self.size+=tree2.size+1
	minTree = self
	maxTree = tree2
	if glueNode.key<maxTree.get_root().key:
        minTree = tree2
        maxTree = self
    if maxTree.get_root().height < minTree.get_root().height:
        self = minTree
        c = minTree.get_root()
        while c.height > maxTree.get_root().height:
        	c = c.right
        c.parent.connect(glueNode)
        glueNode.connect(c)
        glueNode.connect(maxTree.get_root())
    else:
        self = maxTree
        c = maxTree.get_root()
        while c.height > minTree.get_root().height:
            c = c.left
        c.parent.connect(glueNode)
        glueNode.connect(c)
        glueNode.connect(minTree.get_root())
    glueNode.heigth = c.height+1
    newBalance(glueNode.height)


	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
def split(self, node):
		t1 = AVLTree()
		t2 = AVLTree()
		x = node
		if x.left.is_real_node():
			t1.root = x.left
			x.left.parent = None
		if x.right.is_real_node():
			t2.root = x.right
			x.right.parent = None
		while x.parent!=None:
			if x.parent.key<x.key:
				x.parent.left.parent = None
				tmp = AVLTree()
				tmp.root = x.parent.left
				tmp.insert(x.key, x.value)
				t1.join(tmp)
			else:
				x.parent.right.parent = None
				tmp = AVLTree()
				tmp.root = x.parent.right
				tmp.insert(x.parent.key, x.parent.value)
				t2.join(tmp)
		return(t1, t2)

		

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
def avl_to_array(self):
	array = []
	def ordered_array(node):
		if node:
			ordered_array(node.left)
			array.append(node.key)
			ordered_array(node.right)
	ordered_array(self.root)
	return array
	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		return self.max_node

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.SI


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root

