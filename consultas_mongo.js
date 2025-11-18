// ============================
//  BASE DE DATOS Y COLECCIÓN
// ============================

use granja_inteligente;

// ============================
// 1. AGREGAR UNA LECTURA
// ============================

db.lecturas.insertOne({
    sensor_id: "SEN-001",
    valor: 23.4,
    unidad: "°C",
    estado: "Normal",
    timestamp: ISODate("2025-11-18T10:00:00Z")
});

// ============================
// 2. AGREGAR VARIAS LECTURAS
// ============================

db.lecturas.insertMany([
    {
        sensor_id: "SEN-002",
        valor: 55,
        unidad: "%H",
        estado: "Revisar",
        timestamp: ISODate("2025-11-18T10:05:00Z")
    },
    {
        sensor_id: "SEN-003",
        valor: 18.2,
        unidad: "°C",
        estado: "Normal",
        timestamp: ISODate("2025-11-18T10:10:00Z")
    },
    {
        sensor_id: "SEN-004",
        valor: 900,
        unidad: "ppm",
        estado: "Revisar",
        timestamp: ISODate("2025-11-18T10:15:00Z")
    }
]);

// =================================================
// 3. MOSTRAR LECTURAS DONDE el estado = "Revisar"
// =================================================

db.lecturas.find({ estado: "Revisar" });


// =================================================
// 4. MOSTRAR LECTURAS CON estado = "Normal"
// =================================================

db.lecturas.find({ estado: "Normal" });


// ============================
// 5. MODIFICAR UNA TEMPERATURA
// ============================
// Ejemplo: cambiar valor de un sensor de temperatura

db.lecturas.updateOne(
    { sensor_id: "SEN-001" },
    { $set: { valor: 25.1 } }
);


// ============================
// 6. CONSULTAR POR UNA FECHA ESPECÍFICA
// ============================
// Buscar lecturas registradas exactamente en un día

db.lecturas.find({
    timestamp: {
        $gte: ISODate("2025-11-18T00:00:00Z"),
        $lte: ISODate("2025-11-18T23:59:59Z")
    }
});
