<template>
  <div v-if="pins">
    <h2>Pins</h2>
    <table>
      <thead>
      <tr>
        <th>ID</th>
        <th>Title</th>
        <th>Description</th>
        <th>User</th>
        <th>Modifier</th>
        <th>Supprimer</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="pin in pins" :key="pin.id">
        <td>{{ pin.id }}</td>
        <td>{{ pin.title }}</td>
        <td>{{ pin.description }}</td>
        <td><router-link :to="{ name: 'UsersUpdate', params: { id: pin.user_id } }">Voir</router-link></td>
        <td><router-link :to="{ name: 'PinsUpdate', params: { id: pin.id } }">Modifier</router-link></td>
        <td><router-link :to="{ name: 'PinsDelete', params: { id: pin.id } }">Supprimer</router-link></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PinList',

  data() {
    return {
      pins: []
    }
  },

  mounted() {
    axios.get('http://localhost:8080/pins')
        .then(response => {
          this.pins = response.data
        })
        .catch(error => {
          console.log(error)
        })
  },

  methods: {
    deletePin(id) {
      if (confirm('Are you sure you want to delete this pin?')) {
        axios.delete(`http://localhost:8080/pins/${id}`)
            .then(response => {
              const index = this.pins.findIndex(pin => pin.id === id)
              this.pins.splice(index, 1)
            })
            .catch(error => {
              console.log(error)
            })
      }
    }
  }
}
</script>

<style scoped>
</style>