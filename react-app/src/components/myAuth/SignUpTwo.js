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
  const [errors, setErrors] = useState([]);

  const finalizeSignup = async (e) => {
    e.preventDefault();

    const username = first + ' ' + last;
    const data = await dispatch(signUp(username, signUpEmail, signUpPass));
    if (data) {
      console.log('ERRORS: ', data);
      setErrors(data);
    } else {
      history.push('/account');
    }
  }

  const returnTo = () => {
    history.push('/signup-one');
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
          {errors?.length ? (<div id="barely-necessary-error-div">
            {errors.map((error) => (
              <div>{error}</div>
            ))}
            <div id="return-to-signup-one" onClick={returnTo}>Return to previous page</div>
          </div>) : null }
          <form id="signup-form" onSubmit={finalizeSignup}>
            <input type="text" className="signuptwo-inputs" placeholder="First Name" value={first} onChange={(e) => setFirst(e.target.value)} required></input>
            <input type="text" className="signuptwo-inputs" placeholder="Last Name" value={last} onChange={(e) => setLast(e.target.value)} required></input>
            <button id="login-button-form-two" type="submit">Complete Signup</button>
          </form>
        </div>
      </div>
    </div>
  )
}
