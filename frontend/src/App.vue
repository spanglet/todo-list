<script>

  import TaskTile from './components/TaskTile.vue'
  import ListHeader from './components/ListHeader.vue'
  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'
  import draggable from 'vuedraggable/src/vuedraggable.js'
  import { computed } from 'vue'

  /* var base_url = "http://127.0.0.1:5000/" */
  /* var task_url = base_url + "tasks/" */
  /* var list_url = base_url + "lists/" // Headers for Cross-Origin access to Flask backend */
  /* var config = { headers: {'Access-Control-Allow-Origin': '*' } } */

  export default { 

    components: {
      TaskTile,
      ListHeader,
      AppHeader,
      Sidebar,
      draggable
    },
    provide() {
      return {
        currentListID: computed(() => this.currentList),
        currentLists:  computed(() => this.lists)
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
        lists: {},
        currentTasks: []
      }
    },
    mounted() {
      this.loadTasks()
      this.loadLists()
    },
    beforeUnmount() {
      this.saveTaskOrder()   
    },
    methods: {

      loadTasks() {
        // Tasks fetched from Flask backend
        axios.get("tasks/")
          .then((res) => {
            this.tasks = res.data
          })
      },
      deleteTask(task_id) {
        // DELETE request to remove task from db
        var targetPath = "tasks/" + String(task_id)
        axios.delete(targetPath)
          .then((res) => {
            if (res.status == 200) {
              this.reloadList()
            }
          })
      },
      loadLists() {
        // GET request to Flask backend for list
        axios.get("lists/")
          .then((res) => {
            this.lists = res.data
          })
      },
      changeActiveList (listID) {
        this.currentList = listID
        this.currentTasks = this.getActiveTasks()
      },
      removeList (list) {

        this.getLists()

        //notify user of action for 3 seconds
        this.notification.notify = true
        this.notification.changedItem = list
        setTimeout(function() {
          this.notification.notify = false
        }, 3000)
      },
      getActiveTasks () {
         return this.tasks.filter(task => task["listID"] == this.currentList)
      },
      saveTaskOrder() {
        axios.post("tasks/",{
            this.
          })
          .then((res) => {
          })
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
      @lists-updated="getLists"
      class='sidebar'
    />
    <div class='list'>
      <ListHeader class="item" @view-changed='loadTasks' />

      <draggable 
        :list="currentTasks" 
        @start="drag=true" 
        @end="drag=false" 
        item-key="taskID"
        ghost-class="ghost"
        class="list-group">
        <template #item="{ element }">

          <TaskTile class="list-group-item item"
              :name="element.name"
              :description="element.description"
              :dueDate="element.trueDueDate"
              @remove-item='deleteTask(element.taskID)'>
          </TaskTile>

        </template>
      </draggable>

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
  .list {
    display: flex;
    grid-area: main;
    align-content: flex-start;
    align-items: flex-start;
    flex-flow: row wrap;
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
  }
  .list-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 3px;
  }
  .ghost {
    opacity: 0.5;
    background: lightblue; 
  }
  .list > * {
    flex: 1 100%;
    padding: 5px;
  }
  .item  {
    flex-grow: 1;
  }
</style>

