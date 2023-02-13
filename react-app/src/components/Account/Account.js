import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { login, logout } from "../../store/session";
import AddressPayment from '../AddressPayment/AddressPayment';
import './Account.css'

export default function Account() {
  const user = useSelector(state => state.session.user);


  const userName = user.username.toUpperCase();

  const [currentRender, setCurrentRender] = useState('home');

  const history = useHistory();
  const dispatch = useDispatch();

  const onLogoutAcc = async (e) => {
    history.push('/');
    await dispatch(logout());
  };

  if (!user) return null;

  return (
    <>
    <div id="outer-account">
      <div id="account-menu">
        <div id="top-bar-blue">
          <div id="blue-left">
            <div id="user-icon-div">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 35.5 32.5"><path d="M30.2 23.1c-3.4-1.6-7.6-2.5-9.5-5.1 1.9-2.2 3.2-6.3 3.2-9.2 0-4.1-2.7-7.5-6-7.5s-6 3.4-6 7.5c0 2.9 1.3 6.9 3.1 9.1-1.9 2.6-6.2 3.6-9.6 5.2-4.2 2-3 8.2-3 8.2h30.8c-.1 0 1.2-6.2-3-8.2z" fill="#fff" stroke="#0f4490" strokeWidth="1.85" strokeMiterlimit="10"></path></svg>
            </div>
            <div id="all-mine">My Account</div>
          </div>
          <div id="blue-right">
            <button id="account-logout" onClick={onLogoutAcc}>Logout</button>
          </div>
        </div>
        <div id="main-account-div">
          <div id="left-slender-options">
            <div id="account-home" className="menu-options" style={{ backgroundColor: currentRender === 'home' ? '#d5e4f8' : '#ebf3fb' }} onClick={() => setCurrentRender('home')}>
              <div id="home-icon">
                <svg style={{ opacity: currentRender === 'home' ? '1' : '0.4' }} xmlns="http://www.w3.org/2000/svg" width="13.164" height="12.151"><path d="M5.063 12.151V8.1h3.038v4.05h3.088V6.076h1.975L6.582 0 0 6.076h1.975v6.076z"></path></svg>
              </div>
              <div>My Account Home</div>
            </div>
            <div className="menu-options" style={{ backgroundColor: currentRender === 'address' ? '#d5e4f8' : '#ebf3fb' }} onClick={() => setCurrentRender('address')}>
              <div id="pencil-icon">
                <svg style={{ opacity: currentRender === 'address' ? '1' : '0.4' }} xmlns="http://www.w3.org/2000/svg" width="12.853" height="12.298"><g data-name="Icon feather-edit-3"><path data-name="Path 11" d="M12.102 12.298H6.426a.75.75 0 1 1 0-1.5h5.676a.75.75 0 1 1 0 1.5Z"></path><path data-name="Path 12" d="M10.21 0a2.088 2.088 0 0 1 1.476 3.564l-7.883 7.884a.75.75 0 0 1-.348.2l-2.523.631a.75.75 0 0 1-.91-.91L.65 8.844a.75.75 0 0 1 .2-.348L8.734.612A2.074 2.074 0 0 1 10.21 0ZM2.889 10.24l7.737-7.737a.588.588 0 1 0-.831-.831L2.058 9.409l-.277 1.109Z"></path></g></svg>
              </div>
              <div>Address & Payment Info</div>
            </div>
          </div>
          <div id="fill-left"></div>
          <div id="right-render-comps">
            {currentRender === 'home' && (<div id="hey-now">hello {userName}.</div>)}
            {currentRender === 'address' && (<AddressPayment />)}
          </div>
        </div>
      </div>
      {currentRender === 'home' && (<div id="filler"></div>)}
    </div>
    {/* <div>Hey Now</div> */}
    </>
  )
}
