from app.modules.products.schema.product_schema import ProductDB, ProductSchema
from fastapi import APIRouter, HTTPException, Path
from typing import List 
from datetime import datetime as dt
router = APIRouter()