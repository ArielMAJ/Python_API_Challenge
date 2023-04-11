import React from "react";
import "./Modal.css";
import Table from "../Table/Table";

function Modal(params) {
  const body = document.getElementById("body");
  if (body) body.style.overflow = "hidden";

  return (
    <div className="modal flex-container flex-column">
      <button className="modal-close" onClick={params.handleCloseModal}>
        ✖️
      </button>
      <div id="modal-content">
        <h1>{params.tableName}</h1>
        <Table tableData={params.tableData} endpoint={params.endpoint} />
      </div>
    </div>
  );
}

export default Modal;
