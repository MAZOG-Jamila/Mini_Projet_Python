import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('ecommerce_dataset_updated.csv')

# Affichage les premières lignes
print(df.head())

# affichage toutes les infos du DataFrame
print(df.info())

# Transformation du colonne 'Purchase_Date' correctement
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], dayfirst=True)

# Afficher tous les achats par carte de crédit
print(df[df['Payment_Method'] == 'Credit Card'])

# Voir les achats faits en 2025
print(df[df['Purchase_Date'].dt.year == 2025])

# Produits avec un discount > 30%
print(df[df['Discount (%)'] > 30])

# Statistiques rapides sur les prix
print(df['Price (Rs.)'].describe())


# Fonction pour calculer la moyenne d'une colonne
def calculer_moyenne(df, colonne):
    return df[colonne].mean()

# Fonction pour calculer la médiane d'une colonne
def calculer_mediane(df, colonne):
    return df[colonne].median()

# Fonction pour calculer l'écart-type d'une colonne
def calculer_ecart_type(df, colonne):
    return df[colonne].std()


# Convertir la date proprement
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], dayfirst=True)

# Calculs
moyenne_prix = calculer_moyenne(df, 'Price (Rs.)')
mediane_prix = calculer_mediane(df, 'Price (Rs.)')
ecart_type_prix = calculer_ecart_type(df, 'Price (Rs.)')

print(f"Moyenne des prix : {moyenne_prix:.2f} Rs")

print(f"Médiane des prix : {mediane_prix:.2f} Rs")

print(f"Écart-type des prix : {ecart_type_prix:.2f} Rs")

# Ajouter une colonne pour le montant économisé
df['Savings (Rs.)'] = df['Price (Rs.)'] * df['Discount (%)'] / 100
print(df.head())

# Visualiser les catégories les plus achetées
category_counts = df['Category'].value_counts()

plt.figure(figsize=(8,5))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Nombre de produits achetés par catégorie')
plt.xlabel('Catégorie')
plt.ylabel('Nombre d\'achats')
plt.xticks(rotation=45)
plt.show()

# Visualiser les méthodes de paiement
payment_counts = df['Payment_Method'].value_counts()

plt.figure(figsize=(6,4))
payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Répartition des méthodes de paiement')
plt.ylabel('')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Purchase_Date'], df['Price (Rs.)'], marker='o', linestyle='-', color='purple')
plt.title('Évolution des Prix dans le Temps')
plt.xlabel('Date d\'Achat')
plt.ylabel('Prix (Rs.)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df['Price (Rs.)'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution des Prix')
plt.xlabel('Prix (Rs.)')
plt.ylabel('Nombre de Produits')
plt.grid(True)
plt.show()

categorie_prix_moyen = df.groupby('Category')['Price (Rs.)'].mean().sort_values()

plt.figure(figsize=(10, 6))
categorie_prix_moyen.plot(kind='barh', color='lightgreen')
plt.title('Prix Moyen par Catégorie')
plt.xlabel('Prix Moyen (Rs.)')
plt.ylabel('Catégorie')
plt.grid(axis='x')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Discount (%)'], df['Final_Price(Rs.)'], alpha=0.7, color='red')
plt.title('Discount vs Final Price')
plt.xlabel('Discount (%)')
plt.ylabel('Final Price (Rs.)')
plt.grid(True)
plt.show()