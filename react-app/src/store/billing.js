

// Actions
const CREATE_BILLING = 'billing/CREATE_BILLING';
const READ_BILLING = 'billing/READ_BILLING';
const UPDATE_BILLING = 'bookings/UPDATE_BOOKINGS';
const DELETE_BILLING = 'bookings/DELETE_BOOKING';


// Action Creators
export const actionCreateBilling = (newbilling) => {
  return {
    type: CREATE_BILLING,
    newbilling
  }
}

export const actionReadBilling = (billings) => {
  return {
    type: READ_BILLING,
    billings
  }
}

export const actionUpdateBilling = (billing) => {
  return {
    type: UPDATE_BILLING,
    billing
  }
}

export const actionDeleteBilling = (billingId) => {
  return {
    type: DELETE_BILLING,
    billingId
  }
}

// Thunks
export const thunkCreateBilling = (info) => async (dispatch) => {
  const response = await fetch(`/api/billing/add`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ...info
  })
  });

  if (response.ok) {
    const newInfo = await response.json();
    dispatch(actionCreateBilling(newInfo));
    return null;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

export const thunkReadBilling = (user_id) => async (dispatch) => {
  const response = await fetch(`/api/billing/${user_id}`);

  if (response.ok) {
    const info = await response.json();
    dispatch(actionReadBilling(info));
    return info;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

export const thunkUpdateBilling = (id, new_info) => async (dispatch) => {
  const response = await fetch(`/api/billing/update/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ...new_info
    })
  });

  if (response.ok) {
    const updated = await response.json();
    dispatch(actionUpdateBilling(updated));
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


export const thunkDeleteBilling = (id, user_id) => async (dispatch) => {
  const response = await fetch('/api/billing/delete', {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      id: id,
      user_id: user_id,
    })
  });

  if (response.ok) {
    const info = await response.json();
    dispatch(actionDeleteBilling(id));
    return null;
  } else {
    const data = await response.json()
    if (data.errors) {
      return data;
    } else {
      return ['Could Not Read Info'];
    }
  }
}

// Reducer
export default function billingReducer(state = {}, action) {
  switch(action.type) {
    case CREATE_BILLING: {
      const newState = {...state}
      newState[action.newbilling.id] = action.newbilling;
      return newState;
    }
    case READ_BILLING: {
      const newState = {...action.billings};

      return newState;
    }
    case UPDATE_BILLING: {
      const newState = {...state};

      newState[action.billing.id] = action.billing;
      return newState;
    }
    case DELETE_BILLING: {
      const newState = {...state};

      delete newState[action.billingId];
      return newState;
    }
    default: {
      return state;
    }
  }
}
