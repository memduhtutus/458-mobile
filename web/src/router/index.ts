import { createRouter, createWebHistory } from 'vue-router'
import SigninView from '@/views/SigninView/'
import HomeView from '@/views/HomeView/'
// import { onAuthStateChanged } from 'firebase/auth'
// import { auth } from '@/config/firebase'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      // meta: {
      //   requiresAuth: true,
      // },
    },
    {
      path: '/signin',
      name: 'signin',
      component: SigninView,
      meta: {
        onlyGuest: true,
      },
    },
  ],
})

// router.beforeEach((to, from, next) => {
//   onAuthStateChanged(auth, (user) => {
//     console.log('user', user)
//     if (to.meta.requiresAuth && !user) {
//       next('/signin')
//     } else if (to.meta.onlyGuest && user) {
//       next('/')
//     } else {
//       next()
//     }
//   })
// })

export default router
