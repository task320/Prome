<template>
    <div>
        <table>
            <tr>
                <th>
                    タイトル
                </th>
                <td>
                    <input v-model="contentsTitle" type="text" value="" />
                </td>
            </tr>
            <tr>
                <th>
                    タグ
                </th>
                <td>
                    <input v-model='contentsTags' type="text" value="" />
                </td>
            </tr>
            <tr>
                <th>
                    .md
                </th>
                <td>
                    <input type="file" id='contents' ref='contents' v-on:change="handleContent()" />
                </td>
            </tr>
        </table>
        <input type="button" v-on:click="upload()" value="アップロード" />
    </div>
</template>

<script>
/* eslint-disable */
import {mapActions} from 'vuex'
export default {
  name: 'UploadContents',
  data: () => {
    return {
      contentsTitle: '',
      contentsTags: '',
      file: ''
    }
  },
  methods: {
    ...mapActions({
      uploadFile: 'contents/uploadFile'
    }),
    handleContents: () => {
      this.file = this.$refs.file.files[0]
    },
    upload () {
      this.uploadFile({title: this.contentsTitle, tags: this.contentsTags, file:this.file})
    }
  }
}
</script>
