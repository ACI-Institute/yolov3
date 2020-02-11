# Setup on Windows

Dependencies
---------
- Type 'python'.. if you get a windows store page to install 3.7, install it.
  If you already have it installed and it's not the 64bit version or 3.7, then uninstall it and install from the windows store.
- Install pipenv using ` pip install pipenv`. If you get a warning about pipenv.exe not being available in the PATH,
  you need to add the path to the System Variables (not user vars). Make sure you get the help menu when you type `pipenv`
- Install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)
  It can take a while to install (10m) and will require a restart. Obviously, you need an NVIDIA GPU to do this.
- Setup git to clone properly (avoiding stupid line ending issues) TODO

Installing
------
- Clone this repo and cd into yolov3
- Download the latest weights from [GDrive](https://drive.google.com/file/d/1nmZBGyzCbrGcjFM33uuSkHilvzFPzDEZ/view?usp=sharing) to weights/
- run `pipenv install` to install a pipenv virtualenv that keeps your python dependencies from conflicting with one another.
- You will probably get an error around "torch version not available".. that's ok, go into the next steps to fix that.
- start a pipenv shell (virtualenv) with `pipenv shell`
- run `pip install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html`

Running
--------
- Ensure you are within the `pipenv shell`.
- Having oculus sensors plugged in may cause issues finding the webcam (on linux it was an issue).
- `python detect.py --source 0 --cfg cfg\fable-yolov3.cfg --weights weights\faces4coco-yolov3_weights_best.pt`
- This should start your webcam, load the model, and start running it. It presents a UI for seeing the bounding boxes.

# NOTES: Things that didn't work

## Pyenv
- We usually use this on linux as an easier was to manage multiple accounts
- there is a pyenv-win fork that I tried to use, but it seemed a bit buggy.
- For some reason pyenv couldn't be found intermittently, may have been a bug in the PATH settings?
- By default, the windows-32 versions were installed instead of the necessary amd64 versions, so these needed to be installed explicitly.

## WSL(1)

- Looks like the camera is not available in WSL, at least at /dev/video*
- WSL by default gets the windows PATH var added to it's own PATH, seemingly making pyenv-win and pyenv conflict.

## WSL(2)
- Still in developer preview, so not available unless you subscribe to the windows beta channel and get newer versions.
- Still not sure webcam will be visible from that.

## Pipenv

- Generally worked
- Torch versions didn't work (requires a special version installed via pip)
