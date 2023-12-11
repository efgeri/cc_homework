import { Link } from "react-router-dom";

// You can use sfc to create a skeleton of this component
const NavBar = () => {
  return (
    <ul>
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/about">About</Link>
      </li>
      <li>
        <Link to="/pricing">Pricing</Link>
      </li>
      <li>
        <Link to="/tobivore">Tobyvore</Link>
      </li>
    </ul>
  );
};

export default NavBar;
