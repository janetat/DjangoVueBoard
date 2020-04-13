import Vue from 'vue';
import App from './App';
import router from './router/index';
import store from './store/index';

import './element-ui/index'
import './assets/css/base.css'

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
  created() {
    console.log('this.$router.options.routes:', this.$router.options.routes);
    console.log('this.$socket:', this.$socket);
}
}).$mount('#app');
