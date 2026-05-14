import React from 'react'
import StatementTable from '../components/StatementTable';
import "../styles/Statement.css";
import { statementData } from '../utils/statement';

export default function Statement() {
    return (
        <div>
            <StatementTable statementData={statementData}/>
        </div>
    )
}
