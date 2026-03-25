import { useState } from "react";
import { Link } from "react-router-dom";

import "../styles/Header.css";

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const closeMenu = () => setMenuOpen(false);

  return (
    <header className="header">
      <div className="header-container">

        <div className="logo">
          <img src="/logo.png" alt="logo" />
          <span><Link to="/">IT School</Link></span>
        </div>

        <nav className={`nav ${menuOpen ? "open" : ""}`}>
        <Link to="/news" onClick={closeMenu}>Новости</Link>
          <Link to="/schedule" onClick={closeMenu}>Расписание</Link>
          <Link to="/price" onClick={closeMenu}>Стоимость</Link>
          <Link to="/statement" onClick={closeMenu}>Ведомость</Link>
          <Link className="btn" to="/consultation" onClick={closeMenu}>Консультация</Link>
        </nav>

        <div
          className={`burger ${menuOpen ? "active" : ""}`}
          onClick={() => setMenuOpen(!menuOpen)}
        >
          <span></span>
          <span></span>
          <span></span>
        </div>

      </div>
    </header>
  );
};

export default Header;