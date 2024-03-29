import { useContext, useEffect, useState } from 'react'
import { SweetContext } from '../../context/Context'
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import './Cart.css'
import { thunkDeleteSingle, thunkClearCart, thunkUpdateCart } from '../../store/cart';

export default function Cart() {
  const { numInCart, setNumInCart } = useContext(SweetContext);
  const cart = useSelector(state => state.cart);
  const dispatch = useDispatch();
  const history = useHistory();

  useEffect(() => {
    let sum = 0;
    cart.forEach(element => {
      sum += element.quantity;
    });
    setNumInCart(sum);
  }, [numInCart])

  const toPriceCart = (floater) => {
    if (!floater) return null;
    let temp_str = floater.toString();
    let char;
    let count = 0;
    let final_str = ''

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

  const clearCart = () => {
    dispatch(thunkClearCart());
  }

  const removeItem = (e) => {
    e.preventDefault();

    let temp = JSON.parse(e.target.id);
    dispatch(thunkDeleteSingle(temp[0]));
    setNumInCart(numInCart - temp[1]);
  }

  const updateQty = async (e) => {
    e.preventDefault();
    const offsetY = e.nativeEvent.offsetY;
    const offsetX = e.nativeEvent.offsetX;

    if (offsetX <= 40) return null;



    if (offsetY < 10) {
      await dispatch(thunkUpdateCart(e.target.id, 1));
      setNumInCart(cart.length + 1)
    } else {
      await dispatch(thunkUpdateCart(e.target.id, -1));
      setNumInCart(numInCart - 1)
    }
  }

  let lessThanTwo;
  if (cart.length < 2) {
    lessThanTwo = true;
  }

  const checkoutCart = async () => {
    history.push('/checkedout');
    setTimeout(history.push, 2000, '/');
    await dispatch(thunkClearCart());
  }



  let isEmpty;
  if (numInCart === 0) isEmpty = true;

  return (
    <>
    {isEmpty && (<div id="cart-page">
      <div id="top-o-page">
        <div id="cart-empty-flex">
          <div id="guitar-img-cont">
            <img id="guitar-img" src="/png/blue-guitar.png" style={{width: '404px', height: '270px'}}></img>
          </div>
          <div id="margin-empty">
            <div id="empty-cart">Your Cart Is Empty</div>
            <div id="gear-ideas">There's no gear here! Need some ideas?</div>
          </div>
        </div>
      </div>
      <div id="spacer"></div>
    </div>)}
    {!isEmpty && (
      <div id="cart-full-outer">
        <div id="cart-jitai">
          <div id="cart-header">
            <div id="cart-icon"><img id="icon-img" src="/svg/cart-filled.svg"></img></div>
            <div id="cart-title">Shopping Cart</div>
          </div>
          <div id="col-bar">
            <div>PRODUCT</div>
            <div id="grey-bar-right">
              <div>QTY.</div>
              <div>PRICE</div>
            </div>
          </div>
          {cart.map((item, idx) => (
            <div key={item.item_id} className="item-div">
              <div className="item-thumb" style={{ backgroundImage: `url(${item.preview})`}}></div>
              <div className="mid-div">
                <div className="item-link">{item.name}</div>
                <div className="description">{item.description}</div>
              </div>
              <div className="far-div">
                <div className="qty">
                  <input id={item.item_id} className="qty-input" type="number" min="1" value={item.quantity} placeholder={item.quantity} onClick={(e) => updateQty(e)}></input>
                  <div id={JSON.stringify([item.id, item.quantity])} className="remove-item" onClick={(e) => removeItem(e)} >Remove</div>
                </div>
                <div className="price-div">
                  <div className="price">{toPriceCart(item.price * item.quantity)}</div>
                </div>
              </div>
            </div>
          ))}
          <div id="cart-bottom-buttons">
            <button id="clear" className="cart-buttons" onClick={clearCart}>Clear Cart</button>
              <button className="cart-buttons" onClick={checkoutCart}>Checkout</button>
          </div>
        </div>
        {lessThanTwo && (<div id="spacer"></div>)}
        <div id="doshite-sweet">
            <div id="why-title">Why Choose Sweetwafer?</div>
            <div><b>At Sweetwater, we have one single goal in mind: to make you a satisfied customer.</b></div>
            <div id="text-wrap-why">We want you to be 100% satisfied with not only the gear you purchase, but also with the service you receive. The Sweetwater difference goes far beyond this, including extras you simply won't find anywhere else—all designed to ensure that you are a happy customer.</div>
        </div>
      </div>
    )}
    </>
  )
}
