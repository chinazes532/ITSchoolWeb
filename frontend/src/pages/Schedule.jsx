import React from 'react'
import ScheduleTable from '../components/ScheduleTable';
import "../styles/Schedule.css";
import { scheduleData } from '../utils/schedule';

export default function Schedule() {
    return (
        <div>
            <ScheduleTable scheduleData={scheduleData} />
        </div>
    )
}
