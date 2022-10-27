import { defineStore } from 'pinia'
import { axios } from "../axios.js"
import Fetch from "../fetch.js"

// Holds list-related data and functions across project
export const useLists = defineStore('lists', {
  state: () => ({
    _lists: [],
    currentListID: 0,
  }),
  getters: {
    currentList(state) {
      return state.currentListID
    },
    lists(state) {
      return this._lists
    },
  },
  actions: {
    async fetchLists() {
      var json = await Fetch.get("lists/")
      if (json.data) {
        this._lists = json.data
      }
      if (this.currentListID == 0) {
        this.currentListID = this._lists[0].id
      }
    },
    // Sends delete request to backend and removes from store on success
    async deleteList(list_id) {
      var targetPath = "lists/" + String(list_id)
      var response = await Fetch.delete(targetPath)
      // TODO: add returned id to list rather than refetching, for improving efficiency
      this.fetchLists()
    },
    async addList(list_name, description) {

	var json = {
	  'name': list_name,
	}
        var results = await Fetch.post("lists/", json)
	// TODO: add returned id to list rather than refetching, for improving efficiency
        this.fetchLists()
    },
  }
})

