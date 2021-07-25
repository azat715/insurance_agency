<template>
  <main>
    <div class="main_wrapper">
      <div class="products">
        <h4>Список продуктов</h4>
        <div class="uk-margin">
          <select v-model="type" class="uk-select">
            <option disabled value="">Выберите тип страховки</option>
            <option value="AUTO">Автомобиль</option>
            <option value="HOME">Недвижимость</option>
            <option value="LIFE">Жизнь</option>
          </select>
        </div>
        <div class="uk-inline">
          <span>Name Filter</span>
          <input v-model="name" class="uk-input" />
        </div>
        <ul class="uk-list">
          <ProductItem
            v-for="product in products"
            v-bind:product="product"
            v-bind:key="product.id"
          ></ProductItem>
        </ul>
      </div>
    </div>
  </main>
  <Footer></Footer>
</template>

<script>
import axios from 'axios';
import ProductItem from '@/components/ProductItem.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'Products',
  data() {
    return {
      name: '',
      type: '',
      products: [],
    };
  },
  methods: {
    getProducts(params) {
      const path = 'http://localhost:3080/api/products/';
      axios
        .get(path, {
          params,
        })
        .then((res) => {
          this.products = res.data;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getProducts({});
  },
  computed: {
    params() {
      console.log('я вычисляю params');
      const entries = new Map(
        [
          ['name', this.name],
          ['type', this.type],
        ].filter(([, v]) => Boolean(v)),
      );
      const obj2 = Object.fromEntries(entries);
      return obj2;
    },
  },
  watch: {
    params() {
      console.log('params изменился');
      // вот это че нормально?
      const isEmpty = Object.values(this.params).every(
        (x) => x === null || x === '',
      );
      if (isEmpty) {
        this.getProducts({});
      } else {
        this.getProducts(this.params);
      }
    },
  },
  components: {
    ProductItem,
    Footer,
  },
};
</script>
