from fastapi import FastAPI
from pymongo import MongoClient
from typing import List, Optional

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

@app.get("/products/popular")
async def get_popular_products(limit: int = 5):
    """
    Récupérer les produits les plus populaires.
    Paramètre `limit` pour contrôler le nombre de produits.
    """
    popular_products = db.orders.aggregate([
        {"$match": {"Product ID": {"$ne": None}}},
        {"$group": {"_id": "$Product ID", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": limit}
    ])
    products = [{"Product ID": p["_id"], "Commandes": p["count"]} for p in popular_products]
    return {"popular_products": products}

@app.get("/customers/active")
async def get_active_customers(limit: int = 5):
    """
    Récupérer les clients les plus actifs.
    Paramètre `limit` pour contrôler le nombre de clients.
    """
    active_customers = db.orders.aggregate([
        {"$group": {"_id": "$Customer ID", "total_orders": {"$sum": 1}}},
        {"$sort": {"total_orders": -1}},
        {"$limit": limit}
    ])
    customers = [{"Client ID": c["_id"], "Commandes": c["total_orders"]} for c in active_customers]
    return {"active_customers": customers}

@app.get("/categories/popular")
async def get_popular_categories(limit: int = 5):
    """
    Récupérer les catégories les plus populaires.
    Paramètre `limit` pour contrôler le nombre de catégories.
    """
    popular_categories = db.products.aggregate([
        {"$group": {"_id": "$Category", "total_products": {"$sum": 1}}},
        {"$sort": {"total_products": -1}},
        {"$limit": limit}
    ])
    categories = [{"Catégorie": c["_id"], "Produits": c["total_products"]} for c in popular_categories]
    return {"popular_categories": categories}
