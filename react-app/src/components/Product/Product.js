import { thunkReadProduct } from "../../store/product"
import { useSelector, useDispatch } from "react-redux"
import { useParams } from "react-router-dom"
import { useState, useEffect } from "react";

export default function Product() {
  useEffect(() => {
    dispatch(thunkReadProduct(id))
  }, [])

  const { id } = useParams();
  const dispatch = useDispatch();
  const product = useSelector(state => state.products[id]);


  if (!product) return null;

  return (
    <div>
      {product.name}
    </div>
  )
}
