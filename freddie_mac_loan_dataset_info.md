
# Freddie Mac Single-Family Loan-Level Dataset

## Overview

This dataset contains loan-level origination and monthly loan performance data on fully amortizing fixed-rate Single-Family mortgages acquired by Freddie Mac. The data includes loans with origination dates from 1999 to 2023 and is refreshed quarterly.

## Dataset Description

### Loan-Level Origination Data

- **Credit Score:** Numeric assessment of borrower's creditworthiness.
- **First Payment Date:** Date of first scheduled mortgage payment.
- **First Time Homebuyer Flag:** Indicates if borrower is purchasing their first primary residence.
- **Maturity Date:** Final monthly payment due date.
- **Metropolitan Statistical Area (MSA):** Urban area designation based on population.
- **Mortgage Insurance Percentage (MI %):** Percentage of loan covered by mortgage insurance.
- **Number of Units:** Indicates property type (one-, two-, three-, or four-unit).
- **Occupancy Status:** Type of property occupancy (Primary, Investment, Second Home).
- **Original Combined Loan-to-Value (CLTV):** Ratio of loan amount to property value at origination.
- **Original Debt-to-Income (DTI) Ratio:** Ratio of borrower's debt payments to income at origination.
- **Original UPB:** Mortgage unpaid principal balance on note date.
- **Original Loan-to-Value (LTV):** Loan amount to property value ratio at origination.
- **Original Interest Rate:** Interest rate at loan origination.
- **Channel:** Loan origination type (Retail, Broker, Correspondent).
- **Prepayment Penalty Mortgage (PPM) Flag:** Indicates if mortgage has prepayment penalties.
- **Amortization Type:** Mortgage type (Fixed Rate or Adjustable Rate).
- **Property State:** State or territory where property is located.
- **Property Type:** Type of property secured by mortgage.
- **Postal Code:** Postal code of mortgaged property location.
- **Loan Sequence Number:** Unique identifier for each loan.
- **Loan Purpose:** Purpose of mortgage (Purchase, Refinance - Cash Out, etc.).
- **Original Loan Term:** Number of scheduled monthly payments.
- **Number of Borrowers:** Number of borrowers on mortgage note.
- **Seller Name:** Name of seller delivering mortgage loan to Freddie Mac.
- **Servicer Name:** Entity servicing the mortgage to Freddie Mac.
- **Super Conforming Flag:** Indicates if mortgage exceeds conforming loan limits.
- **Pre-HARP Loan Sequence Number:** Identifier linking Relief Refinance loan to original loan.
- **Program Indicator:** Indicates participation in Freddie Mac programs.
- **HARP Indicator:** Indicates if loan is part of Freddie Mac's Relief Refinance Program.
- **Property Valuation Method:** Method used for property appraisal.
- **Interest Only (I/O) Indicator:** Indicates if loan requires interest-only payments initially.
- **Mortgage Insurance Cancellation Indicator:** Indicates if mortgage insurance has been cancelled post-purchase.

### Monthly Loan Performance Data

- **Loan Sequence Number:** Unique identifier for each loan.
- **Monthly Reporting Period:** As-of month for loan information.
- **Current Actual UPB:** Current mortgage balance reported by the servicer.
- **Current Loan Delinquency Status:** Number of days delinquent based on MBA method.
- **Loan Age:** Number of scheduled payments from origination or modification.
- **Remaining Months to Legal Maturity:** Months remaining until mortgage maturity.
- **Defect Settlement Date:** Date of underwriting or servicing defect settlement.
- **Modification Flag:** Indicates if the loan was modified.
- **Zero Balance Code:** Reason for reducing loan balance to zero.
- **Zero Balance Effective Date:** Date of event triggering zero balance.
- **Current Interest Rate:** Current interest rate on the mortgage note.
- **Current Non-Interest Bearing UPB:** Non-interest bearing portion of UPB.
- **Due Date of Last Paid Installment (DDLPI):** Due date of last paid installment.
- **MI Recoveries:** Mortgage insurance recoveries amount.
- **Net Sales Proceeds:** Proceeds from property sale after expenses.
- **Non MI Recoveries:** Non-mortgage insurance recoveries amount.
- **Total Expenses:** Total expenses related to property maintenance or sale.
- **Legal Costs:** Legal costs associated with property sale.
- **Maintenance and Preservation Costs:** Costs for property upkeep.
- **Taxes and Insurance:** Taxes and insurance expenses related to property.
- **Miscellaneous Expenses:** Miscellaneous expenses related to property sale.
- **Actual Loss Calculation:** Calculated loss for loans with specific zero balance codes.
- **Cumulative Modification Cost:** Cumulative modification costs for modified loans.
- **Step Modification Flag:** Indicates if modification includes step rate changes.
- **Payment Deferral:** Indicates if loan received payment deferral.
- **Estimated Loan-to-Value (ELTV):** Estimated loan-to-value ratio.
- **Zero Balance Removal UPB:** UPB prior to zero balance code application.
- **Delinquent Accrued Interest:** Delinquent interest owed at default.
- **Delinquency Due to Disaster:** Flag indicating delinquency due to disaster.
- **Borrower Assistance Status Code:** Code indicating borrower's assistance plan.
- **Current Month Modification Cost:** Modification cost for the current month.
- **Interest Bearing UPB:** Current interest-bearing UPB of modified mortgages.

## Usage

This dataset is valuable for analyzing mortgage origination trends, loan performance metrics, and understanding credit risk in the Single-Family mortgage market.

## Source

For more details and updates, visit [Freddie Mac Research](https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset).
