import './GuitarInspection.css'

export default function GuitarInspection() {

  return (
    <div id="inspection-outer">
      <div id="video-div">
        <iframe width="1019" height="612" src="https://www.youtube.com/embed/4iWfqakaV0Y" title="Take a Tour of Sweetwater's Guitar Gallery" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
      <div id="doshite">
        <div>Why would you buy your</div>
        <div>guitar anywhere else?</div>
      </div>
      <div className="border-one"></div>
      <div id="let-me-tell-you-one">Sweetwater makes sure that shopping for a guitar or bass on our site is as exciting and reassuring as it is in person. That's why we go to great lengths to carefully inspect, play test, individually photograph, and weigh every stringed instrument we sell priced above $299. In fact, we put trained eyes and hands on hundreds of guitars and basses every day, because we want each one to arrive just as you had imagined, leaving you totally satisfied with your new instrument. We do this simply because it's the right thing to do.</div>
      <div id="tan-boy-one">
        <div id="guitar-img">
        </div>
        <div id="guitar-icon">
          <img src='/svg/guitar-inspect.svg'></img>
        </div>
        <div id="point-55">Sweetwater's 55-point Inspection</div>
        <div id="guesswork">Taking the guesswork out of buying your next guitar online.</div>
        <div className="border-one"></div>
        <div className="tan-p-one">Our detailed 55-point Inspection ensures that each instrument valued $299 and above is shipped in factory-fresh condition and ready to play. Plus, our professional technicians, inspectors, and luthiers are trained in factory specifications and tolerances and steeped in years of customer feedback.</div>
        <div className="tan-p-one">You can count on the fact that they have looked at every aspect of that guitar or bass, from the input jack to the headstock, the same way you would in a store. And each instrument ships with its own individually signed certificate of inspection, giving it our personal seal of approval that the instrument meets or exceeds factory standards.</div>
      </div>
      <div id="checklist">
        <div id="checklist-title"></div>
        <div className="border-one"></div>
        <div id="checklist-div">
          <div id="col-one">
            <h3 id="handling-h3">Handling</h3>
            <ul>
              <li className="checklist-items">24-hour climate acclimation & professional handling</li>
              <li className="checklist-items">Inspect case/gig bag interior & exterior</li>
              <li className="checklist-items">Verify contents & accessories</li>
            </ul>
          </div>
          <div id="col-two">

          </div>
        </div>

      </div>
      <div id="tan-boy-two">
        <div id="guitar-img-2"></div>
        <div className="como-doshite">Is the 55-point Inspection</div>
        <div className="como-doshite">the same as a "setup"?</div>
        <div className="border-one"></div>
        <div id="let-me-tell-you-two">Our 55-point Inspection is different than a setup, because our inspection ensures that the instrument meets manufacturer tolerances, whereas a setup tailors the guitar to a player's specific preferences. A setup typically involves our world-class Guitar Workshop installing your preferred strings, adjusting to a requested action height, and even installing new pickups or other parts. If you would like your instrument set up before it ships, simply tell your Sales Engineer. They'll be happy to oblige.</div>
      </div>
    </div>
  )
}
