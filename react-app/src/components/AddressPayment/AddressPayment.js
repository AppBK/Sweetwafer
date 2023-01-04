import Shipping from '../Shipping/Shipping'
import './AddressPayment.css'

export default function AddressPayment() {

  return (
    <div id="address-outer">
      <div id="address-jitai">
        <div id="address-title">Address & Payment</div>
        <div id="address-description">You can store as many addresses and payment methods as you like. When you place future orders, you will be able to choose from a list of your saved addresses and payment methods. Click the buttons below to add a new address or payment method. Click the "Change" link next to an existing address or payment method to make changes.</div>
      </div>
      <Shipping />
    </div>
  )
}
