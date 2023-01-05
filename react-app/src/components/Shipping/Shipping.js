import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { thunkReadShipping, thunkCreateShipping, thunkDeleteShipping, thunkUpdateShipping } from '../../store/shipping'
import './Shipping.css'

export default function Shipping() {
  // Get from Store
  const user = useSelector(state => state.session.user);
  const shipping = useSelector(state => state.shipping);

  // States:
  const [renderAdd, setRenderAdd] = useState(false);
  const [renderUpdate, setRenderUpdate] = useState(false);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [addressOne, setAddressOne] = useState('');
  const [addressTwo, setAddressTwo] = useState('');
  const [cityName, setCityName] = useState('');
  const [stateName, setStateName] = useState('');
  const [zip, setZip] = useState('');
  const [countryName, setCountryName] = useState('USA');
  const [primary, setPrimary] = useState(false);
  const [shippingId, setShippingId] = useState('');
  const [editObj, setEditObj] = useState({});

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(thunkReadShipping(user.id));
  }, [])

  if (!shipping) return null;

  const states = ["AK - Alaska",
    "AL - Alabama",
    "AR - Arkansas",
    "AS - American Samoa",
    "AZ - Arizona",
    "CA - California",
    "CO - Colorado",
    "CT - Connecticut",
    "DC - District of Columbia",
    "DE - Delaware",
    "FL - Florida",
    "GA - Georgia",
    "GU - Guam",
    "HI - Hawaii",
    "IA - Iowa",
    "ID - Idaho",
    "IL - Illinois",
    "IN - Indiana",
    "KS - Kansas",
    "KY - Kentucky",
    "LA - Louisiana",
    "MA - Massachusetts",
    "MD - Maryland",
    "ME - Maine",
    "MI - Michigan",
    "MN - Minnesota",
    "MO - Missouri",
    "MS - Mississippi",
    "MT - Montana",
    "NC - North Carolina",
    "ND - North Dakota",
    "NE - Nebraska",
    "NH - New Hampshire",
    "NJ - New Jersey",
    "NM - New Mexico",
    "NV - Nevada",
    "NY - New York",
    "OH - Ohio",
    "OK - Oklahoma",
    "OR - Oregon",
    "PA - Pennsylvania",
    "PR - Puerto Rico",
    "RI - Rhode Island",
    "SC - South Carolina",
    "SD - South Dakota",
    "TN - Tennessee",
    "TX - Texas",
    "UT - Utah",
    "VA - Virginia",
    "VI - Virgin Islands",
    "VT - Vermont",
    "WA - Washington",
    "WI - Wisconsin",
    "WV - West Virginia",
    "WY - Wyoming"]

  const stateCodeParser = (code) => {
    const temp = code.split('-');
    const state = temp[0];
    return state;
  }

  // console.log('CURRENT STATE NAME: ', stateCodeParser(stateName));

  const addShippingAddress = () => {
    setRenderAdd(true);
  }

  const closeAddForm = () => {
    setRenderAdd(false);
  }

  const editShippingAddress = (e) => {
    e.preventDefault();

    const tempObj = JSON.parse(e.target.id);
    const tempNames = tempObj.shipping_name.split(' ');
    // setEditObj(tempObj)
    setAddressOne(tempObj.street);
    setAddressTwo(tempObj.apt_number);
    setCityName(tempObj.city);
    setCompanyName(tempObj.company);
    setCountryName(tempObj.country);
    setFirstName(tempNames[0]);
    setLastName(tempNames[1]);
    setStateName(tempObj.state);
    setZip(tempObj.zip);
    setPrimary(tempObj.primary);
    setShippingId(tempObj.id);




    setRenderUpdate(true);
  }

  const closeEditForm = () => {
    setRenderUpdate(false);
  }

  const createShippingInfo = async (e) => {
    e.preventDefault();

    console.log('VALUE OF PRIMARY: ', primary)

    const info = {
      apt_number: addressTwo,
      city: cityName,
      company: companyName,
      country: countryName,
      primary: primary,
      shipping_name: firstName + ' ' + lastName,
      state: stateCodeParser(stateName),
      street: addressOne,
      user_id: user.id,
      zip: zip,
    }

    await dispatch(thunkCreateShipping(info));

    closeAddForm();
  }

  const deleteShipping = async () => {
    console.log('SHIPPING ID TO DELETE: ', shippingId);
    await dispatch(thunkDeleteShipping(shippingId));
  }

  const updateShipping = async (e) => {
    e.preventDefault();

    const update = {
      apt_number: addressTwo,
      city: cityName,
      company: companyName,
      country: countryName,
      primary: primary,
      shipping_name: firstName + ' ' + lastName,
      state: stateCodeParser(stateName),
      street: addressOne,
      user_id: user.id,
      zip: zip,
    }

    setRenderUpdate(false);
    await dispatch(thunkUpdateShipping(shippingId, update));

    console.log('CURRENT VALUE OF RENDER: ', renderUpdate)
  }


  return (
    <div id="shipping-outer">
      <div id="veil" style={{opacity: renderAdd ? '0.4' : '1'}}>
        <div id="shipping-title">Your Shipping Info</div>
        {!renderUpdate && (<div id="shipping-list">
          {shipping.map((address, idx) => (
            <div className="edit-flex-pusher">
              <div key={idx} className="subete-no-shipping">
                <div id="shipping-info-name-box">
                  <div className="shipping-info-name">{address.shipping_name}</div>
                  {address.primary && (<div className="primary"><div className="primary-nudge">PRIMARY</div></div>)}
                </div>
                {address.company && (<div className="shipping-info-company">{address.company}</div>)}
                <div className="shipping-info-street">{address.street}</div>
                {address?.apt_number && (<div>{address.apt_number}</div>)}
                <div className="shipping-info-city-state-zip">{address.city}, {address.state} {address.zip}</div>
                <div className="shipping-info-country">{address.country}</div>
              </div>
              <div className="change-button-div">
                <button id={JSON.stringify(address)} className="shipping-edit-button" onClick={editShippingAddress}>Change</button>
              </div>
            </div>
          ))}
        </div>)}
      </div>
      {!renderAdd && (<div>
        <button id="shipping-add-button" onClick={addShippingAddress}>Add Address</button>
      </div>)}
      {renderAdd && (<>
      <div id="add-new">Add A New Shipping Address</div>
        <form onSubmit={createShippingInfo}>
        <div id="shipping-name-label">Shipping Name</div>
        <div id="shipping-name-flex">
          <input id="first-name" className="shipping-input" type="text" placeholder="First" value={firstName} onChange={(e) => setFirstName(e.target.value)} required></input>
            <input className="shipping-input" type="text" placeholder="Last" value={lastName} onChange={(e) => setLastName(e.target.value)} required></input>
        </div>
        <div id="company-div">
          <div id="company-title"><div>Company&nbsp;</div><div className="tiny-option">(optional)</div></div>
            <input className="shipping-input" type="text" placeholder="Company" value={companyName} onChange={(e) => setCompanyName(e.target.value)}></input>
          <div className="floating-option-placeholder tiny-option">optional</div>
        </div>
        <div id="shipping-address-div">
          <div id="shipping-address-label">Shipping Address</div>
            <input className="shipping-input" type="text" placeholder="Address Line 1" value={addressOne} onChange={(e) => setAddressOne(e.target.value)} required></input>
            <input className="shipping-input" type="text" placeholder="Address Line 2" value={addressTwo} onChange={(e) => setAddressTwo(e.target.value)}></input>
          <div className="floating-option-placeholder tiny-option" id="nudge-one">optional</div>
            <input className="shipping-input" type="text" placeholder="City" value={cityName} onChange={(e) => setCityName(e.target.value)} required></input>
          <div id="state-zip-flex">
              <select id="select-state" value={stateName} onChange={(e) => setStateName(e.target.value)} required>
              <option className="state-opts" value="" disabled selected>Select a State</option>
              {states.map(code => (
                <option key={code} className="state-opts">{code}</option>
              ))}
            </select>
              <input className="shipping-input" type="text" placeholder="ZIP/PostalCode" value={zip} onChange={(e) => setZip(e.target.value)} required></input>
          </div>
          <select id="select-country" value={countryName} onChange={(e) => setCountryName(e.target.value)} required>
            <option selected>USA</option>
            <option >Mexico</option>
            <option >Canada</option>
            <option >China</option>
            <option >Japan</option>
          </select>
          <div id="checkbox-div">
            <input id="primary-address" type="checkbox" value={primary} onChange={() => setPrimary(!primary)}></input>
            <div id="checkbox-label">Make this my primary shipping address</div>
          </div>
          <div id="button-box-bottom">
            <button id="cancel-shipping-button"><div id="cancel-label" onClick={closeAddForm}>Cancel</div></button>
              <button id="confirm-shipping-button" type="submit"><div id="save-label">Save This Shipping Address</div></button>
          </div>
        </div>
      </form>
      </>)}
      {renderUpdate && (<div id="inset-shadow-box">
        {/* {console.log('OPENED!', editObj)} */}
        <div id="update-address">Update Shipping Address</div>
        <form onSubmit={updateShipping}>
          <div id="shipping-edit-label">Shipping Name</div>
          <div id="shipping-name-flex">
            <input id="first-name" className="shipping-input" type="text" placeholder="First" value={firstName} onChange={(e) => setFirstName(e.target.value)} required></input>
            <input className="shipping-input" type="text" placeholder="Last" value={lastName} onChange={(e) => setLastName(e.target.value)} required></input>
          </div>
          <div id="company-div">
            <div id="company-title"><div>Company&nbsp;</div><div className="tiny-option">(optional)</div></div>
            <input className="shipping-input" type="text" placeholder="Company" value={companyName} onChange={(e) => setCompanyName(e.target.value)}></input>
            <div className="floating-option-placeholder tiny-option" id="nudge-two-edit">optional</div>
          </div>
          <div id="shipping-address-div">
            <div id="shipping-address-edit">Shipping Address</div>
            <input className="shipping-input" type="text" placeholder="Address Line 1" value={addressOne} onChange={(e) => setAddressOne(e.target.value)} required></input>
            <input className="shipping-input" type="text" placeholder="Address Line 2" value={addressTwo ? addressTwo : ''} onChange={(e) => setAddressTwo(e.target.value)}></input>
            <div className="floating-option-placeholder tiny-option" id="nudge-one-edit">optional</div>
            <input className="shipping-input" type="text" placeholder="City" value={cityName} onChange={(e) => setCityName(e.target.value)} required></input>
            <div id="state-zip-flex">
              <select id="select-state" value={stateName} onChange={(e) => setStateName(e.target.value)} required>
                <option className="state-opts" value="" disabled selected>Select a State</option>
                {states.map(code => (
                  <option key={code} className="state-opts">{code}</option>
                ))}
              </select>
              <input className="shipping-input" type="text" placeholder="ZIP/PostalCode" value={zip} onChange={(e) => setZip(e.target.value)} required></input>
            </div>
            <select id="select-country" value={countryName} onChange={(e) => setCountryName(e.target.value)} required>
              <option selected>USA</option>
              <option >Mexico</option>
              <option >Canada</option>
              <option >China</option>
              <option >Japan</option>
            </select>
            {!primary && (<div id="checkbox-div">
              <input id="primary-address" type="checkbox" value={primary} onChange={() => setPrimary(!primary)}></input>
              <div id="checkbox-label">Make this my primary shipping address</div>
            </div>)}
            <div id="button-box-bottom-edit">
              <div id="delete-shipping-button-div">
                <button id="delete-shipping-button" onClick={deleteShipping}>Remove This Address</button>
              </div>
              <div>
                <button id="cancel-shipping-button"><div id="cancel-label" onClick={closeEditForm}>Cancel</div></button>
                <button id="confirm-shipping-button" type="submit"><div id="save-label">Update This Shipping Address</div></button>
              </div>
            </div>
          </div>
        </form>
      </div>)}
    </div>
  )
}
