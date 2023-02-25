// -------------------
// (for POST method)

// const url = 'http://127.0.0.1:8000/api/create/'

// let obj = {
//     title: 'новая API запись',
//     text: 'Ура! Новая запись!'
// }

// fetch(url, {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json;charset=utf-8'
//     },
//     body: JSON.stringify(obj)
// })

// ---------------------------
// Delete method

// const url = 'http://127.0.0.1:8000/api/drop/4'

// fetch(url, {
//     method: 'DELETE',
//     headers: {
//         'Content-Type': 'application/json;charset=utf-8'
//     }})

// ------------------------------------
// Get method with auth

// fetch('http://127.0.0.1:8000/api/get_all/',
//       {headers: {
//           'Authorization': `Bearer ${token}`
//       }
//       })
//     .then(res => res.json())
//     .then(data => console.log(data))