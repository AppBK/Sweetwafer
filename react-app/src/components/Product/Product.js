import { thunkReadProduct } from "../../store/product"
import { useSelector, useDispatch } from "react-redux"
import { useParams } from "react-router-dom"
import { useState, useEffect, useContext } from "react";
import { SweetContext } from "../../context/Context";
import { thunkAddCart } from "../../store/cart";
import './Product.css'

export default function Product() {

  const { id } = useParams();
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const cart = useSelector(state => state.cart);
  const product = useSelector(state => state.products[id]);


  const { numInCart, setNumInCart } = useContext(SweetContext);

  const [selectedThumb, setSelectedThumb] = useState('');
  const [keepBorder, setKeepBorder] = useState('');

  console.log(user);


  useEffect(() => {
    dispatch(thunkReadProduct(id))
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

  // const selectMainImage = (e) => {
  //   // e.preventDefault();

  //   if (e) setSelectedThumb(e.target.id);

  //   let nextImg;
  //   if (keepBorder) {
  //     console.log('KEPT: ', keepBorder);
  //     let current = document.getElementById(keepBorder);
  //     current.classList.remove('selected-thumb');
  //     console.log('CLASS: ', current);

  //     let next = document.getElementById(selectedThumb);
  //     next.classList.add('selected-thumb');
  //     setKeepBorder(selectedThumb)
  //   } else {
  //     setKeepBorder(selectedThumb);
  //     let next = document.getElementById(selectedThumb);
  //     next.classList.add('selected-thumb');
  //   }
  // }

  const addToCart = async () => {
    await dispatch(thunkAddCart(user.id, product.id));
    setNumInCart(cart.length + 1);
  }


  function removeTabs(str) {
    let output = '';
    for (let i = 0; i < str.length; i++) {
      if (str[i] === '\t') {
        output += ' ';
      } else {
        output += str[i];
      }
    }
    return output;
  }


  function parseTechSpecs(string) {
    let temp = removeTabs(string)
    let pairs = temp.split(';');

    let output = [];

    for (let i = 0; i < pairs.length; i++) {
      output.push(pairs[i].split(':'))
    }

    let temp1;
    let temp2;
    let temp3;
    let temp4;
    const outputObject = {};

    if (output[0][0].split('#').length > 1) {
      for (let i = 0; i < output.length; i++) {
        temp1 = output[i][0];
        temp1 = temp1.split('#')
        if (temp1.length > 1) {
          outputObject[temp1[0]] = [[temp1[1], output[i][1]]];
          for (let j = i + 1; j < output.length; j++) {
            temp2 = output[j];
            temp3 = temp2[0].split('#');

            if (temp3.length > 1) {
              i = j - 1;
              break;
            } else {
              outputObject[temp1[0]].push(temp2);
            }
          }
        }
      }
      outputObject['MISCELLANEOUS'].pop();
      return [outputObject, true];
    }
    output.pop();
    return [output, false];
  }

  if (!product) return null;

  let tech_specs;
  let specsArray;
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
            </div>
            <div id="thumbs-div">
              {product.product_images.map(img => (
                <div id={img.url} className="product-tiny-thumbs" style={{backgroundImage: `url(${img.url})`}} onClick={(e) => setSelectedThumb(e.target.id)}></div>
              ))}
            </div>
            {/* {keepBorder ? null : setKeepBorder(selectedThumb)}
            {keepBorder ? selectMainImage('') : null } */}
          </div>
          <div id="sidebar-right">
            <div id="main-price">{toPriceMain(product.price)}</div>
            <div id="button-wrap">
              {!alreadyInCart && (<button id="add-to-cart" onClick={addToCart}>Add to Cart</button>)}
              {alreadyInCart && (<button id="already">Already in Your Cart</button>)}
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
            <div id="link-learn-more">Learn More</div>
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
