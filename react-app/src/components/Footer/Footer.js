import { useHistory } from 'react-router-dom'
import './Footer.css'

export default function Footer() {
  const history = useHistory();

  const toNewGear = () => {
    history.push('/newgearday');
  }

  return (
    <div id="footer">
      <div id="about-me-left">
        <div>About&nbsp;Me</div>
        <a className="about-me-links" href="https://www.linkedin.com/in/brian-kiesel-94475696/">LinkedIn</a>
      </div>
      <div id="trademark-cont">
        <div id="sweetwafer-sound">Sweetwafer Sound, 5501 U.S. Hwy 30 W, Fort Wayne, IN 46818</div>
        <div id="sweetwafer-trademark">© 2022 Sweetwafer - All rights reserved.</div>
      </div>
      <div id="about-me-right">
        <div>About&nbsp;Me</div>
        <a className="about-me-links" href="https://github.com/AppBK/Sweetwafer">Github</a>
      </div>
    </div>
  )
}
