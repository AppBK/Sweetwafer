import { useState, createContext } from 'react';

export const SweetContext = createContext();

export const SweetProvider = props => {
  const [signUpEmail, setSignUpEmail] = useState('')
  const [signUpPass, setSignUpPass] = useState('')

  return (
    <SweetContext.Provider value={{
      signUpEmail, setSignUpEmail,
      signUpPass, setSignUpPass,
    }}>
      {props.children}
    </SweetContext.Provider>
  );
}
