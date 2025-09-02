import React from "react";

const ConditionSelector = ({ filter, setFilter }) => {
  return (
    <div className="condition-selector">
      <label htmlFor="filter">Select view: </label>
      <select
        id="filter"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      >
        <option value="all">Show all countries</option>
        <option value="ra">Rheumatoid Arthritis</option>
        <option value="pregnancy">Pregnancy</option>
      </select>
    </div>
  );
};

export default ConditionSelector;
