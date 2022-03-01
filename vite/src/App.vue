<script>

  import TaskTile from './components/TaskTile.vue'
  import ListHeader from './components/ListHeader.vue'
  import AppHeader from './components/AppHeader.vue'
  import Sidebar from './components/Sidebar.vue'

  var url = "http://127.0.0.1:5000/tasks/list"
  var base_url = "http://127.0.0.1:5000/tasks/"

  // Headers for Cross-Origin access to Flask backend
  var config = { headers: {'Access-Control-Allow-Origin': '*' } }

  export default { 

    components: {
      TaskTile,
      ListHeader,
      AppHeader,
      Sidebar
    },
    data() {
      return {
        name: "",
        description: "",
        tasks: {}
      }
    },
    mounted() {
      this.reloadList()
    },
    methods: {

      reloadList() {
        // GET request to Flask backend for list
        axios.get(url, config
	        ).then((res) => {
            this.tasks = res.data
          })
      },
      deleteTask(task_id) {
        // DELETE request to remove task from db
        var target = base_url + String(task_id)
        axios.delete(target, config
          ).then((res) => {
            if (res.status == 200) {
              this.reloadList()
              // todo: remove element rather than reload list (time intensive)
            }
          })
      }
    }
  }
</script>

<template>
  <div class='app'>
    <AppHeader class='header'></AppHeader>
    <Sidebar class='sidebar'></Sidebar>
    <div class='list'>
      <ListHeader class="item" @view-changed='reloadList'></ListHeader>
      <div v-for='task in tasks'>
        <TaskTile class="item" :name="task.name" :description="task.description"
            @remove-item='deleteTask(task.taskID)'>
        </TaskTile>
      </div>
    </div>
    <div class="footer"></div>
  </div>
</template>

<style>

  .app {
    display: grid;
    margin: 0;
    grid-template-columns: 10% 80% 10%;
    grid-template-rows: 10% 85% 5%;
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
    grid-area: sidebar;
    margin: 0;
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
    flex-grow:1;
   }
</style>

