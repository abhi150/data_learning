from sklearn.tree import DecisionTreeClassifier

# Make a decision tree and train

tree = DecisionTreeClassifier(random_state=RSEED)
tree.fit(X, y)