import { useHistory } from 'react-router-dom'
import { useContext } from 'react'
import { SweetContext } from '../../context/Context'
import './Navigation.css'

const categories = ['Studio & Recording', 'Live Sound & Lighting', 'Guitars', 'Bass', 'Keyboards and Synthesizers', 'Microphones', 'DJ Equipment']
const vendors = {
  'Studio & Recording': ['Dangerous', 'Manley'],
  'Live Sound & Lighting': ['Allen & Heath', 'Obsidian', 'Martin'],
  'Guitars': ['ESP', 'Marshall'],
  'Bass': ['Ernie Ball', 'Ampeg'],
}

export default function Navigation() {
  const history = useHistory();

  const { vendor, setVendor } = useContext(SweetContext);

  const routeToSubCategory = (e) => {
    e.preventDefault();
    let destination;

    if (!vendors[e.target.id]) {
      for (const cat in vendors) {
        if (vendors[cat].includes(e.target.id)) {
          destination = cat;
          setVendor(e.target.id);
        }
      }
    } else {
      destination = e.target.id;
    }

    history.push(`/products/category/${destination}`);
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
              <button key={cat} id={cat} className="category-dropdown-cell" onClick={(e) => routeToSubCategory(e)}>
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
