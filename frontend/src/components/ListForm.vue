
<template>
  <div class="list-form" @click="showForm = true">
    <div class="list-form-header" v-if="!showForm">
      <div>
        New List
      </div>
      <font-awesome-icon class="icon" icon="plus" />
    </div>
    <div class="list-form-body" v-else>
    <!-- <label for="list-name"> List Name </label> -->
      <input
        v-model="name"
        id="list-name"
        type="text"
      >
      <SymbolButton
        :icons="submitIcon"
        @click.stop="createList"
        class='form-submit-button'
      />
      <SymbolButton
        :icons="cancelIcon"
        @click.stop="hideForm"
        class='form-cancel-button'
      />
    </div>
  </div>

</template>

<script>

  import SidebarTile from "./SidebarTile.vue"
  import SymbolButton from "./SymbolButton.vue"
  import { useLists } from '../stores/lists.js'

  export default {
    setup() {
      const store = useLists()
      return {
        store,
      }
    },
    components: {
      SymbolButton,
    },
    emits: [
      'notification'
    ],
    data() {
      return {
        submitIcon: ["check"],
        cancelIcon: ["xmark"],
        showForm: false,
        name: "",
      }
    },
    methods: {
      hideForm: function () {
        this.showForm = false
      },
      // Creates a new list for user
      createList: function() {
        this.store.addList(this.name)
        this.hideForm()
      },
    },
  }

</script>

<style>
  .list-form {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: stretch;
    gap: .5em;
    width: 100%;
  }
  .list-form-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .list-form input {
    font-size: 18pt;
    width: 100%;
  }
  .list-form-body {
    display: flex;
    gap: 2px;
  }
  .form-submit-button {
    flex: 1;
  }
  .form-cancel-button {
    flex: 1;
  }
</style>
