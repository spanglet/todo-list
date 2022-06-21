<script>

  import TaskList from './components/TaskList.vue'
  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'
  import { computed } from 'vue'

  export default { 

    components: {
      AppHeader,
      Sidebar,
      TaskList
    },
    provide() {
      return {
        currentListID: computed(() => this.currentList),
        currentLists: computed(() => this.lists),
        currentTasks: computed(() => this.currentTasks)  
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
        currentList: 1,
        lists: {}
      }
    },
    mounted() {
      this.loadLists()
      this.loadTasks()
    },
    methods: {

      loadTasks() {
        // Tasks fetched from Flask backend
        this.axios.get("tasks/")
          .then((res) => {
            this.tasks = res.data
          })
      },
      deleteTask(task_id) {
        // DELETE request to remove task from db
        var targetPath = "tasks/" + String(task_id)
        this.axios.delete(targetPath)
          .then((res) => {
            if (res.status == 200) {
              this.reloadList()
            }
          })
      },
      loadLists() {
        // GET request to Flask backend for list
        this.axios.get("lists/")
          .then((res) => {
            this.lists = res.data
          })
      },
      changeActiveList (listID) {
        this.currentList = listID
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
      saveTaskOrder() {
        taskOrder = this.currentTasks.map(({taskID}) => taskID)
        this.axios.put("tasks/",{
            'task_order': taskOrder
          })
      }
    },
    computed: {
      currentTasks() {
        return this.tasks.filter(task => task["listID"] == this.currentList)
      }
    }
  }
</script>

<template>
  <div class='app'>
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
    <div class='list'>
      <TaskList />
    </div>
    <div class="footer"></div>
  </div>
</template>

<style>

  .app {
    display: grid;
    margin: 0;
    grid-template-columns: 2fr 12fr 1fr;
    grid-template-rows: 3fr 17fr 1fr;
    grid-template-areas:
      "header header header"
      "sidebar main edge"
      "footer footer footer";
    height: 100vh;
    width: 100vw;
  } 

  .header {
    grid-area: header;
    margin: 0; 
  }
  .list {
    display: flex;
    grid-area: main;
    align-content: stretch;
    flex-flow: column nowrap;
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
  }
  .sidebar {
    margin: 0;
    grid-area: sidebar;
  }
  .footer {
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
  .list > * {
    flex: 1 100%;
    padding: 5px;
  }
</style>

