<template>
  <el-menu class="categories" default-active="0" @select="handleSelect" active-text-color="red">
    <el-menu-item v-for="(item, i) in categoryList" :key="i" :index="item.id">
      <i :class="item.icon"></i>
      <span slot="title">{{item.name}}</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
console.log('5555555555555')
export default {
  name: 'SideMenu',
  data () {
    return {
      categoryList: []
    }
  },
  mounted () {
    this.loadCategories()
  },
  methods: {
    handleSelect (key, keyPath) {
      this.cid = key
      this.$emit('indexSelect')
      console.log(key, keyPath)
    },
    loadCategories () {
      var _this = this
      this.$axios.get('/categories').then(resp => {
        if (resp && resp.status === 200) {
          _this.categoryList = resp.data.reverse()
        }
      })
    }
  }
}
</script>

<style scoped>
  .categories {
    position: fixed;
    margin-left: 50%;
    left: -800px;
    top: 100px;
    width: 150px
  }
</style>
