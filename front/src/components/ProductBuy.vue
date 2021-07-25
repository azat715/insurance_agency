<template>
  <div class="uk-container uk-container-small">
    <form @submit="onSubmit" @reset="onReset">
      <div>
        <label class="uk-form-label" for="form-text">Name</label>
        <div class="uk-form-controls">
          <input
            class="uk-input"
            id="form-text"
            type="text"
            v-model="buyForm.name"
            placeholder="Name field"
          />
        </div>
      </div>
      <div>
        <label class="uk-form-label" for="form-email">Email</label>
        <div class="uk-form-controls">
          <input
            class="uk-input"
            id="form-email"
            type="email"
            v-model="buyForm.email"
            placeholder="Email field"
          />
        </div>
      </div>
      <div>
        <label class="uk-form-label" for="form-telephone">Telephone</label>
        <div class="uk-form-controls">
          <input
            class="uk-input"
            id="form-telephone"
            type="tel"
            v-model="buyForm.telephone"
            placeholder="Telefon field"
          />
        </div>
      </div>
      <button class="uk-button uk-button-default" type="submit">Submit</button>
      <button class="uk-button uk-button-default" type="reset">Reset</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProductBuy',
  props: {
    id: Number,
  },
  data() {
    return {
      buyForm: {
        name: '',
        email: '',
        telefon: '',
      },
    };
  },
  methods: {
    buyPOST(payload) {
      const path = 'http://localhost:3080/api/products/';
      console.log(payload);
      axios
        .post(path, payload)
        .then(() => {
          console.log('success');
          this.$emit('formSent');
          this.initForm();
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.log(error);
        });
    },
    initForm() {
      this.buyForm.name = '';
      this.buyForm.email = '';
      this.buyForm.telefon = '';
    },
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        product: this.id,
        name: this.buyForm.name,
        email: this.buyForm.email,
        telephone: this.buyForm.telephone,
      };
      this.buyPOST(payload, event);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$emit('formSent');
      this.initForm();
    },
  },
};
</script>
