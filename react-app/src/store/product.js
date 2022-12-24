//
const READ_PRODUCT = 'product/READ_PRODUCT';

// ACTIONS
export const actionReadProduct = (product) => ({
  type: READ_PRODUCT,
  payload: product
})


// THUNKS
export const thunkReadProduct = (id) => async (dispatch) => {
  const response = await fetch(`/api/inventory/${id}`);

  if (response.ok) {
    const product = await response.json();
    dispatch(actionReadProduct(product));
  } else {
    const data = await (await response).json();
    if (data.errors) {
      return data;
    } else {
      return ['Product not found']
    }
  }
}



// REDUCER
export default function productReducer(state = {}, action) {
  switch(action.type) {
    case READ_PRODUCT: {
      const newState = { ...state };
      newState[action.payload.id.toString()] = action.payload;
      console.log('FROM READ_PRODUCT: ', newState)

      return newState;
    }
    default: {
      return state;
    }
  }
}
