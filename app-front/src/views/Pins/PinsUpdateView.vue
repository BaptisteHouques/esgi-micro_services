<template>
  <div>
    <h2>Update Pin</h2>
    <form @submit.prevent="updatePin">
      <div>
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="pin.title" required>
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="pin.description" required></textarea>
      </div>
      <div>
        <label for="user">User:</label>
        <select id="user" v-model="pin.user_id" required>
          <option v-for="user in users" :key="user.id" :value="user.id">{{ user.username }}</option>
        </select>
      </div>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'PinUpdate',
  computed: {
    ...mapGetters(['getUserById']),
    users() {
      return this.$store.state.users
    },
  },
  data() {
    return {
      pin: {
        id: this.$route.params.id,
        title: '',
        description: '',
        user_id: '',
      },
    }
  },
  created() {
    const pin = this.$store.getters.getPinById(this.pin.id)
    this.pin.title = pin.title
    this.pin.description = pin.description
    this.pin.user_id = pin.user_id
  },
  methods: {
    ...mapActions(['updatePin']),
  },
}
</script>
