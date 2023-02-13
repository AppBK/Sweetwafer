import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import cartReducer from './cart';
import inventoryReducer from './inventory';
import productReducer from './product';
import shippingReducer from './shipping';
import billingReducer from './billing';

const rootReducer = combineReducers({
  session,
  cart: cartReducer,
  inventory: inventoryReducer,
  products: productReducer,
  shipping: shippingReducer,
  billing: billingReducer,
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
