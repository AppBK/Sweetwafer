import { useSelector, useDispatch } from "react-redux"
import { useHistory } from "react-router-dom";
import { login, logout } from "../../store/session";
import { useContext } from "react";
import { SweetContext } from "../../context/Context";
import './Header.css'

export default function Header() {
  const { numInCart, setNumInCart } = useContext(SweetContext);

  const user = useSelector(state => state.session.user);
  const cart = useSelector(state => state.cart);

  let sum = 0;
  cart.forEach(element => {
    sum += element.quantity;
  });
  setNumInCart(sum);

  console.log('CART: ', cart);
  let renderCart = user ? true : false;
  let renderLogout = user ? true : false;
  let renderDemo = user ? false : true;
  let renderLogin = user ? false : true;
  let renderSignUp = user ? false : true;
  let renderAccount = user ? true : false;

  const history = useHistory();
  const dispatch = useDispatch();


  const toLogin = () => {
    history.push('/login_page');
  }

  const goHome = () => {
    history.push('/');
  }

  const viewCart = () => {
    history.push('/cart');
  }

  const loginDemo = async (e) => {
    e.preventDefault();
    const data = await dispatch(login('demo@aa.io', 'password'))
    if (data) {
      console.log('Invalid Login!')
    } else {
      history.push('/account');
    }
  }

  const onLogout = async (e) => {
    history.push('/');
    await dispatch(logout());
  };

  const toAccount = () => {
    history.push('/account');
  }

  return (
    <div id="flex-header">
      <button id="sweet-logo" onClick={goHome}>
        <img id="img-logo" src="/png/sweetwafer-logo-trans.png"></img>
      </button>
      <div id="search-bar-cont">
        <input id="search-bar" type="search" placeholder="Search feature coming soon!"></input>
      </div>
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
          {renderLogin && (<button id="login-button" onClick={toLogin}>Log in</button>)}
          {renderSignUp && (<div id="borderline">
            <div id="new-here">New&nbsp;here?&nbsp;&nbsp;</div>
            <a id="signup-link" href="/signup-one">Create&nbsp;&nbsp;your account</a>
          </div>)}
          {renderDemo && (<button id="demo-button" onClick={loginDemo}>Demo user</button>)}
          {renderAccount && (<div id="your-account" onClick={toAccount}>Your Account</div>)}
          {renderLogout && (<button id="logout-button" onClick={onLogout}>Logout</button>)}
        </div>
      </div>
      {renderCart ? (<button id="cart-button" onClick={viewCart}><div id="num-in-cart" style={{left: numInCart > 9 ? '20px' : '24px'}} onClick={viewCart}>{numInCart}</div><img id="cart-img" src="/svg/cart-0.svg" onClick={viewCart}></img></button>) : (<div id="placeholder-cart"></div>)}
    {/* {<div id="placeholder-cart"></div>} */}
    </div>
  )
}
