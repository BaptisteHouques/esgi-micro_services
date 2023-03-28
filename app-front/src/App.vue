<script>
export default {
  name: 'App'
}

</script>
<template>
  <div>
    <header>
      <nav>
          <router-link to="/users">Users</router-link>
          <router-link to="/users/new">New User</router-link>
          <router-link to="/pins">Pins</router-link>
          <router-link to="/pins/new">New Pin</router-link>
      </nav>
    </header>
    <div id="app-container">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
header {
}

nav {
  width: 25%;
  display: flex;
  justify-content: space-around;
}

header a {
  font-size: 16px;
}

#app-container {
  margin: 20px;
}
</style>
