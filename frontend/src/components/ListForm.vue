
<template>
  <div class="list-form" @click="showForm = true">
    <SymbolButton
      :icons="plusIcon"
      v-if="!showForm"
      class="list-form-header"
    >
      New List
    </SymbolButton>
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
      />
      <SymbolButton
        :icons="cancelIcon"
        @click.stop="hideForm"
      />
    </div>
  </div>

</template>

<script>

  import SidebarTile from "./SidebarTile.vue"
  import SymbolButton from "./SymbolButton.vue"
  import { useLists } from '../stores/lists.js'

  const store = useLists()

  var submitIcon = ["check"]
  var cancelIcon = ["xmark"]
  var plusIcon =  ["plus"]
  var showForm =  false
  var name =  ""

  function hideForm() {
    this.showForm = false
    this.name = ""
  }
  // Creates a new list for user
  function createList() {
    this.store.addList(this.name)
    this.hideForm()
  }

</script>

<style>
  .list-form {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: stretch;
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
</style>
