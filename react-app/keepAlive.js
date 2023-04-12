const axios = require('axios');

const routinicaURL = 'https://routinica.onrender.com';
const sweetwaferURL = 'https://sweetwafer.onrender.com';
const splangyURL = 'https://splangy01.herokuapp.com';


const keepAlive = () => {
  setInterval(async () => {
    let res;

    try {
      res = await axios.get(routinicaURL);
      // console.log('RESPONSE: ', res.request.res.responseUrl, res.request.res.redirects);
      console.log('RESPONSE ROUTINICA: ', res.data);
    } catch (err) {
      console.log(err);
    }

    try {
      res = await axios.get(sweetwaferURL);
      console.log('RESPONSE SWEETWAFER', res.data);
    } catch (err) {
      console.log(err);
    }

    try {
      res = await axios.get(splangyURL);
      console.log('RESPONSE SPLANGY: ', res.data);
    } catch (err) {
      console.log(err);
    }
  }, 900000);
}

keepAlive();
