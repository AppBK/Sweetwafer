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
        <div id="about-me-right">
          <a className="about-me-links" href="https://www.linkedin.com/in/brian-kiesel-94475696/" target="_blank" rel="noopener noreferrer"><i className="fa-brands fa-linkedin fa-2x fa-hover"></i></a>
        </div>
      </div>
      <div id="trademark-cont">
        <div id="sweetwafer-sound">Sweetwafer Sound, 5501 U.S. Hwy 30 W, Fort Wayne, IN 46818</div>
        <div id="sweetwafer-trademark">© 2022 Sweetwafer - All rights reserved.</div>
      </div>
      <div id="about-me-right">
        <a className="about-me-links" href="https://github.com/AppBK/Sweetwafer" target="_blank" rel="noopener noreferrer"><i className="fa-brands fa-github fa-2x fa-hover"></i></a>
      </div>
    </div>
  )
}
