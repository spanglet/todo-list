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

  data() {
    return {

    }
  }

  }
</script>


<style>

</style>
