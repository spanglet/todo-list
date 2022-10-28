import { defineStore, acceptHMRUpdate } from 'pinia'
import Fetch from "../fetch.js"
import { useLists } from "./lists.js"

export const useTasks = defineStore('tasks', {
  state: () => ({
    tasks: [],
    /** @type {'all' | 'completed' | 'incomplete' | 'currentList' | 'none'} */
    filter: 'currentList',
    taskFormActive: false,
  }),
  getters: {
    currentListID(state) {
      return useLists().currentList
    },
    completedTasks(state) {
      return state.tasks.filter((task) => task.completed)
    },
    incompleteTasks(state) {
      return state.tasks.filter((task) => !task.completed)
    },
    currentListTasks(state) {
      return state.tasks.filter((task) => task.listID == this.currentListID && !task.completed)
    },
    /**
     * @returns {{ text: string, id: number, isFinished: boolean }[]}
     */
    filteredTasks(state) {
      if (this.filter === 'completed') {
        return this.completedTasks
      }
      else if (this.filter === 'incomplete') {
        return this.incompleteTasks
      }
      else if (this.filter === 'currentList') {
        return this.currentListTasks
      }
      else if (this.filter === 'none') {
        return []
      }
      return this.tasks
    },
  },
  actions: {
    // Retrieves all tasks owned by active user
    async fetchTasks() {
      var json = await Fetch.get("tasks/")
      if (json.data) {
        this.tasks = json.data
      }
    },
    // Send delete request and remove task from store
    async deleteTask(task) {
      var json = await Fetch.delete("tasks/" + String(task.id))
      if (json.data) {
        this.tasks.splice(this.tasks.indexOf(task), 1)
      }
    },
    // New task is posted to backend
    async addTask(data) {
      var json = await Fetch.post('tasks/', data)
      if (json.data) {
        this.tasks.push(json.data)
      }
    },
    // Marks task as completed after sending update
    async completeTask(task) {
      var json = await Fetch.put("tasks/" + task.id, {'completed': true})
      if (json.data) {
        task.completed = true
      }
    },
    // Filters tasks by date for calendar days
    getTasksOnDate(date) {
      return this.tasks.filter((task) => task.dueDate === date)
    },
  }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useTasks, import.meta.hot))
}
