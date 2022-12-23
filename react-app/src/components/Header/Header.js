import { useSelector, useDispatch } from "react-redux"
import { useHistory } from "react-router-dom";
import { login, logout } from "../../store/session";
import './Header.css'

export default function Header() {
  const user = useSelector(state => state.session.user)
  let render_cart = user ? true : false;

  const history = useHistory();
  const dispatch = useDispatch();

  const toLogin = () => {
    history.push('/login_page');
  }

  const goHome = () => {
    history.push('/');
  }

  const loginDemo = async (e) => {
    e.preventDefault();
    const data = await dispatch(login('demo@aa.io', 'password'))
    if (data) {
      console.log('Invalid Login!')
    }
  }

  const onLogout = async (e) => {
    await dispatch(logout());
  };

  return (
    <div id="flex-header">
      <button id="sweet-logo" onClick={goHome}>
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
          <button id="login-button" onClick={toLogin}>Log in</button>
          <button id="demo-button" onClick={loginDemo}>Demo user</button>
          <button id="logout-button" onClick={onLogout}>Logout</button>
        </div>
        {/* <div id="demo-login">
          <button id="demo-button" onClick={loginDemo}>Demo user</button>
        </div> */}
      </div>
      {render_cart && (<button id="cart-button">
        <img id="cart-img" src="/svg/cart-0.svg"></img>
      </button>)}
    </div>
  )
}
