<template>
    <li>
        {{ product.name}}
        <button v-on:click="showForm">Купить</button>
    </li>
    <div v-if="show_form">
      <ProductBuy v-bind:id="product.id" @form-sent="showForm"></ProductBuy>
    </div>
</template>

<script>
import ProductBuy from '@/components/ProductBuy.vue';

export default {
  name: 'ProductItem',
  props: {
    product: Object,
  },
  data() {
    return {
      show_form: false,
    };
  },
  methods: {
    showForm() {
      if (this.show_form) {
        this.show_form = false;
      } else {
        this.show_form = true;
      }
      console.log(this.show_form);
    },
  },
  components: {
    ProductBuy,
  },
};
</script>
