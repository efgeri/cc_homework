const express = require('express')
const app = express()
const cors = require('cors')
app.use(cors())

app.get('/', (req, res) => {
    res.json({greeting: "Hello world", year: 2023})
})

app.listen(9000, () => {
    console.log("Express running on port 9000")
})