import React, { useState } from "react";

const CountryCard = ({ country }) => {
  const [open, setOpen] = useState(false);
  const id = `details-${country.country?.replace(/\s+/g, "-").toLowerCase()}`;

  return (
    <div className="country-card" onClick={() => setOpen(!open)} role="button" tabIndex={0}>
      <h3>{country.country}</h3>
      <div className="toggle">{open ? "−" : "+"}</div>

      {open && (
        <div className="details" id={id}>
          <p><strong>Most travellers:</strong> {country.most_travellers || "—"}</p>
          <p><strong>Some travellers:</strong> {country.some_travellers || "—"}</p>
          {country.url && (
            <p><strong>URL:</strong> <a href={country.url} target="_blank" rel="noreferrer">{country.url}</a></p>
          )}
        </div>
      )}
    </div>
  );
};

export default CountryCard;
