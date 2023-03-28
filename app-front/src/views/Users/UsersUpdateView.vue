<template>
  <div v-if="user">
    <h2>Modifier un utilisateur</h2>
    <form @submit.prevent="updateUser">
      <label>
        Username:
        <input type="text" v-model="user.username" required />
      </label>
      <br />
      <label>
        Email:
        <input type="email" v-model="user.email" required />
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
      user: null,
    };
  },
  async created() {
    const userId = this.$route.params.id;
    const response = await axios.get(`http://localhost:8080/users/${userId}`);
    this.user = response.data;
  },
  methods: {
    async updateUser() {
      const response = await axios.put(
          `http://localhost:8080/users/${this.user.id}`,
          this.user
      );
      console.log(response.data);
      // Rediriger vers la liste des utilisateurs après la mise à jour réussie
      this.$router.push('/users');
    },
  },
};
</script>