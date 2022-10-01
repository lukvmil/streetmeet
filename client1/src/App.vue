<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view />
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}
</style>
