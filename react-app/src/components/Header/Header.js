import { useSelector } from "react-redux"
import './Header.css'

export default function Header() {
  const user = useSelector(state => state.session.user)
  let render_cart = user ? true : false;

  return (
    <div id="flex-header">
      <button id="sweet-logo">
        <img id="img-logo" src="/png/sweetwafer-logo-trans.png"></img>
      </button>
      <div id="contact">
        <div>
          <h2 id="sweet-phone-number">(800) 222-4700</h2>
        </div>
        <div id="call">Call for the best deals!</div>
      </div>
      <div id="account">
        <p>Account</p>
        <img className="down-arrow" src="/svg/gobbled-svgs/arrow-down.svg"></img>
        <div id="account-window">
          Login
        </div>
      </div>
      {render_cart && (<button id="cart-button">
        <img id="cart-img" src="/svg/cart-0.svg"></img>
      </button>)}
    </div>
  )
}
