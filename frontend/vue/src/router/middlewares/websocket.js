import Vue from 'vue';
import store from '@/store';
import VueNativeSock from 'vue-native-websocket';


export default function WebSocketMiddleware(router) {
  router.beforeEach((to, from, next) => {
    if (from.meta.ws) {
      Vue.prototype.$disconnect();
      // 离开上一个页面时，断开上一个页面的websocket链接。
      const index = Vue._installedPlugins.indexOf(VueNativeSock);
      if (index > -1) {
        Vue._installedPlugins.splice(index, 1);
      }
    }

    if (to.meta.ws) {
      console.log(to, `/ws${to.path}`);
      Vue.use(VueNativeSock, `//${window.location.host}/ws${to.meta.ws(to)}`, {
        connectManually: true,
        reconnection: true,
        reconnectionAttempts: 5,
        reconnectionDelay: 3000,
        //With format: 'json' enabled
        // All data passed through the websocket is expected to be JSON.
        //
        // Each message is JSON.parsed if there is a data (content) response.
        //
        // If there is no data, the fallback SOCKET_ON* mutation is called with the original event data, as above.
        //
        // If there is a .namespace on the data, the message is sent to this namespaced: true store (be sure to turn this on in the store module).
        //
        // If there is a .mutation value in the response data, the corresponding mutation is called with the name SOCKET_[mutation value], 实际上是[mutation]。
        // 例如.mutation是setBoardData, 那么setBoardData会接收response data
        //
        // If there is an .action value in the response data ie. action: 'customerAdded', the corresponding action customerAdded is called by name:
        format: 'json',
        store,
      });
      Vue.prototype.$connect();
    }
    next();
  });
}
