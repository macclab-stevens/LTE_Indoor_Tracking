# LTE_Indoor_Tracking
This is a home project trying to leverage the KPI data from srsran and use machine learning to correlate the location of my dog in my apartment. He is a very lazy boy so periodicly logging the places where he naps should be fairly easy. Hopfully with enough learning data and metrics we can guestimate where my dog is snoozing!

# System Under Test
<!-- Insert Picture of B200 and other things -->

<img width="900" alt="image"
src="https://github.com/user-attachments/assets/5d9c67b4-93e6-48d3-bb97-c820e55a118d">

# UE (User Equipment)
The UE is a cheap LTE watch that has a Sim card. Ideally we would use a 5G capable device, however most 5G IoT/SmartWatches leverage eSIM. eSIM is not friendly for open source networks as they requied GSMA keys to program which are not available. As of this project eSIM devices are not programmable for open source private networks. Therefore this project leverages currently available smart watches that have sim cards. Due to this constraint we leveraged srsRAN 4G. 

# SuT (Subject Under Test)

<img width="448" alt="image" src="https://github.com/macclab-stevens/LTE_Indoor_Tracking/blob/main/images/Booker_cropped.png?raw=true">
Booker is our 4yr old Sheep-a-doodle. He loves long walks, playing bacon ball, and NAPS! Using a dog to collect data is simple enough, because he moves around the apt a lot durring the day but also takes lots of naps. Having low movement is key for this sort of experiment. We don't expect to be able to track the specific movements, like moving from the bedroom to the living room. The goal is to guess where he is napping! This makes for datasets that should be long, and have common KPI data (At least this is the goal anyway!). 

# Data Collection
The data collection is done with a quick html locally hosted site. This allows the user to click on a given grid and then log the location and time (in ms). This makes it fairly painless to gather learning data. 


<img width="600" alt="image"
src="https://github.com/macclab-stevens/LTE_Indoor_Tracking/blob/main/images/apt-diagram.png?raw=true)![image](https://github.com/user-attachments/assets/50f322e2-5917-4578-b36d-2a69a2d7c716">

```csv
Grid Index,Click Time
B7,2024-11-13 08:21:53.19
C6,2024-11-13 08:22:15.31
C6,2024-11-13 08:23:01.90
B6,2024-11-13 08:27:24.44
B6,2024-11-13 08:27:28.85
A8,2024-11-13 08:40:41.09
A8,2024-11-13 08:41:10.06
A5,2024-11-13 09:09:37.74
A5,2024-11-13 09:21:57.05
A5,2024-11-13 09:22:00.06
D7,2024-11-13 11:33:46.74
D7,2024-11-13 12:06:45.13
A8,2024-11-13 12:26:38.03
A8,2024-11-13 12:26:42.32
A8,2024-11-13 12:26:43.59
D7,2024-11-13 13:47:22.00
D7,2024-11-13 15:11:32.08
B5,2024-11-13 15:42:25.03
```

# Data Results:

<img width="900" alt="image"
src="https://github.com/user-attachments/assets/8ab0a6be-e766-4e43-b2d7-999419394f1f">

The eNb metrics collected are generated in a .json file. We run a quick script to convert these to .csv to be able to graph them more easily in graphana. 

