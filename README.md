# Angular CLI Tools
Angular extra Command Line tools for simplifying dev routines.

## Features
So far there is only one feature to dump all the Routes in an Angular project

## Installation:
1. Python 3 and up need to be installed (https://www.python.org/downloads/)
2. In the command line run:
```
pip3 install -r requirements.txt
``` 

## Usage
1. Navigate to folder with AngularCLITools.py
2. Call: 
```
python3 AngularCLITools.py --help
```

## Example
Dump all the routes in an Angular project
```
python3 AngularCLITools.py routes --project "path-to-root-folder-of-angular-project"
```
Result:
```
Simple Angular CLI Toolset by Artem Bordiuh
Looking for routes of the project: /path-to-root-folder-of-angular-project
/path-to-root-folder-of-angular-project/src/app/app-routing.module.ts: 
const routes: Routes = [
  {
    path: "",
    component: MyComponent,
  }
];
```
