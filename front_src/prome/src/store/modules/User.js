import axios from 'axios'

const state = {
  authorized: 0
}

const getters = {
  isAuthorized: (state) => {
    return state.authorized
  }
}

const mutations = {
  changeAuthorized: (state, value) => {
    state.authorized = value
  }
}

const actions = {
  login: (context) => {
    axios.post('http://localhost:5000/api/user/login')
      .then(response => {
        if (response.status === 200) {
          context.commit('changeAuthorized', 1)
          alert('SUCCESSED LOGIN!!')
          return true
        }
      })
      .catch(e => {
        alert(e)
        return false
      })
  },
  logout: (context) => {
    axios.post('http://localhost:5000/api/user/logout')
      .then(response => {
        if (response.status === 200) {
          context.commit('changeAuthorized', 0)
          alert('SUCCESSED LOGOUT!!')
          return true
        }
      })
      .catch(e => {
        alert(e)
        return false
      })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
