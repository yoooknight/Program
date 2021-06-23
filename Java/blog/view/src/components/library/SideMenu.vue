<template>
  <el-menu class="categories" default-active="0" @select="handleSelect" active-text-color="red">
    <el-menu-item v-for="(item, i) in categoryList" :key="i" :index="item.index">
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
      categoryList: [
        {'name': '全部', 'index': '0', 'icon': 'el-icon-menu'},
        {'name': '文学', 'index': '1', 'icon': 'el-icon-menu'},
        {'name': '流行', 'index': '2', 'icon': 'el-icon-menu'},
        {'name': '文化', 'index': '3', 'icon': 'el-icon-menu'},
        {'name': '生活', 'index': '4', 'icon': 'el-icon-menu'},
        {'name': '经营', 'index': '5', 'icon': 'el-icon-menu'},
        {'name': '科技', 'index': '6', 'icon': 'el-icon-menu'}
      ]
    }
  }
}
</script>

<style scoped>
  .categories {
    position: fixed;
    margin-left: 50%;
    left: -600px;
    top: 100px;
    width: 150px
  }
</style>
