import React from "react";
import ReactDOM from "react-dom/client";
import Modal from "../Modal/Modal";
import "./OpenModalButton.css";

function OpenModalButton(params: { btn_text: any }) {
  function handleCloseModal() {
    document.removeEventListener("keydown", esc);
    const container = document.getElementById("modal-container");
    if (container) container.childNodes.forEach((node) => node.remove());
  }

  function esc(event) {
    if (event.key === "Escape") handleCloseModal();
  }
  
  function handleOpenModal() {
    document.scrollingElement?.scrollTo(0, 0);
    const container = document.getElementById("modal-container");
    ReactDOM.createRoot(container as HTMLElement).render(
      <Modal handleCloseModal={handleCloseModal} />
    );

    setTimeout(function () {
      document.addEventListener("keydown", esc);
    }, 200);
  
    return;
  }
  return (
    <div>
      <div onClick={handleOpenModal}>
        <button className="open-modal-button">{params.btn_text}</button>
      </div>
      <div id="modal-container"></div>
    </div>
  );
}

export default OpenModalButton;
