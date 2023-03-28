<template>
  <div class="create-pin" v-if="users">
    <h2>Create Pin</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="pin.title" required>
      </div>
      <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" v-model="pin.description" required></textarea>
      </div>
      <div class="form-group">
        <label for="user_id">User:</label>
        <select id="user_id" v-model="pin.user_id" required>
          <option v-for="user in users" :key="user.id" :value="user.id">{{ user.username }}</option>
        </select>
      </div>
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreatePin',
  data() {
    return {
      pin: {
        title: '',
        description: '',
        user_id: null
      },
      users: []
    }
  },
  created() {
    this.loadUsers()
  },
  methods: {
    loadUsers() {
      axios.get('http://localhost:8080/users')
          .then(response => {
            this.users = response.data
            this.pin.user_id = this.users[0].id
          })
          .catch(error => {
            console.log(error)
          })
    },
    submitForm() {
      axios.post('http://localhost:8080/pins', this.pin)
          .then(response => {
            this.$router.push('/pins')
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>