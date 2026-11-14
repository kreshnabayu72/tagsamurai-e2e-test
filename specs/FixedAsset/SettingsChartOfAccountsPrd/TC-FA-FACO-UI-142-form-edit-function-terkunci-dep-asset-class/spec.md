---
id: TC-FA-FACO-UI-142-form-edit-function-terkunci-dep-asset-class
title: "Form Edit Account: tooltip Account Function terkunci karena dipakai Asset Class"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - §4.2b#r3
smoke: []
dependsOn:
  - "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"
trace:
  §4.2b#r3: [2, 4, 7]
coverage:
  web: automated
---

# Form Edit Account: tooltip Account Function terkunci karena dipakai Asset Class

## Prerequisites
- Aktor: Total Control.
- Layar awal: Modal Edit Account pada Settings > Accounting > Chart of Accounts.
- Komponen: Modal Edit Account
- Data:
  - DU-142-1: Akun, Account Code `5-6002`, Account Name `Depreciation Expense – Warehouse`, Account Function `Depreciation Expense`, Status `Active`, Used By `1`, Last Used in Journal `—`.
  - DU-142-2: Akun, Account Code `5-6003`, Account Name `Depreciation Expense – Branch`, Account Function `Depreciation Expense`, Status `Active`, Used By `2`, Last Used in Journal `—`.
- Kondisi:
  - K1: modal Edit Account untuk akun DU-142-1 terbuka
  - K2: modal Edit Account untuk akun DU-142-2 terbuka

## Test Steps

### Alasan Account Function terkunci untuk satu Asset Class pemakai
1. Tampilkan Modal Edit Account dengan kondisi K1
2. Verifikasi Select Account Function Disabled
3. Arahkan kursor ke Select Account Function
4. Verifikasi alasan `Account Function can't be changed because this account is used by 1 Asset Class.` tersampaikan pada Select Account Function yang Disabled

### Alasan Account Function terkunci untuk beberapa Asset Class pemakai
5. Tampilkan Modal Edit Account dengan kondisi K2
6. Arahkan kursor ke Select Account Function
7. Verifikasi alasan `Account Function can't be changed because this account is used by 2 Asset Classes.` tersampaikan pada Select Account Function yang Disabled
