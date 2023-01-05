// TYPES
const CREATE_SHIPPING = 'shipping/CREATE_SHIPPING';
const READ_SHIPPING = 'shipping/READ_SHIPPING';
const UPDATE_SHIPPING = 'shipping/UPDATE_SHIPPING';
const DELETE_SHIPPING = 'shipping/DELETE_SHIPPING';

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
    console.log('RETURNED INFO: ', info)
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

// Read
export const thunkReadShipping = (user_id) => async (dispatch) => {
  const response = await fetch(`/api/shipping/${user_id}`);

  if (response.ok) {
    const info = await response.json();
    console.log('RETURNED INFO: ', info)
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
  const response = await fetch(`/api/shipping/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ...new_info
    })
  });

  if (response.ok) {
    const updated = await response.json();
    dispatch(actionUpdateShipping(updated));
    return updated;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

export const thunkDeleteShipping = (id) => async (dispatch) => {
  const response = await fetch('/api/shipping/delete', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      id: id,
    })
  });

  if (response.ok) {
    const updated = await response.json();
    dispatch(actionUpdateShipping(updated));
    return updated;
  } else {
    const data = await response.json();
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
      const newState = [...action.payload];

      return newState;
    }
    default: {
      return state;
    }
  }
}
