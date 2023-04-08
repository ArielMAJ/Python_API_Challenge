import React from "react";
import "./App.css";
import OpenModalButton from "./OpenModalButton/OpenModalButton";

function App() {
  return (
    <div className="flex-container flex-column page">
      <div className="button-container">
        <OpenModalButton btn_text="Add/Update Partner" />
        <OpenModalButton btn_text="See/Delete Partners" />
        <OpenModalButton btn_text="Add/Update Plant" />
        <OpenModalButton btn_text="See/Delete Plants" />
      </div>
    </div>
  );
}

export default App;
