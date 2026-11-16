---
id: TC-FA-FACO-E2E-082-delete-terekspor-dan-dipakai-dep-export-journal
title: "Delete akun yang pernah diekspor dan masih dipakai Asset Class menampilkan D-05 dengan kalimat pemakaian"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [D-05, "§[F-FACO-05] Delete Account#r3", "§9.4.2#r18", FACO-LOGIC-03c]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal", "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  D-05: [4, 5, 6, 7, 9, 13, 14, 15, 16, 18]
  "§[F-FACO-05] Delete Account#r3": [5, 14]
  "§9.4.2#r18": [5, 14]
  FACO-LOGIC-03c: [5, 14]
coverage:
  web: automated
---

# Delete akun yang pernah diekspor dan masih dipakai Asset Class menampilkan D-05 dengan kalimat pemakaian

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-082-1: Account Code `DEA1-{runId}`, Account Name `Heavy Machinery Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `1`, bukan nilai default company, Last Used in Journal `M0 − 2 bulan`, dipakai DU-082-3, ada di entitas aktor.
  - DU-082-2: Account Code `DEB1-{runId}`, Account Name `Fleet Accumulated Depreciation {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Used By `2`, bukan nilai default company, Last Used in Journal `M0 − 2 bulan`, dipakai DU-082-3 dan DU-082-4, ada di entitas aktor.
  - DU-082-3: Asset Class `Kelas Alat Berat {runId}`; Asset Cost `DEA1-{runId}`, Accumulated Depreciation `DEB1-{runId}`.
  - DU-082-4: Asset Class `Kelas Armada {runId}`; Accumulated Depreciation `DEB1-{runId}`.
  - Label akun pada bullet dialog dibentuk dari Account Code dan Account Name:
    - DU-082-1: `DEA1-{runId} – Heavy Machinery Cost {runId}`, dari Account Code `DEA1-{runId}` dan Account Name `Heavy Machinery Cost {runId}`.
    - DU-082-2: `DEB1-{runId} – Fleet Accumulated Depreciation {runId}`, dari Account Code `DEB1-{runId}` dan Account Name `Fleet Accumulated Depreciation {runId}`.
- Kondisi:
  - Akun DU-082-1 dan DU-082-2 sudah ikut dalam Export Journal untuk periode jurnal `M0 − 2 bulan`, sehingga Last Used in Journal keduanya terisi periode itu.

## Test Steps

### Delete akun terekspor yang dipakai 1 Asset Class menampilkan D-05 dengan kalimat pemakaian tunggal
1. Ketik Search `DEA1-{runId}`, tekan Enter
2. Klik `⋯` pada baris `DEA1-{runId}`
3. Klik `Delete`
4. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `DEA1-{runId} – Heavy Machinery Cost {runId}`
5. Verifikasi kalimat `This account was last used in a journal in [Month Year]. Deleting it may break historical records.` tampil dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`
6. Verifikasi kalimat `This account is used by 1 Asset Class and cannot be deleted.` tampil
7. Verifikasi kalimat saran `Deactivate it instead.` tidak tampil, karena akun dipakai Asset Class
8. Klik `[OK]`
9. Verifikasi baris `DEA1-{runId}` masih tampil di tabel dengan Status `Active`

### Delete akun terekspor yang dipakai 2 Asset Class menampilkan D-05 dengan kalimat pemakaian jamak
10. Ganti isi kotak search dengan `DEB1-{runId}`, tekan Enter
11. Klik `⋯` pada baris `DEB1-{runId}`
12. Klik `Delete`
13. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `DEB1-{runId} – Fleet Accumulated Depreciation {runId}`
14. Verifikasi kalimat `This account was last used in a journal in [Month Year]. Deleting it may break historical records.` tampil dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`
15. Verifikasi kalimat `This account is used by 2 Asset Classes and cannot be deleted.` tampil
16. Verifikasi kalimat saran `Deactivate it instead.` tidak tampil, karena akun dipakai Asset Class
17. Klik `[OK]`
18. Verifikasi baris `DEB1-{runId}` masih tampil di tabel dengan Status `Active`
