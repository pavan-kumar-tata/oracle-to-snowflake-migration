
The dataset contains loan-level origination, monthly loan performance data  on fully amortizing fixed-rate Single-Family mortgages that Freddie Mac acquired with origination dates from 1999 to the Origination Cutoff Date which is 2023 (https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset). The data is refreshed quarterly and includes loans that closely resemble those eligible for the Single-Family Credit Risk Transfer (CRT) transactions.

## Dataset Description
 

Loan-Level Origination Data
 Information about the origination of loans.


ORIGINATION DATA FILE
FIELD POSITION	ATTRIBUTE NAME	DATA TYPE & FORMAT	MAX LENGTH
1	Credit Score	Numeric	4
2	First Payment Date	Date	6
3	First Time Homebuyer Flag	Alpha	1
4	Maturity Date	Date	6
5	Metropolitan Statistical Area (MSA) Or Metropolitan Division	Numeric	5
6	Mortgage Insurance Percentage (MI %)	Numeric	3
7	Number of Units	Numeric	2
8	Occupancy Status	Alpha	1
9	Original Combined Loan-to-Value (CLTV)	Numeric	3
10	Original Debt-to-Income (DTI) Ratio	Numeric	3
11	Original UPB	Numeric	12
12	Original Loan-to-Value (LTV)	Numeric	3
13	Original Interest Rate	Numeric - 6,3	6
14	Channel	Alpha	1
15	Prepayment Penalty Mortgage (PPM) Flag	Alpha	1
16	Amortization Type (Formerly Product Type)	Alpha	5
17	Property State	Alpha	2
18	Property Type	Alpha	2
19	Postal Code	Numeric	5
20	Loan Sequence Number	Alpha Numeric - PYYQnXXXXXXX	12
21	Loan Purpose	Alpha	1
22	Original Loan Term	Numeric	3
23	Number of Borrowers	Numeric	2
24	Seller Name	Alpha Numeric	60
25	Servicer Name	Alpha Numeric	60
26	Super Conforming Flag	Alpha	1
27	Pre-HARP Loan Sequence Number	Alpha Numeric - PYYQnXXXXXXX	12
28	Program Indicator	Alpha Numeric	1
29	HARP Indicator	Alpha	1
30	Property Valuation Method	Numeric	1
31	Interest Only (I/O) Indicator	Alpha	1
32	Mortgage Insurance Cancellation Indicator	Alpha	1


CREDIT SCORE: Third-party assessment of borrower's creditworthiness, indicating likelihood of timely repayments. Range: 300-850.
FIRST PAYMENT DATE: Date of first scheduled mortgage payment. Format: YYYYMM.
FIRST TIME HOMEBUYER FLAG: Indicates if borrower is purchasing their first primary residence. Values: Y = Yes, N = No.
MATURITY DATE: Final monthly payment due date as per mortgage note. Format: YYYYMM.
METROPOLITAN STATISTICAL AREA (MSA): Designation of the area's urban status based on population.
MORTGAGE INSURANCE PERCENTAGE (MI %): Percentage of loan covered by mortgage insurance at Freddie Mac's purchase. Range: 1% - 55%.
NUMBER OF UNITS: Indicates property type (one-, two-, three-, or four-unit). Values: 1, 2, 3, 4.
OCCUPANCY STATUS: Type of property occupancy (Primary, Investment, Second Home). Values: P = Primary Residence, I = Investment Property, S = Second Home.
ORIGINAL COMBINED LOAN-TO-VALUE (CLTV): Ratio of loan amount to property value at origination. Range varies.
ORIGINAL DEBT-TO-INCOME (DTI) RATIO: Ratio of borrower's debt payments to income at origination. Range: 0% < DTI <= 65%.
ORIGINAL UPB: Mortgage unpaid principal balance on note date, rounded. Numeric, 12 digits.
ORIGINAL LOAN-TO-VALUE (LTV): Loan amount to property value ratio at origination. Range varies.
ORIGINAL INTEREST RATE: Interest rate at loan origination. Numeric, 6 digits.
CHANNEL: Loan origination type (Retail, Broker, Correspondent). Values: R = Retail, B = Broker, C = Correspondent.
PREPAYMENT PENALTY MORTGAGE (PPM) FLAG: Indicates if mortgage has prepayment penalties. Values: Y = Yes, N = No.
AMORTIZATION TYPE: Mortgage type (Fixed Rate or Adjustable Rate). Values: FRM = Fixed Rate Mortgage, ARM = Adjustable Rate Mortgage.
PROPERTY STATE: State or territory where property is located. Two-letter abbreviation.
PROPERTY TYPE: Type of property secured by mortgage (Condo, PUD, etc.). Values vary.
POSTAL CODE: Postal code of mortgaged property location. Format: ###00.
LOAN SEQUENCE NUMBER: Unique identifier for each loan. Alpha-numeric, 12 characters.
LOAN PURPOSE: Purpose of mortgage (Purchase, Refinance - Cash Out, etc.). Values vary.
ORIGINAL LOAN TERM: Number of scheduled monthly payments based on First Payment Date and Maturity Date. Numeric, 3 digits.
NUMBER OF BORROWERS: Number of borrowers on mortgage note. Values vary.
SELLER NAME: Name of seller delivering mortgage loan to Freddie Mac.
SERVICER NAME: Entity servicing the mortgage to Freddie Mac. Alpha-numeric, 60 characters.
SUPER CONFORMING FLAG: Indicates if mortgage exceeds conforming loan limits. Values: Y = Yes.
PRE-RELIEF REFINANCE LOAN SEQUENCE NUMBER: Identifier linking Relief Refinance loan to original loan. Alpha-numeric, 12 characters.
PROGRAM INDICATOR: Indicates participation in Freddie Mac programs. Values: H = Home Possible, F = HFA Advantage, R = Refi Possible.
RELIEF REFINANCE INDICATOR: Indicates if loan is part of Freddie Mac's Relief Refinance Program. Values: Y = Relief Refinance Loan.
PROPERTY VALUATION METHOD: Method used for property appraisal. Values: 1 = ACE Loans, 2 = Full Appraisal, etc.
INTEREST ONLY INDICATOR (I/O INDICATOR): Indicates if loan requires interest-only payments initially. Values: Y = Yes, N = No.
MI CANCELLATION INDICATOR: Indicates if mortgage insurance has been cancelled post-purchase. Values: Y = Canceled, N = Not Canceled.

