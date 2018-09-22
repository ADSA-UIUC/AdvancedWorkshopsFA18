# Topics that we will be covering
- Basic probability
- Bayes Theorem
- Binary Hypothesis Testing
- Bayes Classifier
- Naive Bayes Classifier


## Steps to download and format data
### Step 1
Download [mnist_train](https://pjreddie.com/media/files/mnist_train.csv) and [mnist_test](https://pjreddie.com/media/files/mnist_test.csv) 
### Step 2
Run the following command
```
python3 adsa_mnist_reader.py
``` 
This will create two files, test_data.json and train_data.json
The data format for both test_data and train_data is:
```
{

	'ClassName': [
			[pix00,pix01,pix02.....pix2727],
			[pix00,pix01,pix02.....pix2727],
			[pix00,pix01,pix02.....pix2727],
			.
			.
			.
		     ]
.
.
.
}
```
where pixXY is the pixel at the Xth row and Yth columns
and it's value is 0 for background and 1 for foreground
