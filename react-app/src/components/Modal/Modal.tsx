import React from "react";
import "./Modal.css";

function Modal(params) {

  const body = document.getElementById("body");
  if (body) body.style.overflow = "hidden";
  
  return (
    <div className="modal flex-container flex-column">
      <button className="modal-close" onClick={params.handleCloseModal}>
        ✖️
      </button>
      <div id="modal-content"></div>
    </div>
  );
}

export default Modal;
