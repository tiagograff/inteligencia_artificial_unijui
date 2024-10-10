# Importar as bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

data = {
    'peso': [8.0, 8.2, 7.8, 4.5, 6.0, 7.0, 9.0, 9.2],
    'comprimento': [20, 25, 30, 22, 28, 30, 90, 88],
    'pelagem': [0, 0, 0, 1, 1, 1, 3, 3],
    'raça': [0, 0, 0, 1, 1, 1, 2, 2]
}

df = pd.DataFrame(data)

# separar em caracteristicas e raças
X = df[['peso', 'comprimento', 'pelagem']]
y = df['raça']

# função que dividi um conjunto de dados, em um subconjunto. para avaliar o desempenho
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# cria a árvore de decisão
clf = DecisionTreeClassifier()
# função para treinamento
clf.fit(X_train, y_train)
# função para previsões
y_pred = clf.predict(X_test)
# função para calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f'acurácia: {accuracy * 100:.2f}%')
# exibindo a árvore de decisão
plt.figure(figsize=(8, 6))
tree.plot_tree(clf, feature_names=['peso', 'comprimento', 'pelagem'], class_names=[
               'siamês', 'chartreux', 'siberiano'], filled=True, rounded=True, fontsize=10)
plt.show()

# exemplo
gato = np.array([[10.0, 30, 3]])
predicao = clf.predict(gato)
racas = ['siamês', 'chartreux', 'siberiano']
print(f'a raça prevista para o gato é: {racas[predicao[0]]}')
