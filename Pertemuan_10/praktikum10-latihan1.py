
# alur fungsi insert ------
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        
#============================================
# Latihan 2 : traversal inorder
# ===========================================

# alur fungsi inorder------
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
print("Hasil Inorder: ")
inorder(root)

#============================================
# Latihan 3 : search di BST
# ===========================================

def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    elif key < root.data:
        return search(root.left, key)
    
    else:
        return search(root.right, key)
    
# uji pencarian
key = 100

if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")