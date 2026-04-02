import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import useUserStore from '@/stores/userSotre'

const routes: RouteRecordRaw[] = [
  {
    path: '',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
    children: [
      {
        path: '',
        name: 'HomeRoot',
        redirect: {name: 'Introduce'}
      },
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
        path: 'userCenter',
        name: 'UserCenter',
        meta: { requireLogged: true },
        component: () => import('@/pages/home/UserCenter.vue')
      }
    ]
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('@/pages/Auth.vue')
  },
  {
    path: '/writing',
    name: 'Writing',
    meta: { requireLogged: true },
    component: () => import('@/pages/Writing.vue')
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// 添加路由守卫
router.beforeEach((to) => {
  const userStore = useUserStore()

  // 检查是否需要登录访问限制
  if (to.meta.requireLogged) {
    // 如果未登录则返回根路由
    if (!userStore.isLogged) {
      userStore.logout()
      return {path: '/', replace: true}
    }
  }

  // 如果登录且访问auth页面则拒绝跳转
  if (to.name === 'Auth' && userStore.isLogged) {
    return false
  }

  return true
})

export default router
