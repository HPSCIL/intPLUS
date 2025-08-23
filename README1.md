# Interaction network - Patch-generating Land Use Simulation (PLUS) Model software
Second-generation PLUS model, intPLUS: Exploring competitive relationships among multiple land uses helps reveal fundamental mechanisms underlying land system evolution. However, quantifying the competitive interactions between different land uses remains a challenge. Most cellular automata (CA)-based simulation studies fail to adequately capture the driving and inhibitory effects among land use types because they do not account for differences in magnitude or order of influence from spatial suitability, neighborhood aggregation effects, and stochastic factors on land use change. To address this issue, we propose a novel CA model, intPLUS, featuring an innovative framework that can extract interaction networks among different land use types based on simulation consistency and improve the accuracy of future land use change predictions. The model considers the inhibitory effects exerted by other land use types on each land use category and incorporates weights into multiple factors driving land use change through logarithmic transformation. Subsequently, a random forest model analyzes correctly predicted land use changes (i.e., "consistency") to explore the relative weights of driving and inhibitory effects among different land use types and construct a land use interaction network. Results show that incorporating the interaction network improves simulation accuracy by 30% during model calibration and by 13% in future projections. By fully leveraging consistency information generated during spatial simulations, the derived land use interaction network offers new insights into understanding spatial competition among land use types.

# To cite the intPLUS model
Liang Xun , Huang Jun-Long, Guan Qingfeng* (2025). Unveiling land competition through interaction networks: A consistency-based mining and simulation model that integrates inhibiting effects of land uses, Landscape and Urban Planning,263,105458.(https://doi.org/10.1016/j.landurbplan.2025.105458)

# Baidu Cloud Download
https://pan.baidu.com/s/1l_OhKYWUy45F2mK5dQbbfw 
code: tsdw 

# Video Tutorial
Chinese: https://www.bilibili.com/video/BV1L4twzDEQ5/?spm_id_from=333.1387.homepage.video_card.click 
English: https://www.bilibili.com/video/BV1kkevzgEoH/?spm_id_from=333.337.search-card.all.click

# More Information
https://xungst.github.io/

# Interfaces
![add image](https://github.com/HPSCIL/intPLUS/blob/main/pic1.png)
![add image](https://github.com/HPSCIL/intPLUS/blob/main/pic2.png)
![add image](https://github.com/HPSCIL/intPLUS/blob/main/pic3.png)

# Running environment
Run intPLUS software by double-clicking the exe file 'intPLUS V1.3_boxed.exe'. intPLUS software can run independently on Windows Vista/7/8/X 64-bit environment, without any dependencies and setup process.
# User manual
Please find the attached PDF file 'User Manual of the intPLUS model  20250722 English.pdf' in the Repository.  
中文说明：User Manual of the intPLUS model  20250722 Chinese.pdf

# Test data
Please find the compressed file 'intPLUS_test_data.zip' in the Repository. 
 
 # Scope of application
Land use/land cover change(LULC) simulaiton, policy making, knowlege discovery for LULC, urban planning, eco-security early-warning and etc.
  
# Related open source library
intPLUS was developed purely in the C++ language. The parallel technology of intPLUS software is from High-performance Spatial Computational Intelligence Lab @ China University of Geosciences (Wuhan) (https://github.com/HPSCIL). The Random forest technique in our model is from a powerful open source library called Alglib 3.9.2 (http://www.alglib.net/). The linear regression algorithm is from (https://github.com/fengbingchun/NN_Test). The UI of the software is built using a famous open source library Qt 5 (https://www.qt.io/download/). This UI provides a real-time display of dynamic changes of land use in simulation process. Moreover, the using of open source library GDAL 2.0.2 (http://www.gdal.org/) allows our model to directly read and write raster data (.tif, .img, .txt files) that includes geographical coordinate information. 
  
# Consultation 
If you have technical questions regarding intPLUS software, please contact Dr. Xun Liang (liangxun@cug.edu.cn)

# Contact info
High-performance Spatial Computational Intelligence Lab(HPSCIL) (https://github.com/HPSCIL)
School of Geography and Information Engineering, China University of Geosciences, Wuhan, Hubei 430078, China.
For any possible research collaboration, please contact Prof. Qingfeng Guan (guanqf@cug.edu.cn)
