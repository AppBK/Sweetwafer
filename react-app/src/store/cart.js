//
const ADD_CART = 'cart/ADD_CART'
const READ_CART = 'cart/READ_CART'
const UPDATE_CART = 'cart/UPDATE_CART'
const DELETE_CART = 'cart/DELETE_CART'
const CLEAR_CART = 'cart/CLEAR_CART'


// ACTIONS

export const actionAddCart = (item) => ({
  type: ADD_CART,
  payload: item
})

export const actionGetCart = (cart) => ({
  type: READ_CART,
  payload: cart
})

export const actionUpdateCart = (quantity) => ({
  type: UPDATE_CART,
  payload: quantity
})

export const actionClearCart = () => ({
  type: CLEAR_CART
})

// THUNKS
export const thunkAddCart = (user_id, item_id) => async (dispatch) => {
  const response = await fetch('/api/cart/add', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user_id,
      item_id,
    })
  })
  if (response.ok) {
    const addedItem = await response.json();
  }
}

export const thunkGetCart = () => async (dispatch) => {
  const response = await fetch('/api/cart/');
  if (response.ok) {
    const cart = await response.json();
    dispatch(actionGetCart(cart));
    return cart
  } else {
    const data = await response.json();
    if (data.errors) {
      return data;
    } else {
      return ['Cart is Empty'];
    }
  }
}


// REDUCER
export default function cartReducer(state = {}, action) {
  switch(action.type) {
    case READ_CART: {
      const newState = {...action.payload}
      // need to add a quantity key to each item object
      return newState
    }
    case UPDATE_CART: {
      ;
    }
    case CLEAR_CART: {
      return {};
    }
    default: return state;
  }
}

/*
store: cart: { 1: {}, 2: {}}
*/
