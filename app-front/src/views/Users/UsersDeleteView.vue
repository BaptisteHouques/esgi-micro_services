<template>
  <div v-if="user">
    <h1>Delete User {{ user.id }}</h1>
    <p>Are you sure?</p>
    <button @click="deleteUser">Delete</button>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'UserDelete',
  setup() {
    const router = useRouter()
    const userId = router.currentRoute.value.params.id
    const user = ref(null)

    axios.get(`http://localhost:8080/users/${userId}`)
        .then(response => {
          user.value = response.data
        })

    function deleteUser() {
      axios.delete(`http://localhost:8080/users/${userId}`)
          .then(() => {
            router.push('/users')
          })
    }

    return {
      user,
      deleteUser
    }
  }
}
</script>