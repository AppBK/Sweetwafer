import { useHistory } from 'react-router-dom'
import { useDispatch } from 'react-redux';
import { useState } from 'react';
import { login } from '../../store/session';
import './LoginPage.css'

export default function LoginPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const toSignUp = () => {
    history.push('/signup-one');
  }

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      console.log('ERRORS: ', data);
      setErrors(data);
    } else {
      history.push('/account');
    }
  };

  return (
    <div id="background-flex">
      <div id="form-container">
        <div id="upper-portion">
          <img id="signup-logo" src="/png/sweetwafer-logo-trans.png"></img>
          <div id="inspire" >Sign in now</div>
          <div id="the-most" >Get the most from Sweetwater.com</div>
        </div>
        <div id="lower-portion">
          <form id="signup-form" onSubmit={onLogin}>
            <input type="email" className="signup-inputs-one" placeholder="Email address" value={email} onChange={(e) => setEmail(e.target.value)} style={{borderColor: errors.length ? 'red' : 'black'}} required></input>
            <input type="password" className="signup-inputs-one" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} style={{ borderColor: errors.length ? 'red' : 'black' }} required></input>
            <button id="login-button-form-login" type="submit">Log in</button>
            <div id="errors-div">
              {errors.map((error) => (
                <div className="have-arrow">{error}</div>
              ))}
            </div>
          </form>
          <div id="no-account">Don't have an account?</div>
          <button id="sign-up-from-login" onClick={toSignUp}>Create an Account</button>
        </div>
      </div>
    </div>
  )
}
