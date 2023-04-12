import React from "react";
import TableRow from "./TableRow";
import "./Table.css";

function Table(params: { tableData: any[]; endpoint: string }) {
  if (params.tableData === null || params.tableData.length === 0) return <div>No data</div>;
  const tableHeader = Object.keys(params.tableData[0]);
  if (tableHeader.includes("password"))
    tableHeader.splice(tableHeader.indexOf("password"), 1);
  const headerRow = (
    <TableRow
      rowData={tableHeader}
      endpoint={null}
      rowId={-1}
    />
  );
  const bodyRows = params.tableData.map((rowData) => {
    delete rowData["password"];
    const rowId = rowData["partner_id"]
      ? rowData["partner_id"]
      : rowData["plant_id"];
    return (
      <TableRow
        rowData={Object.values(rowData)}
        endpoint={params.endpoint}
        rowId={rowId}
      />
    );
  });

  return (
    <table>
      <thead key="thead">{headerRow}</thead>
      <tbody key="tbody">{bodyRows}</tbody>
    </table>
  );
}

export default Table;
