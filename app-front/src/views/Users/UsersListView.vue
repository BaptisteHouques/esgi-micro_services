<template>
  <div>
    <h2>Liste des utilisateurs</h2>
    <table>
      <thead>
      <tr>
        <th>Id</th>
        <th>Username</th>
        <th>Email</th>
        <th>Modifier</th>
        <th>Supprimer</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.email }}</td>
        <td><router-link :to="{ name: 'UsersUpdate', params: { id: user.id } }">Modifier</router-link></td>
        <td><router-link :to="{ name: 'UsersDelete', params: { id: user.id } }">Supprimer</router-link></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    };
  },
  async mounted() {
    const response = await axios.get('http://localhost:8080/users');
    this.users = response.data;
  },
};
</script>