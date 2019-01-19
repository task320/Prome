<template>
  <div>
    <UploadContents/>
    <Pager/>
    <router-view />
  </div>
</template>

<script>
import UploadContents from './components/UploadContents.vue'
import Pager from './components/Pager.vue'
export default {
  name: 'App',
  data: () => {
  },
  components: {
    UploadContents,
    Pager
  },
  created () {
    this.$store.dispatch('contents/getContents')
  }
}
</script>
