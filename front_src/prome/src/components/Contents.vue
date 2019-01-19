<template>
    <div>
        <div v-for="(content, index) in this.contnets" :key="index">
            <div>
                <div>
                    {{ content.title }}
                </div>
                <div>
                    作成:{{ content.upload_at }}/更新:{{ content.update_at }}
                </div>
            </div>
            <div v-html="content.content">
            </div>
            <div>
                <div v-for="tag in content.tags" :key="tag">
                    {{ tag }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
export default {
  name: 'Contents',
  computed: {
    ...mapState([
      'contents'
    ]),
    ...mapMutations([
      'setPage'
    ]),
    ...mapActions([
      'getContents'
    ])
  },
  watch: {
    '$route' (to, from) {
      let page = this.$route.params.page ? this.$route.params.page : 0
      this.$store.commit('contents/setPage', page)
      this.$store.dispatch('contents/getContents')
    }
  }
}
</script>
