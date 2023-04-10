import React from "react";

function TableRow(params: { rowData: any }) {
  let key = Date.now();
  const cells = params.rowData.map((cellData) => {
    key++;
    return <td key={key}> {cellData} </td>;
  });
  key++;
  return <tr key={key}>{cells}</tr>;
}

export default TableRow;
