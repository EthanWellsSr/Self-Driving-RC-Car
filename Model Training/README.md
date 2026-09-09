# Model Training

Training code for the traffic-sign classifier (Self-Driving RC Car).

## Dataset: GTSRB (German Traffic Sign Recognition Benchmark)

The dataset is **not** committed to the repo (too large; publicly re-downloadable).
To set it up:

1. Make a free Kaggle account.
2. Download the ZIP from
   https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign?resource=download
   (the "Download" button).
3. Unzip it into `Model Training/GTSRB/` so the layout is:

   ```
   Model Training/GTSRB/
       Train/       43 class folders (0-42), images inside  <- used for training
       Test/        12,631 flat images; labels in Test.csv  <- final testing later
       Meta/        one reference image per sign class
       Train.csv  Test.csv  Meta.csv
   ```

`GTSRB/` is gitignored.
