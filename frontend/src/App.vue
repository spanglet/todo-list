<script>

  import TaskTile from './components/TaskTile.vue'
  import ListHeader from './components/ListHeader.vue'
  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'
  import draggable from 'vuedraggable/src/vuedraggable.js'
  import { computed } from 'vue'

  var base_url = "http://127.0.0.1:5000/"
  var task_url = base_url + "tasks/"
  var list_url = base_url + "lists/"
  // Headers for Cross-Origin access to Flask backend
  var config = { headers: {'Access-Control-Allow-Origin': '*' } }

  export default { 

    components: {
      TaskTile,
      ListHeader,
      AppHeader,
      Sidebar,
      draggable
    },
    data() {
      return {
        config: {
          tasks: [],
          drag: true
        },
        currentList: 1,
        lists: {}
      }
    },
    mounted() {
      this.reloadList()
      this.getLists()
    },
    provide() {
      return {
        currentListID: computed(() => this.currentList)
      }
    },
    methods: {

      reloadList() {
        // GET request to Flask backend for list
        axios.get(task_url, config
	        ).then((res) => {
            this.config.tasks = res.data
          })
      },
      deleteTask(task_id) {
        // DELETE request to remove task from db
        var target = task_url + String(task_id)
        axios.delete(target, config
          ).then((res) => {
            if (res.status == 200) {
              this.reloadList()
            }
          })
      },
      getLists() {
        // GET request to Flask backend for list
        axios.get(list_url, config
	        ).then((res) => {
            this.lists = res.data
          })
      },
      changeActiveList (listID) {
        this.currentList = listID
      }
    },
    computed: {

      activeListTasks () {
        return this.config.tasks.filter(task => task["listID"] == this.currentList)
      }
    }
  }
</script>

<template>
  <div class='app'>
    <AppHeader class='header'></AppHeader>
    <Sidebar @list-changed='changeActiveList' @lists-updated="getLists" :lists="lists" class='sidebar'></Sidebar>
    <div class='list'>
      <ListHeader class="item" @view-changed='reloadList'></ListHeader>

      <draggable 
        :list="activeListTasks" 
        @start="config.drag=true" 
        @end="config.drag=false" 
        item-key="taskID"
        class="list-group"> <template #item="{ element }">

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
    grid-template-rows: 2fr 10fr 1fr;
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

  .list {
    display: flex;
    grid-area: main;
    align-content: flex-start;
    align-items: flex-start;
    flex-flow: row wrap;
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
  }
  .list > * {
    flex: 1 100%;
    padding: 5px;
  }
  .item  {
    flex-grow: 1;
  }
</style>

