const api_key = '6ce3ec99ee09c36c103970d557867b3d';
        const ciudad = 'Santiago';
        let lang = 'es';
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&units=metric&appid=${api_key}&lang=${lang}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                document.getElementById('description').innerHTML = data.weather[0].description;
                document.getElementById('temp').innerHTML = `${data.main.temp}°C`;
                document.getElementById('humidity').innerHTML = `Humedad: ${data.main.humidity}%`;
            })
            .catch(error => console.error(error));