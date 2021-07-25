import { createApp } from 'vue';
import Vuikit from 'vuikit';
import VuikitIcons from '@vuikit/icons';
import App from './App.vue';
import router from './router';

import '@vuikit/theme';

const app = createApp(App);
app.use(router);
app.use(Vuikit);
app.use(VuikitIcons);
app.mount('#app');
