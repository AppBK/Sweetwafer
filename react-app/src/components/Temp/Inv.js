import { useState, useEffect, useContext } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { thunkReadInv } from '../../store/inventory.js';
import { actionReadProduct } from '../../store/product.js';
import { useHistory, useParams } from 'react-router-dom';
import { SweetContext } from '../../context/Context.js';

import './Inv.css'

const categories = ['Studio & Recording', 'Live Sound & Lighting', 'Guitars', 'Bass'];
const vendors = {
  'Studio & Recording': ['Dangerous', 'Manley'],
  'Live Sound & Lighting': ['Allen & Heath', 'Obsidian', 'Martin'],
  'Guitars': ['ESP', 'Marshall'],
  'Bass': ['Ernie Ball', 'Ampeg'],
}


export default function Inventory() {
  const dispatch = useDispatch();
  const history = useHistory();
  const inventory = useSelector(state => state.inventory);

  const { vendor, setVendor } = useContext(SweetContext);
  const { cat } = useParams();
  console.log('CATEGORY: ', cat);

  const [downArrow, setDownArrow] = useState(true);


  useEffect(() => {
    dispatch(thunkReadInv(cat ? cat : '', vendor));
  }, [cat, vendor]);

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

  const dropItDown = () => {
    setDownArrow(!downArrow);
  }

  const vendorChange = (e) => {
    e.preventDefault();
    setVendor(e.target.id);
  }


  const toProductPage = (e) => {
    e.preventDefault()
    history.push(`/products/${e.target.id}`);
  }



  if (!inventory) return null;

  let catMap = vendors[cat];

  return (
    <div id="outermost">
      <div id="make-left-cols">
        <div id="refine-search">
          <div id="refined">Refine Your Search</div>
        </div>
        <button id="vendor-drop" onClick={dropItDown}>
          <div id="push-apart">
            <div id="vendor-title">Vendor</div>
            <div id="svg-tamer">
              {downArrow ? (<img src="/svg/gobbled-svgs/arrow-down.svg" style={{ height: '16px', width: '17.60px' }}></img>) : (<img src="/svg/gobbled-svgs/arrow-up.svg" style={{ height: '16px', width: '17.60px' }}></img>)}
            </div>
          </div>
          {!downArrow && (<div id="options-drop">
            <ul id="unordered">
              {catMap.map(categ => (<li id={categ} className="lists" onClick={vendorChange}>{categ}</li>))}
            </ul>
          </div>)}
        </button>
      </div>
      <div id="left-border">
        <div id="current-category"><span className="side-lines-left"></span><div id="cat-title">Shop {vendor ? vendor : cat}</div><span className="side-lines-right"></span></div>
        <div id="inv-cont" style={{ width: 'fit-content', height: 'fit-content', backgroundColor: '#ffffff' }}>
          {inventory.map(item => (
            <div key={item.id}>
              <button className="inventory-buttons" id={item.id} onClick={(e) => toProductPage(e)}>
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
            {/* <div className="spacer"></div> */}
          </div>
          ))}
        </div>
      </div>
    </div>
  )
}
