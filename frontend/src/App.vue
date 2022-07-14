<script>

  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'
  import Footer from './components/Footer.vue'
  import { computed } from 'vue'

  import { useTasks } from './stores/tasks.js'

  export default { 

    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      AppHeader,
      Sidebar,
      Footer,
    },
    provide() {
      return {
        currentLists: computed(() => this.lists),
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
        lists: {},
      }
    },
    beforeMount() {
      this.loadLists()
      this.store.fetchTasks()
    },
    mounted() {
      this.$router.push("/app/todo")
    },
    methods: {

      loadLists() {
        // GET request to Flask backend for list
        this.axios.get("lists/")
          .then((res) => {
            this.lists = res.data
          })
      },
      changeActiveList (listID) {
        this.store.filter = 'none'
        this.store.currentListID = listID
        setTimeout(() => {
          this.store.filter = 'currentList'
        }, 1000)
      },
      removeList (list) {

        this.loadLists()

        //notify user of action for 3 seconds
        this.notification.notify = true
        this.notification.changedItem = list
        setTimeout(function() { console.log("Timout completed")
        }, 3000)
        this.notification.notify = false
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
      @list-changed='changeActiveList'
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
      minmax(120px, 2fr)
      minmax(400px, 8fr)
      minmax(300px, 4fr)
      minmax(20px, 1fr);
    grid-template-rows:
      minmax(60px, 2fr)
      minmax(60px, 1fr)
      minmax(450px, 15fr)
      minmax(80px, 2fr);
    grid-template-areas:
      "header header header header"
      "sidebar app-header app-header edge"
      "sidebar app-main app-main-right edge"
      "footer footer footer footer";
    height: 100vh;
    width: 100vw;
    font-family: Helvetica, sans-serif;
  } 
  .app-main {
    grid-area: app-header / app-main / app-main / app-main-right;
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
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

