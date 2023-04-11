import React from "react";
import ReactDOM from "react-dom/client";
import Modal from "../Modal/Modal";
import "./OpenModalButton.css";

async function getJSONdataAndReturnTableArray(endpoint: string) {
  const response = await fetch(`http://localhost:3000/${endpoint}`);
  const jsonData = await response.json();
  const tableDataArray = jsonData[Object.keys(jsonData)[1]];
  return tableDataArray;
}

function OpenModalButton(params: { btn_text: string; endpoint: string }) {
  function handleCloseModal() {
    document.removeEventListener("keydown", esc);
    const container = document.getElementById("modal-container");
    if (container) container.childNodes.forEach((node) => node.remove());
  }

  function esc(event) {
    if (event.key === "Escape") handleCloseModal();
  }

  async function handleOpenModal() {
    document.scrollingElement?.scrollTo(0, 0);
    const container = document.getElementById("modal-container");
    const modal = ReactDOM.createRoot(container as HTMLElement);
    modal.render(
      <Modal
        handleCloseModal={handleCloseModal}
        tableName={params.endpoint}
        endpoint={params.endpoint}
        tableData={await getJSONdataAndReturnTableArray(params.endpoint)}
      />
    );

    setTimeout(function () {
      document.addEventListener("keydown", esc);
    }, 200);
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
