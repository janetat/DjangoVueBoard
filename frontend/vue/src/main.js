import Vue from 'vue';
import router from './router/index';
import store from './store/index';
import './element-ui/index'

// 引入基本css
import './assets/css/base.css'

new Vue({
  router,
  store,
  el: '#app',
  created() {
    console.log('this.$router.options.routes:', this.$router.options.routes);
    console.log('this.$socket:', this.$socket);
}
});
