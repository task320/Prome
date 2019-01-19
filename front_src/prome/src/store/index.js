import Vue from 'vue'
import Vuex from 'vuex'
import Contents from './modules/Contents'
import User from './modules/User'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    contents: Contents,
    user: User
  },
  strict: true
})
