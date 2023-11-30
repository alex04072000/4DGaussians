import json

data = {}
data['camera_angle_x'] = 0.6911112070083618

frames = []
for i in range(82):
    frame_data = {}
    frame_data['file_path'] = './train/{:05d}'.format(i)
    frame_data['rotation'] = 0.031415926535897934
    frame_data['time'] = i/81
    frame_data['transform_matrix'] = [[1.0,0.0,0.0,0.0],[0.0,0.0,-1.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,0.0,1.0]]
    frames.append(frame_data)
data['frames'] = frames


# save to json
with open('data/dnerf/DAVIS_480p_bear/transforms_train.json', 'w') as outfile:
    json.dump(data, outfile)
with open('data/dnerf/DAVIS_480p_bear/transforms_test.json', 'w') as outfile:
    json.dump(data, outfile)
with open('data/dnerf/DAVIS_480p_bear/transforms_val.json', 'w') as outfile:
    json.dump(data, outfile)