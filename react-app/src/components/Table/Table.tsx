import React from "react";
import TableRow from "./TableRow";
import "./Table.css";

function Table(params: { tableData: any[] }) {
  const headerRow = <TableRow rowData={params.tableData[0]} />;
  const bodyRows = params.tableData.slice(1).map((rowData) => {
    return <TableRow rowData={rowData} />;
  });

  return (
    <table>
      <thead>{headerRow}</thead>
      <tbody>{bodyRows}</tbody>
    </table>
  );
}

export default Table;
