import streamlit as st
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

# ------------------ Titre du tableau de bord ------------------
st.set_page_config(page_title="Dashboard eCommerce", layout="wide")
st.title("📊 Tableau de bord - Analyse eCommerce")

# ------------------ Section KPI : Chiffre d'affaires total ------------------
total_sales = db.orders.aggregate([
    {"$group": {"_id": None, "total": {"$sum": "$Sales"}}}
])
total_sales = list(total_sales)[0]["total"]
st.metric(label="💰 Revenu total", value=f"{total_sales:,.2f} €")

# ------------------ Section Produits les plus populaires ------------------
st.header("📦 Produits les plus populaires")

# Récupération des produits les plus commandés
popular_products = db.orders.aggregate([
    {"$match": {"Product ID": {"$ne": None}}},
    {"$group": {"_id": "$Product ID", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 5}
])

products_data = [{"Product ID": p["_id"], "Commandes": p["count"]} for p in popular_products]
products_df = pd.DataFrame(products_data)

# Affichage des résultats sous forme de tableau et graphique
col1, col2 = st.columns(2)
with col1:
    st.table(products_df)
with col2:
    st.bar_chart(products_df.set_index("Product ID"))

# ------------------ Section Clients les plus actifs ------------------
st.header("👤 Clients les plus actifs")

# Récupération des clients ayant passé le plus de commandes
popular_customers = db.orders.aggregate([
    {"$group": {"_id": "$Customer ID", "total_orders": {"$sum": 1}}},
    {"$sort": {"total_orders": -1}},
    {"$limit": 5}
])

customers_data = [{"Client ID": c["_id"], "Commandes": c["total_orders"]} for c in popular_customers]
customers_df = pd.DataFrame(customers_data)

# Affichage des résultats sous forme de tableau et graphique
col1, col2 = st.columns(2)
with col1:
    st.table(customers_df)
with col2:
    st.bar_chart(customers_df.set_index("Client ID"))

# ------------------ Section Catégories les plus populaires ------------------
st.header("📂 Catégories les plus populaires")

# Récupération des catégories les plus représentées
popular_categories = db.products.aggregate([
    {"$group": {"_id": "$Category", "total_products": {"$sum": 1}}},
    {"$sort": {"total_products": -1}}
])

categories_data = [{"Catégorie": c["_id"], "Produits": c["total_products"]} for c in popular_categories]
categories_df = pd.DataFrame(categories_data)

# Affichage des résultats sous forme de tableau et graphique
col1, col2 = st.columns(2)
with col1:
    st.table(categories_df)
with col2:
    st.bar_chart(categories_df.set_index("Catégorie"))

# ------------------ Section Filtres Interactifs ------------------
st.header("🔍 Filtres interactifs")

# Filtre par catégorie
categories_list = categories_df["Catégorie"].tolist()
selected_category = st.selectbox("Sélectionnez une catégorie :", categories_list)

filtered_products = db.products.find({"Category": selected_category})
filtered_products_data = [{"Product Name": p["Product Name"], "Sub-Category": p["Sub-Category"]} for p in filtered_products]
filtered_products_df = pd.DataFrame(filtered_products_data)

st.write(f"Produits dans la catégorie **{selected_category}**")
st.table(filtered_products_df)

