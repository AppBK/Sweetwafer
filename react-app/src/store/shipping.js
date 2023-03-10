// TYPES
const CREATE_SHIPPING = 'shipping/CREATE_SHIPPING';
const READ_SHIPPING = 'shipping/READ_SHIPPING';
const UPDATE_SHIPPING = 'shipping/UPDATE_SHIPPING';
const DELETE_SHIPPING = 'shipping/DELETE_SHIPPING';

export const parseErrors = (errs) => {
  let output = [];
  for (let i = 0; i < errs.length; i++) {
    if (errs[i] !== 'This field is required.') {
      output.push(errs[i]);
    }
  }
  return output;
}

// ACTIONS
export const actionCreateShipping = (data) => ({
  type: CREATE_SHIPPING,
  payload: data,
});

export const actionReadShipping = (info) => ({
  type: READ_SHIPPING,
  payload: info,
});

export const actionUpdateShipping = (new_data) => ({
  type: UPDATE_SHIPPING,
  payload: new_data
})

export const actionDeleteShipping = (id) => ({
  type: DELETE_SHIPPING,
  payload: id,
})

// THUNKS


// Create
export const thunkCreateShipping = (info) => async (dispatch) => {
  const response = await fetch('/api/shipping/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ...info
    })
  });

  if (response.ok) {
    const info = await response.json();
    dispatch(actionReadShipping(info));
    return null;
  } else {
    const data = await response.json()
    if (data.errors) {
      const filteredErrs = parseErrors([...data.errors])
      return filteredErrs;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

// Read
export const thunkReadShipping = (user_id) => async (dispatch) => {
  const response = await fetch(`/api/shipping/${user_id}`);

  if (response.ok) {
    const info = await response.json();
    dispatch(actionReadShipping(info));
    return info;
  } else {
    const data = await response.json()
    if (data.errors) {
      return data;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

// Update
export const thunkUpdateShipping = (id, new_info) => async (dispatch) => {
  const response = await fetch(`/api/shipping/update/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ...new_info
    })
  });

  if (response.ok) {
    const updated = await response.json();
    dispatch(actionReadShipping(updated));
    return null;
  } else {
    const data = await response.json();
    if (data.errors) {
      const filteredErrs = parseErrors([...data.errors])
      return filteredErrs;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

export const thunkDeleteShipping = (id, user_id) => async (dispatch) => {
  const response = await fetch('/api/shipping/delete', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      id: id,
      user_id: user_id,
    })
  });

  if (response.ok) {
    const info = await response.json();
    console.log('RECIEVED FROM DELETE ROUTE: ', info)
    dispatch(actionReadShipping(info));
    return info;
  } else {
    const data = await response.json()
    if (data.errors) {
      return data;
    } else {
      return ['Could Not Read Info'];
    }
  }
}


// REDUCER

export default function shippingReducer(state = [], action) {
  switch(action.type) {
    case CREATE_SHIPPING: {
      const newState = [...state];
      newState.push(action.payload);

      return newState;
    }
    case READ_SHIPPING: {
      if (Object.keys(action.payload).length === 0) return [];
      const newState = [...action.payload];

      return newState;
    }
    default: {
      return state;
    }
  }
}
