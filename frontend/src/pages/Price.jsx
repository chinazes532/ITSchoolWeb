import React from 'react'
import PriceTable from '../components/PriceTable'
import "../styles/Price.css";
import { priceData } from '../utils/price';

export default function Price() {
  return (
    <div>
      <PriceTable  priceData={priceData}/>
    </div>
  )
}
