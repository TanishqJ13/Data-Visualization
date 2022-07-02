{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"pygments_lexer":"ipython3","nbconvert_exporter":"python","version":"3.6.4","file_extension":".py","codemirror_mode":{"name":"ipython","version":3},"name":"python","mimetype":"text/x-python"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T15:24:26.677355Z\",\"iopub.execute_input\":\"2021-11-07T15:24:26.678184Z\",\"iopub.status.idle\":\"2021-11-07T15:24:29.299279Z\",\"shell.execute_reply.started\":\"2021-11-07T15:24:26.678075Z\",\"shell.execute_reply\":\"2021-11-07T15:24:29.298323Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nimport pandas as pd\nimport numpy as np\n\nimport plotly.graph_objects as go\nimport plotly.express as px\n\nimport networkx as nx\nfrom scipy.io import mmread\n\nimport matplotlib.pyplot as plt\nfrom matplotlib import cm\n\nimport seaborn as sns\nfrom tqdm import tqdm\nimport random\n\nimport ortools\nfrom ortools.constraint_solver import pywrapcp, routing_enums_pb2\nfrom scipy.spatial.distance import squareform, pdist\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T15:28:02.51143Z\",\"iopub.execute_input\":\"2021-11-07T15:28:02.511702Z\",\"iopub.status.idle\":\"2021-11-07T15:28:02.530755Z\",\"shell.execute_reply.started\":\"2021-11-07T15:28:02.511673Z\",\"shell.execute_reply\":\"2021-11-07T15:28:02.529889Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nmat = mmread('../input/dataset/bio-diseasome.mtx')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:04:00.640189Z\",\"iopub.execute_input\":\"2021-11-07T16:04:00.640485Z\",\"iopub.status.idle\":\"2021-11-07T16:04:05.640808Z\",\"shell.execute_reply.started\":\"2021-11-07T16:04:00.640452Z\",\"shell.execute_reply\":\"2021-11-07T16:04:05.639856Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nG = nx.from_numpy_matrix(np.array(mat.todense()))\nplt.figure(figsize=(30,30))\ncmap = plt.cm.coolwarm\ncolors = [n for n in range(len(G.nodes()))]\npos = nx.spring_layout(G)\nnx.draw_networkx(G,pos, node_size=len(G.nodes()), cmap = cmap, node_color=colors, edge_color='grey', font_size=5, width=2, alpha=1)\nplt.show()\nplt.savefig('./output8.png')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:04:11.002068Z\",\"iopub.execute_input\":\"2021-11-07T16:04:11.002385Z\",\"iopub.status.idle\":\"2021-11-07T16:04:13.583259Z\",\"shell.execute_reply.started\":\"2021-11-07T16:04:11.002355Z\",\"shell.execute_reply\":\"2021-11-07T16:04:13.582441Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nplt.figure(figsize=(30,30))\ncmap = plt.cm.coolwarm\ncolors = [n for n in range(len(G.nodes()))]\npos = nx.circular_layout(G)\nnx.draw_networkx(G,pos, node_size=len(G.nodes()), cmap = cmap, node_color=colors, edge_color='grey', font_size=5, width=2, alpha=1)\nplt.show()\nplt.savefig('./output7.png')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T15:37:07.094639Z\",\"iopub.execute_input\":\"2021-11-07T15:37:07.094938Z\",\"iopub.status.idle\":\"2021-11-07T15:37:07.115828Z\",\"shell.execute_reply.started\":\"2021-11-07T15:37:07.094906Z\",\"shell.execute_reply\":\"2021-11-07T15:37:07.11499Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndata = pd.read_csv('../input/dataset/AH_Sickle_Cell_Disease_Provisional_Death_Counts_2019-2021.csv')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:02:11.925326Z\",\"iopub.execute_input\":\"2021-11-07T16:02:11.926145Z\",\"iopub.status.idle\":\"2021-11-07T16:02:12.005897Z\",\"shell.execute_reply.started\":\"2021-11-07T16:02:11.926102Z\",\"shell.execute_reply\":\"2021-11-07T16:02:12.004954Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.DataFrame(data)\nfig = px.parallel_coordinates(df[['Date of Death Year','Quarter','Race or Hispanic Origin' ,'Age Group','SCD_Multi']], color='SCD_Multi', color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)\nfig.show()\nfig.write_html('output6.html')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:02:22.705194Z\",\"iopub.execute_input\":\"2021-11-07T16:02:22.705892Z\",\"iopub.status.idle\":\"2021-11-07T16:02:22.779619Z\",\"shell.execute_reply.started\":\"2021-11-07T16:02:22.705853Z\",\"shell.execute_reply\":\"2021-11-07T16:02:22.778728Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.DataFrame(data)\nfig = px.parallel_coordinates(df[['Date of Death Year','Quarter','Race or Hispanic Origin' ,'Age Group','SCD_Underlying']], color='SCD_Underlying', color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)\nfig.show()\nfig.write_html('output5.html')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:02:26.969227Z\",\"iopub.execute_input\":\"2021-11-07T16:02:26.970072Z\",\"iopub.status.idle\":\"2021-11-07T16:02:27.038899Z\",\"shell.execute_reply.started\":\"2021-11-07T16:02:26.970032Z\",\"shell.execute_reply\":\"2021-11-07T16:02:27.038213Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.DataFrame(data)\nfig = px.parallel_coordinates(df[['Date of Death Year','Quarter','Race or Hispanic Origin' ,'Age Group','SCD and COVID-19']], color='SCD and COVID-19', color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)\nfig.show()\nfig.write_html('output4.html')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:02:30.799533Z\",\"iopub.execute_input\":\"2021-11-07T16:02:30.800176Z\",\"iopub.status.idle\":\"2021-11-07T16:02:30.986874Z\",\"shell.execute_reply.started\":\"2021-11-07T16:02:30.800114Z\",\"shell.execute_reply\":\"2021-11-07T16:02:30.985927Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.DataFrame(data)\nfig = px.treemap(df, path=['Date of Death Year', 'Quarter','Race or Hispanic Origin', 'Age Group'], values = 'SCD_Underlying')\nfig.show()\nfig.write_html('output3.html')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:02:34.812208Z\",\"iopub.execute_input\":\"2021-11-07T16:02:34.812473Z\",\"iopub.status.idle\":\"2021-11-07T16:02:34.97479Z\",\"shell.execute_reply.started\":\"2021-11-07T16:02:34.812446Z\",\"shell.execute_reply\":\"2021-11-07T16:02:34.973771Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.DataFrame(data)\nfig = px.treemap(df, path=['Date of Death Year', 'Quarter','Race or Hispanic Origin', 'Age Group'], values = 'SCD_Multi')\nfig.show()\nfig.write_html('output2.html')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:02:38.265454Z\",\"iopub.execute_input\":\"2021-11-07T16:02:38.265832Z\",\"iopub.status.idle\":\"2021-11-07T16:02:38.428025Z\",\"shell.execute_reply.started\":\"2021-11-07T16:02:38.265798Z\",\"shell.execute_reply\":\"2021-11-07T16:02:38.427208Z\"},\"jupyter\":{\"outputs_hidden\":false}}\ndf = pd.DataFrame(data)\nfig = px.treemap(df, path=['Date of Death Year', 'Quarter','Race or Hispanic Origin', 'Age Group'], values= 'SCD and COVID-19')\nfig.show()\nfig.write_html('output1.html')\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-11-07T16:06:48.591639Z\",\"iopub.execute_input\":\"2021-11-07T16:06:48.592332Z\",\"iopub.status.idle\":\"2021-11-07T16:06:48.846666Z\",\"shell.execute_reply.started\":\"2021-11-07T16:06:48.592289Z\",\"shell.execute_reply\":\"2021-11-07T16:06:48.845668Z\"},\"jupyter\":{\"outputs_hidden\":false}}\nA = nx.to_numpy_matrix(G)\n#sns.heatmap(A)\nplt.imshow(A)","metadata":{"_uuid":"8cfdae36-aadd-42e2-908c-88c9ea74cae2","_cell_guid":"3751e334-8aa1-47e2-bf43-00570d5c2cd4","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}