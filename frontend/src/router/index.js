import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Auth from '@/components/pages/Auth'
import AddSongRecommendation from '@/components/pages/AddSongRecommendation'
import Events from '@/views/Events.vue'
import GetSongRecommendation from '@/components/pages/GetSongRecommendation'
import HomeDiscussion from '@/components/pages/HomeDiscussion'
import Discussion from '@/components/pages/Discussion'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/events',
    name: 'Events',
    component: Events
  },
  {
    path: '/songrecommendation',
    name: 'AddSongRecommendation',
    component: AddSongRecommendation
  },
  {

    path: '/getsongrecommendation',
    name: 'GetSongRecommendation',
    component: GetSongRecommendation
  },
  // {
  //   path: '/discussion',
  //   name: 'HomeDiscussion',
  //   component: HomeDiscussion
  // },
  // {
  //   path: '/discussiontopic',
  //   name: 'Discussion',
  //   component: Discussion
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
