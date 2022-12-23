import { useContext, useState } from 'react'
import { SweetContext } from '../../context/Context'
import { useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { signUp } from '../../store/session';
import './SignUpTwo.css'

export default function SignUpTwo() {
  const { signUpEmail, signUpPass } = useContext(SweetContext);
  const history = useHistory();
  const dispatch = useDispatch();

  const [first, setFirst] = useState('');
  const [last, setLast] = useState('');

  const finalizeSignup = () => {
    const username = first + ' ' + last;
    dispatch(signUp(username, signUpEmail, signUpPass));
    history.push('/');
  }

  return (
    <div id="background-flex">
      <div id="form-container-next">
        <div id="upper-portion">
          <img id="signup-logo" src="/png/sweetwafer-logo-trans.png"></img>
          <div id="inspire" >One last thing!</div>
          <div id="the-most" >Let's get to know each other.</div>
        </div>
        <div id="lower-portion">
          <form id="signup-form">
            <input type="text" className="signup-inputs" placeholder="First Name" value={first} onChange={(e) => setFirst(e.target.value)} required></input>
            <input type="text" className="signup-inputs" placeholder="Last Name" value={last} onChange={(e) => setLast(e.target.value)} required></input>
          </form>
          <button id="login-button-form" onClick={finalizeSignup}>Complete Signup</button>
        </div>
      </div>
    </div>
  )
}
