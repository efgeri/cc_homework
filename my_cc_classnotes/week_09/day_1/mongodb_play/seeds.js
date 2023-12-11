use zoo;

// Setup
// db.dropDatabase()

// db.animals.insertMany([
//     {name: "Janet", type: "Polar Bear"},
//     {name: "Norman", type: "Penguin"}
// ])

// Read
db.animals.findOne({ _id: ObjectId("644695780a1ef908f308358c") });

// Update
db.animals.updateOne(
  { _id: ObjectId("644695780a1ef908f308358c") },
  { $set: { name: "Pip" } }
);

// Delete
db.animals.deleteOne({ _id: ObjectId("644695780a1ef908f308358c") });
