import React from "react";
import "../styles/Advantages.css";

const Advantages = ({ items }) => {
  return (
    <section className="advantages">
      <div className="advantages-container">
        {items.map((item, index) => (
          <div key={index} className="advantage-card">
            <div className="icon">{item.icon}</div>
            <h3>{item.title}</h3>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Advantages;