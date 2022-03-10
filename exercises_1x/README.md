# Run instructions

Exercise answers are run with python3. Tested with version Python 3.8.10

## Prerequisites

opencv for python installed

```
pip3 install opencv
```

## Running

python3 task.py [ARGUMENTS]

Some python answers require arguments, which follow the form described in the task description.


## Exercise 11

1) Picture number one is tested like

```
python3 exercise_11a_flatzone.py input_gran.txt gran01_64.pgm output1.pgm
```


2) Picture number two is tested like

```
python3 exercise_11a_flatzone.py input_2.txt immed_gray_inv_20051218_frgr4.pgm output2.pgm
```

## Exercise 12

To test the exercise the following commands are run

```
8 connectivity
python3 exercise_12a_fznumber.py input_8.txt immed_gray_inv_20051218_thresh127.pgm immed_gray_20051218_8.txt
python3 exercise_12a_fznumber.py input_8.txt immed_gray_inv.pgm immed_gray_8.txt

4 connectivity
python3 exercise_12a_fznumber.py input_4.txt immed_gray_inv.pgm immed_gray_4.txt
python3 exercise_12a_fznumber.py input_4.txt immed_gray_inv_20051218_thresh127.pgm immed_gray_20051218_4.txt
```
