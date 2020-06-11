## happy simple path
* greet
  - utter_botgreet
* Book a Room
  - bookingroomcall
  - form{"name":"bookingroomcall"}
  - form{"name":"null"}
  - utter_slot_values
  - deleteslotss
* ask_faq
    - respond_ask_faq
    - utter_change_bookingroom
* affirm
    - utter_great
    - bookingroomcall
    - form{"name":"bookingroomcall"}
    - form{"name":"null"}
    - utter_slot_values1
* deny
    - utter_goodbye   
    
## cleaningtime
* Room Cleaning
  - utter_clean_time
* ask_faq
    - respond_ask_faq
    - utter_ask_continue
* affirm
    - utter_great
    - utter_clean_time
* deny
    - utter_goodbye   
    
## cleaningnow
* Cleaning right now
  - utter_clean_now 

## cleaning after few hours
* Cleaning after few hours
  - cleaning
  
## FAQ
* ask_faq
    - respond_ask_faq
 
    

