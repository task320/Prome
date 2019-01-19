import axios from 'axios'

const state = {
  currentPage: 0,
  pages: 0,
  contents: []
}

const getters = {
  getContent: (state, getters, value) => {
    return getters.contents[value]
  }
}

const mutations = {
  setContents: (state, contents) => {
    state.contents = contents
  },
  setContent: (state, contents, arrayKey) => {
    state.contents[arrayKey] = contents[0]
  },
  setPager: (state, currentPage, pages) => {
    state.currentPage = currentPage
    state.pages = pages
  },
  setPage: (state, currentPage) => {
    state.currentPage = currentPage
  }
}

const actions = {
  getContents: (context) => {
    axios.get(
      'http://localhost:5000/api/contents/all',
      {
        currentPage: 0
      })
      .then(response => {
        if (response.status === 200) {
          context.commit('setContents', response.data.contents)
          context.commit('setPager', response.data.currentPage, response.data.pages)
          return true
        } else {
          alert(response.data.message)
          return false
        }
      })
      .catch(e => {
        alert(e)
        return false
      })
  },
  getContent: (context, arrayKey, contentsId) => {
    axios.get(
      'http://localhost:5000/api/contents/one',
      {
        contentsId: contentsId
      })
      .then(response => {
        if (response.status === 200) {
          context.commit('setContents', response.data.contents, arrayKey)
          return true
        } else {
          alert(response.data.message)
          return false
        }
      })
      .catch(e => {
        alert(e)
        return false
      })
  },
  uploadFile: (context, {title, tags, file}) => {
    let jsonTags = JSON.stringify(tags.split(';'))

    let formData = new FormData()

    formData.append('title', title)
    formData.append('tags', jsonTags)
    formData.append('upload_file', file)

    axios.post(
      'http://localhost:5000/api/file',
      formData
    )
      .then(response => {
        if (response.status === 200) {
          if (context.dispatch('getContents')) {
            alert('SUCCESSED UPLOAD!!')
            return true
          } else {
            return false
          }
        } else {
          alert(response.data.message)
          return false
        }
      })
      .catch(e => {
        alert(e)
        return false
      })
  },
  updateFile: (context, arrayKey, contentsId, title, tags, file) => {
    let jsonTags = JSON.parse(tags.split(';'))

    let formData = new FormData()

    formData.append('contentsId', contentsId)
    formData.append('title', title)
    formData.append('tags', jsonTags)
    formData.append('upload_file', formData)

    axios.put(
      'http://localhost:5000/api/file',
      formData
    )
      .then(response => {
        if (response.status === 200) {
          if (context.dispatch('getContent', arrayKey, contentsId)) {
            alert('SUCCESSED UPDATE!!')
            return true
          } else {
            return false
          }
        } else {
          alert(response.data.message)
          return false
        }
      })
      .catch(e => {
        alert(e)
        return false
      })
  },
  deleteFile: (context, contentsId) => {
    let formData = new FormData()

    formData.append('contentsId', contentsId)

    axios.delete(
      'http://localhost:5000/api/file',
      formData
    )
      .then(response => {
        if (response.status === 200) {
          if (context.dispatch('getContents')) {
            alert('SUCCESSED DELETE!!')
            return true
          } else {
            return false
          }
        } else {
          alert(response.data.message)
          return false
        }
      })
      .catch(e => {
        alert(e)
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
