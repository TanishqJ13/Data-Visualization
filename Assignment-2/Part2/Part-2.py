{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"pygments_lexer":"ipython3","nbconvert_exporter":"python","version":"3.6.4","file_extension":".py","codemirror_mode":{"name":"ipython","version":3},"name":"python","mimetype":"text/x-python"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# %% [code] {\"id\":\"DM4jd7SEHjKf\",\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-10-06T17:31:56.363928Z\",\"iopub.execute_input\":\"2021-10-06T17:31:56.364270Z\",\"iopub.status.idle\":\"2021-10-06T17:31:56.381613Z\",\"shell.execute_reply.started\":\"2021-10-06T17:31:56.364189Z\",\"shell.execute_reply\":\"2021-10-06T17:31:56.380518Z\"}}\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport os\nfrom PIL import Image\nimport plotly.graph_objects as go\n\n# %% [code] {\"id\":\"STGzMwAnSnlT\",\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-10-06T17:31:56.382910Z\",\"iopub.execute_input\":\"2021-10-06T17:31:56.383172Z\",\"iopub.status.idle\":\"2021-10-06T17:33:35.751520Z\",\"shell.execute_reply.started\":\"2021-10-06T17:31:56.383146Z\",\"shell.execute_reply\":\"2021-10-06T17:33:35.750661Z\"}}\n#Density\n#for time_stamp in range(200):#As there are 200 time stamps in total.\ntime_stamp = 119\nfile = str(time_stamp).zfill(4)#As the file numbers in the data are in the form 0000 to 0199. \ndata_files = pd.read_csv('../input/dv-data-1/multifield.'+ file + '.txt', delimiter=' ',header=None)\ntotal_partical_density = data_files[0].values #Selecting first scalar value to visualize to be density\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-10-06T17:33:35.753206Z\",\"iopub.execute_input\":\"2021-10-06T17:33:35.753689Z\",\"iopub.status.idle\":\"2021-10-06T17:33:40.704777Z\",\"shell.execute_reply.started\":\"2021-10-06T17:33:35.753651Z\",\"shell.execute_reply\":\"2021-10-06T17:33:40.704055Z\"}}\nx=[]\ny=[]\nz=[]\ndata=[]\n\nindex=-1\nfor k in range(248):\n    for j in range(248):\n        for i in range(600):\n            index+=1\n            if index%50==0:\n                x.append(i)\n                y.append(j)\n                z.append(k)\n                data.append(total_partical_density[index])\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-10-06T17:33:40.706079Z\",\"iopub.execute_input\":\"2021-10-06T17:33:40.706612Z\",\"iopub.status.idle\":\"2021-10-06T17:33:40.743659Z\",\"shell.execute_reply.started\":\"2021-10-06T17:33:40.706572Z\",\"shell.execute_reply\":\"2021-10-06T17:33:40.742748Z\"}}\nMIN_DATA = min(data)\nMAX_DATA = max(data)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-10-06T17:33:40.744940Z\",\"iopub.execute_input\":\"2021-10-06T17:33:40.745331Z\",\"iopub.status.idle\":\"2021-10-06T17:33:54.658601Z\",\"shell.execute_reply.started\":\"2021-10-06T17:33:40.745292Z\",\"shell.execute_reply\":\"2021-10-06T17:33:54.657710Z\"}}\nviz= go.Figure(\n    data=go.Isosurface(\n        x=x,\n        y=y,\n        z=z,\n        value=data,\n        isomin=MIN_DATA,\n        isomax=MAX_DATA,\n        surface_count=5,\n        opacity=0.6,\n        caps=dict(x_show=False, y_show=False)\n    )\n)\n\n# %% [code] {\"jupyter\":{\"outputs_hidden\":false},\"execution\":{\"iopub.status.busy\":\"2021-10-06T17:36:50.639931Z\",\"iopub.execute_input\":\"2021-10-06T17:36:50.640270Z\",\"iopub.status.idle\":\"2021-10-06T17:36:52.778086Z\",\"shell.execute_reply.started\":\"2021-10-06T17:36:50.640242Z\",\"shell.execute_reply\":\"2021-10-06T17:36:52.776839Z\"}}\nviz.show()\n#viz.write_html('./output1.html')","metadata":{"_uuid":"908f6670-7013-4dce-af4f-e2892dbbe382","_cell_guid":"1355414b-a09a-4eee-80ae-d06fc81f6ac1","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}