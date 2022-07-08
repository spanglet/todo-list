<template>
  <div class="list-tile">
    <div 
      class="sidebar-expanded-item"
      v-for="list in currentLists"
      :key="list.id"
      :class="{ 'active-list': isActiveList(list.id) }"
      @click="changeList(list.id)">
    
        {{ list.name }}
    
        <Button
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
    
    <Button
      class="new-list-btn"
      v-if="expanded"
      btn-type="plus"
      @click="this.$emit('viewForm')"
    > New List </Button>
  </div>
</template>

<script>
  export default {

  }
</script>


<style>

</style>
