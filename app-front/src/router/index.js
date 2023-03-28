import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/users',
      name: 'Users',
      component: () => import('@/views/Users/UsersListView.vue'),
    },
    {
      path: '/users/new',
      name: 'UsersCreate',
      component: () => import('@/views/Users/UsersCreateView.vue'),
    },
    {
      path: '/users/:id/update',
      name: 'UsersUpdate',
      component: () => import('@/views/Users/UsersUpdateView.vue'),
      props: true,
    },
    {
      path: '/users/:id/delete',
      name: 'UsersDelete',
      component: () => import('@/views/Users/UsersDeleteView.vue'),
      props: true,
    },
    {
      path: '/pins',
      name: 'Pins',
      component: () => import('@/views/Pins/PinsListView.vue'),
    },
    {
      path: '/pins/new',
      name: 'PinCreate',
      component: () => import('@/views/Pins/PinsCreateView.vue'),
    },
    {
      path: '/pins/:id/update',
      name: 'PinsUpdate',
      component: () => import('@/views/Pins/PinsUpdateView.vue'),
      props: true,
    },
  ]
})

export default router
