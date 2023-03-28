<template>
  <div v-if="pin">
    <h1>Delete Pin {{ pin.id }}</h1>
    <p>Are you sure?</p>
    <button @click="deletePin">Delete</button>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'PinDelete',
  setup() {
    const router = useRouter()
    const pinId = router.currentRoute.value.params.id
    const pin = ref(null)

    axios.get(`http://localhost:8080/pins/${pinId}`)
        .then(response => {
          pin.value = response.data
        })

    function deletePin() {
      axios.delete(`http://localhost:8080/pins/${pinId}`)
          .then(() => {
            router.push('/pins')
          })
    }

    return {
      pin,
      deletePin
    }
  }
}
</script>