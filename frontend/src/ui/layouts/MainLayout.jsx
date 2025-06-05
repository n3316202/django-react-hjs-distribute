import React from 'react'
import { Outlet } from 'react-router-dom'


//dev_5
const MainLayout = () => {
  return (
    <div className='vh-100 d-flex flex-column justify-content-between'>
      <Outlet />
    </div>
  )
}

export default MainLayout