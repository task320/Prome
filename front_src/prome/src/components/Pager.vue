<template>
    <div>
        <span>
            ページ:
        </span>
        <span v-for="(n, index) in pages" :key="index">
            <div v-if="n == current_page">
                {{ n }}{{ separate(n, current_page) }}
            </div>
            <router-link v-else :to="{name: 'page', params: {page: n}}" >
                {{ n }}{{ separate(n, current_page) }}
            </router-link>

        </span>

    </div>
</template>

<script>
export default {
  name: 'Pager',
  props: [
    'pages',
    'current_page'
  ],
  methods: {
    // eslint-disable-next-line
    separate: (n, current_page) => {
      // eslint-disable-next-line
      return n >= pages.length ? '' : ','
    }
  }
}
</script>
