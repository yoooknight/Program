<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <switch></switch>
      <SideMenu @indexSelect="listByCategory" ref="sideMenu"></SideMenu>
    </el-aside>
    <el-main>
      <books class="books-area" ref="booksArea" style="position:fixed; left:260px; top:100px; width:1000px"></books>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './SideMenu'
import Books from './Books'
export default {
  name: 'AppLibrary',
  components: {SideMenu, Books},
  methods: {
    listByCategory () {
      var _this = this
      var cid = this.$refs.sideMenu.cid
      var pagesize = this.$refs.booksArea.pagesize
      var currentPage = 1

      console.log(currentPage)
      console.log(pagesize)

      var url = 'categories/' + cid + '/books/' + currentPage + '/' + pagesize

      console.log(url)

      this.$axios.get(url).then(resp => {
        if (resp && resp.status === 200) {
          _this.$refs.booksArea.books = resp.data.content
          _this.$refs.booksArea.cid = cid
          _this.$refs.booksArea.total = resp.data.totalElements
        }
      })
    }
  }
}
</script>

<style scoped>
  .book-area {
    width: 990px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 200px;
  }
</style>
