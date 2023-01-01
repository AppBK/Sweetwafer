import { useContext } from 'react';
import { SweetContext } from '../../context/Context';
import { useHistory } from 'react-router-dom';
import Footer from '../Footer/Footer';
import NewGearFooter from '../NewGearFooter/NewGearFooter';

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

  const goInspection = () => {
    history.push('/inspection');
  }


  return (
    <>
    <div id="home-outer">
      <div id="page-top-adds">
        <div><img id="img-yearend" src="/png/year-end.png"></img></div>
        <div><img id="img-financing" src="/png/financing.png"></img></div>
      </div>
      <div id="getmore-title">Get More at Sweetwafer</div>
      <div id="getmore">
        <div className="getmore-tiles" onClick={goInspection}>
          <div className="floating-circle">
            <div className="thumb-constraint">
              <img className="circle-thum" src="/svg/get-more/guitar-55.svg"></img>
            </div>
          </div>
          <div className="bottom-box">
            <div className="blue-title">55-point Guitar Inspection</div>
            <div className="tiny-text">Guitar perfection right out of the box.</div>
          </div>
        </div>
        <div className="getmore-tiles">
          <div className="floating-circle">
            <div id="shipping-thumb" className="thumb-constraint">
              <img className="circle-thum" src="/svg/get-more/shipping.svg"></img>
            </div>
          </div>
          <div className="bottom-box">
            <div className="blue-title">Fast, FREE Shipping</div>
            <div className="tiny-text">Even the small stuff.</div>
          </div>
        </div>
        <div className="getmore-tiles">
          <div className="floating-circle">
            <div id="warranty-thumb" className="thumb-constraint">
              <img className="circle-thum" src="/svg/get-more/warranty.svg"></img>
            </div>
          </div>
          <div className="bottom-box">
            <div className="blue-title">FREE 2-year Warranty</div>
            <div className="tiny-text">Buy with confidence.</div>
          </div>
        </div>
      </div>
      <div id="popular-cont">
        <div id="popular-title">Popular Categories</div>
        <div id="category-circles-cont">
          {categories.map(cat => <div key={cat} id={cat} className="columnar" onClick={routeToSubCategory}><div id={cat} className="category-circles"><img id={cat} className="img-cat" src={`/jpg/categories/${encodeString(cat)}.webp`}></img></div><div id={cat} className="cat-circle-label">{cat}</div></div>)}
        </div>
      </div>
    </div>
    {/* <NewGearFooter />
    <Footer /> */}
    </>
  )
}
