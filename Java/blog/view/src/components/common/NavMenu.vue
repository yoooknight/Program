<template>
  <el-menu :default-active="'/index'" router class="el-menu-demo" mode="horizontal" @select="handleSelect" style="position: fixed;width:1200px">
    <el-menu-item v-for="(item, i) in navList" :key="i" :index="item.name">
            {{ item.navItem}}
    </el-menu-item>
    <a href="#nowhere" style="color: #222;float: right;padding:20px;">更多功能</a>
    <i class="el-icon-menu" style="float:right;font-size: 45px;color: #222;padding-top: 8px"></i>
    <span style="position: fixed;padding-top: 20px;right: 43%;font-size: 20px;font-weight: bold">White Jotter - Your Mind Palace</span>
  </el-menu>
</template>

<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      navList: [
        {name: '/index', navItem: '首页'},
        {name: '/jotter', navItem: '笔记本'},
        {name: '/library', navItem: '图书馆'},
        {name: '/admin', navItem: '个人中心'}
      ]
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      this.cid = key
      this.$emit('indexSelect')
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
  a{
    text-decoration: none;
  }

  span {
    pointer-events: none;
  }
</style>
