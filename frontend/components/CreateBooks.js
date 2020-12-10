import React, { useEffect, useState } from 'react'
import Select from 'react-select'
import Axios from 'axios'


const CreateBooks = (props) => {

  const [formData, updateFormData] = useState({
    title: '',
    author: '',
    image: '',
    description: '',
    genre: [],
    age: []
  })

  const ages = [
    { value: 'Education', label: 'Education' },
    { value: 'Fiction', label: 'Fiction' },
    { value: 'Poetry', label: 'Poetry' },
    { value: 'Activity Book', label: 'Activity Book' },
    { value: 'Fantasy', label: 'Fantasy' },
    { value: 'Science Fiction', label: 'Science Fiction' },
    { value: 'Picture Book', label: 'Picture Book' }
  ]

  const genres = [
    { value: '0', label: '0-1' },
    { value: '1', label: '1-2' },
    { value: '2', label: '2-3' },
    { value: '3', label: '3-4' },
    { value: '4', label: '4-6' },
    { value: '6', label: '6-8' },
    { value: '8', label: '8-10' },
    { value: '10', label: '10-16' }
  ]

  const [selectedAges, setSelectedAges] = useState([])
  const [selectedGenres, setSelectedGenres] = useState([])

  useEffect(() => {
    // Map catergories to only keep the value property
    const ageArray = selectedAges.map(one => {
      return one.value
    })
    const data = {
      ...formData,
      category: ageArray
    }
    updateFormData(data)
  }, [selectedAges])

  useEffect(() => {
    // Map catergories to only keep the value property
    const genreArray = selectedGenres.map(one => {
      return one.value
    })
    const data = {
      ...formData,
      category: genreArray
    }
    updateFormData(data)
  }, [selectedGenres])

  function handleChange(event) {
    const data = {
      ...formData,
      [event.target.name]: event.target.value
    }
    updateFormData(data)
  }

  function handleSubmit(event) {
    event.preventDefault()
    const token = localStorage.getItem('token')

    return Axios.post('/api/books', data, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then((resp) => {
        console.log(resp.data.errors)
        props.history.push('/books')
      })
  }

  return <div> 
    <form className="" onSubmit={handleSubmit}>
      <div className="field">
        <label className="label">Title</label>
        <div className="control">
          <input
            className="input"
            type="text"
            onChange={handleChange}
            value={formData['title']}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Author</label>
        <div className="control">
          <input
            className="input"
            type="text"
            onChange={handleChange}
            value={formData['author']}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Description</label>
        <div className="control">
          <textarea
            className="textarea"
            type="text"
            onChange={handleChange}
            value={formData['description']}
            name="bio"
          />
        </div>
      </div>
      <div className="field">
        <label className="label"
        >Age Group</label>
      </div>
      <div className="control">
        <Select
          closeMenuOnSelect={false}
          components={makeAnimated()}
          autoFocus
          options={ages}
          isMulti
          onChange={setSelectedAges}
          isSearchable
          placeholder="Select the age group"
          className="basic-multi-select"
        />
      </div>
      <div className="field">
        <label className="label"
        >Genre</label>
      </div>
      <div className="control">
        <Select
          closeMenuOnSelect={false}
          components={makeAnimated()}
          autoFocus
          options={genres}
          isMulti
          onChange={setSelectedGenres}
          isSearchable
          placeholder="Select the age group"
          className="basic-multi-select"
        />
      </div>
      <button>Submit</button>
    </form >
  </div >

}

export default CreateBooks
