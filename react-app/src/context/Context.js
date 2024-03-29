import { useState, createContext } from 'react';

export const SweetContext = createContext();

export const SweetProvider = props => {

  const [signUpEmail, setSignUpEmail] = useState('');
  const [signUpPass, setSignUpPass] = useState('');
  const [vendor, setVendor] = useState('');
  const [numInCart, setNumInCart] = useState(0);
  const [qty, setQty] = useState(true);
  const [keptAlive, setKeptAlive] = useState();


  return (
    <SweetContext.Provider value={{
      signUpEmail, setSignUpEmail,
      signUpPass, setSignUpPass,
      vendor, setVendor,
      numInCart, setNumInCart,
      qty, setQty, keptAlive, setKeptAlive,
    }}>
      {props.children}
    </SweetContext.Provider>
  );
}
