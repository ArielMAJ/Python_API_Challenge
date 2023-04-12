import React from "react";

async function deleteRow(
  endpoint: string | null,
  rowId: number,
) {
  const url = `http://127.0.0.1:3005${endpoint}${rowId}`;
  await fetch(url, {
    method: "DELETE",
    headers: { accept: "application/json" },
  });
  const element = document.getElementById(rowId.toString());
  if (element) element.remove();
}
function TableRow(params: {
  rowData: any;
  endpoint: string | null;
  rowId: number;
}) {
  if (params.rowData === null) return null;
  let numeric_key = Date.now() % 10000;
  const cells = params.rowData.map((cellData) => {
    numeric_key += 0.01;
    return <td key={numeric_key.toString() + cellData}> {cellData} </td>;
  });
  const tableRowKey = numeric_key.toString() + cells;
  let deleteBtn;
  if (params.rowId === -1 || params.endpoint === null) deleteBtn = "Delete";
  else
    deleteBtn = (
      <div
        onClick={() => deleteRow(params.endpoint, params.rowId)}
      >
        <button>Delete</button>
      </div>
    );
  numeric_key += 0.01;
  return (
    <tr id={params.rowId.toString()} key={tableRowKey}>
      {cells}
      <td key={`del${params.rowData}`}>{deleteBtn}</td>
    </tr>
  );
}

export default TableRow;
