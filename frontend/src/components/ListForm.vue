
<template>
  <div class="list-form">
    <label for="list-name"> List Name </label>
    <input
      v-model="name"
      id="list-name"
      type="text"
      placeholder="Name"
    >
    <SymbolButton
      :icons="submitIcon"
      @click="createList"
    />
  </div>

</template>


<script>

  import SidebarTile from "./SidebarTile.vue"
  import SymbolButton from "./SymbolButton.vue"

  export default {
    components: {
      SymbolButton,
    },
    emits: [
      'listChanged',
      'listsUpdated',
      'notification'
    ],
    data() {
      return {
        submitIcon: ["check"],
        showForm: false,
        name: "",
      }
    },
    methods: {
      // Creates a new list for user
      createList: function () {

        this.axios.post("lists/", {
            "name": this.name
          })
          .then((res) => { 
            // Emit to parent container so list is updated
            if (res.status == 200) {
              this.$emit("listsUpdated")
              this.showForm = !this.showForm
            }
          })
      },
    }
  }

</script>

<style>



</style>
