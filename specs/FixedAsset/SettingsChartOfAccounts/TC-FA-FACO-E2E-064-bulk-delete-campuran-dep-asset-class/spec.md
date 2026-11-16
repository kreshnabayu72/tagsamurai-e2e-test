---
id: TC-FA-FACO-E2E-064-bulk-delete-campuran-dep-asset-class
title: "Bulk Delete campuran menghapus akun yang lolos dan melewati akun yang dipakai"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-09, "§4.2f#b2", "§[F-FACO-05] Delete Account#r11", "§[F-FACO-05] Delete Account#r12", "§[F-FACO-05] Delete Account#r13", "§9.4.2#r20", "§9.4.2#r36", EB-BLK-3, T-06]
smoke: [T-06]
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  D-09: [7, 8, 9, 10, 29, 31]
  "§4.2f#b2": [28, 29, 30, 31, 33, 34, 35]
  "§[F-FACO-05] Delete Account#r11": [7, 8, 9, 10]
  "§[F-FACO-05] Delete Account#r12": [13, 14, 15, 22]
  "§[F-FACO-05] Delete Account#r13": 12
  "§9.4.2#r20": [7, 12, 13, 14]
  "§9.4.2#r36": [28, 30, 33, 34, 35]
  EB-BLK-3: [18, 20]
  T-06: 12
anchor: []
coverage:
  web: automated
---

# Bulk Delete campuran menghapus akun yang lolos dan melewati akun yang dipakai

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-064-1: Account Code `DLP1-{runId}`, Account Name `Rak Gudang Utara {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class, bukan nilai default company.
  - DU-064-2: Account Code `DLP2-{runId}`, Account Name `Rak Gudang Selatan {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class, bukan nilai default company.
  - DU-064-3: Account Code `DLB1-{runId}`, Account Name `Forklift Listrik {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-064-6).
  - DU-064-4: Account Code `DLP3-{runId}`, Account Name `Rak Gudang Barat {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class, bukan nilai default company.
  - DU-064-5: Account Code `DLB2-{runId}`, Account Name `Forklift Diesel {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-064-6).
  - DU-064-6: Asset Class `Armada Gudang {runId}`; Asset Cost `DLB1-{runId}`, Accumulated Depreciation `DLB2-{runId}`.
  - Account Label yang diharapkan untuk DU-064-1 adalah `DLP1-{runId} – Rak Gudang Utara {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-064-2 adalah `DLP2-{runId} – Rak Gudang Selatan {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-064-3 adalah `DLB1-{runId} – Forklift Listrik {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-064-4 adalah `DLP3-{runId} – Rak Gudang Barat {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-064-5 adalah `DLB2-{runId} – Forklift Diesel {runId}`, dari Account Code dan Account Name.
  - Bullet beranotasi yang diharapkan untuk DU-064-3 adalah `DLB1-{runId} – Forklift Listrik {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.
  - Bullet beranotasi yang diharapkan untuk DU-064-5 adalah `DLB2-{runId} – Forklift Diesel {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.

## Test Steps

### Bulk Delete campuran menghapus akun yang lolos dan melewati akun yang dipakai
1. Ketik Search `{runId}`, tekan Enter
2. Centang baris `DLP1-{runId}`
3. Centang baris `DLP2-{runId}`
4. Centang baris `DLB1-{runId}`
5. Klik `Bulk Action`
6. Pilih `Delete`
7. Verifikasi dialog `Delete Accounts` tampil
8. Verifikasi dialog memuat bullet `DLP1-{runId} – Rak Gudang Utara {runId}` pada kelompok `The following will be deleted:`
9. Verifikasi dialog memuat bullet `DLP2-{runId} – Rak Gudang Selatan {runId}` pada kelompok `The following will be deleted:`
10. Verifikasi dialog memuat bullet `DLB1-{runId} – Forklift Listrik {runId} (still in use)` pada kelompok `The following will be skipped:`
11. Klik dua kali `[Continue]`
12. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil
13. Verifikasi baris `DLB1-{runId}` yang dilewati tetap ada di tabel
14. Verifikasi baris `DLP1-{runId}` tidak ada lagi di tabel
15. Verifikasi baris `DLP2-{runId}` tidak ada lagi di tabel
16. Klik ikon Changelog
17. Ketik Search `DLP1-{runId}` pada Changelog, tekan Enter
18. Verifikasi Changelog memuat tepat satu entri Action `Delete` untuk Account Code `DLP1-{runId}`
19. Ganti isi Search Changelog dengan `DLP2-{runId}`, tekan Enter
20. Verifikasi Changelog memuat tepat satu entri Action `Delete` untuk Account Code `DLP2-{runId}`
21. Ganti isi Search Changelog dengan `DLB1-{runId}`, tekan Enter
22. Verifikasi Changelog tidak memuat entri Action `Delete` untuk Account Code `DLB1-{runId}`
23. Klik `✕` pada Changelog

### Seleksi campuran yang meloloskan tepat satu akun tetap memakai dialog campuran
24. Centang baris `DLP3-{runId}`
25. Centang baris `DLB2-{runId}`
26. Klik `Bulk Action`
27. Pilih `Delete`
28. Verifikasi dialog `Delete Accounts` tampil, bukan `Delete Account`
29. Verifikasi dialog memuat bullet `DLP3-{runId} – Rak Gudang Barat {runId}` pada kelompok `The following will be deleted:`
30. Verifikasi kelompok `The following will be deleted:` memuat satu bullet
31. Verifikasi dialog memuat bullet `DLB2-{runId} – Forklift Diesel {runId} (still in use)` pada kelompok `The following will be skipped:`
32. Klik `[Continue]`
33. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil
34. Verifikasi baris `DLB2-{runId}` tetap ada di tabel
35. Verifikasi baris `DLP3-{runId}` tidak ada lagi di tabel
