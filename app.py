<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi WebApp</title>
  <style>
    body { font-family: Arial, sans-serif; }
    .container { margin: 20px; }
    h1 { text-align: center; }
    .button { display: block; margin: 10px auto; padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    .button:hover { background-color: #0056b3; }
    pre { white-space: pre-wrap; word-wrap: break-word; background: #f1f1f1; padding: 10px; }
  </style>
</head>
<body>

  <div class="container">
    <h1>Bienvenido a la WebApp</h1>
    <p>Haz clic en el botón para verificar las tarjetas</p>
    <button class="button" onclick="verificar()">Verificar</button>
    <pre id="resultado"></pre>
  </div>

  <script>
    function verificar() {
      const tarjetas = [
        "1111222233334440", "5555666677778881", "1234123412341234",
        "9876543210987652", "1111222233334443", "4444555566667774",
        "8888999900001115", "2222333344445556", "3333444455556667", "6666777788889998"
      ];

      fetch('https://ck-bot.onrender.com/verificar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tarjetas: tarjetas })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('resultado').textContent = JSON.stringify(data.resultados, null, 2);
      })
      .catch(error => console.error('Error al verificar:', error));
    }
  </script>

</body>
</html>
