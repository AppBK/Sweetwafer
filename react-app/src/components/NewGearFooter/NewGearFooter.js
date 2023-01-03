import { useHistory } from 'react-router-dom';
import './NewGearFooter.css'

export default function NewGearFooter() {
  const history = useHistory();

  const toNewGear = () => {
    history.push('/newgearday');
  }

  return (
    <div id="happy-new-gears">
      <div className="resizing" onClick={toNewGear}><div className="photo-tile" style={{ backgroundImage: 'url(https://media.sweetwater.com/m/include/footer/images/new-gear-day/3.jpg)' }}></div></div>
      <div className="resizing" onClick={toNewGear}><div className="photo-tile" style={{ backgroundImage: 'url(https://media.sweetwater.com/m/include/footer/images/new-gear-day/12.jpg)' }}></div></div>
      <div className="resizing" onClick={toNewGear}><div className="photo-tile" style={{ backgroundImage: 'url(https://media.sweetwater.com/m/include/footer/images/new-gear-day/17.jpg)' }}></div></div>
      <div id="new-gears-center">
        <div id="happy">HAPPY</div>
        <div id="new-gear-img"></div>
        <div className="center-text">Happy customers, one piece of</div>
        <div className="center-text">gear at a time!</div>
        <div id="link-to-new-gear" onClick={toNewGear}>Learn More</div>
      </div>
      <div className="resizing" onClick={toNewGear}><div className="photo-tile" style={{ backgroundImage: 'url(https://media.sweetwater.com/m/include/footer/images/new-gear-day/11.jpg)' }}></div></div>
      <div className="resizing" onClick={toNewGear}><div className="photo-tile" style={{ backgroundImage: 'url(https://media.sweetwater.com/m/include/footer/images/new-gear-day/2.jpg)' }}></div></div>
      <div className="resizing" onClick={toNewGear}><div className="photo-tile" style={{ backgroundImage: 'url(https://media.sweetwater.com/m/include/footer/images/new-gear-day/20.jpg)' }}></div></div>
    </div>
  )
}
