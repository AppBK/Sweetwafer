import './Warranty.css'

export default function Warranty() {

  return (
    <div>
      <div className="why-sw about-sw">
        <div className="wrap">
{/*
          <div class="navigation-wrap">
            <ul class="navigation">
              <li><a href="/about">About Us</a></li>
              <li class="why-prop"><a href="/about/our-story/">Our Story</a></li>
              <li><a href="/about/why-choose-sweetwater">Why Choose Sweetwater?</a></li>
              <li class="why-prop"><a href="/about/sales-engineers/">Personalized Gear Advice</a></li>
              <li class="why-prop"><a href="/about/inspections/">Inspected, Tested, <span class="nowrap">Ready to Play</span></a></li>
              <li class="why-prop-two"><a href="/about/guitars/">55-Point Guitar Inspection</a></li>
              <li class="why-prop-two"><a href="/about/band-orchestra/">40-Point Band &amp; Orchestra Inspection</a></li>
              <li class="why-prop"><a href="/about/free-shipping/">Fast, Free Shipping</a></li>
              <li class="why-prop"><a href="/about/support/">Live Support</a></li>
              <li class="why-prop"><a href="/about/warranty/" class="current">Free 2-Year Warranty</a></li>
              <li class="why-prop"><a href="/payments/">Payment Options <span class="nowrap">for Every Budget</span></a></li>
              <li class="why-prop"><a href="/about/wealth-of-resources/">Wealth of Resources <span class="nowrap">at Your Fingertips</span></a></li>
              <li class="why-prop"><a href="/about/massive-selection/">Massive Selection from Boutiques to Best Sellers</a></li>
              <li class="why-prop"><a href="/about/customer-service/">Award-Winning <span class="nowrap">Customer Service</span></a></li>
              <li><a href="/tour/" class="tour"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path d="M15.8.3a1 1 0 00-.7-.3h-4.2l-.6.3-.1.1v1l.2.2.5.2h2L6.4 8.4c-.3.2-.4.5-.3.9.1.3.3.5.6.6h.2l.6-.3 6.7-6.7v2c0 .3.2.6.4.7l.4.1.4-.1c.4 0 .6-.3.6-.6V1c0-.3 0-.5-.2-.7z"></path><path d="M11.1 14.3H2.2c-.3 0-.5-.2-.5-.5V4.9c0-.3.2-.5.5-.5h5.1L9 2.7H1.5c-.4 0-.7.1-1 .4l-.3.4v.1l-.1.3-.1.4v10.2c0 .8.7 1.5 1.5 1.5h10.6l.3-.1.1-.1.4-.4c.2-.3.4-.6.4-1V6.7l-1.7 1.7v5.4c0 .3-.2.5-.5.5z"></path></svg>Virtual Tour</a></li>
            </ul></div> */}

          <div id="content-warranty">

            <div className="warranty-head">
              <img src="https://media.sweetwater.com/m/about/warranty/images/tcc-logo.png?ha=35a79222a1a16c43" alt="Two Year Total Confidence Coverage" className="warranty-head__logo"></img>
                <h1>Sweetwater's FREE 2-Year Total Confidence Coverage Warranty</h1>
                Extra peace of mind at no extra cost.
            </div>

            <div className="warranty-intro">
              <p className="p-warranty">Save money with <strong>FREE</strong> parts <span className="nowrap">and labor</span></p>
              <p className="p-warranty">Get back to making music with the industry's fastest turnaround time</p>
              <p className="p-warranty">Fix it the first time with our award-winning, factory-certifed Service Department</p>
            </div>

            <div className="warranty-split">
              <div className="warranty-split__text">
                <h2>We've got your back</h2>
                <p>At most music stores, customers have to spend an extra 10% to 30% of an item's cost to make sure their gear is covered beyond the manufacturer's warranty.</p>

                <p>You don't have to pay hundreds of dollars - or even more - for extra gear protection at Sweetwater! </p>

                <p>Our Total Confidence Coverage Warranty gives you 24 months of coverage backed by our team of Sales Engineers, Support Specialists, and our factory-certified Service Team at no extra cost.</p>

              </div>
              <div className="warranty-split__img" style={{backgroundImage: 'url("https://media.sweetwater.com/m/about/warranty/images/player.jpg?width=1200&amp;ha=dbf7742cac450b55")'}}>
              </div>
            </div>

            <div className="warranty-split">
              <div className="warranty-split__img" style={{backgroundImage: 'url("https://media.sweetwater.com/m/about/warranty/images/tech.jpg?width=720&amp;optimize=medium&amp;ha=a651e670634575e6")'}}>
              </div>
              <div className="warranty-split__text">
                <h2>Sweetwater's Award-Winning Service Department</h2>
                <p>Treat your gear right with warranty service provided by our on-site, award-winning, and factory-certified Service Department, authorized to repair virtually every piece of gear we sell.</p>

                <p>If we're not authorized to service a piece of gear, we will work directly with the manufacturer for service so you don't have to worry about it!</p>

              </div>
            </div>

            <div className="warranty-faqs">
              <h2>Terms and Conditions</h2>
              <div className="warranty-faq">
                <summary className="warranty-faq__question">Is this the same as the manufacturer warranty?</summary>
                <div className="warranty-faq__answer">The Total Confidence Coverage™ 2-year warranty is exclusive to Sweetwater and should not be confused with a cooperative warranty from any manufacturer. We stand behind the products we sell to you and we want you to be completely confident in the products you purchase from Sweetwater. Please note, your purchase constitutes acceptance of these Terms and Conditions.</div>
              </div>
              <div className="warranty-faq">
                <summary className="warranty-faq__question">Where do I send my gear for TCC warranty service?</summary>
                <div className="warranty-faq__answer">To obtain our warranty service, you will need to send your gear directly to Sweetwater, not the manufacturer. Just as is the case when you send a product to a manufacturer for repair, you will be responsible for paying all shipping costs — both the cost of shipping your items to Sweetwater and the cost of Sweetwater shipping them back to you.</div>
              </div>
              <div className="warranty-faq">
                <summary className="warranty-faq__question">Is the warranty transferrable?</summary>
                <div className="warranty-faq__answer">Although some manufacturers may allow you to transfer ownership of their warranties, Sweetwater's Total Confidence Coverage is not transferable. Most of the products we sell include a manufacturer's warranty, but some don't. Our warranty does not, in any way, change or adversely affect the terms of any product's existing manufacturer's warranty, regardless of the length of that warranty, whatever it may be. In turn, if you choose to deal directly with the manufacturer and their warranty (within their stated warranty time frame; of course), it does not adversely affect Sweetwater's 2-year warranty.</div>
              </div>
              <div className="warranty-faq">
                <summary className="warranty-faq__question">What is covered under warranty?</summary>
                <div className="warranty-faq__answer">The Sweetwater Total Confidence Coverage™ Warranty is NOT a “no-fault” warranty. We're going to do our best to take care of you, but coverage applies only if your product malfunctions under normal operating conditions. Normal wear and tear or abuse to our products is not covered under this warranty. “Consumable” parts, components, and accessories are not covered under this warranty. Some examples of “consumables” are strings, lamps and light bulbs, printer cartridges, drum heads, tape heads, regular and rechargeable batteries, amplifier tubes, etc. Cymbals are not covered under this warranty. The Solid State Logic AWS 948 is not covered by this warranty, but SSL offers an optional extended warranty. Call for details. <a href="#exclusions">Click here</a> for a complete list of items not covered under the Sweetwater Total Confidence Coverage™ Warranty.</div>
              </div>
              <div className="warranty-faq">
                <summary className="warranty-faq__question">What isn't covered?</summary>
                <div className="warranty-faq__answer">As musicians ourselves, we really do identify with the frustrations that arise when a piece of gear breaks down, but we have to be realistic and state that we can't be held responsible for lost work, lost studio time, lost wages, emotional strife, or other ancillary issues that are created when a piece of equipment fails and/or during the time the equipment has been sent to us for repair. What we will do is our very, very best to get your gear back to you in working order as quickly as possible. </div>
              </div>
              <div className="warranty-faq">
                <summary className="warranty-faq__question">Are there any exclusions?</summary>
                <div className="warranty-faq__answer">
                  <ul>
                    <li>Drums and drum hardware are covered for manufacturer defects, but not for normal wear and tear or abuse.</li>
                    <li>Software, in any form, is not covered.</li>
                    <li>Data recovery from faulty hard drives, solid state drives, USB keys, and flash drives is not a service covered by this warranty.</li>
                    <li>This warranty does not apply to Apple products; however, Apple does offer its own great warranty programs — check with your Sales Engineer to learn more about AppleCare+.</li>
                    <li>Products identified as “Used” are not covered by this warranty. See our exclusive <a href="https://www.sweetwater.com/help/returns-exchanges.php#90-day-guarantee">90-day Used Gear Guarantee</a>.</li>
                    <li id="exclusions">Power conditioners, surge protectors, and power regulators are covered under our warranty and will be repaired should they become defective, but this warranty does not cover the repair or replacement of equipment connected to these products or offer any kind of cash value.</li>
                  </ul>
                  <div>
                    Detailed Warranty Exclusion List
                    <div className="warranty-exclusion-list" id="warranty-excluded-details">
                      <p>AppleCare</p><p>All Apple products</p><p>All Groove Tubes products</p><p>Batteries</p><p>Banjo heads</p><p>Bows</p><p>Brass care</p><p>Brass mutes</p><p>Brass practice aids</p><p>Brushes</p><p>CD audio</p><p>CD audio consignment</p><p>CD blanks</p><p>Clothing</p><p>Crotales</p><p>Cymbals</p><p>Cymbal accessories</p><p>Cymbal boom stands</p><p>Cymbal cases</p><p>Cymbal stands</p><p>Drumheads</p><p>Drumhead accessories</p><p>Drumsticks</p><p>Drumstick accessories</p><p>Drumstick rods</p><p>DVD blanks</p><p>Gong</p><p>Guitar picks</p><p>Harmonicas</p><p>Harmonica accessories</p><p>iLok 3</p><p>Instructional books</p><p>Instructional videos</p><p>Ligatures: clarinet</p><p>Ligatures: saxophone</p><p>Mallets</p><p>Marching cymbals</p><p>MIDI loop</p><p>Mouthpieces</p><p>Orchestral string accessories</p><p>Orchestral string pickups</p><p>Plug-ins: Avid DSP</p><p>Plug-ins: d8b</p><p>Plug-ins: Native</p><p>Plug-ins: PowerCore</p><p>Plug-ins: VS</p><p>Printer ink</p><p>Processor plug-ins</p><p>Reeds</p><p>Reeds care</p><p>Rosin</p><p>Service parts</p><p>Sheet music</p><p>Snare wires</p><p>Software</p><p>Sound samples</p><p>Strings</p><p>Tape cassette</p><p>Tape DAT</p><p>Tape reel</p><p>Tape video/digital</p><p>Tubes</p><p>Vocal care</p><p>Woodwind care</p>                </div>
                  </div>
                </div>
              </div>

              <div className="warranty-content">
                <div className="warranty-content__centering">
                  <h2 id="final-word">A final word on the 2-Year Total Confidence Coverage™ Warranty</h2>
                  <div id="final-word-text">It's our goal to be fair and offer you real value when you buy gear from us. We also need to make sure that by offering our Free 2-year Warranty, we're not creating an opportunity for someone who's less than honest to take advantage of us. So, we reserve the right to accept or reject any product presented to us for warranty coverage. And for the same reasons stated above, we also reserve the right to modify the conditions of this warranty at our discretion.</div>
                </div>
              </div>

              <div className="warranty-content">
                <div className="warranty-content__centering">
                  <div id="blue-question"></div>
                  <div className="warranty-questions">WARRANTY QUESTIONS?</div>
                  <h2 >Call a friendly Sales Engineer!</h2>
                  <p>They know gear inside and out, and they're musicians just like you. Your Sweetwater Sales Engineer can help with warranty questions or help you find the perfect piece of gear.</p>
                  <h2>(800) 222-4700</h2>
                </div>
              </div>
            </div>

          </div>
        </div>


      </div>
    </div>
  )
}
