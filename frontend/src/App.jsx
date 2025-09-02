import React, { useState, useEffect } from "react";
import ConditionSelector from "./components/ConditionSelector";
import CountryList from "./components/CountryList";
import Disclaimer from "./components/Disclaimer";
import "./App.css";

function App() {
  const [filter, setFilter] = useState("all");
  const [countries, setCountries] = useState([]);
  const [excluded, setExcluded] = useState([]);

  useEffect(() => {
    fetch(`/countries?filter=${filter}`)
      .then((res) => res.json())
      .then((data) => {
        setCountries(data.countries || []);
        setExcluded(data.excluded || []);
      })
      .catch((err) => console.error("Error fetching countries:", err));
  }, [filter]);

  return (
    <div className="App">
      <h1>Vaccine Travel Advisor</h1>
      <Disclaimer />

      <ConditionSelector filter={filter} setFilter={setFilter} />

      {filter !== "all" && excluded.length > 0 && (
        <div className="excluded-countries">
          <strong>Countries excluded:</strong>{" "}
          {excluded.map((c) => c.country).join(", ")}
        </div>
      )}
        <CountryList countries={countries} />
    </div>
  );
}

export default App;
