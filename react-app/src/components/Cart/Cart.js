import './Cart.css'

export default function Cart() {
  return (
    <div id="cart-page">
      <div id="top-o-page">
        <div id="cart-empty-flex">
          <div id="guitar-img-cont">
            <img id="guitar-img" src="/png/blue-guitar.png"></img>
          </div>
          <div id="margin-empty">
            <div id="empty-cart">Your Cart Is Empty</div>
            <div id="gear-ideas">There's no gear here! Need some ideas?</div>
          </div>
        </div>
      </div>
    </div>
  )
}
