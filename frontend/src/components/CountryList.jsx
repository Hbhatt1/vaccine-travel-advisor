import React, { useState } from "react";
import CountryCard from "./CountryCard";
import "./CountryList.css";

const CountryList = ({ countries }) => {
  return (
    <div className="country-grid">
      {countries.map((country, index) => (
        <CountryCard key={index} country={country} />
      ))}
    </div>
  );
};

export default CountryList;
