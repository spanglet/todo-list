<template>

  <div class='app' @click='setFormVisibility(false)'>
    <AppHeader class='header' />
    <Sidebar
      class='sidebar'
    />
    <router-view class="app-main"></router-view>
    <Footer class="footer-area" />
    <div class="edge"></div>
  </div>

</template>

<script setup>

  import { computed, onMounted, onBeforeMount, ref, provide } from 'vue'
  import { useRouter } from 'vue-router'

  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'
  import Footer from './components/Footer.vue'
  import { useTasks } from './stores/tasks.js'
  import { useLists } from './stores/lists.js'

  const store = useTasks()
  const listStore = useLists()
  const router = useRouter()

  onBeforeMount(() => {
    listStore.fetchLists()
    store.fetchTasks()
  })
  onMounted(() => {
    router.push("/app/todo/" + store.currentListID)
  })

  function setFormVisibility(visible) {
    store.taskFormActive = visible
  }

</script>

<style>

  * {
    margin: 0;
    padding: 0;
  }
  a {
    color: inherit;
    text-decoration: inherit;
  }
  .app {
    display: grid;
    grid-template-columns:
      minmax(140px, 2fr)
      minmax(400px, 5fr)
      minmax(300px, 3fr)
      minmax(20px, 2fr);
    grid-template-rows:
      minmax(70px, 1fr)
      minmax(600px, 13fr)
      minmax(80px, 1fr);
    grid-template-areas:
      "header header header header"
      "sidebar app-main app-main-right edge"
      "footer footer footer footer";
    height: 100vh;
    width: 100vw;
    font-family: Verdana, sans-serif;
  } 
  .app-main {
    grid-area: app-main / app-main / app-main / app-main-right;
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
    padding: 5px;
    z-index: 1;
  }
  .header {
    grid-area: header;
  }
  .sidebar {
    grid-area: sidebar;
    position: relative;
    background: hsl(var(--hue-purple),100%,var(--lgt-3));
    box-shadow: 4px 0px 8px -7px black;
  }
  .edge {
    grid-area: edge;
    background: hsl(var(--hue-purple), 100%, var(--lgt-4));
  }
  .footer-area {
    grid-area: footer;
    background: #b3b6b7;
    margin: 0;
  }
</style>

