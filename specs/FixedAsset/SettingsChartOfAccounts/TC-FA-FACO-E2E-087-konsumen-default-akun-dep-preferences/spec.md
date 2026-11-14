---
id: TC-FA-FACO-E2E-087-konsumen-default-akun-dep-preferences
title: "Akun tercermin sebagai nilai default company di Preferences"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FACO-LOGIC-01d, FACO-LOGIC-01f, "§9.2#p2", "§11.1#r4", "EB-XM-2@preferences"]
smoke: []
dependsOn: ["Settings > Accounting > Preferences: akun default company"]
trace:
  FACO-LOGIC-01d: [10, 32]
  FACO-LOGIC-01f: [13, 15]
  "§9.2#p2": [13, 15, 23]
  "§11.1#r4": [10, 15]
  "EB-XM-2@preferences": [10, 23, 32]
anchor: [2, 31]
coverage:
  web: automated
---
# Akun tercermin sebagai nilai default company di Preferences

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-087-1: Account Code `RFL1-{runId}`, Account Name `Proceeds Clearing {runId}`, Account Function `Disposal Proceeds`, Status `Active`, Used By `0`, belum pernah diekspor, ada di entitas aktor.
  - DU-087-2: Account Name baru untuk DU-087-1, yaitu `Proceeds Clearing Revised {runId}`.
  - DU-087-3: Account Code `RFL2-{runId}`, Account Name `Offset Created {runId}`, Account Function `Capitalization Offset`, dibuat oleh spec ini lewat `[+ Account]`.
  - DU-087-4: Account Code `RFL3-{runId}`, Account Name `Offset Anchor {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, belum pernah diekspor, ada di entitas aktor.
  - Label akun pada opsi Select di Preferences dibentuk dari Account Code dan Account Name:
    - DU-087-1: `RFL1-{runId} – Proceeds Clearing {runId}`, dari Account Code `RFL1-{runId}` dan Account Name `Proceeds Clearing {runId}`.
    - DU-087-1 sesudah diubah: `RFL1-{runId} – Proceeds Clearing Revised {runId}`, dari Account Code `RFL1-{runId}` dan Account Name `Proceeds Clearing Revised {runId}`.
    - DU-087-3: `RFL2-{runId} – Offset Created {runId}`, dari Account Code `RFL2-{runId}` dan Account Name `Offset Created {runId}`.
    - DU-087-4: `RFL3-{runId} – Offset Anchor {runId}`, dari Account Code `RFL3-{runId}` dan Account Name `Offset Anchor {runId}`.
  - Keempat data DU-087-1 sampai DU-087-4 adalah seluruh akun milik spec ini.
- Kondisi: Settings > Accounting > Preferences menyimpan akun DU-087-1 sebagai nilai `Default Disposal Proceeds Account` untuk entitas aktor.

## Test Steps

### Akun Capitalization Offset yang dibuat muncul sebagai opsi Default Capitalization Offset di Preferences
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `RFL1-{runId}` dan `RFL3-{runId}` tampil
3. Klik `[+ Account]`
4. Isi field Account Code dengan `RFL2-{runId}`
5. Isi field Account Name dengan `Offset Created {runId}`
6. Pilih `Capitalization Offset` pada field Account Function
7. Klik `[Submit]`
8. Klik tab `Preferences`
9. Buka Select `Default Capitalization Offset`
10. Verifikasi opsi `RFL2-{runId} – Offset Created {runId}` tampil di daftar opsi Select `Default Capitalization Offset`

### Akun Disposal Proceeds yang menjadi default company tidak menambah Used By dan tercermin di Preferences
11. Klik tab `Chart of Accounts`
12. Ketik Search `RFL1-{runId}`, tekan Enter
13. Verifikasi Used By baris `RFL1-{runId}` bernilai `0`, yaitu pemakaian sebagai Default Disposal Proceeds Account tidak dihitung Used By
14. Klik tab `Preferences`
15. Verifikasi Select `Default Disposal Proceeds Account` menampilkan `RFL1-{runId} – Proceeds Clearing {runId}`

### Account Name yang diubah tercermin pada label akun di Preferences
16. Klik tab `Chart of Accounts`
17. Ketik Search `RFL1-{runId}`, tekan Enter
18. Klik `⋯` pada baris `RFL1-{runId}`
19. Klik `Edit`
20. Ganti isi field Account Name dengan `Proceeds Clearing Revised {runId}`
21. Klik `[Save]`
22. Klik tab `Preferences`
23. Verifikasi Select `Default Disposal Proceeds Account` menampilkan `RFL1-{runId} – Proceeds Clearing Revised {runId}`

### Akun yang dihapus hilang dari opsi Default Capitalization Offset di Preferences
24. Klik tab `Chart of Accounts`
25. Ketik Search `RFL2-{runId}`, tekan Enter
26. Klik `⋯` pada baris `RFL2-{runId}`
27. Klik `Delete`
28. Klik `[Delete]` pada dialog konfirmasi
29. Klik tab `Preferences`
30. Buka Select `Default Capitalization Offset`
31. Verifikasi opsi `RFL3-{runId} – Offset Anchor {runId}` tampil di daftar opsi Select `Default Capitalization Offset`
32. Verifikasi opsi `RFL2-{runId} – Offset Created {runId}` tidak tampil di daftar opsi Select `Default Capitalization Offset`
