import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { SweetProvider } from './context/Context';
import './index.css';
import App from './App';
import configureStore from './store';

const store = configureStore();

ReactDOM.render(
  <React.StrictMode>
    <SweetProvider>
      <Provider store={store}>
          <App />
        </Provider>
    </SweetProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
