{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5b096c9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "114ae546",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_csv(\"train.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d0a4918f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0         NaN             360.0   \n",
       "1             4583             1508.0       128.0             360.0   \n",
       "2             3000                0.0        66.0             360.0   \n",
       "3             2583             2358.0       120.0             360.0   \n",
       "4             6000                0.0       141.0             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  \n",
       "0             1.0         Urban           Y  \n",
       "1             1.0         Rural           N  \n",
       "2             1.0         Urban           Y  \n",
       "3             1.0         Urban           Y  \n",
       "4             1.0         Urban           Y  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "77b01daf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(614, 13)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b9080c76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 614 entries, 0 to 613\n",
      "Data columns (total 13 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Loan_ID            614 non-null    object \n",
      " 1   Gender             601 non-null    object \n",
      " 2   Married            611 non-null    object \n",
      " 3   Dependents         599 non-null    object \n",
      " 4   Education          614 non-null    object \n",
      " 5   Self_Employed      582 non-null    object \n",
      " 6   ApplicantIncome    614 non-null    int64  \n",
      " 7   CoapplicantIncome  614 non-null    float64\n",
      " 8   LoanAmount         592 non-null    float64\n",
      " 9   Loan_Amount_Term   600 non-null    float64\n",
      " 10  Credit_History     564 non-null    float64\n",
      " 11  Property_Area      614 non-null    object \n",
      " 12  Loan_Status        614 non-null    object \n",
      "dtypes: float64(4), int64(1), object(8)\n",
      "memory usage: 62.5+ KB\n"
     ]
    }
   ],
   "source": [
    "dataset.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "621f361a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>614.000000</td>\n",
       "      <td>614.000000</td>\n",
       "      <td>592.000000</td>\n",
       "      <td>600.00000</td>\n",
       "      <td>564.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5403.459283</td>\n",
       "      <td>1621.245798</td>\n",
       "      <td>146.412162</td>\n",
       "      <td>342.00000</td>\n",
       "      <td>0.842199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6109.041673</td>\n",
       "      <td>2926.248369</td>\n",
       "      <td>85.587325</td>\n",
       "      <td>65.12041</td>\n",
       "      <td>0.364878</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>150.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>12.00000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2877.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3812.500000</td>\n",
       "      <td>1188.500000</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>5795.000000</td>\n",
       "      <td>2297.250000</td>\n",
       "      <td>168.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>81000.000000</td>\n",
       "      <td>41667.000000</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>480.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "count       614.000000         614.000000  592.000000         600.00000   \n",
       "mean       5403.459283        1621.245798  146.412162         342.00000   \n",
       "std        6109.041673        2926.248369   85.587325          65.12041   \n",
       "min         150.000000           0.000000    9.000000          12.00000   \n",
       "25%        2877.500000           0.000000  100.000000         360.00000   \n",
       "50%        3812.500000        1188.500000  128.000000         360.00000   \n",
       "75%        5795.000000        2297.250000  168.000000         360.00000   \n",
       "max       81000.000000       41667.000000  700.000000         480.00000   \n",
       "\n",
       "       Credit_History  \n",
       "count      564.000000  \n",
       "mean         0.842199  \n",
       "std          0.364878  \n",
       "min          0.000000  \n",
       "25%          1.000000  \n",
       "50%          1.000000  \n",
       "75%          1.000000  \n",
       "max          1.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c10dd243",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Loan_Status</th>\n",
       "      <th>N</th>\n",
       "      <th>Y</th>\n",
       "      <th>All</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit_History</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0.0</th>\n",
       "      <td>82</td>\n",
       "      <td>7</td>\n",
       "      <td>89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1.0</th>\n",
       "      <td>97</td>\n",
       "      <td>378</td>\n",
       "      <td>475</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>All</th>\n",
       "      <td>179</td>\n",
       "      <td>385</td>\n",
       "      <td>564</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Loan_Status       N    Y  All\n",
       "Credit_History               \n",
       "0.0              82    7   89\n",
       "1.0              97  378  475\n",
       "All             179  385  564"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(dataset['Credit_History'], dataset['Loan_Status'], margins=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b445c13a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset.boxplot(column='ApplicantIncome')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ea92f01c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['ApplicantIncome'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "20bb44d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['CoapplicantIncome'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0fd20a81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'ApplicantIncome'}, xlabel='Education'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAY4AAAEcCAYAAADQqlM0AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAuwUlEQVR4nO3de3xddZ3v/9e7SUsLCFIumUKBdqTjSRsPxWYYdOpMY1XQOQ51DmgLStF4OnI4URlFwTDKnDHzA1HxyM2pRikogYIjoA6DWBo1w7UgSGlkrFKgUsBSwBalkPTz+2N9d1nZzWWvXrKT9v18PPZjr/1d67vWd+2s7M/+Xvb6KiIwMzOr1JhqF8DMzEYXBw4zMyvEgcPMzApx4DAzs0IcOMzMrBAHDjMzK8SBw6pGUkg6qtrlqCZJcyStHWR9Vd4jSVdK+nwVjvuwpDnDfVwrxoHDkLRG0h8lbZL0nKQfSjq82uUqkXS6pK5ql2M0S+9hb/ob5x+HVrFM2wSniJgREZ1VKpJVyIHDSt4dEfsCk4CngUuqXJ5dRlJttctQJXdGxL5ljyerXSgbfRw4rI+IeAm4AZheSpO0v6SrJP1O0mOSzpM0RtJESWslvTttt6+k1ZJOS6+vlPQ1SbdJ2ijpJ5KO7O+4gxyjHvga8Kb0Dfn5AfJPlfTTdJwfS7pM0rfTuimpyadZ0uPA7Wnf56VjPZOOvX/afpvmo1Qre1taPl/SDZKuS8e7X9LRuW0PlfTddC6PSvpobt2E9L48J2kV8OcV/FneJek3ktZLuiiVfS9JGyS9IbfvQ1LN8eAK9ln+/h2TzmOjpOuA8bl129T48k1o6Zy+lN7LFyR1SZqQ1l0v6amU/lNJM1L6IuBU4FPp7/r9ft7nvSR9RdKT6fEVSXuldXPStfeJ9PdbJ+mDRc/bto8Dh/UhaW/gfcBdueRLgP2BPwX+GjgN+GBEbAA+BHxd0iHAxcADEXFVLu+pwD8DBwEPAN8Z4NADHaMb+Aivflt+7QD5rwHuAQ4Ezgc+0M82fw3UA8cDp6dHUzrmvsClA+y7PycC1wMT07FvlDRW0hjg+8CDwGHAXODjko5P+T4HvC49jgcWVnCs9wCNwBvTcT8UEZuBa4H357ZbAPw4In5X4DyQNA64Ebg6nc/1wP8ssIsvArOAN6f8nwK2pHW3ANOAQ4D7SX//iFiclr+Q/q7v7me/rcBxwEzgaOBY4Lzc+j8hu2YOA5qByyQdUKDctr0iwo89/AGsATYBzwM9wJPAG9K6GmAzMD23/d8DnbnXlwAPpXwH5tKvBK7Nvd4X6AUOT68DOGqoY5B9wHcNUv4jUrn3zqV9G/h2Wp6SjvWnufXLgP+de/164BWgFpgDrO3nPXpbWj4fuCu3bgywDngL8BfA42V5zwW+lZZ/A5yQW7eo/FhleaNs+/8NLEvLfwE8AYxJr1cA7x1gP6en9+j53OPXad1fpb+dctvfAXx+oPc/97cbA/wROLqC6+y1Kd/+uevj84O8z78G3pVbdzywJi3PScetza1/Bjiu2v9Pe8LDNQ4rmRfZt/m9gP8D/ETSn5DVFMYBj+W2fYzsW17JYqCB7MPx2bL9PlFaiIhNwAagvEO2kmMM5lBgQ0T8ob/jDpB2aD/HqwXqKjxm/ry2AGvTPo8EDpX0fOkBfCa330PLypEvw5DHStsfmo57N/Ai8NeS/hvZB/nNg+znroh4be7xulyZfhvp07dAuSD7240n+5DvQ1KNpAsk/VrS78mCQilPJfr7G+WvnWcjoif3+g9kX05sF3PgsD4iojci/o2sZjAbWE/2TTzfN3EE8FvIPhyAfwWuAs7QtkNHt47OkrQvWVNGeYfsoMcg+5Y6mHXAxNTMts1x86eXW34SODLXfl+qtTxC1vyxdV/pHMv7DfLnNQaYnPb5BPBo2Qf0ayLiXbmy5st2xBDnVn4uR9D3/VtC1lz1AeCGyPqoiloHHCZJA5TrRfq+H3+SW7ceeIms6a3cKWRNa28je0+nlHaRnof6uz7JtteEO/NHAAcO60OZE4EDgO6I6AWWAm2SXqOsc/sfyJqCIPs2DVlfxxeBq9IHbcm7JM1O7ej/DNwdEX1qAxUc42lgsqRxkjpTx/JeufyPkTXTnJ+2eRPQX5t5XgdwFtm33zHAvwDXRTayrBMYL+lvJI0la1ffqyz/LEl/p2yE1sfJmtruIutn+b2kT6dO4xpJDZJKneBLgVskvVHSZKAF2Ku8M77M2ZIOUDZE+mPAdbl1V5P1gbyfLHhvjzvJguZHJdVK+juy/oSSB4EZkmZKGk/WVAdsrW19E/hyGhRQI+lN6e/zmvS+PEsWeP6l7LhPk/UvDaQDOE/SwZIOAj7Lq9eEVVO128r8qP6DrAnhj2T9HBuBlcCpufUHkP3D/o7sG/VnyT5sZwHPAUel7WqA/wRa0+sryUZE3Zb2/VNgam6/kcvb7zHSunHAD8na5YOsuevksnN4HfCzVP5lZM1n7WndlJQv3x4+Jh3jWbLazreBA3LrTyf7Jv4M8Em27eO4gewDfCPwc+CNubyHkn3oPZXen7tyefdOZfk9sAo4O51zv/0caduPkvWNPAt8Cagp2+bHqXzqbx+58+lNf4f848/T+sZ0HhvTeV1Hrv+BrKN6ffrbvL/sbzcB+ApZDfGF9HeeQNZsdFPa52NkAx7y+aaRDZh4Hrgxdy2W3qvxwFfT32FdWh6f1s0pf8/yef3YxZ8Z1S6AH7vvg346P3dwf58lC0xfBn5QdpxSgNoI/IRsZNM/pfX5D9/1wEW8GpROJ9fx288H4pfSh94LQFdKOz+lPZX7oJxRVp7LyILdRuBu4HVp3U/TMV5MH9zvK/8QJKvx/HM6143Aj4CDcutnk3VeP58+yH8KfJ6sOegqskD0GFlNKX+e/0k28u359F68OaU/QRYgF+aOsRdZDfJxsprB14AJ1b6m/BgZDzdV2WhyGtkQzu8Ax0vKd2R/AGgn64t4DvgbsiGmJdsMaa3geIMNM32SfoaZ5iwA/omsJrUaaAOIiL9K64+ObBjqdfTvFOCDaf/jyGo9SDqCbIjrJelc3w0ck8693yHNuX3+BfALsiHL15AN5/1zsk719wOXpn4ogAuBPyMbCnsU2UCFzw74TtkexYHDRgVJs8k6SpdGxH1ko3hOyW1yH1lNYgMwI6Wtz62/MCI2RMTjZM0qC4Y43hiy4PKxiPhtZIMG7ojs9xOQDWXdmF6fDxyt9APC5N8i4p7IRv18h+wDuIhvRcR/RcQfyfpFSvlPJfutRgfZB3kXcAFZzeB9wLmpXGvIakv537M8GhHfiqxP6TqyTvf/GxGbI+JHwMvAUamT/H8BZ6X3bCNZ/8T8gudgu6k99dYLNgwi4vSduLuFwI8iohQMrklpF6fXd+e+zSPpd/Qd+trvkNZBDDjMlKwZqU3Sr8m+9W/J5XkhLT+V2357hokOlP/wUpki4h+BfwRIta+hhjQ/nVv+Y9pHedq+ZOe0N3BfbqCVyPqwzBw4bORLt694L1AjqfSBuhfwWr16q4+hhv0eDjyclisZ1pkfZvpg2br8MNM1ZM1Dz/HqMNNd6Qn6jngqyQ9pXpXS8kOai1hPFkRmRMT25LfdnJuqbDSYRzYiaDpZk81MsluH/IysHR+GHvY72JDWbcSODTMdylDDUAfzHeBtkt6bhs4eKGlmDD2kuWLp3L8OXJxuJYOkw3K3TbE9nAOHjQYLydr8H4+Ip0oPsntLnUpWc76G7D5QG8g6tE8t28dNZP0gD5CNdmqv4LifJLuVyr1pvxeS/c9cRdYM9Fuyb/d3DbSDAZwPLEm/LH9vkYypj+ZdwCdSmR4gu48TZL8JeZFsxFQX2XvyzYJlK/k0Waf+XelX3z8muy2LWTbu22w0k3Ql2XDW8wZYH8C0iFg9rAUz2025xmFmZoU4cJiZWSFuqjIzs0Jc4zAzs0IcOMzMrJBR+wPAgw46KKZMmVLtYux2XnzxRfbZZ59qF8OsYr5md5377rtvfURsM4f9qA0cU6ZMYcWKFdUuxm6ns7OTOXPmVLsYZhXzNbvrSOp3Jkg3VZmZWSEOHGZmVogDh5mZFeLAYWZmhThwmJlZIQ4cBkBHRwcNDQ3MnTuXhoYGOjo6ql0kMxuhKhqOK+ks4MNAkN1m+oNk8xBcB0whm8zmvRHxXNr+XKCZbA6Fj0bErSl9FnAlMAH4d7JpOSPNcXAV2e2wnwXel6a+tGHQ0dFBa2sr7e3t9Pb2UlNTQ3NzMwALFgw6w6qZ7YGGrHFIOgz4KNAYEQ1k00fOB84BlkXENGBZeo2k6Wn9DOAE4HJJpSknrwAWAdPS44SU3gw8FxFHkU0FeuFOOTurSFtbG+3t7TQ1NVFbW0tTUxPt7e20tbVVu2hmNgJV2lRVC0yQVEtW03iSbOrMJWn9ErJZ2kjp10bE5oh4lGwymGMlTQL2i4g7I7uz4lVleUr7ugGYq9xkx7ZrdXd3M3v27D5ps2fPpru7u0olMrORbMjAkeYc/iLwOLAOeCEifgTURcS6tM064JCU5TCyeZFL1qa0w9JyeXqfPBHRA7wAHLh9p2RF1dfX09XV1Setq6uL+vr6KpXIzEayIfs4JB1AViOYCjwPXC/p/YNl6SctBkkfLE95WRaRNXVRV1dHZ2fnIMWwSr3nPe/h1FNP5eyzz2bq1KlcfPHFXHTRRTQ3N/s9thFv06ZNvk6HWSWd428DHo2I3wFI+jfgzcDTkiZFxLrUDPVM2n4tcHgu/2Sypq21abk8PZ9nbWoO259sPuU+ImIxsBigsbExfH+anWPOnDlMnz6dtrY2uru7qa+v50tf+pI7xm1U8L2qhl8lfRyPA8dJ2jv1O8wFuoGbgYVpm4XATWn5ZmC+pL0kTSXrBL8nNWdtlHRc2s9pZXlK+zoJuD08w9SwWrBgAStXrmTZsmWsXLnSQcPMBjRkjSMi7pZ0A3A/0AP8nOxb/77AUknNZMHl5LT9w5KWAqvS9mdGRG/a3Rm8Ohz3lvQAaAeulrSarKYxf6ecnZmZ7XQV/Y4jIj4HfK4seTNZ7aO/7duAbcZyRsQKoKGf9JdIgcfMzEY2/3LczMwKceAwM7NCHDjMzKwQBw4zMyvEgcPMzApx4DAzs0IcOMzMrBAHDjMzK8SBw8zMCnHgMDOzQhw4zMysEAcOMzMrxIHDzMwKceAwM7NCHDjMzKwQBw4zMytkyMAh6fWSHsg9fi/p45ImSrpN0q/S8wG5POdKWi3pEUnH59JnSXoorftqmkKWNM3sdSn9bklTdsnZmpnZDhsycETEIxExMyJmArOAPwDfA84BlkXENGBZeo2k6WRTv84ATgAul1STdncFsIhsHvJpaT1AM/BcRBwFXAxcuFPOzszMdrqiTVVzgV9HxGPAicCSlL4EmJeWTwSujYjNEfEosBo4VtIkYL+IuDMiAriqLE9pXzcAc0u1ETMzG1kqmnM8Zz7QkZbrImIdQESsk3RISj8MuCuXZ21KeyUtl6eX8jyR9tUj6QXgQGB9/uCSFpHVWKirq6Ozs7Ng8W0omzZt8vtqo4qv2eFXceCQNA74W+DcoTbtJy0GSR8sT9+EiMXAYoDGxsaYM2fOEEWxojo7O/H7aqOJr9nhV6Sp6p3A/RHxdHr9dGp+Ij0/k9LXAofn8k0Gnkzpk/tJ75NHUi2wP7ChQNnMzGyYFAkcC3i1mQrgZmBhWl4I3JRLn59GSk0l6wS/JzVrbZR0XOq/OK0sT2lfJwG3p34QMzMbYSpqqpK0N/B24O9zyRcASyU1A48DJwNExMOSlgKrgB7gzIjoTXnOAK4EJgC3pAdAO3C1pNVkNY35O3BOZma2C1UUOCLiD2Sd1fm0Z8lGWfW3fRvQ1k/6CqChn/SXSIHHzMxGNv9y3MzMCnHgMDOzQhw4zMysEAcOMzMrxIHDzMwKceAwM7NCHDjMzKwQBw4zMyvEgcMA6OjooKGhgblz59LQ0EBHR8fQmcxsj1T0tuq2G+ro6KC1tZX29nZ6e3upqamhubkZgAULFlS5dGY20rjGYbS1tdHe3k5TUxO1tbU0NTXR3t5OW9s2d40xM3PgMOju7mb27Nl90mbPnk13d3eVSmRmI5kDh1FfX09XV1eftK6uLurr66tUIjMbyRw4jNbWVpqbm1m+fDk9PT0sX76c5uZmWltbq100MxuB3DluWzvAW1pa6O7upr6+nra2NneMm1m/KqpxSHqtpBsk/VJSt6Q3SZoo6TZJv0rPB+S2P1fSakmPSDo+lz5L0kNp3VfTTICk2QKvS+l3S5qy08/UBrVgwQJWrlzJsmXLWLlypYOGmQ2o0qaq/wf8R0T8N+BooBs4B1gWEdOAZek1kqaTzeA3AzgBuFxSTdrPFcAisulkp6X1AM3AcxFxFHAxcOEOnpeZme0iQwYOSfsBf0U2vSsR8XJEPA+cCCxJmy0B5qXlE4FrI2JzRDwKrAaOlTQJ2C8i7kzziV9Vlqe0rxuAuaXaiJmZjSyV1Dj+FPgd8C1JP5f0DUn7AHURsQ4gPR+Stj8MeCKXf21KOywtl6f3yRMRPcALlE1Va2ZmI0MlneO1wBuBloi4W9L/IzVLDaC/mkIMkj5Ynr47lhaRNXVRV1dHZ2fnIMWw7bFp0ya/rzaq+JodfpUEjrXA2oi4O72+gSxwPC1pUkSsS81Qz+S2PzyXfzLwZEqf3E96Ps9aSbXA/sCG8oJExGJgMUBjY2PMmTOnguJbEZ2dnfh9tdHE1+zwG7KpKiKeAp6Q9PqUNBdYBdwMLExpC4Gb0vLNwPw0UmoqWSf4Pak5a6Ok41L/xWlleUr7Ogm4PfWDmJnZCFPp7zhagO9IGgf8BvggWdBZKqkZeBw4GSAiHpa0lCy49ABnRkRv2s8ZwJXABOCW9ICs4/1qSavJahrzd/C8zMxsF6kocETEA0BjP6vmDrB9G7DNHfIiYgXQ0E/6S6TAY2ZmI5tvOWJmZoU4cJiZWSEOHGZmVogDh5mZFeLAYWZmhThwmJlZIQ4cZmZWiAOHmZkV4sBhZmaFOHCYmVkhDhxmZlaIA4eZmRXiwGEAdHR00NDQwNy5c2loaKCjo6PaRTKzEarS26rbbqyjo4PW1lba29vp7e2lpqaG5uZmABYsWFDl0pnZSOMah9HW1kZ7eztNTU3U1tbS1NREe3s7bW3b3BnfzKyywCFpjaSHJD0gaUVKmyjpNkm/Ss8H5LY/V9JqSY9IOj6XPivtZ7Wkr6aZAEmzBV6X0u+WNGUnn6cNoru7m9mzZ/dJmz17Nt3d3VUqkZmNZEVqHE0RMTMiShM6nQMsi4hpwLL0GknTyWbwmwGcAFwuqSbluQJYRDad7LS0HqAZeC4ijgIuBi7c/lOyourr6+nq6uqT1tXVRX19fZVKZGYj2Y40VZ0ILEnLS4B5ufRrI2JzRDwKrAaOlTQJ2C8i7kzziV9Vlqe0rxuAuaXaiO16ra2tNDc3s3z5cnp6eli+fDnNzc20trZWu2hmNgJV2jkewI8kBfCvEbEYqIuIdQARsU7SIWnbw4C7cnnXprRX0nJ5einPE2lfPZJeAA4E1hc/JSuq1AHe0tJCd3c39fX1tLW1uWPczPpVaeD4y4h4MgWH2yT9cpBt+6spxCDpg+Xpu2NpEVlTF3V1dXR2dg5aaKvcpEmTuPTSS9m0aRP77rsvgN9fGxU2bdrka3WYVRQ4IuLJ9PyMpO8BxwJPS5qUahuTgGfS5muBw3PZJwNPpvTJ/aTn86yVVAvsD2zopxyLgcUAjY2NMWfOnEqKbwV0dnbi99VGE1+zw2/IPg5J+0h6TWkZeAewErgZWJg2WwjclJZvBuankVJTyTrB70nNWhslHZf6L04ry1Pa10nA7akfxMzMRphKahx1wPdSX3UtcE1E/Ieke4GlkpqBx4GTASLiYUlLgVVAD3BmRPSmfZ0BXAlMAG5JD4B24GpJq8lqGvN3wrmZmdkuMGTgiIjfAEf3k/4sMHeAPG3ANr8ei4gVQEM/6S+RAo+ZmY1s/uW4mZkV4sBhZmaFOHCYmVkhDhxmZlaIA4eZmRXiwGFmZoU4cJiZWSEOHGZmVogDh5mZFeLAYWZmhThwmJlZIQ4cZmZWiAOHmZkV4sBhZmaFOHCYmVkhDhxmZlZIxYFDUo2kn0v6QXo9UdJtkn6Vng/IbXuupNWSHpF0fC59lqSH0rqvpilkSdPMXpfS75Y0ZSeeo1Wgo6ODhoYG5s6dS0NDAx0dHdUukpmNUJVMHVvyMaAb2C+9PgdYFhEXSDonvf60pOlkU7/OAA4Ffizpz9L0sVcAi4C7gH8HTiCbPrYZeC4ijpI0H7gQeN8On51VpKOjg9bWVtrb2+nt7aWmpobm5mYAFixYUOXSmdlIU1GNQ9Jk4G+Ab+SSTwSWpOUlwLxc+rURsTkiHgVWA8dKmgTsFxF3RkQAV5XlKe3rBmBuqTZiu15bWxunnHIKLS0tHH/88bS0tHDKKafQ1rbN7L9mZhXXOL4CfAp4TS6tLiLWAUTEOkmHpPTDyGoUJWtT2itpuTy9lOeJtK8eSS8ABwLr84WQtIisxkJdXR2dnZ0VFt8Gs2rVKp599lk+9alPMXXqVB599FG+8IUv8PTTT/s9thFv06ZNvk6H2ZCBQ9L/AJ6JiPskzalgn/3VFGKQ9MHy9E2IWAwsBmhsbIw5cyopjg1l3LhxnH322Zx11ll0dnZy1llnERF85jOfwe+xjXSdnZ2+TodZJTWOvwT+VtK7gPHAfpK+DTwtaVKqbUwCnknbrwUOz+WfDDyZ0if3k57Ps1ZSLbA/sGE7z8kKevnll7nkkks45phj6O3tZfny5VxyySW8/PLL1S6amY1AQ/ZxRMS5ETE5IqaQdXrfHhHvB24GFqbNFgI3peWbgflppNRUYBpwT2rW2ijpuNR/cVpZntK+TkrH2KbGYbvG9OnTmTlzJu985zt5+9vfzjvf+U5mzpzJ9OnTq100MxuBioyqKncBsFRSM/A4cDJARDwsaSmwCugBzkwjqgDOAK4EJpCNprolpbcDV0taTVbTmL8D5bKCmpqa+NrXvsaFF17I9OnTWbVqFZ/+9Kf5yEc+Uu2imdkIpNH6xb6xsTFWrFhR7WLsFhoaGpg3bx433ngj3d3d1NfXb329cuXKahfPbFDu49h1JN0XEY3bpDtwWE1NDS+99BJjx47d+k/4yiuvMH78eHp7e4fegVkVOXDsOgMFDt9yxKivr6erq6tPWldXF/X19VUqkZmNZA4cRmtrK83NzSxfvpyenh6WL19Oc3Mzra2t1S6amY1AO9I5bruJ0m1FWlpatvZxtLW1+XYjZtYvBw4DsuCxYMECtxeb2ZDcVGVmZoU4cBjg26qbWeXcVGW+rbqZFeIah9HW1kZ7eztNTU3U1tbS1NREe3u7b6tuZv1y4DC6u7uZPXt2n7TZs2fT3d1dpRKZ2UjmwGH+AaCZFeLAYf4BoJkV4s5x8w8AzawQBw4D/ANAM6ucm6rMzKyQIQOHpPGS7pH0oKSHJf1TSp8o6TZJv0rPB+TynCtptaRHJB2fS58l6aG07qtpJkDSbIHXpfS7JU3ZBedqZmY7QSU1js3AWyPiaGAmcIKk44BzgGURMQ1Yll4jaTrZDH4zgBOAyyXVpH1dASwim052WloP0Aw8FxFHARcDF+74qZmZ2a5QyZzjERGb0sux6RHAicCSlL4EmJeWTwSujYjNEfEosBo4VtIkYL+IuDPNJ35VWZ7Svm4A5pZqI2ZmNrJU1Dmeagz3AUcBl0XE3ZLqImIdQESsk3RI2vww4K5c9rUp7ZW0XJ5eyvNE2lePpBeAA4H1ZeVYRFZjoa6ujs7OzgpP0yq1adMmv682qviaHX4VBY6I6AVmSnot8D1JDYNs3l9NIQZJHyxPeTkWA4shmzrWo392Po+qstHG1+zwKzSqKiKeBzrJ+iaeTs1PpOdn0mZrgcNz2SYDT6b0yf2k98kjqRbYH9hQpGxmZjY8KhlVdXCqaSBpAvA24JfAzcDCtNlC4Ka0fDMwP42UmkrWCX5PatbaKOm41H9xWlme0r5OAm5P/SBmZjbCVNJUNQlYkvo5xgBLI+IHku4ElkpqBh4HTgaIiIclLQVWAT3AmampC+AM4EpgAnBLegC0A1dLWk1W05i/M07OzMx2viEDR0T8Ajimn/RngbkD5GkDtrknd0SsALbpH4mIl0iBx8zMRjb/ctzMzApx4DAzs0IcOMzMrBAHDjMzK8SBw8zMCnHgMDOzQhw4zMysEAcOA6Cjo4OGhgbmzp1LQ0MDHR0d1S6SmY1QnjrW6OjooLW1lfb2dnp7e6mpqaG5uRnA846b2TZc4zDa2tpob2+nqamJ2tpampqaaG9vp61tmx//m5k5cBh0d3cze/bsPmmzZ8+mu7u7SiUys5HMgcOor6+nq6urT1pXVxf19fVVKpGZjWQOHEZrayvNzc0sX76cnp4eli9fTnNzM62trdUumpmNQO4ct60d4C0tLXR3d1NfX09bW5s7xs2sX65xGAB33HEHq1evZsuWLaxevZo77rij2kUysxGqkhkAD5e0XFK3pIclfSylT5R0m6RfpecDcnnOlbRa0iOSjs+lz5L0UFr31TQTIGm2wOtS+t2SpuyCc7UBtLS0cNlll9HT0wNAT08Pl112GS0tLVUumZmNRJXUOHqAT0REPXAccKak6cA5wLKImAYsS69J6+YDM8jmJr88zR4IcAWwiGw62WlpPUAz8FxEHAVcDFy4E87NKnTFFVcQERx88MGMGTOGgw8+mIjgiiuuqHbRzGwEGjJwRMS6iLg/LW8EuoHDgBOBJWmzJcC8tHwicG1EbI6IR4HVwLGSJgH7RcSdaT7xq8rylPZ1AzC3VBuxXa+3t5d99tmH8ePHAzB+/Hj22Wcfent7h8hpZnuiQp3jqQnpGOBuoC4i1kEWXCQdkjY7DLgrl21tSnslLZenl/I8kfbVI+kF4EBgfZHy2fYbM2YM3/zmN7f+cvzEE0+sdpHMbISqOHBI2hf4LvDxiPj9IBWC/lbEIOmD5SkvwyKypi7q6uro7OwcotRWqY0bN3L99dfz1re+ldtvv52NGzcC+D22EW/Tpk2+TodbRAz5AMYCtwL/kEt7BJiUlicBj6Tlc4Fzc9vdCrwpbfPLXPoC4F/z26TlWrKahgYr06xZs8J2DrIg3e/DbKS65pprYsaMGTFmzJiYMWNGXHPNNdUu0m4HWBH9fP4OWeNIfQ3tQHdEfDm36mZgIXBBer4pl36NpC8Dh5J1gt8TEb2SNko6jqyp6zTgkrJ93QmcBNyeCm3DYOLEiWzYsIGampqtTVW9vb1MnDix2kUz65dvzFldGurzWdJs4GfAQ8CWlPwZsg//pcARwOPAyRGxIeVpBT5ENiLr4xFxS0pvBK4EJgC3AC0REZLGA1eT9Z9sAOZHxG8GK1djY2OsWLGi6PlaPw4//HA2bNjAK6+8wiuvvMLYsWMZO3YsEydO5Iknnqh28cy20dDQwLx587jxxhu3/mi19HrlypXVLt5uQ9J9EdG4Tfpo/WLvwLHzjBkzhoMOOoh99tmHxx9/nCOOOIIXX3yR9evXs2XLlqF3YDbMxowZw5FHHtlnQMeHPvQhHnvsMV+zO9FAgcO/HDfGjRtHTU0Na9asYcuWLaxZs4aamhrGjRtX7aKZ9WvcuHG0tLT0mQqgpaXF1+ww8b2qjM2bN/PUU08hiYhAEk899VS1i2U2oJdffplLL72UY445ht7eXpYvX86ll17Kyy+/XO2i7REcOGyrMWPG0Nvbu/XZbKSaPn068+bN63NjzlNOOYUbb7yx2kXbIzhw2FZf+MIXmD59OqtWreITn/hEtYtjNqDW1tZ+R1V51srh4cBhANTW1vYJFrW1tVtvemg20ngqgOryqCpjsNuCjdbrw/YcnZ2dzJkzp9rF2C15VJWZme0UDhwGZB3jg702Myvxp4MBWXPV2LFjARg7duygzVdmtmdz57gB2ZwcpV/c9vT0uG/DzAbkGodtVQoWDhpmNhgHDjMzK8SBw7YqdYi7Y9zMBuNPCNuq1Mfhu4ua2WAcOMzMrJAhA4ekb0p6RtLKXNpESbdJ+lV6PiC37lxJqyU9Iun4XPosSQ+ldV9NMwsiaS9J16X0uyVN2cnnaBUqDcH1UFwzG0wlNY4rgRPK0s4BlkXENGBZeo2k6cB8YEbKc7mkmpTnCmAR2VSy03L7bAaei4ijgIuBC7f3ZGzHHHLIIX2ezcz6M2TgiIifkk3nmncisCQtLwHm5dKvjYjNEfEosBo4VtIkYL+IuDPNJX5VWZ7Svm4A5spfeavi2Wef7fNsZtaf7e3jqIuIdQDpufQV9TAgP0n12pR2WFouT++TJyJ6gBeAA7ezXFYhSVsfJaW74ebvipvfzvHczGDn/3K8v0+WGCR9sDzb7lxaRNbcRV1dHZ2dndtRRANYvnz51uWzzz6b/u403NjYyEUXXdQnze+5jTSbNm3ydTnMtjdwPC1pUkSsS81Qz6T0tcDhue0mA0+m9Mn9pOfzrJVUC+zPtk1jAETEYmAxZLdV962Ud457772X448/nttuu23r1LFvf/vbufXWW6tdNLMh+bbqw297m6puBham5YXATbn0+Wmk1FSyTvB7UnPWRknHpf6L08rylPZ1EnB7+J4Xw+7WW29ly5YtHPnpH7BlyxYHDTMbUCXDcTuAO4HXS1orqRm4AHi7pF8Bb0+viYiHgaXAKuA/gDMjojR59RnAN8g6zH8N3JLS24EDJa0G/oE0QsvMbDAtLS2MHz+epqYmxo8fT0tLS7WLtMcYsqkqIgaai3HuANu3AdtM/BsRK4CGftJfAk4eqhxmZiUtLS1ceumlW19v3rx56+tLLrmkWsXaY/iX42Y26lx22WUAnHHGGXz/+9/njDPO6JNuu5YDh5mNOhHBhz/8YS6//HL23XdfLr/8cj784Q97SoBh4sBhZqPSlClTBn1tu45nADSzUaH8B6jnnXce55133pDbuRay87nGYWajQkRsfbzjHe8Atp1D5h3veEef7Rw0dg2N1je2sbEx+vu1s/V19D/9iBf++MouPcb+E8by4OfesUuPYVbOP1rd9STdFxGN5eluqtrNvfDHV1hzwd9UvP32/Ap3yjk/LFgqsx1XChJTzvlhoWvcdpybqszMrBAHDjMzK8RNVWY2Ymxvn1zR5lL3y+0YB47d3Gvqz+ENSwre/mvJ0Jv0PQaA25htxxXtkwP3y1WDA8dubmP3Be4ct1Fju77ogL/sDDMHjj1A4Q/2/yhe7TfbGYp+0QF/2akGB47dXNF/Qg9ttGrbrg91f9kZVg4cZjZibM+XFn/ZGX4ejmtmZoWMmMAh6QRJj0haLcmzAJqZjVAjInBIqgEuA94JTAcWSJpe3VKZmVl/RkTgAI4FVkfEbyLiZeBa4MQql8nMzPoxUjrHDwOeyL1eC/xF+UaSFgGLAOrq6ujs7ByWwu2OmpqaBlynCwfOt3z58l1QGrOh+ZodOUZK4FA/advc7z0iFgOLIbutetGx2/aqgW6nvz1j4s2Gg6/ZkWOkNFWtBQ7PvZ4MPFmlspiZ2SBGSuC4F5gmaaqkccB84OYql8nMzPoxIpqqIqJH0v8BbgVqgG9GxMNVLpaZmfVjRAQOgIj4d+Dfq10OMzMb3EhpqjIzs1HCgcPMzApx4DAzs0IcOMzMrBAN9KOakU7S74DHql2O3dBBwPpqF8KsAF+zu86REXFweeKoDRy2a0haERGN1S6HWaV8zQ4/N1WZmVkhDhxmZlaIA4eVW1ztApgV5Gt2mLmPw8zMCnGNw8zMCnHgGMUk1Um6RtJvJN0n6U5J79mB/Z0v6ZPbmXeKpFO299g2ekkKSV/Kvf6kpPOHyDNvsOmhJb1f0i8kPSzpQUnfkPTaHSznph3Ie7qkQ3fk+LsTB45RSpKAG4GfRsSfRsQsstvRTy7bbrhuZDkFcODYM20G/k7SQQXyzAP6DRySTgDOAt4ZETOANwJ3AHX9bFtTuLTb53TAgSNx4Bi93gq8HBFfKyVExGMRcUn6dnS9pO8DP5K0r6Rlku6X9JCkrfO5S2qV9IikHwOvz6V3SmpMywdJWpOWp0j6WdrX/ZLenLJcALxF0gOSzpJUI+kiSfemb45/v+vfEquSHrIO6rPKV0g6Ml17v0jPR6Rr5m+Bi9L18rqybK3AJyPitwAR0RsR34yIR9I+10j6rKQu4GRJ/ytdZw9K+q6kvdN2U1Mt/F5J/5wr0xxJP8i9vlTS6Wn5s2n7lZIWK3MS0Ah8J5V3gqRZkn6Savq3Spq0897OUSAi/BiFD+CjwMUDrDudbFbFiel1LbBfWj4IWE02Xe8s4CFgb2C/lP7JtF0n0JjLsyYt7w2MT8vTgBVpeQ7wg1wZFgHnpeW9gBXA1Gq/b37skmtxU7p+1gD7A58Ezk/rvg8sTMsfAm5My1cCJw2wvw3A/oMcbw3wqdzrA3PLnwda0vLNwGlp+UxgU1ouv1YvBU5PyxNz6VcD707L+f+HsWQ1oIPT6/eRzSFU9b/FcD1c49hNSLosfeO6NyXdFhEbSquBf5H0C+DHwGFk1f63AN+LiD9ExO+pbNbFscDXJT0EXM8AzQ3AO4DTJD0A3A0cSBZobDeUrp+ryL7Q5L0JuCYtXw3MLrJfSW9I3/J/Lel9uVXX5ZYbUi34IeBUYEZK/0ugI3fsSjRJujvt6625feW9HmgAbkvX93mUNRHv7kbMRE5W2MPA/yy9iIgzUxvzipT0Ym7bU4GDgVkR8UpqdhpfyjrA/nt4tSlzfC79LOBp4Oi0/qUB8ovsm9+tFZ2N7Q6+AtwPfGuQbSoZ//8wWb/G8oh4CJgp6VJgQm6b/PV9JTAvIh5MTU5zhjhe/tqGdH1LGg9cTlazeCJ18I/fNjsCHo6IN1VwLrsl1zhGr9uB8ZLOyKXtPcC2+wPPpKDRBByZ0n8KvCe12b4GeHcuzxqypiyAk8r2tS4itgAfIJvqF2Aj8JrcdrcCZ0gaCyDpzyTtU+QEbXRJNdylQHMu+Q6yQRuQfYHpSsvl10ve/wd8UVL+W/yEAbYl7WddutZOzaX/Z9mxSx4DpkvaS9L+wNyUXgoS6yXtS9/rPl/eR4CDJb0JQNJYSf3VTHZbDhyjVGSNq/OAv5b0qKR7gCXAp/vZ/DtAo6QVZP9Av0z7uJ+syv8A8F3gZ7k8XyT74L+DrI+j5HJgoaS7gD/j1W9+vwB6UnPZWcA3gFXA/ZJWAv+Ka7h7gi/R93r5KPDB1Ez6AeBjKf1a4GxJPy/vHI9sGumvArdIWpWuwV6yLyP9+Uey5tDbSNd28jHgzNR8u39u/0+QBbhfkP1v/DylPw98nazf70bg3ty+rgS+lpqmasiCyoWSHiT7/3kzexD/ctzMzApxjcPMzApx4DAzs0IcOMzMrBAHDjMzK8SBw8zMCnHgMEsk9aZfKZce5/SzTZ/7HO2k487J3fMLSR+RdNrOPIbZzuRx9Wav+mNEzKzCceeQ3e/pDoDI3bjSbCRyjcNsCJJOkPTLdDfWv8ul95m/JN1RdUpaPi3dEfZBSVentHen+yD9XNKPlc2nMgX4CHBWquW8Jb9fSTMl3ZX29T1JB6T0TkkXSrpH0n9JesuwvSG2x3PgMHvVhLKmqvel+xd9nex2LG8B/mSonaTbT7QCb42Io3n119JdwHERcQzZL6c/FRFrgK+R3el4ZkT8rGx3VwGfjoj/TvaL5s/l1tVGxLHAx8vSzXYpN1WZvWqbpipJM4FHI+JX6fW3yW4ZP5i3AjdExHrYeg8nyO6gel2au2Ec8OhgO0n3UXptRPwkJS0huyNxyb+l5/vIJtIyGxaucZgNrZI7CMOrN8nTAHkuAS6NiDcAf0//d14tYnN67sVfAm0YOXCYDe6XwNTcjfgW5NatIbv9N5LeCExN6cuA90o6MK2bmNL3B36blhfm9tPvnWIj4gXguVz/xQeAn5RvZzbcHDjMXlXex3FBRLxE1jT1w9Q5/lhu++8CE9MdU88A/gsgIh4G2oCfpLunfjltfz5wvaSfAetz+/k+2e3tH+ink3sh2RSrvwBmAv93552u2fbx3XHNzKwQ1zjMzKwQBw4zMyvEgcPMzApx4DAzs0IcOMzMrBAHDjMzK8SBw8zMCnHgMDOzQv5/0Sj5TJd/zcsAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset.boxplot(column='ApplicantIncome', by='Education')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c4b3431b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset.boxplot(column='LoanAmount')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "06cc1e4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['LoanAmount'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4a96b33c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAARiElEQVR4nO3dbYxcZ3nG8f/VmJcQQ14UWFl2VKeVlRZwW2CVQiOhMeElbRDOhyIZAXJoKqtSoGnlijrwAfVD1EhVaPlQKllAsQTFTQMoFmkBy2WKkJpQO9A6iUkTgRuchLgtBNg0Cl1698OeoMUe492Z2Z3Zx/+fZM2c55w559atnWuPnzlzNlWFJKktPzfpAiRJ42e4S1KDDHdJapDhLkkNMtwlqUHrJl0AwKWXXlqbN2/mqaee4oILLph0OVPHvgxmX05nTwZrtS9Hjhz5r6p68aB1UxHumzdv5vDhw/T7fXq93qTLmTr2ZTD7cjp7MlirfUnyH2da57SMJDXorOGe5GNJTia5b8C6P0pSSS5dNHZzkoeTPJjkTeMuWJJ0dks5c/84cM2pg0kuA94APLJo7KXADuBl3Ws+nOS8sVQqSVqys4Z7VX0Z+O6AVX8OvBdYfP+C7cD+qnqmqr4FPAxcOY5CJUlLN9QHqkneAjxaVf+aZPGqjcDdi5ZPdGOD9rEL2AUwMzNDv99nbm6Ofr8/TElNsy+D2ZfT2ZPBzsW+LDvck7wAeD/wxkGrB4wNvDNZVe0F9gLMzs5Wr9dr9hPtUdmXwezL6ezJYOdiX4Y5c/9F4HLg2bP2TcC9Sa5k4Uz9skXbbgIeG7VISdLyLPtSyKo6WlUvqarNVbWZhUB/ZVV9BzgA7EjyvCSXA1uAr461YknSWS3lUshPAf8MXJHkRJIbzrRtVd0P3A48AHweuLGqfjyuYiVJS3PWaZmqettZ1m8+ZfkW4JbRypLasHnPXUO/9vit146xEp1r/IaqJDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUoKH+WIeklTfMfWl2b53n+j13eV8aeeYuSS0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNOmu4J/lYkpNJ7ls09mdJvpHk35J8NslFi9bdnOThJA8medMK1S1J+hmWcub+ceCaU8YOAi+vql8B/h24GSDJS4EdwMu613w4yXljq1aStCRnDfeq+jLw3VPGvlhV893i3cCm7vl2YH9VPVNV3wIeBq4cY72SpCUYx43Dfgf42+75RhbC/lknurHTJNkF7AKYmZmh3+8zNzdHv98fQ0ltsS+DrYW+7N46f/aNxmjm/IVjTntfVtta+FkZt5HCPcn7gXngk88ODdisBr22qvYCewFmZ2er1+vR7/fp9XqjlNQk+zLYWujL9UPc2XEUu7fOc9vRdRx/e29Vjzvt1sLPyrgNHe5JdgJvBq6uqmcD/ARw2aLNNgGPDV+eJGkYQ10KmeQa4I+Bt1TV/yxadQDYkeR5SS4HtgBfHb1MSdJynPXMPcmngB5waZITwAdYuDrmecDBJAB3V9XvVdX9SW4HHmBhuubGqvrxShUvSRrsrOFeVW8bMPzRn7H9LcAtoxQlSRqN31CVpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJatBZwz3Jx5KcTHLforFLkhxM8lD3ePGidTcneTjJg0netFKFS5LObCln7h8HrjllbA9wqKq2AIe6ZZK8FNgBvKx7zYeTnDe2aiVJS3LWcK+qLwPfPWV4O7Cve74PuG7R+P6qeqaqvgU8DFw5nlIlSUs17Jz7TFU9DtA9vqQb3wh8e9F2J7oxSdIqWjfm/WXAWA3cMNkF7AKYmZmh3+8zNzdHv98fc0lrn30ZbC30ZffW+VU93sz5C8ec9r6strXwszJuw4b7E0k2VNXjSTYAJ7vxE8Bli7bbBDw2aAdVtRfYCzA7O1u9Xo9+v0+v1xuypHbZl8HWQl+u33PXqh5v99Z5bju6Do4+NdJ+jt967Zgqmg5r4Wdl3IadljkA7Oye7wTuXDS+I8nzklwObAG+OlqJkqTlOuuZe5JPAT3g0iQngA8AtwK3J7kBeAR4K0BV3Z/kduABYB64sap+vEK1S5LO4KzhXlVvO8Oqq8+w/S3ALaMUJUkajd9QlaQGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDRop3JP8YZL7k9yX5FNJnp/kkiQHkzzUPV48rmIlSUszdLgn2Qj8PjBbVS8HzgN2AHuAQ1W1BTjULUuSVtGo0zLrgPOTrANeADwGbAf2dev3AdeNeAxJ0jKlqoZ/cXITcAvwNPDFqnp7kier6qJF23yvqk6bmkmyC9gFMDMz86r9+/czNzfH+vXrh66nVfZlsLXQl6OPfn9VjzdzPjzx9Oj72brxwtF3MkXWws/KMLZt23akqmYHrVs37E67ufTtwOXAk8DfJXnHUl9fVXuBvQCzs7PV6/Xo9/v0er1hS2qWfRlsLfTl+j13rerxdm+d57ajQ7+tf+L423ujFzNF1sLPyriNMi3zeuBbVfWfVfW/wGeA3wCeSLIBoHs8OXqZkqTlGCXcHwFeneQFSQJcDRwDDgA7u212AneOVqIkabmG/v9bVd2T5A7gXmAe+BoL0yzrgduT3MDCL4C3jqNQSdLSjTQ5V1UfAD5wyvAzLJzFS5ImxG+oSlKDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQSP9gWzpXLB5z12TLkFatpHO3JNclOSOJN9IcizJa5JckuRgkoe6x4vHVawkaWlGnZb5EPD5qvol4FeBY8Ae4FBVbQEOdcuSpFU0dLgneRHwWuCjAFX1o6p6EtgO7Os22wdcN1qJkqTlSlUN98Lk14C9wAMsnLUfAW4CHq2qixZt972qOm1qJskuYBfAzMzMq/bv38/c3Bzr168fqp6W2ZfBVqsvRx/9/oofY1xmzocnnh59P1s3Xjj6TqZIq++hbdu2Hamq2UHrRgn3WeBu4KqquifJh4AfAO9ZSrgvNjs7W4cPH6bf79Pr9Yaqp2X2ZbDV6sta+kB199Z5bjs6+nUSx2+9dgzVTI9W30NJzhjuo8y5nwBOVNU93fIdwCuBJ5Js6A68ATg5wjEkSUMYOtyr6jvAt5Nc0Q1dzcIUzQFgZze2E7hzpAolScs26v/f3gN8MslzgW8C72LhF8btSW4AHgHeOuIxJEnLNFK4V9XXgUHzPVePsl9J0mi8/YAkNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSg0YO9yTnJflaks91y5ckOZjkoe7x4tHLlCQtxzjO3G8Cji1a3gMcqqotwKFuWZK0ikYK9ySbgGuBjywa3g7s657vA64b5RiSpOVLVQ3/4uQO4E+BFwJ/VFVvTvJkVV20aJvvVdVpUzNJdgG7AGZmZl61f/9+5ubmWL9+/dD1tMq+DLZafTn66PdX/BjjMnM+PPH06PvZuvHC0XcyRVp9D23btu1IVc0OWrdu2J0meTNwsqqOJOkt9/VVtRfYCzA7O1u9Xo9+v0+vt+xdNc++DLZafbl+z10rfoxx2b11ntuODv22/onjb++NXswUORffQ6P8FFwFvCXJbwHPB16U5BPAE0k2VNXjSTYAJ8dRqCRp6Yaec6+qm6tqU1VtBnYA/1hV7wAOADu7zXYCd45cpSRpWVbiOvdbgTckeQh4Q7csSVpFo0/OAVXVB/rd8/8Grh7HfiVJw/EbqpLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBY7kUUpp2m9fQLQSmwSj9On7rtWOsRMPyzF2SGmS4S1KDDHdJapDhLkkN8gNVSWPlh7HTwTN3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lq0NDhnuSyJF9KcizJ/Ulu6sYvSXIwyUPd48XjK1eStBSjnLnPA7ur6peBVwM3JnkpsAc4VFVbgEPdsiRpFQ0d7lX1eFXd2z3/IXAM2AhsB/Z1m+0DrhuxRknSMo1lzj3JZuAVwD3ATFU9Dgu/AICXjOMYkqSlS1WNtoNkPfBPwC1V9ZkkT1bVRYvWf6+qTpt3T7IL2AUwMzPzqv379zM3N8f69etHqqdF9mWw5fTl6KPfX+FqpsPM+fDE05OuYnhbN164Ivtt9T20bdu2I1U1O2jdSOGe5DnA54AvVNUHu7EHgV5VPZ5kA9Cvqit+1n5mZ2fr8OHD9Pt9er3e0PW0yr4Mtpy+nCt/Q3X31nluO7p27+S9Urf8bfU9lOSM4T7K1TIBPgocezbYOweAnd3zncCdwx5DkjScUX7FXwW8Ezia5Ovd2PuAW4Hbk9wAPAK8daQKJUnLNnS4V9VXgJxh9dXD7lcaZNC0yu6t81x/jky3SMvlN1QlqUGGuyQ1yHCXpAYZ7pLUIMNdkhq0dr/tIKk5o3zZbKW+ALVWeeYuSQ3yzF2r5ly5BYA0DTxzl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ3yUkhJ57xRL9Odxi9QeeYuSQ3yzF1SE37W2fe5+IddDHdJGtE03hPHaRlJapBn7loW7w8jrQ2G+xrU4if7ksbLaRlJatCKnbknuQb4EHAe8JGqunWljqXlcWpFat+KhHuS84C/BN4AnAD+JcmBqnpgJY43qU+qp/ETckmClZuWuRJ4uKq+WVU/AvYD21foWJKkU6Sqxr/T5LeBa6rqd7vldwK/XlXvXrTNLmBXt3gF8CBwKfBfYy9o7bMvg9mX09mTwVrty89X1YsHrVipOfcMGPup3yJVtRfY+1MvSg5X1ewK1bRm2ZfB7Mvp7Mlg52JfVmpa5gRw2aLlTcBjK3QsSdIpVirc/wXYkuTyJM8FdgAHVuhYkqRTrMi0TFXNJ3k38AUWLoX8WFXdv4SX7j37Juck+zKYfTmdPRnsnOvLinygKkmaLL+hKkkNMtwlqUETD/cklyX5UpJjSe5PctOka5oGSZ6f5KtJ/rXry59MuqZpkuS8JF9L8rlJ1zItkhxPcjTJ15McnnQ90yLJRUnuSPKNLmdeM+maVsM03BVyHthdVfcmeSFwJMnBlbpVwRryDPC6qppL8hzgK0n+oarunnRhU+Im4BjwokkXMmW2VVWLX9YZxYeAz1fVb3dX771g0gWthomfuVfV41V1b/f8hyy8YTdOtqrJqwVz3eJzun9++g0k2QRcC3xk0rVouiV5EfBa4KMAVfWjqnpyokWtkomH+2JJNgOvAO6ZcClToZt6+DpwEjhYVfZlwV8A7wX+b8J1TJsCvpjkSHd7D8EvAP8J/HU3jfeRJBdMuqjVMDXhnmQ98GngD6rqB5OuZxpU1Y+r6tdY+IbvlUlePuGSJi7Jm4GTVXVk0rVMoauq6pXAbwI3JnntpAuaAuuAVwJ/VVWvAJ4C9ky2pNUxFeHezSl/GvhkVX1m0vVMm+6/kX3gmslWMhWuAt6S5DgLdxt9XZJPTLak6VBVj3WPJ4HPsnB31nPdCeDEov/13sFC2Ddv4uGeJCzMhx2rqg9Oup5pkeTFSS7qnp8PvB74xkSLmgJVdXNVbaqqzSzc1uIfq+odEy5r4pJc0F2QQDft8EbgvslWNXlV9R3g20mu6IauBs6JizWm4WqZq4B3Ake7+WWA91XV30+upKmwAdjX/eGTnwNuryov+9OZzACfXThXYh3wN1X1+cmWNDXeA3yyu1Lmm8C7JlzPqvD2A5LUoIlPy0iSxs9wl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ36f+QDFkmmvmD3AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['LoanAmount_log']=np.log(dataset['LoanAmount'])\n",
    "dataset['LoanAmount_log'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f2d52b9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender               13\n",
       "Married               3\n",
       "Dependents           15\n",
       "Education             0\n",
       "Self_Employed        32\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount           22\n",
       "Loan_Amount_Term     14\n",
       "Credit_History       50\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "LoanAmount_log       22\n",
       "dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e2cbe216",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b220d35c",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Married'].fillna(dataset['Married'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ab6d0d1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Dependents'].fillna(dataset['Dependents'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ed0c93e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4cd67807",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset.LoanAmount = dataset.LoanAmount.fillna(dataset.LoanAmount.mean())\n",
    "dataset.LoanAmount_log = dataset.LoanAmount_log.fillna(dataset.LoanAmount_log.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ff892ca1",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d000aabe",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bd3037a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID              0\n",
       "Gender               0\n",
       "Married              0\n",
       "Dependents           0\n",
       "Education            0\n",
       "Self_Employed        0\n",
       "ApplicantIncome      0\n",
       "CoapplicantIncome    0\n",
       "LoanAmount           0\n",
       "Loan_Amount_Term     0\n",
       "Credit_History       0\n",
       "Property_Area        0\n",
       "Loan_Status          0\n",
       "LoanAmount_log       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "19c50ef4",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['TotalIncome']= dataset['ApplicantIncome'] + dataset['CoapplicantIncome']\n",
    "dataset['TotalIncome_log']= np.log(dataset['TotalIncome'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "78d17602",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAD4CAYAAADhNOGaAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAARMUlEQVR4nO3da4xcZ33H8e+/MRcnC7GNy9Y4aZ1KVgpkRRWvaCBStCvTlmKEQ9VIQYHaVSoLCWiK3BdLKxX1RVRTNZXo7YXVoLoFZWXStLEIN9fNQvsiKXaAbhxDHYhr7BibS2K6NAK2/ffFnJTpeDc7O2cuJ3m+H2k1M2eeM+eXZyb+7TkzczYyE0lSuX5i1AEkSaNlEUhS4SwCSSqcRSBJhbMIJKlwa0YdAGDjxo25ZcuWkWb4/ve/zxVXXDHSDJ2amAnMtVrm6l4TM0Fzcx07duzbmfmTtR8oM0f+s23bthy1Bx98cNQRLtHETJnmWi1zda+JmTKbmws4mn34N9hDQ5JUOItAkgpnEUhS4SwCSSqcRSBJhbMIJKlwFoEkFc4ikKTCWQSSVLhGnGJCzx9bZh5g78Qiu2ceWPW6p/btGEAiSXW5RyBJhbMIJKlwFoEkFc4ikKTCWQSSVDiLQJIKZxFIUuEsAkkqnEUgSYWzCCSpcJ5iokBbejg9hKQXLvcIJKlwFoEkFc4ikKTCWQSSVDiLQJIKZxFIUuEsAkkq3IpFEBEfiYgLEfFo27INEXE4Ik5Wl+vb7vtARDweEV+NiF8eVHBJUn90s0fw18CbO5bNAEcycytwpLpNRLwGuBV4bbXOX0bEZX1LK0nquxWLIDM/D3y3Y/FO4EB1/QBwc9vy2cz8QWY+ATwOvL4/USVJgxCZufKgiC3AJzLzuur205m5ru3+pzJzfUT8OfBQZn60Wn438KnMvHeJx9wD7AEYHx/fNjs724f/nN4tLCwwNjY20gydBpVp/uzFWuuPr4Xzz6x+vYnNV9ba7kqa+ByCuVajiZmgubmmp6ePZeZk3cfp97mGYollSzZNZu4H9gNMTk7m1NRUn6OsztzcHKPO0GlQmXbXPNfQ3olF7ppf/Uvn1G1Ttba7kiY+h2Cu1WhiJmhurn7p9VND5yNiE0B1eaFafga4um3cVcCTvceTJA1ar0VwCNhVXd8F3N+2/NaIeElEXANsBf61XkRJ0iCtuH8fEfcAU8DGiDgDfBDYBxyMiNuB08AtAJl5PCIOAo8Bi8B7MvO/B5RdktQHKxZBZr5jmbu2LzP+TuDOOqEkScPjN4slqXAWgSQVziKQpMJZBJJUOItAkgpnEUhS4SwCSSpcv881JC1rS41zHJ3at6OPSSS1c49AkgpnEUhS4SwCSSqcRSBJhbMIJKlwFoEkFc4ikKTCWQSSVDiLQJIKZxFIUuEsAkkqnEUgSYWzCCSpcBaBJBXOIpCkwlkEklQ4i0CSCmcRSFLhLAJJKpxFIEmFq1UEEfH+iDgeEY9GxD0R8dKI2BARhyPiZHW5vl9hJUn913MRRMRm4LeAycy8DrgMuBWYAY5k5lbgSHVbktRQdQ8NrQHWRsQa4HLgSWAncKC6/wBwc81tSJIGKDKz95Uj7gDuBJ4BPpuZt0XE05m5rm3MU5l5yeGhiNgD7AEYHx/fNjs723OOflhYWGBsbGykGTotl2n+7MURpPmx8bVw/pnhbnNi85UrjmnicwjmWo0mZoLm5pqenj6WmZN1H2dNrytWx/53AtcATwMfj4h3drt+Zu4H9gNMTk7m1NRUr1H6Ym5ujlFn6LRcpt0zDww/TJu9E4vcNd/zS6cnp26bWnFME59DMNdqNDETNDdXv9Q5NPQm4InM/FZm/gi4D3gjcD4iNgFUlxfqx5QkDUqdIjgN3BARl0dEANuBE8AhYFc1Zhdwf72IkqRB6nn/PjMfjoh7gUeAReCLtA71jAEHI+J2WmVxSz+CSpIGo9aB3sz8IPDBjsU/oLV3IEl6HvCbxZJUOItAkgpnEUhS4SwCSSqcRSBJhbMIJKlwFoEkFc4ikKTCWQSSVDiLQJIKZxFIUuEsAkkqnEUgSYWzCCSpcBaBJBXOIpCkwlkEklQ4i0CSCmcRSFLhLAJJKpxFIEmFswgkqXAWgSQVziKQpMJZBJJUOItAkgpnEUhS4SwCSSpcrSKIiHURcW9EfCUiTkTEGyJiQ0QcjoiT1eX6foWVJPVf3T2CDwOfzsyfA14HnABmgCOZuRU4Ut2WJDVUz0UQES8HbgLuBsjMH2bm08BO4EA17ABwc72IkqRBiszsbcWInwf2A4/R2hs4BtwBnM3MdW3jnsrMSw4PRcQeYA/A+Pj4ttnZ2Z5y9MvCwgJjY2MjzdBpuUzzZy+OIM2Pja+F888Md5sTm69ccUwTn0Mw12o0MRM0N9f09PSxzJys+zh1imASeAi4MTMfjogPA98D3tdNEbSbnJzMo0eP9pSjX+bm5piamhpphk7LZdoy88Dww7TZO7HIXfNrhrrNU/t2rDimic8hmGs1mpgJmpsrIvpSBHXeIzgDnMnMh6vb9wLXA+cjYhNAdXmhXkRJ0iD1XASZ+U3gGxFxbbVoO63DRIeAXdWyXcD9tRJKkgaq7v79+4CPRcSLga8Dv0GrXA5GxO3AaeCWmtuQJA1QrSLIzC8BSx2f2l7ncSVJw+M3iyWpcBaBJBXOIpCkwlkEklQ4i0CSCmcRSFLhLAJJKtxwTxgj9aib8yvtnVhk9zLjujlXkVQq9wgkqXAWgSQVziKQpMJZBJJUOItAkgpnEUhS4SwCSSqcRSBJhbMIJKlwFoEkFc4ikKTCWQSSVDiLQJIKZxFIUuEsAkkqnEUgSYWzCCSpcBaBJBXOIpCkwlkEklS42kUQEZdFxBcj4hPV7Q0RcTgiTlaX6+vHlCQNSj/2CO4ATrTdngGOZOZW4Eh1W5LUULWKICKuAnYAf9W2eCdwoLp+ALi5zjYkSYMVmdn7yhH3An8IvAz4ncx8a0Q8nZnr2sY8lZmXHB6KiD3AHoDx8fFts7OzPefoh4WFBcbGxkaaodNymebPXhxBmh8bXwvnnxlphCU9V66JzVcON0ybJr62oJm5mpgJmptrenr6WGZO1n2cNb2uGBFvBS5k5rGImFrt+pm5H9gPMDk5mVNTq36Ivpqbm2PUGTotl2n3zAPDD9Nm78Qid833/NIZmOfKdeq2qeGGadPE1xY0M1cTM0Fzc/VLnf+bbwTeFhFvAV4KvDwiPgqcj4hNmXkuIjYBF/oRVJI0GD2/R5CZH8jMqzJzC3Ar8E+Z+U7gELCrGrYLuL92SknSwAxi/34fcDAibgdOA7cMYBvSqmypcTjt1L4dfUwiNU9fiiAz54C56vp3gO39eFxJ0uD5zWJJKpxFIEmFswgkqXAWgSQVziKQpMI17+uhhejm44x7JxZH/i1iSS987hFIUuEsAkkqnEUgSYWzCCSpcBaBJBXOIpCkwlkEklQ4i0CSCmcRSFLhLAJJKpxFIEmFswgkqXAWgSQVziKQpMJZBJJUOItAkgpnEUhS4fwLZdIKuvlrcss5tW9HH5NIg+EegSQVziKQpMJZBJJUOItAkgrXcxFExNUR8WBEnIiI4xFxR7V8Q0QcjoiT1eX6/sWVJPVbnT2CRWBvZr4auAF4T0S8BpgBjmTmVuBIdVuS1FA9F0FmnsvMR6rr/wmcADYDO4ED1bADwM01M0qSBigys/6DRGwBPg9cB5zOzHVt9z2VmZccHoqIPcAegPHx8W2zs7O1c9SxsLDA2NjY0LY3f/biimPG18L5Z4YQZpXM1b2JzVcO/bXVrSbmamImaG6u6enpY5k5WfdxahdBRIwBnwPuzMz7IuLpboqg3eTkZB49erRWjrrm5uaYmpoa2va6+ZLS3olF7ppv3nf+zNW9U/t2DP211a0m5mpiJmhurojoSxHU+r8mIl4E/B3wscy8r1p8PiI2Zea5iNgEXKgbsqnqfONUkpqizqeGArgbOJGZf9J21yFgV3V9F3B/7/EkSYNWZ4/gRuBdwHxEfKla9rvAPuBgRNwOnAZuqZVQkjRQPRdBZv4LEMvcvb3Xx5VeSLbMPMDeiUV293AY0RPWaVj8ZrEkFc4ikKTCWQSSVDiLQJIKZxFIUuEsAkkqnEUgSYVr1olZJP2fOqcw8TsIWg33CCSpcBaBJBXOIpCkwlkEklQ4i0CSCmcRSFLhLAJJKpxFIEmFswgkqXAWgSQVzlNMSC9A3Zye4rn+hKanqCiLewSSVLji9wie/c2p1z8wLknPd+4RSFLhLAJJKlzxh4YkNcf82Ys9H6L1De7euUcgSYWzCCSpcBaBJBXO9wgkXaLO30uuY+/ESDZbvIHtEUTEmyPiqxHxeETMDGo7kqR6BrJHEBGXAX8B/CJwBvhCRBzKzMcGsb1R/fYiqTkG+e/AIL9w2oRPOw1qj+D1wOOZ+fXM/CEwC+wc0LYkSTVEZvb/QSN+DXhzZv5mdftdwC9k5nvbxuwB9lQ3rwW+2vcgq7MR+PaIM3RqYiYw12qZq3tNzATNzXVtZr6s7oMM6s3iWGLZ/2uczNwP7B/Q9lctIo5m5uSoc7RrYiYw12qZq3tNzATNztWPxxnUoaEzwNVtt68CnhzQtiRJNQyqCL4AbI2IayLixcCtwKEBbUuSVMNADg1l5mJEvBf4DHAZ8JHMPD6IbfVRYw5TtWliJjDXapmre03MBC/wXAN5s1iS9PzhKSYkqXAWgSQVrpgiiIhrI+JLbT/fi4jf7hgzFREX28b8/pCyvT8ijkfEoxFxT0S8tOP+iIg/rU7X8W8RcX1Dco1qvu6oMh3vfA6r+4c+X11kGspcRcRHIuJCRDzatmxDRByOiJPV5fpl1h3YaWFq5joVEfPVvPXl45Ir5Lqleh7/JyKW/cjoCOar21yrn6/MLO6H1hvY3wR+pmP5FPCJIWfZDDwBrK1uHwR2d4x5C/ApWt/PuAF4uCG5RjFf1wGPApfT+rDDPwJbRzlfXWYaylwBNwHXA4+2LfsjYKa6PgN8aIn1LgO+Bvws8GLgy8BrRp2ruu8UsHGI8/VqWl9ynQMml1lvFPO1Yq5e56uYPYIO24GvZeZ/jDpIZQ2wNiLW0PrHpPM7FzuBv8mWh4B1EbGpAblG4dXAQ5n5X5m5CHwOeHvHmGHPVzeZhiIzPw98t2PxTuBAdf0AcPMSqw70tDA1cg3UUrky80RmrnSmg6HPV5e5elJqEdwK3LPMfW+IiC9HxKci4rWDDpKZZ4E/Bk4D54CLmfnZjmGbgW+03T5TLRt1LhjyfNH6zfumiHhFRFxO67f/qzvGDHu+uskEw5+rZ41n5jmA6vKVS4wZ+musy1zQOivBZyPiWLROTdMEo5ivbq16voorgmh9we1twMeXuPsRWoeLXgf8GfAPQ8izntZvEtcArwKuiIh3dg5bYtWBfu63y1xDn6/MPAF8CDgMfJrWLvlix7ChzleXmYY+V6s09NfYKtyYmdcDvwK8JyJuGnUgXmDzVVwR0JqcRzLzfOcdmfm9zFyorn8SeFFEbBxwnjcBT2TmtzLzR8B9wBs7xozilB0r5hrRfJGZd2fm9Zl5E63d55MdQ4Y+XytlGtVcVc4/e2isurywxJhRvMa6yUVmPlldXgD+ntZhmVFr7Gl0epmvEovgHSxzWCgifioiorr+elrz850B5zkN3BARl1fb3g6c6BhzCPj16tMwN9A6THNu1LlGNF9ExCury58GfpVLn8+hz9dKmUY1V5VDwK7q+i7g/iXGjOK0MCvmiogrIuJlz14HfonWobhRa+RpdHqer369y/18+KH1hud3gCvblr0beHd1/b3AcVq79g8BbxxSrj8AvlI9YX8LvKQjV9D6Qz9fA+Z5jk8MDDnXqObrn4HHqu1uX+J5HPp8dZFpKHNFq4DOAT+i9Vvr7cArgCO09lKOABuqsa8CPtm27luAf6/m7feakIvWp3K+XP0cH1Kut1fXfwCcBz7TkPlaMVev8+UpJiSpcCUeGpIktbEIJKlwFoEkFc4ikKTCWQSSVDiLQJIKZxFIUuH+F9cjG/feLRFwAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataset['TotalIncome_log'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "72d67922",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>Loan_Status</th>\n",
       "      <th>LoanAmount_log</th>\n",
       "      <th>TotalIncome</th>\n",
       "      <th>TotalIncome_log</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001002</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5849</td>\n",
       "      <td>0.0</td>\n",
       "      <td>146.412162</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.857444</td>\n",
       "      <td>5849.0</td>\n",
       "      <td>8.674026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001003</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4583</td>\n",
       "      <td>1508.0</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Rural</td>\n",
       "      <td>N</td>\n",
       "      <td>4.852030</td>\n",
       "      <td>6091.0</td>\n",
       "      <td>8.714568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001005</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>66.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.189655</td>\n",
       "      <td>3000.0</td>\n",
       "      <td>8.006368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001006</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2583</td>\n",
       "      <td>2358.0</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.787492</td>\n",
       "      <td>4941.0</td>\n",
       "      <td>8.505323</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001008</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>Y</td>\n",
       "      <td>4.948760</td>\n",
       "      <td>6000.0</td>\n",
       "      <td>8.699515</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001002   Male      No          0      Graduate            No   \n",
       "1  LP001003   Male     Yes          1      Graduate            No   \n",
       "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
       "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
       "4  LP001008   Male      No          0      Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5849                0.0  146.412162             360.0   \n",
       "1             4583             1508.0  128.000000             360.0   \n",
       "2             3000                0.0   66.000000             360.0   \n",
       "3             2583             2358.0  120.000000             360.0   \n",
       "4             6000                0.0  141.000000             360.0   \n",
       "\n",
       "   Credit_History Property_Area Loan_Status  LoanAmount_log  TotalIncome  \\\n",
       "0             1.0         Urban           Y        4.857444       5849.0   \n",
       "1             1.0         Rural           N        4.852030       6091.0   \n",
       "2             1.0         Urban           Y        4.189655       3000.0   \n",
       "3             1.0         Urban           Y        4.787492       4941.0   \n",
       "4             1.0         Urban           Y        4.948760       6000.0   \n",
       "\n",
       "   TotalIncome_log  \n",
       "0         8.674026  \n",
       "1         8.714568  \n",
       "2         8.006368  \n",
       "3         8.505323  \n",
       "4         8.699515  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "affcff1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "X= dataset.iloc[:,np.r_[1:5,9:11,13:15]].values\n",
    "y= dataset.iloc[:,12].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "04a87178",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['Male', 'No', '0', ..., 1.0, 4.857444178729353, 5849.0],\n",
       "       ['Male', 'Yes', '1', ..., 1.0, 4.852030263919617, 6091.0],\n",
       "       ['Male', 'Yes', '0', ..., 1.0, 4.189654742026425, 3000.0],\n",
       "       ...,\n",
       "       ['Male', 'Yes', '1', ..., 1.0, 5.53338948872752, 8312.0],\n",
       "       ['Male', 'Yes', '2', ..., 1.0, 5.231108616854587, 7583.0],\n",
       "       ['Female', 'No', '0', ..., 0.0, 4.890349128221754, 4583.0]],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b51cea76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'Y',\n",
       "       'Y', 'Y', 'N', 'Y', 'N', 'N', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'Y',\n",
       "       'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y',\n",
       "       'N', 'N', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N',\n",
       "       'N', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'N',\n",
       "       'N', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'N', 'N', 'N', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'N', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'N', 'Y', 'N',\n",
       "       'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'N',\n",
       "       'Y', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y',\n",
       "       'N', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'N',\n",
       "       'Y', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'Y',\n",
       "       'Y', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'N', 'N',\n",
       "       'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'Y',\n",
       "       'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N',\n",
       "       'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y',\n",
       "       'Y', 'N', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y',\n",
       "       'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N', 'N', 'Y',\n",
       "       'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'Y', 'N', 'Y', 'N', 'Y',\n",
       "       'N', 'N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'N', 'Y', 'Y',\n",
       "       'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'Y', 'N', 'Y', 'Y',\n",
       "       'Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y',\n",
       "       'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'N', 'N',\n",
       "       'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N',\n",
       "       'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y',\n",
       "       'N', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'N', 'N', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N', 'N', 'Y', 'N',\n",
       "       'Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'N',\n",
       "       'N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N',\n",
       "       'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y',\n",
       "       'Y', 'Y', 'N'], dtype=object)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "337668e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "fb07d50f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Male' 'Yes' '0' ... 1.0 4.875197323201151 5858.0]\n",
      " ['Male' 'No' '1' ... 1.0 5.278114659230517 11250.0]\n",
      " ['Male' 'Yes' '0' ... 0.0 5.003946305945459 5681.0]\n",
      " ...\n",
      " ['Male' 'Yes' '3+' ... 1.0 5.298317366548036 8334.0]\n",
      " ['Male' 'Yes' '0' ... 1.0 5.075173815233827 6033.0]\n",
      " ['Female' 'Yes' '0' ... 1.0 5.204006687076795 6486.0]]\n"
     ]
    }
   ],
   "source": [
    "print(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "18b893b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "labelencoder_X = LabelEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "1265655d",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0, 5):\n",
    "    X_train[:,i]= labelencoder_X.fit_transform(X_train[:,i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "09e7837d",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train[:,7]= labelencoder_X.fit_transform(X_train[:,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b2722d21",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 1, 0, ..., 1.0, 4.875197323201151, 267],\n",
       "       [1, 0, 1, ..., 1.0, 5.278114659230517, 407],\n",
       "       [1, 1, 0, ..., 0.0, 5.003946305945459, 249],\n",
       "       ...,\n",
       "       [1, 1, 3, ..., 1.0, 5.298317366548036, 363],\n",
       "       [1, 1, 0, ..., 1.0, 5.075173815233827, 273],\n",
       "       [0, 1, 0, ..., 1.0, 5.204006687076795, 301]], dtype=object)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "505d13fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "labelencoder_y=LabelEncoder()\n",
    "y_train= labelencoder_y.fit_transform(y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "97975a4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,\n",
       "       0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,\n",
       "       1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0,\n",
       "       1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0,\n",
       "       1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,\n",
       "       0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1,\n",
       "       0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1,\n",
       "       0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1,\n",
       "       1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0,\n",
       "       1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,\n",
       "       1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1,\n",
       "       1, 1, 1, 0, 1, 0, 1])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d5523fdf",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0, 5):\n",
    "    X_test[:,i]= labelencoder_X.fit_transform(X_test[:,i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "86aee9c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test[:,7]= labelencoder_X.fit_transform(X_test[:,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "822dbba9",
   "metadata": {},
   "outputs": [],
   "source": [
    "labelencoder_y=LabelEncoder()\n",
    "y_test= labelencoder_y.fit_transform(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "569a55d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 0, 0, 5, 1.0, 4.430816798843313, 85],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.718498871295094, 28],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.780743515792329, 104],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.700480365792417, 80],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.574710978503383, 22],\n",
       "       [1, 1, 0, 1, 3, 0.0, 5.10594547390058, 70],\n",
       "       [1, 1, 3, 0, 3, 1.0, 5.056245805348308, 77],\n",
       "       [1, 0, 0, 0, 5, 1.0, 6.003887067106539, 114],\n",
       "       [1, 0, 0, 0, 5, 0.0, 4.820281565605037, 53],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.852030263919617, 55],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.430816798843313, 4],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.553876891600541, 2],\n",
       "       [0, 0, 0, 0, 5, 1.0, 5.634789603169249, 96],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.4638318050256105, 97],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.564348191467836, 117],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.204692619390966, 22],\n",
       "       [1, 0, 1, 1, 5, 1.0, 5.247024072160486, 32],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.882801922586371, 25],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.532599493153256, 1],\n",
       "       [1, 1, 0, 1, 5, 0.0, 5.198497031265826, 44],\n",
       "       [0, 1, 0, 0, 5, 0.0, 4.787491742782046, 71],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.962844630259907, 43],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.68213122712422, 91],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.10594547390058, 111],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.060443010546419, 35],\n",
       "       [1, 1, 1, 0, 5, 1.0, 5.521460917862246, 94],\n",
       "       [1, 0, 0, 0, 5, 1.0, 5.231108616854587, 98],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.231108616854587, 110],\n",
       "       [1, 1, 3, 0, 5, 0.0, 4.852030263919617, 41],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.634728988229636, 50],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.429345628954441, 99],\n",
       "       [1, 0, 0, 1, 5, 1.0, 3.871201010907891, 46],\n",
       "       [1, 1, 1, 1, 5, 1.0, 4.499809670330265, 52],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.19295685089021, 102],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.857444178729353, 95],\n",
       "       [0, 1, 0, 1, 5, 0.0, 5.181783550292085, 57],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.147494476813453, 65],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.836281906951478, 39],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.852030263919617, 75],\n",
       "       [1, 1, 2, 1, 5, 1.0, 4.68213122712422, 24],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.382026634673881, 9],\n",
       "       [1, 1, 3, 0, 5, 0.0, 4.812184355372417, 68],\n",
       "       [1, 1, 2, 0, 2, 1.0, 2.833213344056216, 0],\n",
       "       [1, 1, 1, 1, 5, 1.0, 5.062595033026967, 67],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.330733340286331, 21],\n",
       "       [1, 0, 0, 0, 5, 1.0, 5.231108616854587, 113],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.7535901911063645, 18],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.74493212836325, 37],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.852030263919617, 72],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.941642422609304, 78],\n",
       "       [1, 1, 3, 1, 5, 1.0, 4.30406509320417, 8],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.867534450455582, 84],\n",
       "       [1, 1, 0, 1, 5, 1.0, 4.672828834461906, 31],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.857444178729353, 61],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.718498871295094, 19],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.556828061699537, 107],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.553876891600541, 34],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.890349128221754, 74],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.123963979403259, 62],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.787491742782046, 27],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.919980925828125, 108],\n",
       "       [0, 0, 0, 0, 5, 1.0, 5.365976015021851, 103],\n",
       "       [1, 1, 0, 1, 5, 1.0, 4.74493212836325, 38],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.330733340286331, 13],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.890349128221754, 69],\n",
       "       [1, 1, 1, 0, 5, 1.0, 5.752572638825633, 112],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.075173815233827, 73],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.912654885736052, 47],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.204006687076795, 81],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.564348191467836, 60],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.204692619390966, 83],\n",
       "       [0, 1, 0, 0, 5, 1.0, 4.867534450455582, 5],\n",
       "       [1, 1, 2, 1, 5, 1.0, 5.056245805348308, 58],\n",
       "       [1, 1, 1, 1, 3, 1.0, 4.919980925828125, 79],\n",
       "       [0, 1, 0, 0, 5, 1.0, 4.969813299576001, 54],\n",
       "       [1, 1, 0, 1, 4, 1.0, 4.820281565605037, 56],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.499809670330265, 120],\n",
       "       [1, 0, 3, 0, 5, 1.0, 5.768320995793772, 118],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.718498871295094, 101],\n",
       "       [0, 0, 0, 0, 5, 0.0, 4.7535901911063645, 26],\n",
       "       [0, 0, 0, 0, 6, 1.0, 4.727387818712341, 33],\n",
       "       [1, 1, 1, 0, 5, 1.0, 6.214608098422191, 119],\n",
       "       [0, 0, 0, 0, 5, 1.0, 5.267858159063328, 89],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.231108616854587, 92],\n",
       "       [1, 0, 0, 0, 6, 1.0, 4.2626798770413155, 6],\n",
       "       [1, 1, 0, 0, 0, 1.0, 4.709530201312334, 90],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.700480365792417, 45],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.298317366548036, 109],\n",
       "       [1, 0, 1, 0, 3, 1.0, 4.727387818712341, 17],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.6443908991413725, 36],\n",
       "       [0, 1, 0, 1, 5, 1.0, 4.605170185988092, 16],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.30406509320417, 7],\n",
       "       [1, 1, 1, 0, 1, 1.0, 5.147494476813453, 88],\n",
       "       [1, 1, 3, 0, 4, 0.0, 5.19295685089021, 87],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.2626798770413155, 3],\n",
       "       [1, 0, 0, 1, 3, 0.0, 4.836281906951478, 59],\n",
       "       [1, 0, 0, 0, 3, 1.0, 5.1647859739235145, 82],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.969813299576001, 66],\n",
       "       [1, 1, 2, 1, 5, 1.0, 4.394449154672439, 51],\n",
       "       [1, 1, 1, 0, 5, 1.0, 5.231108616854587, 100],\n",
       "       [1, 1, 0, 0, 5, 1.0, 5.351858133476067, 93],\n",
       "       [1, 1, 0, 0, 5, 1.0, 4.605170185988092, 15],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.787491742782046, 106],\n",
       "       [1, 0, 0, 0, 3, 1.0, 4.787491742782046, 105],\n",
       "       [1, 1, 3, 0, 5, 1.0, 4.852030263919617, 64],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.8283137373023015, 49],\n",
       "       [1, 0, 0, 1, 5, 1.0, 4.6443908991413725, 42],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.477336814478207, 10],\n",
       "       [1, 1, 0, 1, 5, 1.0, 4.553876891600541, 20],\n",
       "       [1, 1, 3, 1, 3, 1.0, 4.394449154672439, 14],\n",
       "       [1, 0, 0, 0, 5, 1.0, 5.298317366548036, 76],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.90527477843843, 11],\n",
       "       [1, 0, 0, 0, 6, 1.0, 4.727387818712341, 18],\n",
       "       [1, 1, 2, 0, 5, 1.0, 4.248495242049359, 23],\n",
       "       [1, 1, 0, 1, 5, 0.0, 5.303304908059076, 63],\n",
       "       [1, 1, 0, 0, 3, 0.0, 4.499809670330265, 48],\n",
       "       [0, 0, 0, 0, 5, 1.0, 4.430816798843313, 30],\n",
       "       [1, 0, 0, 0, 5, 1.0, 4.897839799950911, 29],\n",
       "       [1, 1, 2, 0, 5, 1.0, 5.170483995038151, 86],\n",
       "       [1, 1, 3, 0, 5, 1.0, 4.867534450455582, 115],\n",
       "       [1, 1, 0, 0, 5, 1.0, 6.077642243349034, 116],\n",
       "       [1, 1, 3, 1, 3, 0.0, 4.248495242049359, 40],\n",
       "       [1, 1, 1, 0, 5, 1.0, 4.564348191467836, 12]], dtype=object)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7498a6b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,\n",
       "       1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "e08f74e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "ss=StandardScaler()\n",
    "X_train=ss.fit_transform(X_train)\n",
    "X_test=ss.fit_transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "ca00b88b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(criterion='entropy', random_state=0)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "DTClassifier= DecisionTreeClassifier(criterion='entropy' , random_state=0)\n",
    "DTClassifier.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "92a2c8a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,\n",
       "       1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred= DTClassifier.predict(X_test)\n",
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "56d7a166",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The accuracy of decision tree is: 0.7073170731707317\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "print('The accuracy of decision tree is:', metrics.accuracy_score(y_pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "cb480938",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB()"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "NBClassifier = GaussianNB()\n",
    "NBClassifier.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e52f8d5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=NBClassifier.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c2873d4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "5a723c64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The accuracy of naive Bayes is:  0.8292682926829268\n"
     ]
    }
   ],
   "source": [
    "print('The accuracy of naive Bayes is: ',metrics.accuracy_score(y_pred,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "0493b243",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata= pd.read_csv(\"test.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "8d219377",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001015</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5720</td>\n",
       "      <td>0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001022</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>3076</td>\n",
       "      <td>1500</td>\n",
       "      <td>126.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001031</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5000</td>\n",
       "      <td>1800</td>\n",
       "      <td>208.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001035</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2340</td>\n",
       "      <td>2546</td>\n",
       "      <td>100.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001051</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>3276</td>\n",
       "      <td>0</td>\n",
       "      <td>78.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001015   Male     Yes          0      Graduate            No   \n",
       "1  LP001022   Male     Yes          1      Graduate            No   \n",
       "2  LP001031   Male     Yes          2      Graduate            No   \n",
       "3  LP001035   Male     Yes          2      Graduate            No   \n",
       "4  LP001051   Male      No          0  Not Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5720                  0       110.0             360.0   \n",
       "1             3076               1500       126.0             360.0   \n",
       "2             5000               1800       208.0             360.0   \n",
       "3             2340               2546       100.0             360.0   \n",
       "4             3276                  0        78.0             360.0   \n",
       "\n",
       "   Credit_History Property_Area  \n",
       "0             1.0         Urban  \n",
       "1             1.0         Urban  \n",
       "2             1.0         Urban  \n",
       "3             NaN         Urban  \n",
       "4             1.0         Urban  "
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "28cfac37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 367 entries, 0 to 366\n",
      "Data columns (total 12 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Loan_ID            367 non-null    object \n",
      " 1   Gender             356 non-null    object \n",
      " 2   Married            367 non-null    object \n",
      " 3   Dependents         357 non-null    object \n",
      " 4   Education          367 non-null    object \n",
      " 5   Self_Employed      344 non-null    object \n",
      " 6   ApplicantIncome    367 non-null    int64  \n",
      " 7   CoapplicantIncome  367 non-null    int64  \n",
      " 8   LoanAmount         362 non-null    float64\n",
      " 9   Loan_Amount_Term   361 non-null    float64\n",
      " 10  Credit_History     338 non-null    float64\n",
      " 11  Property_Area      367 non-null    object \n",
      "dtypes: float64(3), int64(2), object(7)\n",
      "memory usage: 34.5+ KB\n"
     ]
    }
   ],
   "source": [
    "testdata.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "abba0b56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender               11\n",
       "Married               0\n",
       "Dependents           10\n",
       "Education             0\n",
       "Self_Employed        23\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount            5\n",
       "Loan_Amount_Term      6\n",
       "Credit_History       29\n",
       "Property_Area         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "710f6b44",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata['Gender'].fillna(testdata['Gender'].mode()[0],inplace=True)\n",
    "testdata['Dependents'].fillna(testdata['Dependents'].mode()[0],inplace=True)\n",
    "testdata['Self_Employed'].fillna(testdata['Self_Employed'].mode()[0],inplace=True)\n",
    "testdata['Loan_Amount_Term'].fillna(testdata['Loan_Amount_Term'].mode()[0],inplace=True)\n",
    "testdata['Credit_History'].fillna(testdata['Credit_History'].mode()[0],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5b5b2723",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID              0\n",
       "Gender               0\n",
       "Married              0\n",
       "Dependents           0\n",
       "Education            0\n",
       "Self_Employed        0\n",
       "ApplicantIncome      0\n",
       "CoapplicantIncome    0\n",
       "LoanAmount           5\n",
       "Loan_Amount_Term     0\n",
       "Credit_History       0\n",
       "Property_Area        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3bf8f688",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "testdata.boxplot(column='LoanAmount')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "3fd1e9a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "testdata.boxplot(column='ApplicantIncome')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "d010e617",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata.LoanAmount= testdata.LoanAmount.fillna(testdata.LoanAmount.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "77d5dac7",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata['LoanAmount_log']=np.log(testdata['LoanAmount'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "67445f80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID              0\n",
       "Gender               0\n",
       "Married              0\n",
       "Dependents           0\n",
       "Education            0\n",
       "Self_Employed        0\n",
       "ApplicantIncome      0\n",
       "CoapplicantIncome    0\n",
       "LoanAmount           0\n",
       "Loan_Amount_Term     0\n",
       "Credit_History       0\n",
       "Property_Area        0\n",
       "LoanAmount_log       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "6ac2cdc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "testdata['TotalIncome']= testdata['ApplicantIncome']+testdata['CoapplicantIncome']\n",
    "testdata['TotalIncome_log']= np.log(testdata['TotalIncome'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3da6bfae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Loan_ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "      <th>LoanAmount_log</th>\n",
       "      <th>TotalIncome</th>\n",
       "      <th>TotalIncome_log</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LP001015</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5720</td>\n",
       "      <td>0</td>\n",
       "      <td>110.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>4.700480</td>\n",
       "      <td>5720</td>\n",
       "      <td>8.651724</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LP001022</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>3076</td>\n",
       "      <td>1500</td>\n",
       "      <td>126.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>4.836282</td>\n",
       "      <td>4576</td>\n",
       "      <td>8.428581</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LP001031</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>5000</td>\n",
       "      <td>1800</td>\n",
       "      <td>208.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>5.337538</td>\n",
       "      <td>6800</td>\n",
       "      <td>8.824678</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LP001035</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2340</td>\n",
       "      <td>2546</td>\n",
       "      <td>100.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>4.605170</td>\n",
       "      <td>4886</td>\n",
       "      <td>8.494129</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LP001051</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>3276</td>\n",
       "      <td>0</td>\n",
       "      <td>78.0</td>\n",
       "      <td>360.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Urban</td>\n",
       "      <td>4.356709</td>\n",
       "      <td>3276</td>\n",
       "      <td>8.094378</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
       "0  LP001015   Male     Yes          0      Graduate            No   \n",
       "1  LP001022   Male     Yes          1      Graduate            No   \n",
       "2  LP001031   Male     Yes          2      Graduate            No   \n",
       "3  LP001035   Male     Yes          2      Graduate            No   \n",
       "4  LP001051   Male      No          0  Not Graduate            No   \n",
       "\n",
       "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "0             5720                  0       110.0             360.0   \n",
       "1             3076               1500       126.0             360.0   \n",
       "2             5000               1800       208.0             360.0   \n",
       "3             2340               2546       100.0             360.0   \n",
       "4             3276                  0        78.0             360.0   \n",
       "\n",
       "   Credit_History Property_Area  LoanAmount_log  TotalIncome  TotalIncome_log  \n",
       "0             1.0         Urban        4.700480         5720         8.651724  \n",
       "1             1.0         Urban        4.836282         4576         8.428581  \n",
       "2             1.0         Urban        5.337538         6800         8.824678  \n",
       "3             1.0         Urban        4.605170         4886         8.494129  \n",
       "4             1.0         Urban        4.356709         3276         8.094378  "
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testdata.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "11464683",
   "metadata": {},
   "outputs": [],
   "source": [
    "test= testdata.iloc[:,np.r_[1:5,9:11,13:15]].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "b4b8beac",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0,5):\n",
    "    test[:,i]=labelencoder_X.fit_transform(test[:,i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "d1c7f20b",
   "metadata": {},
   "outputs": [],
   "source": [
    "test[:,7]= labelencoder_X.fit_transform(test[:,7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "807a1f83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 1, 0, ..., 1.0, 5720, 207],\n",
       "       [1, 1, 1, ..., 1.0, 4576, 124],\n",
       "       [1, 1, 2, ..., 1.0, 6800, 251],\n",
       "       ...,\n",
       "       [1, 0, 0, ..., 1.0, 5243, 174],\n",
       "       [1, 1, 0, ..., 1.0, 7393, 268],\n",
       "       [1, 0, 0, ..., 1.0, 9200, 311]], dtype=object)"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "fbc046ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "test= ss.fit_transform(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "9937e847",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred= NBClassifier.predict(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "459cbebc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1,\n",
       "       0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,\n",
       "       1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1,\n",
       "       0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,\n",
       "       1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,\n",
       "       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01630775",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52386bb9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1872b57",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
