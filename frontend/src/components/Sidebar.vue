<template>

  <div class="sidebar">
    <SidebarTile @view-form="toggleForm"  @list-removed="removeList" @list-changed="changeList" text="Lists" :lists="lists" />
    <div v-if="showForm" class="list-form">
      <input type="text" placeholder="Name" v-model="name">
      <Button :btn-type="submitIcon" :action="createList" />
    </div>
  </div>

</template>


<script>

  import SidebarTile from "./SidebarTile.vue"
  import Button from "./Button.vue"

  var url = "http://127.0.0.1:5000/lists/"

  export default {
    data() {
      return {
        submitIcon: "check",
        showForm: false,
        name: "",
      }
    },
    props: ["lists"],
    components: {
      SidebarTile,
      Button
    },
    emits: [
      'listChanged',
      'listsUpdated',
      'notification'
    ],
    methods: {

      // Toggles whether lists are shown in dropdown
      showLists: function () {
        this.listsVisible = !this.listsVisible
      },
      // Change current list view at App component
      changeList: function (list) {
        this.$emit("listChanged", list)
      },
      // Send delete request for list to backend
      removeList: function (list) {
        axios.delete(url + list.id
          ).then((res) => {
            if (res.status == 200) {
              this.$emit("notification",list.name)
            }
          })
      },
      toggleForm: function () {
        this.showForm = !this.showForm
      },
      // Creates a new list for user
      createList: function () {

        axios.post(url, {
            "name": this.name
          },  {
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        }).then((res) => { 
          // Emit to parent container so list is updated
          if (res.status == 200) {
            this.$emit("listsUpdated")
            this.showForm = !this.showForm
          }
        })
      }
    }      
  }

</script>


<style>

  .sidebar {
    display: flex;
    background: hsl(var(--hue-purple),100%,var(--lgt-3));
    color: white;
    flex-flow: column nowrap;
    align-items: stretch;
    margin: 8px;
    gap: 3px;

  }
  
.list-form {
  display: flex;
  justify-content: center;
  align-items: stretch;
  height: 20px;
  

}

</style>