### Monthly Loan Performance Data
- Monthly updates on loan performance.
- Includes payment history, delinquency status, and other performance metrics.


MONTHLY PERFORMANCE DATA FILE
FIELD POSITION	ATTRIBUTE NAME	DATA TYPE & FORMAT	MAX LENGTH
1	Loan Sequence Number	Alpha Numeric - PYYQnXXXXXXX	12
2	Monthly Reporting Period	Date	6
3	Current Actual UPB	Numeric - 12,2	12
4	Current Loan Delinquency Status	Alpha Numeric	3
5	Loan Age	Numeric 	3
6	Remaining Months to Legal Maturity	Numeric 	3
7	Defect Settlement Date	Date	6
8	Modification Flag	Alpha	1
9	Zero Balance Code	Numeric	2
10	Zero Balance Effective Date	Date	6
11	Current Interest Rate	Numeric - 8,3	8
12	Current Deferred UPB	Numeric	12
13	Due Date of Last Paid Installment (DDLPI)	Date	6
14	MI Recoveries	Numeric - 12,2	12
15	Net Sales Proceeds	Alpha-Numeric 	14
16	Non MI Recoveries	Numeric - 12,2	12
17	Expenses	Numeric - 12,2	12
18	Legal Costs	Numeric - 12,2	12
19	Maintenance and Preservation Costs	Numeric - 12,2	12
20	Taxes and Insurance	Numeric - 12,2	12
21	Miscellaneous Expenses	Numeric - 12,2	12
22	Actual Loss Calculation	Numeric - 12,2	12
23	Modification Cost	Numeric - 12,2	12
24	Step Modification Flag	Alpha	1
25	Deferred Payment Plan	Alpha	1
26	Estimated Loan-to-Value (ELTV)	Numeric	4
27	Zero Balance Removal UPB	Numeric - 12,2	12
28	Delinquent Accrued Interest	Numeric - 12,2	12
29	Delinquency Due to Disaster	Alpha	1
30	Borrower Assistance Status Code	Alpha	1
31	Current Month Modification Cost	Numeric - 12,2	12
32	Interest Bearing UPB	Numeric - 12,2	12



•  LOAN SEQUENCE NUMBER - Unique identifier for each loan.
•  MONTHLY REPORTING PERIOD - As-of month for loan information.
•  CURRENT ACTUAL UPB - Current mortgage balance reported by the servicer.
•  CURRENT LOAN DELINQUENCY STATUS - Number of days delinquent based on MBA method.
•  LOAN AGE - Number of scheduled payments from origination or modification.
•  REMAINING MONTHS TO LEGAL MATURITY - Months remaining until mortgage maturity.
•  DEFECT SETTLEMENT DATE - Date of underwriting or servicing defect settlement.
•  MODIFICATION FLAG - Indicates if the loan was modified.
•  ZERO BALANCE CODE - Reason for reducing loan balance to zero.
•  ZERO BALANCE EFFECTIVE DATE - Date of event triggering zero balance.
•  CURRENT INTEREST RATE - Current interest rate on the mortgage note.
•  CURRENT NON-INTEREST BEARING UPB - Non-interest bearing portion of UPB.
•  DUE DATE OF LAST PAID INSTALLMENT (DDLPI) - Due date of last paid installment.
•  MI RECOVERIES - Mortgage insurance recoveries amount.
•  NET SALE PROCEEDS - Proceeds from property sale after expenses.
•  NON MI RECOVERIES - Non-mortgage insurance recoveries amount.
•  TOTAL EXPENSES - Total expenses related to property maintenance or sale.
•  LEGAL COSTS - Legal costs associated with property sale.
•  MAINTENANCE AND PRESERVATION COSTS - Costs for property upkeep.
•  TAXES AND INSURANCE - Taxes and insurance expenses related to property.
•  MISCELLANEOUS EXPENSES - Miscellaneous expenses related to property sale.
•  ACTUAL LOSS CALCULATION - Calculated loss for loans with specific zero balance codes.
•  CUMULATIVE MODIFICATION COST - Cumulative modification costs for modified loans.
•  STEP MODIFICATION FLAG - Indicates if modification includes step rate changes.
•  PAYMENT DEFERRAL - Indicates if loan received payment deferral.
•  ESTIMATED LOAN TO VALUE (ELTV) - Estimated loan-to-value ratio.
•  ZERO BALANCE REMOVAL UPB - UPB prior to zero balance code application.
•  DELINQUENT ACCRUED INTEREST - Delinquent interest owed at default.
•  DELINQUENCY DUE TO DISASTER - Flag indicating delinquency due to disaster.
•  BORROWER ASSISTANCE STATUS CODE - Code indicating borrower's assistance plan.
•  CURRENT MONTH MODIFICATION COST - Modification cost for the current month.
•  INTEREST BEARING UPB - Current interest-bearing UPB of modified mortgages.
