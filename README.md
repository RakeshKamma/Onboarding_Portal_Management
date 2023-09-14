# on-boarding-application

---------------
### Setting Up Development Environment  
  
Follow the instructions below to setup development environment.
  
**Install Python Package dependencies**  
```bash  
pip install -r requirements.txt  
```  
  
**Start the Application**  
```bash  
python app.py
```  
  
  Not specifying the port will make the app start in the port specified in the config file.  
  
### Configurations 
Add configuration variables below in conf/application.conf file to run application.
  
| **Section** | **Value** | **Description** |  
| -- | -- | -- |  
| database | onportal_database | Name of the data base |  
| user | postgres | username in the database |  
| password | postgres | password for the user |  
| host | 192.168.0.210 | Host |  
| port | 5432 | port | 
| document_upload_path | D:\documents | Download the Documents here |  
| profile_upload_path | C:\documents | Download the Documents here | 
| account_name | documentuploadfile | Azure storage account name |  
| account_key | 3eKMVgylAZB2eCYYVbBAm9V5NxjVa9DHdDZWCos8Ogqp1HO8yCef5MasEj0LJV5BXjBXPxqyB8P75ikjeQRfVg== | Azure storage account key | 
| container_name | documen | Azure storage account container name |


  
  
## Authors  
* **Rakesh Kamma**
* **Netturi Koushik Basha**
* **Jagapati Babu Pujari**
* **Preethi P**
* **Bhavana KS**
* **Aashrith Kandimalla**
* **Chetan Kumar**
* **Vamsi Krishna Grandhi**
* **Omesh Majety**
