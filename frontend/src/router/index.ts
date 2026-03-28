import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
    children: [
      {
        path: 'introduce',
        name: 'Introduce',
        component: () => import('@/pages/home/Introduce.vue')
      },
      {
        path: 'myNovels',
        name: 'MyNovels',
        meta: { requireLogged: true },
        component: () => import('@/pages/home/MyNovels.vue')
      },
      {
        path: 'writing',
        name: 'Writing',
        meta: { requireLogged: true },
        component: () => import('@/pages/home/Writing.vue')
      }
    ]
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('@/pages/Auth.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
