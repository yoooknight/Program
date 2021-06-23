// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

// 引入element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 设置反向代理，抢断请求默认发送到http://localhost:8843/api
var axios = require('axios')
axios.defaults.baseURL = 'http://127.0.0.1:8445/api'
// 全局注册，之后可在其他组件中通过this.$axios发送数据
Vue.prototype.$axios = axios

Vue.config.productionTip = false

Vue.use(ElementUI)

// 这个需要放在前面才能生效，否则没有效果
router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.user.username) {
      console.log('1111111111111')
      next()
    } else {
      console.log('222222222')
      next({
        path: 'login',
        qurey: {redirect: to.fullPath}
      })
    }
  } else {
    console.log('3333333333')
    next()
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store,
  components: { App },
  template: '<App/>'
})
