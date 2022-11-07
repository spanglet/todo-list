<template>

  <div class="list-header">
    <div class="col-header"> Task Name </div>
    <div class="col-header date-col"> Due Date </div>
    <div class="button-col">
      <SymbolButton
        :icons="buttonIcons"
        @click.stop="changeFormVisibility"
        class="list-header-button"
      >
        New Task
      </SymbolButton>
    </div>
  </div>

</template>

<script setup>

  import SymbolButton from "./SymbolButton.vue"
  import { useTasks } from "../stores/tasks.js"

  const store = useTasks()
  
  const buttonIcons =  ["plus", "minus"]

  function changeFormVisibility() {
    store.taskFormActive = !store.taskFormActive
  }

</script>

<style>

  .list-header {
    display: flex;
    justify-content: center;
    align-items: stretch;
    color: #fdfdfd;
    font-size: 1.75em;
    margin: .4em;
    border-radius: 8px;
    border: 1px solid black;
    background: hsl(var(--hue-purple), 100%, var(--lgt-4 ));
    box-shadow: 0 4px 8px -7px black;
    padding: .25em;
  }
  .col-header {
    display: flex;
    flex: 4;
    text-align: center;
    align-items: center;
    justify-content: center;
    border-right: 2px solid black;
  }
  .button-col {
    display: flex;
    flex: 1;
    align-items: stretch;
    justify-content: center;
  }
  .list-header-button {
    display: flex;
    justify-content: space-between;
    gap: .5em;
    font-size: .8em;
    padding: .4em;
  }
  .date-col {
    flex: 1;
  }

</style>
