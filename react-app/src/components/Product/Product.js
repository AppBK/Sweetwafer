import { thunkReadProduct } from "../../store/product"
import { useSelector, useDispatch } from "react-redux"
import { useParams, useHistory } from "react-router-dom"
import { useState, useEffect, useContext, useRef } from "react";
import { SweetContext } from "../../context/Context";
import { thunkAddCart } from "../../store/cart";
import './Product.css'

export default function Product() {

  const { id } = useParams();
  const history = useHistory();
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const cart = useSelector(state => state.cart);
  const product = useSelector(state => state.products[id]);


  const { numInCart, setNumInCart } = useContext(SweetContext);

  const [selectedThumb, setSelectedThumb] = useState('');

  // Lines 24-29, 173-205, 222-223: For future implementation of 'auto-zoom' hover effect...
  const [keepBorder, setKeepBorder] = useState('');
  const [mousePosition, setMousePosition] = useState(0);
  const [gridPosition, setGridPosition] = useState('0px');
  const [trackImgY, setTrackImgY] = useState('0px');
  const [trackImgX, setTrackImgX] = useState('50px');
  const [bgSize, setBgSize] = useState('');

  const hoveredImgRef = useRef();

  useEffect(() => {
    if (!product) {
      dispatch(thunkReadProduct(id));
    }
  }, [])

  let alreadyInCart;
  if (product && cart) {
    for (let i = 0; i < cart.length; i++) {
      if (cart[i].item_id === product.id) {
        alreadyInCart = true;
        break;
      }
    }
  }

  const toPriceMain = (floater) => {
    let temp_str = floater.toString();
    let char;
    let count = 0;
    let final_str = ''

    for (let i = temp_str.length - 1; i >= 0; i--) {
      char = temp_str[i];

      if (count === 3) {
        final_str = char + ',' + final_str;
        count = 0;
      } else {
        final_str = char + final_str;
        count++;
      }
    }

    final_str = '$' + final_str + '.00';

    return final_str;
  }

  const addToCart = async () => {
    await dispatch(thunkAddCart(user.id, product.id));

    setNumInCart(numInCart + 1);
  }


  function removeTabs(str) {
    let output = [];
    for (let i = 0; i < str.length; i++) {
      if (str[i] === '\t') {
        output.push(' ');
      } else {
        output.push(str[i]);
      }
    }
    return output.join('');
  }


  // Example Input String 1: 'GENERAL#Number of Strings: 6;Left-/Right-handed: Right-handed;BODY#Body Type: Solidbody;Body Shape: JP15;Body Material: Okoume;Top Material: Flamed Maple;Body Finish: High Gloss Polyester;Color: Purple Nebula Flame;NECK#Neck Material: Roasted Figured Maple;Neck Shape: 	Super Thin/Flat;Neck Joint: 5-way Bolt-on;Radius: 17";Fingerboard Material: Roasted Figured Maple;Fingerboard Inlay: JP Shields;Number of Frets: 24, Medium Jumbo, Stainless Steel;Scale Length: 25.5" Multi-scale;Nut Width: 1.6875";Nut Material: Melamine;HARDWARE#Bridge/Tailpiece: Music Man Custom Piezzo Floating Tremolo;Tuners: Schaller M6-IND Locking;ELECTRONICS#Neck Pickup: DiMarzio Illuminator Humbucker;Bridge Pickup: DiMarzio Illuminator Humbucker, Piezo Pickup;Controls: 	1 x volume (push/push gain boost), 1 x tone (push/push pickup config), 1 x Piezo volume, 2 x 1/4" (mono/stereo);Switching: 3-way toggle pickup switch, 3-way piezo/magnet toggle switch;MISCELLANEOUS#Strings: Ernie Ball Slinky, .010-.046;Case/Gig Bag: Softshell Case;Manufacturer Part Number: 661-JJF-10-00-MB-CR;'
  // Example Input String 2: 'Number of Strings: 5;Left-/Right-handed: Right-handed;Body Shape:	StingRay Special;Body Material: Select Hardwoods;Body Finish: Gloss;Color: Burnt Ends;Neck Material:	Select Roasted Maple;Neck Joint: 5-way Bolt-on;Radius: 11";Fingerboard Material: Rosewood;Fingerboard Inlay: White Dots;Number of Frets:	22, High Wide;Scale Length:	34";Nut Width: 1.75";Nut Material: Melamine;Bridge/Tailpiece: Vintage Music Man Topload Steel Bridge with Vintage Nickel Plated Steel Saddles;Tuners:	Custom Music Man;Neck Pickup:	Music Man Neodymium Humbucker;Bridge Pickup:	Music Man Neodymium Humbucker;Controls:	1 x master volulme, 1 x balance, 4-band Stacked Active EQ;Switching: 5-way blade pickup switch;Strings:	Super Slinky Bass, .045-.130;Case/Gig Bag: Softshell Case;Manufacturer Part Number:	208-HA-20-03-MB-CR;'

  function parseTechSpecs(string) {
    let temp = removeTabs(string); // Some tabs are masquerading as spaces on the Sweetwater site. Beware! Lines: 80-90 for the code.
    let pairs = temp.split(';');

    let output = [];

    for (let i = 0; i < pairs.length; i++) {
      output.push(pairs[i].split(':')); // each tech-spec is added to the output as an array with 2 values
      // The first being the title and the second it's value.
    }

    let temp1;
    let temp2;
    let temp3;
    const outputObject = {};

    // If the input string has been additionally delimited with the '#' symbol, we are gonna make an object!
    // O(n * (n(n-1)/2)) time complexity
    if (output[0][0].split('#').length > 1) { // If we found a '#', commence!!
      for (let i = 0; i < output.length; i++) {
        temp1 = output[i][0]; // Get the category headder and value key
        temp1 = temp1.split('#'); // Separate the above
        if (temp1.length > 1) {
          // Below: { 'GENERAL': [['Number of Strings:', 6], ...] }
          outputObject[temp1[0]] = [[temp1[1], output[i][1]]];
          for (let j = i + 1; j < output.length; j++) {
            temp2 = output[j];
            temp3 = temp2[0].split('#'); // Check to see if we have come to a new category

            if (temp3.length > 1) { // If so, set i to the previous value of j and break inner loop
              i = j - 1;
              break;
            } else {
              // If not a new category, continue pushing key/value pairs into the current category array
              outputObject[temp1[0]].push(temp2);
            }
          }
        }
      }

      // REMOVE the empty '' at the end of array caused by splitting on the semi-colon
      outputObject['MISCELLANEOUS'].pop(); // O(1)
      // Return the output object along with a boolean indicating the TYPE of that object!
      return [outputObject, true];
    }

    // REMOVE the empty '' at the end of array caused by splitting on the semi-colon
    output.pop(); // O(1)
    // Return the output object along with a boolean indicating the TYPE of that object!
    return [output, false];
  }




  if (!product) return null;

  let tech_specs;

  // 'NOPE' is given as a default value when a product does not have technical spec info
  if (product.tech_specs !== 'NOPE') {
    tech_specs = true;
  }

  let isObj;
  let specValues;
  if (tech_specs) {
    let tester = parseTechSpecs(product.tech_specs);
    if (tester[1]) {
      isObj = true;
    }
    specValues = tester[0];
  }

  const goWarranty = (e) => {
    e.preventDefault();
    history.push('/warranty');
  }


  // ZOOM
  const stripText = (text) => {
    const currentValue = text.split('px')[0];
    return parseInt(currentValue);
  }

  const trackImgPosition = (e) => {
    e.preventDefault();

    const hoveredImgWidth = hoveredImgRef.current.clientWidth;
    const hoveredImgHeight = hoveredImgRef.current.clientHeight;

    setBgSize(hoveredImgWidth * 3.5 + 'px');

    const halfWidth = Math.floor(hoveredImgWidth / 2);
    const halfHeight = Math.floor(hoveredImgHeight / 2);


    console.log('X POS: ', e.nativeEvent.offsetX);
    console.log('Y POS: ', e.nativeEvent.offsetY);

    if (e.nativeEvent.offsetX > halfWidth) {
      setTrackImgX((e.nativeEvent.offsetX * -2.4 - (128)) + 'px');
    } else {
      setTrackImgX((e.nativeEvent.offsetX * -2.4 + (120)) + 'px');
    }

    if (e.nativeEvent.offsetY > halfHeight) {
      setTrackImgY((e.nativeEvent.offsetY * -2.4) - (128) + 'px');
    } else {
       setTrackImgY((e.nativeEvent.offsetY * -2.4) + (16) + 'px');
    }
  }

  return (
    <div id="product-page">
      {selectedThumb ? null : setSelectedThumb(product.product_images[0].url)}
      <div id="everything-else">
        <div id="name-desc-logo">
          <div id="name-desc">
            <div id="product-name">{product.name}</div>
            <div id="product-description">{product.description}</div>
          </div>
          <div id="vendor-logo"><img src={product.logo}></img></div>
        </div>
        <div id="main-event">
          <div id="product-pics">
            <div id="main-img-div">
              <img src={selectedThumb}></img>
              {/* <img src={selectedThumb} onMouseMove={trackImgPosition} ref={hoveredImgRef}></img> */}
              {/* <div id="zoomed-in-baby" style={{backgroundPosition: `${trackImgX} ${trackImgY}`, backgroundSize: `${bgSize}`}}></div> */}
            </div>
            <div id="thumbs-div">
              {product.product_images.map(img => (
                <div id={img.url} className="product-tiny-thumbs" style={{backgroundImage: `url(${img.url})`}} onClick={(e) => setSelectedThumb(e.target.id)}></div>
              ))}
            </div>
          </div>
          <div id="sidebar-right">
            <div id="main-price">{toPriceMain(product.price)}</div>
            <div id="button-wrap">
              {!alreadyInCart && user && (<button id="add-to-cart" onClick={addToCart}>Add to Cart</button>)}
              {alreadyInCart && user && (<button id="already">Already in Your Cart</button>)}
              {!user && (<button id="not-logged">Login to Shop!</button>)}
            </div>
          </div>
        </div>
        <div id="bitchin-warranty">
          <div id="warranty-details">
            <div id="warranty-info">Warranty Info</div>
            <div id="two-free">Sweetwater's FREE 2-Year Total Confidence Coverage Warranty</div>
            <div>Extra peace of mind at no extra cost.</div>
            <ul id="warranty-ul">
              <li className="warranty-li">Save money with FREE parts and labor</li>
              <li className="warranty-li">Get back to making music with the industry's fastest turnaround time</li>
              <li className="warranty-li">Fix it the first time with our award-winning, factory-certified Service Department</li>
            </ul>
            <div id="link-learn-more" onClick={goWarranty}>Learn More</div>
          </div>
          <div id="warranty-logo">
            <div id="place-badge">
              <img id="badge" src="https://media.sweetwater.com/about/warranty/images/2year-badge-large.svg"></img>
            </div>
            <div id="place-total">
              <img id="total" src="https://media.sweetwater.com/m/about/warranty/images/tcc.png?ha=688f91f1a55780d6"></img>
            </div>
            <div id="price-wrap">
              <div id="strike">$249.00</div>
              <div id="free">FREE!</div>
            </div>
          </div>
        </div>
        {tech_specs && (<div id="tech-specs-div">
            <div id="specs">
              <div id="specs-title">Tech Specs</div>
              <div id="spanning-tree">
                {!isObj ? specValues.map((spec, idx) => (
                  <div className="span-div">
                    <span className={idx % 2 == 0 ? 'spec-cat-dark' : 'spec-cat-light'}>{spec[0]}:</span><span className={idx % 2 == 0 ? 'spec-val-dark' : 'spec-val-light'}>{spec[1]}</span>
                  </div>
                )) : null }
                {isObj ? Object.entries(specValues).map(entry => (
                  <>
                  <div className="obj-cat-name">{entry[0]}</div>
                  {entry[1].map((spec, idx) => (
                    <div className="span-div">
                      <span className={idx % 2 == 0 ? 'spec-cat-dark' : 'spec-cat-light'}>{spec[0]}:</span><span className={idx % 2 == 0 ? 'spec-val-dark' : 'spec-val-light'}>{spec[1]}</span>
                    </div>
                  ))}
                  </>
                )) : null}
              </div>
            </div>
        </div>)}
      </div>
    </div>
  )
}
