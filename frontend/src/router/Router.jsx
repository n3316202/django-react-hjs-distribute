import { createBrowserRouter } from 'react-router-dom'
import MainPage from '../src/ui/pages/MainPage';

import MainLayout from '../src/ui/layouts/MainLayout';
import CategoryPage from '../src/ui/pages/CategoryPage';


//dev_5
const routes = [
  {
    path: '/',
    element: <MainLayout />,
    loader: () => '메인 레이아웃',
    children: [
      {
        path: '', 
        element: <MainPage></MainPage>,
        loader: () => '메인페이지',
      },
      {
        path: 'categories', 
        element: <CategoryPage></CategoryPage>,
        loader: () => '메인페이지',
      },    
    ]  
  },
];

const router = createBrowserRouter(routes)

export { router, routes }