import { useSelector } from "react-redux"
import './Header.css'

export default function Header() {
  const user = useSelector(state => state.session.user)
  let render_cart = user ? true : false;

  return (
    <div id="flex-header">
      <button id="sweet-logo">
        <img id="img-logo" src="/png/Sweetwafer-logo.png"></img>
      </button>
      <div id="contact">
        <div>
          <h2>(800)222-4700</h2>
        </div>
        <div id="call">Call for the best deals!</div>
      </div>
      <button id="cart-button">
        <img id="cart-img" src="/svg/cart-0.svg"></img>
      </button>
    </div>
  )
}
