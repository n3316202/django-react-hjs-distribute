import React, { useEffect, useState } from 'react'
import { getCategories } from '../../api/CategoryApi';

//dev_5
const CategoryPage = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {

    //http://localhost:8000/api/categories/
    getCategories()
    .then(res => setCategories(res.data))
    .catch(err => console.log(err))

  }, []);

  return (
    <div>
      <h2>카테고리 목록</h2>
      <ul>
        {categories.map(category => (
          <li key={category.id}>{category.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CategoryPage
