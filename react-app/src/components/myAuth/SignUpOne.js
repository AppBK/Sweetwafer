import { useState, useContext } from 'react';
import { SweetContext } from '../../context/Context';
import { useHistory, Redirect } from 'react-router-dom'
import './SignUp.css'

export default function SignUpOne() {
  const {signUpEmail, setSignUpEmail, signUpPass, setSignUpPass } = useContext(SweetContext);

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const history = useHistory();

  const backToLogin = () => {
    history.push('/login_page');
  }

  const toNextForm = () => {
    setSignUpEmail(email)
    setSignUpPass(password)
    history.push('/signup-two')
  }

  return (
    <div id="background-flex">
      <div id="form-container">
        <div id="upper-portion">
          <img id="signup-logo" src="/png/sweetwafer-logo-trans.png"></img>
          <div id="inspire" >Create an Account</div>
          <div id="creating">Creating an account is fast, easy, and free! Plus,<br></br>it gives you access to some great website<br></br>features that allow you to view your order history online, and checkout quickly and easily.</div>
        </div>
        <div id="lower-portion">
          <form id="signup-form">
            <input type="email" className="signupone-inputs" placeholder="Email address" value={email} onChange={(e) => setEmail(e.target.value)}></input>
            <input type="password" className="signupone-inputs" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}></input>
          </form>
          <button id="login-button-form" onClick={toNextForm}>Continue</button>
          <div id="no-account">Already have an account?</div>
          <button id="sign-up-from-login" onClick={backToLogin}>Sign in</button>
        </div>
      </div>
    </div>
  )
}
