import { useState, useEffect, useContext } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { thunkReadInv } from '../../store/inventory.js';
import { actionReadProduct } from '../../store/product.js';
import { useHistory, useParams } from 'react-router-dom';
import { SweetContext } from '../../context/Context.js';

import './Inv.css'

export default function Inventory() {
  const dispatch = useDispatch();
  const history = useHistory();
  const inventory = useSelector(state => state.inventory);

  const { vendor } = useContext(SweetContext);
  const { cat } = useParams();
  console.log('CATEGORY: ', cat);

  useEffect(() => {
    dispatch(thunkReadInv(cat ? cat : '', vendor));
  }, [cat]);

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

  const instantiateProductStore = (item) => {
    dispatch(actionReadProduct(item));
    return null;
  }

  const toPrice = (floater) => {
    let temp_str = floater.toString();
    let char;
    let count = 0;
    let final_str= ''

    for (let i = temp_str.length - 1; i >= 0; i--) {
      char = temp_str[i];

      if (count === 3) {
        final_str = char + ',' + final_str;
        count = 0;
      } else {
        final_str = char + final_str;
        count++;
      }
    }
    final_str = '$' + final_str + '.00';

    return final_str;
  }

  const toProductPage = (e) => {
    e.preventDefault()
    history.push(`/products/${e.target.id}`);
  }

  if (!inventory) return null;

  return (
    <div id="inv-cont" style={{ width: '80%', height: '100vh', backgroundColor: '#ffffff' }}>
      {inventory.map(item => (
        <button className="inventory-buttons" key={item.id} id={item.id} onClick={(e) => toProductPage(e)}>
        <div className="item-thumbs" id={item.id}>
          {instantiateProductStore(item)}
            <div className="preview-div" id={item.id}>
              <img className="img-preview" src={item.preview} id={item.id}></img>
          </div>
            <div id={item.id} className="item-name">{item.name}</div>
            <div id={item.id} className="item-description">{item.description}</div>
            <div id={item.id} className="price-div">{toPrice(item.price)}</div>
        </div>
      </button>
      ))}
    </div>
  )
}
