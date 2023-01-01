import { useContext } from 'react'
import { SweetContext } from '../../context/Context'
import './Cart.css'

export default function Cart() {
  const { numInCart, setNumInCart } = useContext(SweetContext);

  let needSpacer;
  if (numInCart === 0) needSpacer = true;

  return (
    <div id="cart-page">
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
      {needSpacer && (<div id="spacer"></div>)}
    </div>
  )
}
