import matplotlib.pyplot as plt 
Products = ['Pen', 'Pencil', 'Eraser', 'Sharpener', 'Ruler'] 
Prices = [20, 7, 2, 4, 10] 
plt.scatter(Products, Prices) 
plt.xlabel('Products') 
plt.ylabel('Prices') 
plt.title('Sales Data Scatter Plot') 
plt.show()


import matplotlib.pyplot as plt 
Subjects = ['ML', 'DA', 'DM', 'AI'] 
Marks = [55, 40, 36, 45] 
plt.bar(Subjects, Marks) 
plt.xlabel('Subjects') 
plt.ylabel('Marks') 
plt.title('Semester Performance Bar Chart') 
plt.show()
