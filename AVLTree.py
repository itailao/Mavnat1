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
		if self.key == None:
			return False
		return True

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
		hasGrandpa = True
		if father.parent == None:
			hasGrandpa = False
		if (isright):
			tmp = kid.right
			kid.right = father
			father.left = tmp
			tmp.parent = father
		else:
			tmp = kid.left
			kid.left = father
			father.right = tmp
			tmp.parent = father
		if hasGrandpa and father.parent.left.key == father.key:
			father.parent.left = kid
			kid.parent = father.parent
		if hasGrandpa and father.parent.right.key == father.key:
			father.parent.right = kid
			kid.parent = father.parent
		father.parent = kid	
		return kid
	#starts from kid of suspicious arch,verify insert 
	def newBalance(self,node):
		isCool = False
		while isCool != True:
			if node.parent.height - node.height

					
	
			
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
			if (node.key = key):
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
	#לאתחל מקסימום
	#לאתחל גודל
	def help_insert(self, node, virt):
		node.height = 0
		self.size += 1
		node.right = AVLNode(None,None)
		node.left = AVLNode(None,None)
		father = virt.parent
		node.parent = father
		if father.right == virt:
			father.right = node
		else:
			father.left = node
		PromCount = 0
		if self.max_node.key < node.key:
			self.max_node = node 
		if father.height == 1:
			return node,0
		isCorrect = False
		while isCorrect == False:
			father.height += 1 
			PromCount += 1 
			if(father.parent.height - father.height == 1):
				isCorrect = True
			else:
				father = father.parent
				if (father.height - father.left.height + father.height - father.right.height == 1):
					father.height += 1
					PromCount += 1
					father = father.parent
				else:
					isRightSon = True
					if father.key < father.parent.key:
						isRightSon = False
					if (isRightSon == False and father.right.height + 2 == father.height) or (isRightSon == True and father.left.height + 2 == father.height):
						AVLTree.rotation(father,not isRightSon)
						isCorrect = True
					else:
						if father.right.height + 1 == father.height:
							tmp = father.right
							AVLTree.roation(tmp,False)
						else:
							tmp = father.left
							AVLTree.rotation(tmp,True)
					if father.parent.key < father.parent.parent.key:
						AVLTree.rotation(father.parent,True)
					else:
						AVLTree.rotation(father.parent,False)
					isCorrect = True
		return node,PromCount

	def insert(self,key,value):
		node = node(key,value)
		tup = self.help_search(self.root,node)
		virt = tup[0]
		e = tup[1]
		tup2 = self.help_insert(node,virt)
		retNode = tup2[0]
		Prom = tup2[1]
		return retNode,e,Prom

		

		/עצרנו בשקופית 22 במצגת 4 בקייס מספר שתיים 
					

		return None, -1, -1


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
		return None, -1, -1


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
		return


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
		return None, None

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


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
