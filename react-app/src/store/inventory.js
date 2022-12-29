//
const READ_INVENTORY = 'inventory/READ_INVENTORY';


// ACTIONS
export const actionReadInv = (inventory) => ({
  type: READ_INVENTORY,
  payload: inventory
})


// THUNKS
export const thunkReadInv = (category, vendor) => async (dispatch) => {
  const response = await fetch('/api/inventory/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      category: category,
      vendor: vendor
    })
  });

  if (response.ok) {
    const inventory = await response.json();
    dispatch(actionReadInv(inventory.parsed_items));
  }
  // } else {
  //   const inventory = await response.json();
  //   if (inventory.errors) {
  //     return inventory;
  //   } else {
  //     return ['Could not fetch inventory'], 500;
  //   }
  // }
}



// REDUCER
export default function inventoryReducer(state = [], action) {
  switch(action.type) {
    case READ_INVENTORY: {
      const newState = [...action.payload];
      return newState;
    }
    default: {
      return state;
    }
  }
}
