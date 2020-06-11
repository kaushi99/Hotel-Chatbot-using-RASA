## happy path 1 (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: utter_botgreet -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_non_veg -->


## happy path 2 (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: utter_botgreet -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_non_veg -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_veg -->


## sad path 1 (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: utter_botgreet -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_non_veg -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_non_veg -->


## sad path 2 (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: utter_botgreet -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_non_veg -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_thanks -->


## sad path 3 (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* greet: hi
    - utter_greet   <!-- predicted: utter_botgreet -->
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_non_veg -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_thanks -->


## say goodbye (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_veg -->


## bot challenge (C:\Users\kaush\AppData\Local\Temp\tmppn9u5gfr\ca11e5c48d5b4ff6bf90230e06a50139_conversation_tests.md)
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: utter_non_veg -->


