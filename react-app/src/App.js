import React, { useState, useEffect, useContext } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import Header from './components/Header/Header';
import LoginPage from './components/myAuth/LoginPage';
import SignUpOne from './components/myAuth/SignUpOne';
import SignUpTwo from './components/myAuth/SignUpTwo';
import Inventory from './components/Temp/Inv';
import Cart from './components/Cart/Cart';
import Product from './components/Product/Product';
import Navigation from './components/Navigation/Navigation';
import Home from './components/Home/Home';
import Footer from './components/Footer/Footer';
import NewGear from './components/SpecialPages/NewGear';
import NewGearFooter from './components/NewGearFooter/NewGearFooter';
import GuitarInspection from './components/SpecialPages/GuitarInspection';
import Account from './components/Account/Account';
import FourOFour from './components/SpecialPages/FourOFour';
import Checkout from './components/Cart/Checkout';
import Warranty from './components/SpecialPages/Warranty';
import FreeShipping from './components/SpecialPages/FreeShipping';
import PracticeAWS from './components/AWS/PracticeAWS';
import { authenticate, login } from './store/session';
import { SweetContext } from './context/Context';
import ScrollToTop from './components/ScrollToTop';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);



  if (!loaded) {
    return null;
  }

  const loginDemo = async (e) => {
    e.preventDefault();
    const data = await dispatch(login('demo@aa.io', 'password'))
    if (data) {
      console.log('Invalid Login!')
    }
  }

  return (
    <BrowserRouter>
      <ScrollToTop />
      <Switch>
        <Route path='/login_page' exact={true}>
          <LoginPage />
        </Route>
        <Route path='/signup-one' exact={true}>
          <SignUpOne />
        </Route>
        <Route path='/signup-two' exact={true}>
          <SignUpTwo />
        </Route>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <Route path='/cart' exact={true}>
          <Header />
          <Navigation />
          <Cart />
          <NewGearFooter />
          <Footer />
        </Route>
        <Route path='/products/:id' exact={true}>
          <Header />
          <Navigation />
          <Product />
          <NewGearFooter />
          <Footer />
        </Route>
        <Route path='/products/category/:cat' exact={true}>
          <Header />
          <Navigation />
          <Inventory />
          <NewGearFooter />
          <Footer />
        </Route>
        <ProtectedRoute path='/users/:userId' exact={true}>
          <User />
        </ProtectedRoute>
        <Route path='/' exact={true} >
          <Header />
          <Navigation />
          <Home />
          <NewGearFooter />
          <Footer />
          {/* <div style={{ width: '100vw', height: '100vh', backgroundColor: '#d5ebf5'}}></div> */}
          {/* <Inventory /> */}
        </Route>
        <Route path='/newgearday' exact={true}>
          <Header />
          <Navigation />
          <NewGear />
          <Footer />
        </Route>
        <Route path='/inspection' exact={true}>
          <Header />
          <Navigation />
          <GuitarInspection />
          <NewGearFooter />
          <Footer />
        </Route>
        <Route path='/account'>
          <Header />
          <Navigation />
          <Account />
          <div style={{}}>
            <NewGearFooter />
            <Footer />
          </div>
        </Route>
        <Route path='/checkedout'>
          <Checkout />
        </Route>
        <Route path='/warranty' exact={true}>
          <Header />
          <Navigation />
          <Warranty />
          <NewGearFooter />
          <Footer />
        </Route>
        <Route path='/free-shipping' exact={true}>
          <Header />
          <Navigation />
          <FreeShipping />
          <NewGearFooter />
          <Footer />
        </Route>
        <Route path='/aws' exact={true}>
          <Header />
          <Navigation />
          <PracticeAWS />
        </Route>
        <Route path="*">
          <FourOFour />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
