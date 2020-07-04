<template>
  <div> 
    <v-text-field 
      v-model="NewTopic" 
      class="MakeTopic" 
      label="Start a New Topic"
    />
    <v-btn v-if='NewTopic != ""' v-on:click="MakeTopic"> Start a New Topic </v-btn>  <br><br><br>
    <h1 style="self-align: center;font-size: 43px;font-family: serif;"><b> Some Previous Topics </b></h1><br><br>
    <v-text-field v-model="SearchTopic" class="SearchTopic" label="Search for Topics" v-on:keyup="SearchinTopics"></v-text-field>
    <div v-for="topic in ListOfTopics" :key=topic>
        <h3 v-if="showalltopics == 1" v-on:click="getConversation(topic)" class="TopicName"> {{ topic }} <v-icon>link</v-icon></h3>
    </div> <br> <br>
  </div>
</template>

<script>
import Discussion from '@/components/pages/Discussion.vue'
import axios from 'axios';
import swal from 'sweetalert2';
import router from '../../router';

export default {
    data: () => ({
        ListOfTopics: [],
        showalltopics: 1,
        NewTopic: "",
        SearchTopic: "",
        credentials: {
            Time: "",
            Topic: "",
            DisplayName: sessionStorage.getItem('username'),
            Author: sessionStorage.getItem('username'),
            Comment: ""
        },
    }),
    
    created() {
        this.checkLoggedIn();
        this.getTopics();
    },

    methods: {
        checkLoggedIn() {
          this.$session.start();
          if (!this.$session.has("token")) {
            router.push("/auth");
          }
        },
        getConversation: function(topic) {
            this.$store.dispatch('setTopic', topic);
            router.push('/discussiontopic');
        },
        getTopics() {
            this.$http.get('comments/gettopics').then(res => {
            this.ListOfTopics = res.data.ListOfTopics;
            console.log(this.ListOfTopics);
            })
            .catch(e => {
            console.log(e);
            });
        },
        MakeTopic: function() {
            this.loading = true;
            this.credentials.DisplayName = "admin";
            this.credentials.Author = "admin";
            this.credentials.Time = Date(Date.now()).toString();
            this.credentials.Comment = "Hey Guys, Please Maintain Peace.";
            this.credentials.Topic = this.NewTopic.toString();
            console.log(this.NewTopic)
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('token');
            axios.post('http://localhost:8000/comments/addcomment/', this.credentials).then(res => { 
              console.log(res);
              this.$store.dispatch('setTopic', this.NewTopic);
              this.getConversation(this.NewTopic);
            })
            .catch(e => {
               this.loading = false;
              console.log(e);
            });
        },
        SearchinTopics: function() {
            var NumberOfTopics = this.ListOfTopics.length;
            var x = document.getElementsByClassName('TopicName'); 
            console.log(x);
            for (var i = 0; i < NumberOfTopics; i++) {
                if (!x[i].innerHTML.toLowerCase().includes(this.SearchTopic.toLowerCase())) {
                    x[i].style.display = "none";
                }
                else { 
                    x[i].style.display="inline";                  
                }
            }
        }
    }
}
</script>

<style scoped>
    .TopicName:hover {
      color: red;
      cursor: pointer;
      font-family: sans-serif;
    }
    .TopicName {
        display: inline;
    }
    .MakeTopic {
      margin-left: 590px;
      width: 300px;
    }
    .SearchTopic {
        margin-left: 640px;
        width: 200px;
    }
</style>