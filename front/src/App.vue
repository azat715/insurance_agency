<template>
<header>
  <div class="logo"> <img src="/logo/logo.png" width=293 height=125 alt="logo"></div>
  <nav>
      <div id="nav">
        <ul class="uk-nav">
          <router-link to="/">Products</router-link>
        </ul>
      </div>
  </nav>
</header>
<router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
