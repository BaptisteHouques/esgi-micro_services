<template>
  <div v-if="pin">
    <h2>Modifier un Pin</h2>
    <form @submit.prevent="updatePin">
      <label>
        Title:
        <input type="text" v-model="pin.title" required />
      </label>
      <br />
      <label>
        Description:
        <input type="text" v-model="pin.description" required />
      </label>
      <br />
      <button type="submit">Enregistrer</button>
    </form>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      pin: null,
    };
  },
  async created() {
    const pinId = this.$route.params.id;
    const response = await axios.get(`http://localhost:8080/pins/${pinId}`);
    this.pin = response.data;
  },
  methods: {
    async updatePin() {
      const response = await axios.put(
          `http://localhost:8080/pins/${this.pin.id}`,
          this.pin
      );
      // Rediriger vers la liste des Pins après la mise à jour réussie
      this.$router.push('/pins');
    },
  },
};
</script>