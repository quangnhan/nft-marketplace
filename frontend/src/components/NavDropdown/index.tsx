// NavDropdown.js
import React, { ReactNode, useState } from "react";
import { Link } from "react-router-dom";

interface NavDropdownProps {
  title: string;
  link: string;
  children?: ReactNode;
}

function NavDropdown({ title, link, children }: NavDropdownProps) {
  const [showDropdown, setShowDropdown] = useState(false);

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };
  return (
    <div
      className="relative transition-all"
      onMouseEnter={toggleDropdown}
      onMouseLeave={toggleDropdown}
    >
      <Link to={link} className="nav-link hover:opacity-80">
            {title}
      </Link>
      {!!children && showDropdown && (
        <div className="absolute top-full left-0 bg-white text-black rounded-xl shadow-lg p-2 flex flex-col">
            {children}
        </div>
      )}
    </div>
  );
}

export default NavDropdown;
