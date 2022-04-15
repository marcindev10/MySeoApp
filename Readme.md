# MySeoApp


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
#### This is an web application is about MSeo company.
##### MSeo is web app about SEO for people to understand what is Seo and what we do as MSeo.We provide people with useful links to google documentation and the best tools used in the SEO industry to understan the SEO better.Additionally we help peaple with improving their websites dependings on their needs and demands. MSeo can adapt to any request regarding SEO.

## Technologies
Project is created with:
* HTML5
* CSS3
* BOOTSTRAP5
* PYTHON 3.10
* CLICK 8.0.4
* FLASK 2.0.3
* MARKAPSAFE  2.1.1
* PyYAML 6.0
* Werkzeug 2.0.3
* TERRAFORM
* AZURE CLI

## Setup
To run this project, install it locally using Flask:
```
$ git clone https://github.com/marcindev10/MySeoApp.git
```
locate this on the computer path and run this command
```
$ cd MySeoApp
```
Create a virtual environment for the app:
```
$ python3 -m venv .venv
source .venv/bin/activate
```
Install the dependencies:
```
$ pip install -r requirements.txt
```

run the application
```
flask run

```

Check if the applications is running locally

### Create resorces in AZURE

##### If you need AZURE account with an active subscription. Create an account for free click [here](https://azure.microsoft.com/en-us/free/search/?&ef_id=Cj0KCQjwr-SSBhC9ARIsANhzu155QQMNE_8AoMl5CLxRQIJT4g2bKZvel3hrvUaO9PBA_KtsemMLCS4aAgtYEALw_wcB:G:s&OCID=AID2200242_SEM_Cj0KCQjwr-SSBhC9ARIsANhzu155QQMNE_8AoMl5CLxRQIJT4g2bKZvel3hrvUaO9PBA_KtsemMLCS4aAgtYEALw_wcB:G:s&gclid=Cj0KCQjwr-SSBhC9ARIsANhzu155QQMNE_8AoMl5CLxRQIJT4g2bKZvel3hrvUaO9PBA_KtsemMLCS4aAgtYEALw_wcB).

 Log in to AZURE  and install Terraform  follow the instructions [here](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started)
 once the Terraform is installed in the terminal you would be ready to create the resources for our applications.

 In Azure terminal run these comands:
 ```
$ mkdir app
$ cd app  
$ code main.tf
 ```
pass this code to the file

 ```
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.99.0"
    }
  }
}
# Create a resource group
resource "azurerm_resource_group" "dev-rg" {
  name     = "dev-environment-rg"
  location = "South Central US"
}
# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}
# Create app service plan
resource "azurerm_app_service_plan" "service-plan" {
  name = "simple-service-plan"
  location = azurerm_resource_group.dev-rg.location
  resource_group_name = azurerm_resource_group.dev-rg.name
  kind = "Linux"
  reserved = true
  sku {
    tier = "Standard"
    size = "S1"
  }
  tags = {
    environment = "dev"
  }
}

# Create PYTHON app service
resource "azurerm_app_service" "app-service" {
  name = "myseoapp"
  location = azurerm_resource_group.dev-rg.location
  resource_group_name = azurerm_resource_group.dev-rg.name
  app_service_plan_id = azurerm_app_service_plan.service-plan.id

site_config {
    linux_fx_version = "PYTHON3.8"
  }
tags = {
    environment = "dev"
  }
}
 ```
-----------------------------
save it and cloes the editor

run these commands to create resorces
 ```
$ terraform init 
$ terraform plan
$ terraform apply

 ```
 the resorces will be created on Azure

 ##### You can deploy your application code from a local Git repository to Azure by configuring a Git remote in your local repo pointing at Azure to push code to. The URL of the remote repository and Git credentials needed for configuration can be retrieved using either the Azure portal or the Azure CLI.

 Install AZURE CLI in terminal how to [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

```
 $RESOURCE_GROUP_NAME='dev-environment-rg'
 $APP_SERVICE_NAME='app-service'

 $ az webapp deployment source config-local-git `
     --name $APP_SERVICE_NAME `
     --resource-group $RESOURCE_GROUP_NAME `
     --output tsv

```
Retrieve the deployment credentials for your application. These will be needed for Git to authenticate to Azure when you push code to Azure in a later step.

```
$ az webapp deployment list-publishing-credentials `
    --name $APP_SERVICE_NAME `
    --resource-group $RESOURCE_GROUP_NAME `
    --query "{Username:publishingUserName, Password:publishingPassword}" `
    --output table
```
Next, in the root directory of your application, configure a Git remote that points to Azure using the Git URL of the Azure remote obtained in a previous step.

```
$ git remote add azure <https://github.com/marcindev10/MySeoApp.git>
```
You can now push code from your local Git repository to Azure using the Git remote you just configured. Master is the default deployment branch for App Service. You must specify the mapping from local branch name to remote branch name in the push.


```
$ git push azure main:master
```
The first time you push code to Azure, Git will prompt you for the Azure deployment credentials you obtained in a previous step. Git will then cache these credentials so you will not have to reenter them on subsequent deployments.

Browse to the deployed application in your web browser at the URL http://myseoapp.azurewebsites.net. If you see a default app page, wait a minute and refresh the browser.
