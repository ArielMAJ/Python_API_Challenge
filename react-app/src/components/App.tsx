import React from "react";
import "./App.css";
import OpenModalButton from "./OpenModalButton/OpenModalButton";

function App() {
  return (
    <div className="flex-container flex-column page">
      <div className="button-container">
        {/* <OpenModalButton btn_text="Add/Update Partner" endpoint="/partners/" /> */}
        <OpenModalButton btn_text="See Partners" endpoint="/partners/" />
        {/* <OpenModalButton btn_text="Add/Update Plant" endpoint="/plants/"/> */}
        <OpenModalButton btn_text="See Plants" endpoint="/plants/" />
      </div>
    </div>
  );
}

export default App;
