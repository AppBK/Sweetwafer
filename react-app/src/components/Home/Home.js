import { useContext } from 'react';
import { SweetContext } from '../../context/Context';
import { useHistory } from 'react-router-dom';
import './Home.css'

const categories = ['Studio & Recording', 'Live Sound & Lighting', 'Guitars', 'Bass'];
const vendors = {
  'Studio & Recording': ['Dangerous', 'Manley'],
  'Live Sound & Lighting': ['Allen & Heath', 'Obsidian', 'Martin'],
  'Guitars': ['ESP', 'Marshall'],
  'Bass': ['Ernie Ball', 'Ampeg'],
}

export default function Home() {
  const { vendor, setVendor } = useContext(SweetContext);

  const history = useHistory();

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
      setVendor('');
      destination = e.target.id;
    }

    history.push(`/products/category/${destination}`);
  }


  const encodeString = (string) => {
    let output = '';
    for (let i = 0; i < string.length; i++) {
      if (string[i] === ' ') {
        output += '_';
      } else {
        output += string[i];
      }
    }
    return output;
  }


  return (
    <div id="home-outer">
      <div id="page-top-adds">
        <div><img id="img-yearend" src="/png/year-end.png"></img></div>
        <div><img id="img-financing" src="/png/financing.png"></img></div>
      </div>
      <div id="popular-cont">
        <div id="popular-title">Popular Categories</div>
        <div id="category-circles-cont">
          {categories.map(cat => <div key={cat} id={cat} className="columnar" onClick={routeToSubCategory}><div id={cat} className="category-circles"><img id={cat} className="img-cat" src={`/jpg/categories/${encodeString(cat)}.webp`}></img></div><div id={cat} className="cat-circle-label">{cat}</div></div>)}
        </div>
      </div>
    </div>
  )
}
