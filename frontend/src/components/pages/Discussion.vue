<template>
    <div> <br> <v-icon large class="backarrow" v-on:click="GoBack"> arrow_back </v-icon>
        <br><br><br><br>
        <div v-if='selectedTopic!=""'>
            <h1 style="font-size: 44px;"><b><i> {{ info[0].Topic }} </i></b></h1> <br> <br>
            <v-card light class="comment" v-for="item in info" :key="item.Author">
                <h5 class="author" ><i><b> <h2>{{ item.DisplayName }}</h2> </b></i> wrote on {{ item.Time }} </h5><br>
                <h2 class="message"> {{ item.Comment }} </h2>
                <v-btn  dark v-if="item.Author != user" class="reply" v-on:click="reply(item)">Reply</v-btn>
                <v-btn  dark v-if='item.Author == user || user == "admin"' class="delete" v-on:click="crosscheck(item)">Delete</v-btn>
                <v-dialog
                v-model="dialog"
                max-width="290"
            >
          <v-card>
            <v-card-title class="headline">Are you sure you want to delete it?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                color="green darken-1"
                text
                @click="dialog = false"
              >
                Disagree
              </v-btn>

              <v-btn
                color="green darken-1"
                text
                v-on:click="deletecomment(itemToDelete)"
                @click="dialog = false"
              >
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
            </v-card><br><br>
       <v-card light class="CommentBox">
       <v-text-field v-model="message" class="text_field" id="mess" label="Message"></v-text-field>
            <v-btn dark class="btn" v-if='message != ""' v-on:click="addcomment">POST</v-btn><br><br>
       </v-card>
        <br><br><br>
    </div></div>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert2';
import router from '../../router';
import { bus } from '../../main';
import {mapGetters} from 'vuex';

export default {
    name: "Discussion",
    data: () => ({
        info: {},
        Topic: "First",
        message: "",
        dialog: 0,
        itemToDelete: {},
        ListOfTopics: [],
        MakeTopic: "",
        showalltopics: 1,
        credentials: {
            Time: "",
            Topic: "",
            DisplayName: sessionStorage.getItem('username'),
            Author: sessionStorage.getItem('username'),
            Comment: ""
        },
    }),
    
    created () { 
      this.getTopics();
      this.checkLoggedIn();
      this.Get_Info(this.selectedTopic);
      console.log(this.user);
      console.log(this.selectedTopic);
    },

    computed: {
      ...mapGetters ({
        selectedTopic: 'selectedTopic',
        user: 'user'
      })
    },

    methods: {
        
        GoBack: function() {
          router.push('/discussion');
        },

        checkLoggedIn() {
          this.$session.start();
          if (!this.$session.has("token")) {
            router.push("/auth");
          }
        },

        crosscheck(item) {
            this.itemToDelete = item;
            this.dialog = true;
        },

        reply: function(item) {
            
            this.credentials.DisplayName = this.user + " replying to " + item.Author;
            document.getElementById("mess").focus();
        },

        deletecomment(item) {
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('token');
            axios.delete('http://localhost:8000/comments/delete/'+String(item.commentId)).then(() => {
              this.Get_Info(this.selectedTopic);
            })
        },

        addcomment() {
              this.loading = true;
              this.credentials.Time = Date(Date.now()).toString();
              this.credentials.Comment = this.message;
              this.credentials.Topic = this.selectedTopic;
              axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('token');
              axios.post('http://localhost:8000/comments/addcomment/', this.credentials).then(() => { 
                this.credentials.DisplayName = this.user;
                document.getElementById("mess").value = "";
                this.Get_Info(this.selectedTopic);
              }).catch(e => {
                this.loading = false;
                console.log(e);
              });
        },

        getConversation: function(topic) {
            this.selectedTopic = topic;
            this.Get_Info(topic);
        },

        Get_Info(topic) {
            this.$http.get('comments/get/'+topic+'/').then(res => {
            this.info = res.data;
            })
            .catch(e => {
            console.log(e);
            });
        },

        getTopics() {
            this.$http.get('comments/gettopics').then(res => {
            this.ListOfTopics = res.data.ListOfTopics;
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
            this.credentials.Comment = "Hey Guys";
            this.credentials.Topic = this.MakeTopic;
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('token');
            axios.post('http://localhost:8000/comments/addcomment/', this.credentials).then(() => { 
              this.Get_Info(this.MakeTopic);
            })
            .catch(e => {
               this.loading = false;
              console.log(e);
            });
        }
    }
}
</script>

<style scoped>
    .comment {
        margin-left: 45px;
        width: 1400px;
        padding: 6px 20px;
        border: 5px solid rgb(145, 137, 137);
        margin-top: 13px;
    }
    .author {
        text-align: left;
    }
    .message {
        text-align: left;
    }
    .text_field {
        margin-left: 30px;
        width: 680px;
    }
    .btn {
        background-color: black;
        margin-left: 590px;
        width: 80px;
        height: 10px;
    }
    .delete {
        margin-left: 1250px;
    }
    .reply {
        margin-left: 1250px;
    }
    .backarrow {
        margin-left: -1400px;
    }
    .backarrow:hover {
        cursor: pointer;
    }
    .CommentBox {
      width: 750px;
      margin-left: 696px;
      height: 120px;
    }
</style>