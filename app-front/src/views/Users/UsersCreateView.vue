<template>
  <div>
    <h2>Créer un utilisateur</h2>
    <form @submit.prevent="createUser">
      <label>
        Username:
        <input type="text" v-model="username" required />
      </label>
      <br />
      <label>
        Email:
        <input type="email" v-model="email" required />
      </label>
      <br />
      <button type="submit">Créer</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
    };
  },
  methods: {
    async createUser() {
      const response = await axios.post('http://localhost:8080/users', {
        username: this.username,
        email: this.email,
      });
      console.log(response.data);
      // Rediriger vers la liste des utilisateurs après la création réussie
      this.$router.push('/users');
    },
  },
};
</script>