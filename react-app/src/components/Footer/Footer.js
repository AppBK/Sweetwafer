import { useHistory } from 'react-router-dom'
import './Footer.css'

export default function Footer() {
  const history = useHistory();

  const toNewGear = () => {
    history.push('/newgearday');
  }

  return (
    <div id="footer">
      <div id="trademark-cont">
        <div id="sweetwafer-sound">Sweetwafer Sound, 5501 U.S. Hwy 30 W, Fort Wayne, IN 46818</div>
        <div id="sweetwafer-trademark">© 2022 Sweetwafer - All rights reserved.</div>
      </div>
    </div>
  )
}
