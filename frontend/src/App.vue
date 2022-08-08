<script>

  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'
  import Footer from './components/Footer.vue'
  import { computed } from 'vue'

  import { useTasks } from './stores/tasks.js'
  import { useLists } from './stores/lists.js'

  export default { 

    setup() {
      const store = useTasks()
      const listStore = useLists()
      return {
        store,
        listStore,
      }
    },
    components: {
      AppHeader,
      Sidebar,
      Footer,
    },
    provide() {
      return {
        currentLists: computed(() => this.listStore.lists),
      }
    },
    data() {
      return {
        tasks: [],
        drag: true,
        notification: {
          notify: false,
          changedItem: ""
        },
        lists: [],
      }
    },
    beforeMount() {
      this.loadLists()
      this.loadTasks()
    },
    mounted() {
      this.$router.push("/app/todo/" + this.store.currentListID)
    },
    methods: {

      loadLists() {
        this.listStore.fetchLists()
      },
      loadTasks() {
        this.store.fetchTasks()
      },
      removeList(list_id) {
        this.listStore.deleteList(list_id)
      },
      setFormVisibility(visible) {
        this.store.taskFormActive = visible
      },
    }
  }
</script>

<template>
  <div class='app' @click='setFormVisibility(false)'>
    <AppHeader class='header' />
    <div
      class="notification header"
      v-show="notification.notify"
    >
      The list _____ has been removed
    </div>
    <Sidebar
      @notification='removeList'
      @lists-updated="loadLists"
      class='sidebar'
    />
    <router-view class="app-main"></router-view>
    <Footer class="footer-area" />
    <div class="edge"></div>
  </div>
</template>

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
      minmax(80px, 1fr)
      minmax(450px, 13fr)
      minmax(80px, 1fr);
    grid-template-areas:
      "header header header header"
      "sidebar app-main app-main-right edge"
      "footer footer footer footer";
    height: 100vh;
    width: 100vw;
    font-family: Helvetica, sans-serif;
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
    margin: 0;
    grid-area: sidebar;
    position: relative;
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
  .notification {
    border-radius: 12px;
    background: hsl(var(--hue-purple), 100%, var(--lgt-5));
    height: 50px;
    width: 120px;
  }
</style>

