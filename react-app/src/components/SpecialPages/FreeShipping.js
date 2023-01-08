import './FreeShipping.css'

export default function FreeShipping() {

  return (
    <div id="free-shipping-outermost">
      <div id="free-shipping-inner">
        <div id="header-div">
          <h1 id="h1-shipping-header"><span id="count-on-it">Count on reliable</span> FREE Shipping!</h1>
        <div id="lower-header-flex">
          <div id="no-min"></div>
          <div id="more-value">
            <p className="p-value">Sweetwater's Free Shipping Means <strong>More Value</strong> for You.</p>
            <ul id="ul-value">
              <li className="li-value">No Minimum Purchase Required</li>
              <li className="li-value"><i>Thousands</i> of Items Qualify</li>
              <li className="li-value">Most Orders Ship the Same Day</li>
            </ul>
          </div>
          </div>
        </div>
        <div id="south-of-header">
          <div id="reasons-flex">
            <div id="left-columns">
              <h3 id="h3-another">Another Reason to Buy from Sweetwater!</h3>
              <div className="p-top">At Sweetwater, we're committed to giving you the most for your money. That's why almost everything you buy ships FREE, courtesy of Sweetwater! No matter how small the item — guitar strings, cables, accessories, and more — if it's in stock, then it qualifies. Unlike many retailers' policies, there's no minimum purchase required! It's one more thing that makes Sweetwater the most convenient and most affordable place to shop.</div>
              <div className="apo-fpo">Have an APO or FPO address?</div>
              <div className="p-top">Sweetwater is happy to offer FREE shipping via the United States Postal Service to your APO or FPO address. If you need faster delivery, please call us at (800) 222-4700. We'll help find the shipping solution that works best for you.</div>
              <div className="apo-fpo">Additional Shipping Options</div>
              <div className="p-top">If your order does not qualify for free shipping, or if you require faster delivery, you will still enjoy very reasonable shipping rates. After entering your Zip Code on the Sweetwater checkout page, we'll show you your shipping options and charges.</div>
            </div>
            <div id="how-can">
              <h2 id="how-can-header"><strong id="big-talk">How can I tell</strong> if an item ships for <span>FREE</span>?</h2>
              <div id="how-can-lower">
                <p id="p-every">Every product that qualifies for free shipping is clearly marked with the following graphic:</p>
                <div id="graphic-div"></div>
              </div>
            </div>
          </div>
          <div id="free-shipping-details">
            <h2 id="h2-details">Free Shipping <span className="bold-div">Details:</span></h2>
            <ul id="last-list">
              <li className="li-details">Our Free Shipping offer is available on orders shipped to the contiguous United States only. Orders shipped to Alaska, Hawaii, or international addresses may not qualify. See checkout for available shipping options and rates.</li>
              <li className="li-details">Items purchased with a PO (purchase order) do not qualify for Free Shipping.</li>
              <li className="li-details">Free Shipping does not apply to special orders and oversized/overweight products.</li>
              <li className="li-details">If you return your purchase, then the cost of shipping will be deducted from any refund or credit.</li>
              <li className="li-details">Lightweight items (13 ounces or less) will be shipped via the United States Postal Service First Class Mail. This is trackable and normally arrives within two to four days. Heavier items ship via FedEx Ground® or UPS Ground. Delivery times range from one to five days, depending upon the distance to the destination.</li>
              <li className="li-details">Free Shipping, where available, may not be combined with other offers or discounts.</li>
            </ul>
          </div>
          <div id="questions-div">
            <div>Questions? Call us!</div>
            <div className="smaller">Your Sweetwater Sales Engineer can help you with shipping or any questions you may have about the gear you want.</div>
            <div className="smaller" id="bottom-most">Call toll free: (800) 222-4700 </div>
          </div>
        </div>
      </div>
      <div id="bottom-border"></div>
    </div>
  )
}
