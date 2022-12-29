import { useState, createContext } from 'react';

export const SweetContext = createContext();

export const SweetProvider = props => {
  const [signUpEmail, setSignUpEmail] = useState('')
  const [signUpPass, setSignUpPass] = useState('')
  const [vendor, setVendor] = useState('')

  return (
    <SweetContext.Provider value={{
      signUpEmail, setSignUpEmail,
      signUpPass, setSignUpPass,
      vendor, setVendor,
    }}>
      {props.children}
    </SweetContext.Provider>
  );
}
