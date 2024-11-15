# LTE_Indoor_Tracking
LTE indoor location 

This is a home project trying to leverage the KPI data from srsran and use machine learning to correlate the location of my dog in my apartment. He is a very lazy boy so periodicly logging the locaion of his naps should be fairly easy. Hopfully with enough learning data and metrics we can guestimate where my dog is napping!

The UE is a cheap LTE watch that has a Sim card. Ideally we would use a 5G capable device, however most 5G IoT/SmartWatches leverage eSIM. eSIM is not friendly for open source networks as they requied GSMA keys to program which are not available. As of this project eSIM devices are not programmable for open source private networks. Therefore this project leverages currently available smart watches that have sim cards. Due to this constraint we leveraged srsRAN 4G. 

The data collection is done with a quick html locally hosted site. This allows the user to click on a given grid and then log the location and time (in ms). This makes it fairly painless to gather learning data. 

<img width="800" alt="image"
src="https://github.com/user-attachments/assets/bc8b6845-049e-4fd5-afab-3eb368ac151b">

<img width="448" alt="image"
src="https://github.com/user-attachments/assets/7ddd229e-0e5d-41e7-a6da-797bf1611a8c">

<img width="448" alt="image" src="https://github.com/macclab-stevens/LTE_Indoor_Tracking/blob/main/images/Booker_cropped.png?raw=true">






