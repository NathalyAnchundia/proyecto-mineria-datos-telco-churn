const formulario = document.getElementById("formularioChurn");
const resultado = document.getElementById("mensajeResultado");

formulario.addEventListener("submit", async function(evento) {

    evento.preventDefault();

    const datos = {
        tenure: Number(document.getElementById("tenure").value),
        MonthlyCharges: Number(document.getElementById("monthlyCharges").value),
        TotalCharges: Number(document.getElementById("totalCharges").value),
        TotalServices: Number(document.getElementById("totalServices").value)
    };

    resultado.textContent = "Procesando predicción...";

    try {

        const respuesta = await fetch("http://127.0.0.1:5000/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        });

        const datosRespuesta = await respuesta.json();

        if (!respuesta.ok) {
            throw new Error(
                datosRespuesta.error || "No se pudo realizar la predicción."
            );
        }

        resultado.textContent =
            datosRespuesta.mensaje ||
            "Predicción realizada correctamente.";

    } catch (error) {

        console.error(error);

        resultado.textContent =
            "No fue posible conectar con la API. Verifique que la API esté ejecutándose.";
    }
});