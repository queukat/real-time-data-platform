import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';

function ChartComponent() {
  const [chartData, setChartData] = useState({});

  const fetchData = () => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => {
        const timestamps = data.map(d => new Date(d.timestamp));
        const values = data.map(d => d.value);
        setChartData({
          labels: timestamps,
          datasets: [
            {
              label: 'Real-Time Data',
              data: values,
              borderColor: '#3e95cd',
              fill: false,
            },
          ],
        });
      });
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(() => fetchData(), 1000);
    return () => clearInterval(interval);
  }, []);

  return <Line data={chartData} />;
}

export default ChartComponent;