```csv
type,timestamp,carrier_id,pci,nof_rach,ue_list,ue_rnti,dl_cqi,dl_mcs,ul_pusch_rssi,ul_pucch_rssi,ul_pucch_ni,ul_pusch_tpc,ul_pucch_tpc,dl_cqi_offset,ul_snr_offset,dl_bitrate,dl_bler,ul_snr,ul_mcs,ul_bitrate,ul_bler,ul_phr,ul_bsr,bearer_list,bearer_id,qci,dl_total_bytes,ul_total_bytes,dl_latency,ul_latency,dl_buffered_bytes,ul_buffered_bytes
metrics,1731590329152,0,1,1,"[{'ue_container': {'ue_rnti': 70, 'dl_cqi': 14.759999, 'dl_mcs': 12.388889, 'ul_pusch_rssi': -98.91316, 'ul_pucch_rssi': -96.947395, 'ul_pucch_ni': 48.44835, 'ul_pusch_tpc': 0, 'ul_pucch_tpc': 0, 'dl_cqi_offset': 0.013000001, 'ul_snr_offset': 0.04399998, 'dl_bitrate': 2080.0, 'dl_bler': 0.0, 'ul_snr': 5.5352015, 'ul_mcs': 2.877193, 'ul_bitrate': 4528.0, 'ul_bler': 0.0, 'ul_phr': 40.0, 'ul_bsr': 0, 'bearer_list': [{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 0, 'ul_total_bytes': 0, 'dl_latency': 0.0, 'ul_latency': 0.0, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]}}]",70,14.759999,12.388889,-98.91316,-96.947395,48.44835,0,0,0.013000001,0.04399998,2080.0,0.0,5.5352015,2.877193,4528.0,0.0,40.0,0,"[{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 0, 'ul_total_bytes': 0, 'dl_latency': 0.0, 'ul_latency': 0.0, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]",3,9,0,0,0.0,0.0,0,0
metrics,1731590330152,0,1,1,"[{'ue_container': {'ue_rnti': 70, 'dl_cqi': 14.639999, 'dl_mcs': 20.0, 'ul_pusch_rssi': -98.815, 'ul_pucch_rssi': -96.71284, 'ul_pucch_ni': 48.2701, 'ul_pusch_tpc': 0, 'ul_pucch_tpc': 0, 'dl_cqi_offset': 0.014000001, 'ul_snr_offset': 0.04499998, 'dl_bitrate': 776.0, 'dl_bler': 0.0, 'ul_snr': 4.8874025, 'ul_mcs': 4.0, 'ul_bitrate': 256.0, 'ul_bler': 0.0, 'ul_phr': 40.0, 'ul_bsr': 0, 'bearer_list': [{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 84, 'ul_total_bytes': 0, 'dl_latency': 0.037, 'ul_latency': 0.0, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]}}]",70,14.639999,20.0,-98.815,-96.71284,48.2701,0,0,0.014000001,0.04499998,776.0,0.0,4.8874025,4.0,256.0,0.0,40.0,0,"[{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 84, 'ul_total_bytes': 0, 'dl_latency': 0.037, 'ul_latency': 0.0, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]",3,9,84,0,0.037,0.0,0,0
metrics,1731590331152,0,1,1,"[{'ue_container': {'ue_rnti': 70, 'dl_cqi': 14.400002, 'dl_mcs': 20.0, 'ul_pusch_rssi': -99.94582, 'ul_pucch_rssi': -97.51748, 'ul_pucch_ni': 48.094852, 'ul_pusch_tpc': 0, 'ul_pucch_tpc': 0, 'dl_cqi_offset': 0.0150000015, 'ul_snr_offset': 0.045999978, 'dl_bitrate': 776.0, 'dl_bler': 0.0, 'ul_snr': 5.0549154, 'ul_mcs': 2.0, 'ul_bitrate': 176.0, 'ul_bler': 0.0, 'ul_phr': 40.0, 'ul_bsr': 0, 'bearer_list': [{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 168, 'ul_total_bytes': 0, 'dl_latency': 0.035, 'ul_latency': 0.0, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]}}]",70,14.400002,20.0,-99.94582,-97.51748,48.094852,0,0,0.0150000015,0.045999978,776.0,0.0,5.0549154,2.0,176.0,0.0,40.0,0,"[{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 168, 'ul_total_bytes': 0, 'dl_latency': 0.035, 'ul_latency': 0.0, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]",3,9,168,0,0.035,0.0,0,0
metrics,1731590332152,0,1,1,"[{'ue_container': {'ue_rnti': 70, 'dl_cqi': 15.0, 'dl_mcs': 12.0, 'ul_pusch_rssi': -99.25221, 'ul_pucch_rssi': -97.3586, 'ul_pucch_ni': 48.71894, 'ul_pusch_tpc': 0, 'ul_pucch_tpc': 0, 'dl_cqi_offset': 0.017, 'ul_snr_offset': 0.06299995, 'dl_bitrate': 832.0, 'dl_bler': 0.0, 'ul_snr': 4.6591682, 'ul_mcs': 1.8604652, 'ul_bitrate': 2872.0, 'ul_bler': 0.0, 'ul_phr': 40.0, 'ul_bsr': 0, 'bearer_list': [{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 252, 'ul_total_bytes': 147, 'dl_latency': 0.033, 'ul_latency': 0.009, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]}}]",70,15.0,12.0,-99.25221,-97.3586,48.71894,0,0,0.017,0.06299995,832.0,0.0,4.6591682,1.8604652,2872.0,0.0,40.0,0,"[{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 252, 'ul_total_bytes': 147, 'dl_latency': 0.033, 'ul_latency': 0.009, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]",3,9,252,147,0.033,0.009,0,0
metrics,1731590333152,0,1,1,"[{'ue_container': {'ue_rnti': 70, 'dl_cqi': 14.5199995, 'dl_mcs': 9.333333, 'ul_pusch_rssi': -99.395966, 'ul_pucch_rssi': -97.656395, 'ul_pucch_ni': 48.515915, 'ul_pusch_tpc': 0, 'ul_pucch_tpc': 0, 'dl_cqi_offset': 0.020000001, 'ul_snr_offset': 0.091000006, 'dl_bitrate': 888.0, 'dl_bler': 0.0, 'ul_snr': 4.3269286, 'ul_mcs': 0.9583333, 'ul_bitrate': 3664.0, 'ul_bler': 0.0, 'ul_phr': 40.0, 'ul_bsr': 0, 'bearer_list': [{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 336, 'ul_total_bytes': 296, 'dl_latency': 0.031, 'ul_latency': 0.013, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]}}]",70,14.5199995,9.333333,-99.395966,-97.656395,48.515915,0,0,0.020000001,0.091000006,888.0,0.0,4.3269286,0.9583333,3664.0,0.0,40.0,0,"[{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 336, 'ul_total_bytes': 296, 'dl_latency': 0.031, 'ul_latency': 0.013, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]",3,9,336,296,0.031,0.013,0,0
metrics,1731590334152,0,1,1,"[{'ue_container': {'ue_rnti': 70, 'dl_cqi': 14.875, 'dl_mcs': 7.6, 'ul_pusch_rssi': -101.39813, 'ul_pucch_rssi': -100.12996, 'ul_pucch_ni': 48.498047, 'ul_pusch_tpc': 0, 'ul_pucch_tpc': 0, 'dl_cqi_offset': 0.0040000025, 'ul_snr_offset': 0.110000044, 'dl_bitrate': 848.0, 'dl_bler': 25.0, 'ul_snr': 3.0760658, 'ul_mcs': 0.0, 'ul_bitrate': 1672.0, 'ul_bler': 0.0, 'ul_phr': 40.0, 'ul_bsr': 0, 'bearer_list': [{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 420, 'ul_total_bytes': 382, 'dl_latency': 0.029, 'ul_latency': 0.012, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]}}]",70,14.875,7.6,-101.39813,-100.12996,48.498047,0,0,0.0040000025,0.110000044,848.0,25.0,3.0760658,0.0,1672.0,0.0,40.0,0,"[{'bearer_container': {'bearer_id': 3, 'qci': 9, 'dl_total_bytes': 420, 'ul_total_bytes': 382, 'dl_latency': 0.029, 'ul_latency': 0.012, 'dl_buffered_bytes': 0, 'ul_buffered_bytes': 0}}]",3,9,420,382,0.029,0.012,0,0
```





