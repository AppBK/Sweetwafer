import { useHistory } from 'react-router-dom'
import './Navigation.css'

const categories = ['Studio & Recording', 'Live Sound & Lighting', 'Guitars', 'Bass', 'Keyboards and Synthesizers', 'Microphones', 'DJ Equipment']
const vendors = {
  'Studio & Recording': ['Dangerous', 'Manley'],
}

export default function Navigation() {
  const history = useHistory();

  const routeToSubCategory = (e) => {
    e.preventDefault();

    history.push(`/inventory/${e.target.id}`);
  }

  return (
    <>
      <div id="nav-container">
        <div className="nav-option">
          <div className="nav-title">Shop By Category</div>
          <div className="down-arrow-container">
            <img className="class-down-arrow" src="/svg/gobbled-svgs/arrow-down.svg"></img>
          </div>
          <div className="category-dropdown">
            {categories.map(cat => (
              <button id={cat} className="category-dropdown-cell" onClick={(e) => routeToSubCategory(e)}>
                <div id={cat} className="cat-title">{cat}</div>
                <div id={cat} className="right-arrow-container">
                  <img id={cat} className="class-right-arrow" src="/svg/gobbled-svgs/svg-11.svg"></img>
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>
      <div id="giftcards">

      </div>
    </>
  )
}
