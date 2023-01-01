import './NewGear.css'

export default function NewGear() {
  return (
    <div id="newgear-outer">
      <div id="happy-happy">
        <div id="just-happy">HAPPY</div>
        <div id="newgear-img"></div>
        <div id="social">
          <div className="wrap-social">
            <div className="social-img" style={{ backgroundImage: 'url(https://media.sweetwater.com/newgearday/icon-photo@2xv2.png)'}}></div>
            <div className="social-message">Grab a pic</div>
          </div>
          <div className="wrap-social">
            <div className="social-img" style={{ backgroundImage: 'url(https://media.sweetwater.com/newgearday/icon-tag@2xv3.png)'}}></div>
            <div className="social-middle">
              <div id="wrap-tiny"><div>Tag&nbsp;</div><div id="newgear-tiny"></div></div>
              <div>and #Sweetwafer</div>
            </div>
          </div>
          <div className="wrap-social">
            <div className="social-img" style={{ backgroundImage: 'url(https://media.sweetwater.com/newgearday/icons-share.gif)' }}></div>
            <div className="social-message">Share it</div>
          </div>
        </div>
      </div>
      <div id="celebrate">
        <div id="dude-rows">
          <div id="dude-celebrates"></div>
          <div id="dude-cols">
            <div className="dude-wrap">There simply is nothing like #NewGearDay. Trust us, as gearheads and musicians ourselves, we know just how incredible this day feels. That's why we wanted to create a place where we can all celebrate together!</div>
            <div id="wrap-mid" className="dude-wrap">Celebrate #NewGearDay and Win!</div>
            <div className="dude-wrap">If you got some new gear from us, grab a pic, share it in social using the tag <b>#NewGearDay</b> or <b>#Sweetwafer</b>, and you'll be entered to win Sweetwater swag! Plus, we'll be sure to feature it on our site and in our emails and newsletters.</div>
          </div>
        </div>
      </div>
      <div id="terms">
        <div id="term-text">Terms and Conditions</div>
        <div id="paragraph">No purchase or payment is required to win. Our weekly "#NewGearDay" swag giveaway will accept entries every day of every week. Entries are only eligible for selection during the seven day period leading up to the weekly drawing. Once a winner is selected, all other entries during that period are no longer eligible for selection. To be eligible, participants must submit a brand new entry. A Sweetwater SWAG prize will be granted to ONE randomly drawn individual who enters the promotion. The SWAG winner will be drawn and announced every Friday at 2:00 PM (EST). Entry is accomplished by posting a photo to Facebook, Instagram or Twitter and tagging it with the hashtags "#NewGearDay" and "Sweetwater". Winner must be a legal resident of the United States and at least 18 years of age. Multiple entries by one person or social media account will not increase odds of winning. Odds of winning will depend on the number of eligible entries received. Sweetwater employees and their immediate family members — as well as employees of affiliated manufacturers — are not eligible to participate. Winner of the sweepstakes will be notified via a reply to in the comments of the winner's New Gear Day post on the respective social media channel. Winner must provide Sweetwater with a valid Social Security number or taxpayer identification number before prize will be awarded. If one or more prizes, with a total value of $600 or more, are awarded to a winner during any calendar year, a Form 1099 will be issued. This promotion is in no way sponsored, endorsed, administered by, or associated with Facebook, Instagram or Twitter. By entering this promotion, you agree that Sweetwater, Facebook, Instagram and Twitter will have no liability regarding any and all matters related to your participation in the promotion, as well as acceptance or possession of the prize. The sponsor of this promotion is Sweetwater Sound, Inc.</div>
      </div>
    </div>
  )
}
