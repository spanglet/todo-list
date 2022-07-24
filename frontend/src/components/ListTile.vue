<template>
  <div class="list-tile">
    <div 
      class="sidebar-expanded-item"
      v-for="list in currentLists"
      :key="list.id"
      :class="{ 'active-list': isActiveList(list.id) }"
      @click="changeList(list.id)">
    
        {{ list.name }}
    
        <SymbolButton
          class="del-btn"
          btn-type="xmark"
          @click="this.$emit('listRemoved', list)"
        />
    
    </div>
    <div
      class="completed-list sidebar-expanded-item"
      @click="changeList(-1)"
      :class="{ 'active-list': isActiveList(-1) }"
    >
      Completed Tasks
    </div>
    
    <SymbolButton
      v-if="expanded"
      icons="['plus']"
      @click="this.$emit('viewForm')"
      class="new-list-btn"
    > New List </SymbolButton>
  </div>
</template>

<script>
  export default {

    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      SymbolButton,
    },
    inject: ['currentLists'],
    emits: ['viewForm','listChanged', "listRemoved"],
    data() {
      return {

      }
    }
  }

</script>


<style>
  .active-list {
    background-color: hsl(var(--hue-purple),100%,var(--lgt-2));
  }
  .new-list-btn {
    background: aquamarine;
    font-size: 18pt;
    justify-content: space-evenly;
  }
  .completed-list {
    border-top: 2px solid black;
    box-shadow: 0px -3px 9px -5px black;
  }

</style>
