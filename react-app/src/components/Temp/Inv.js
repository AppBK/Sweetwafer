import { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { thunkReadInv } from '../../store/inventory.js';

import './Inv.js'

export default function Inventory() {
  const dispatch = useDispatch();
  const inventory = useSelector(state => state.inventory);

  useEffect(() => {
    dispatch(thunkReadInv());
  }, []);

  const len = (iter) => {
    let count = 0;
    if (!iter) {
      return 0;
    }
    else {
      for (let i = 0; i < iter.length; i++) {
        count++;
      }
    }
    return count;
  }

  if (!inventory) return null;

  return (
    <div id="inv-cont" style={{ width: '100vw', height: '100vh', backgroundColor: '#d5ebf5' }}>
      {inventory.map(item => (
        <div className="item-thumbs" key={item.id}>
          {len(item.product_images) === 0 ? null : <img className="thumb-one" src={item.product_images[0].url}></img>}
        </div>
      ))}
    </div>
  )
}
