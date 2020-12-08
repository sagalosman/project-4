import React, { useEffect, useState } from 'react'
import axios from 'axios'

const BookSearch = (props) => {
  console.log(props)
  const [result, updateResults] = useState([])

  // http://openlibrary.org/search.json?q=the%20very%20hungry%20caterpillar

  const searchFunction = (query) => {
    if (query) {
      axios.get(`api/proxy-books/${query}`)
        .then(resp => {
          updateResults(resp.data)
          console.log(resp.data)
        })
    }
  }
  return <div>
    <h2> search page </h2>

  </div>
}


export default BookSearch