

// Actions
const CREATE_BILLING = 'billing/CREATE_BILLING';
const READ_BILLING = 'billing/READ_BILLING';
const UPDATE_BILLING = 'bookings/UPDATE_BOOKINGS';
const DELETE_BILLING = 'bookings/DELETE_BOOKING';


// Action Creators
export const actionCreateBilling = (billing) => {
  return {
    type: CREATE_BILLING,
    billing
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

export const thunkReadBilling = (user_id) => async (dispatch) => {
  const response = await fetch(`/api/billing/${user_id}`);

  if (response.ok) {
    const info = await response.json();
    dispatch(actionReadBilling(info));
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


// Reducer

export default function billingReducer(state = [], action) {
  switch(action.type) {
    case READ_BILLING: {
      if (Object.keys(action.billings).length === 0) return [];
      const newState = [...action.billings];

      return newState;
    }
    default: {
      return state;
    }
  }
}
