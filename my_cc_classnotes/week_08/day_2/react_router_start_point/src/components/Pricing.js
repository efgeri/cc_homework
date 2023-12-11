import React from "react";
import { Link } from "react-router-dom";

const Pricing = ({pricing}) => (
  <div>
    <h4>Pricing</h4>
    <ul>
      {
        pricing.map((price, index) => <li key={index}>{price.level}: £{price.cost}</li>)
      }
    </ul>
    
  </div>
);

export default Pricing;
