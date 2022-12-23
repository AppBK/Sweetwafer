import { useHistory } from 'react-router-dom'
import './LoginPage.css'

export default function LoginPage() {
  const history = useHistory();

  const toSignUp = () => {
    history.push('/signup-one');
  }


  return (
    <div id="background-flex">
      <div id="form-container">
        <div id="upper-portion">
          <img id="signup-logo" src="/png/sweetwafer-logo-trans.png"></img>
          <div id="inspire" >Sign in now</div>
          <div id="the-most" >Get the most from Sweetwater.com</div>
        </div>
        <div id="lower-portion">
          <form id="signup-form">
            <input type="email" className="signup-inputs" placeholder="Email address"></input>
            <input type="password" className="signup-inputs" placeholder="Password"></input>
          </form>
          <button id="login-button-form">Log in</button>
          <div id="no-account">Don't have an account?</div>
          <button id="sign-up-from-login" onClick={toSignUp}>Create an Account</button>
        </div>
      </div>
    </div>
  )
}
