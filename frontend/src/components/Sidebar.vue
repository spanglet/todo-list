<template>
  <!-- Sidebar allows changes to the user's view of the list -->

  <div class="sidebar">
    <SidebarTile
      text="Lists"
      @view-form="toggleForm"
      @list-removed="removeList"
      @list-changed="changeList"
    />
    <div
      v-if="showForm"
      class="list-form">
      <input
        v-model="name"
        type="text"
        placeholder="Name"
      >
      <Button
        :btn-type="submitIcon"
        :action="createList"
      />
    </div>
  </div>

</template>


<script>

  import SidebarTile from "./SidebarTile.vue"
  import Button from "./Button.vue"

  export default {
    components: {
      SidebarTile,
      Button
    },
    inject: ["currentListID"],
    emits: [
      'listChanged',
      'listsUpdated',
      'notification'
    ],
    data() {
      return {
        submitIcon: "check",
        showForm: false,
        name: "",
      }
    },
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
        axios.delete("lists/" + String(list.id))
          .then((res) => {
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

        axios.post("lists/", {
            "name": this.name
          })
          .then((res) => { 
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

