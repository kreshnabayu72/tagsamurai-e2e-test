---
id: TC-FA-FACO-E2E-062-bulk-deactivate-campuran-dep-asset-class
title: "Bulk Deactivate campuran menonaktifkan akun yang lolos dan melewati akun yang dipakai"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-03, FACO-LOGIC-02d, "§4.2f#b2", "§[F-FACO-04] Deactivate Account#r9", "§[F-FACO-04] Deactivate Account#r10", "§[F-FACO-04] Deactivate Account#r11", "§9.4.2#r14", "§9.4.2#r36", T-05]
smoke: [T-05]
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  D-03: [7, 8, 9, 10, 21, 23]
  FACO-LOGIC-02d: [7, 10]
  "§4.2f#b2": [20, 21, 22, 23, 25, 26, 27]
  "§[F-FACO-04] Deactivate Account#r9": [7, 8, 9, 10]
  "§[F-FACO-04] Deactivate Account#r10": [13, 14, 15]
  "§[F-FACO-04] Deactivate Account#r11": 12
  "§9.4.2#r14": [7, 12, 13, 15]
  "§9.4.2#r36": [20, 22, 25, 27]
  T-05: 12
anchor: []
coverage:
  web: automated
---

# Bulk Deactivate campuran menonaktifkan akun yang lolos dan melewati akun yang dipakai

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-062-1: Account Code `DBP1-{runId}`, Account Name `Gudang Penyusutan Utara {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-062-2: Account Code `DBP2-{runId}`, Account Name `Gudang Penyusutan Selatan {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-062-3: Account Code `DBB1-{runId}`, Account Name `Armada Truk {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-062-6).
  - DU-062-4: Account Code `DBP3-{runId}`, Account Name `Gudang Penyusutan Barat {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, tidak dipakai Asset Class.
  - DU-062-5: Account Code `DBB2-{runId}`, Account Name `Armada Pickup {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-062-6).
  - DU-062-6: Asset Class `Armada Distribusi {runId}`; Asset Cost `DBB1-{runId}`, Accumulated Depreciation `DBB2-{runId}`.
  - Account Label yang diharapkan untuk DU-062-1 adalah `DBP1-{runId} – Gudang Penyusutan Utara {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-062-2 adalah `DBP2-{runId} – Gudang Penyusutan Selatan {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-062-3 adalah `DBB1-{runId} – Armada Truk {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-062-4 adalah `DBP3-{runId} – Gudang Penyusutan Barat {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-062-5 adalah `DBB2-{runId} – Armada Pickup {runId}`, dari Account Code dan Account Name.
  - Bullet beranotasi yang diharapkan untuk DU-062-3 adalah `DBB1-{runId} – Armada Truk {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.
  - Bullet beranotasi yang diharapkan untuk DU-062-5 adalah `DBB2-{runId} – Armada Pickup {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.

## Test Steps

### Bulk Deactivate campuran menonaktifkan akun yang lolos dan melewati akun yang dipakai
1. Ketik Search `{runId}`, tekan Enter
2. Centang baris `DBP1-{runId}`
3. Centang baris `DBP2-{runId}`
4. Centang baris `DBB1-{runId}`
5. Klik `Bulk Action`
6. Pilih `Deactivate`
7. Verifikasi dialog `Deactivate Accounts` tampil
8. Verifikasi dialog memuat bullet `DBP1-{runId} – Gudang Penyusutan Utara {runId}` pada kelompok `The following will be deactivated:`
9. Verifikasi dialog memuat bullet `DBP2-{runId} – Gudang Penyusutan Selatan {runId}` pada kelompok `The following will be deactivated:`
10. Verifikasi dialog memuat bullet `DBB1-{runId} – Armada Truk {runId} (still in use)` pada kelompok `The following are still in use and will be skipped:`
11. Klik `[Continue]`
12. Verifikasi toast `Success, account has been deactivated. Some items were skipped (still in use).` tampil
13. Verifikasi switch Status baris `DBP1-{runId}` Inactive
14. Verifikasi switch Status baris `DBP2-{runId}` Inactive
15. Verifikasi switch Status baris `DBB1-{runId}` tetap Active

### Seleksi campuran yang meloloskan tepat satu akun tetap memakai dialog campuran
16. Centang baris `DBP3-{runId}`
17. Centang baris `DBB2-{runId}`
18. Klik `Bulk Action`
19. Pilih `Deactivate`
20. Verifikasi dialog `Deactivate Accounts` tampil, bukan `Deactivate Account`
21. Verifikasi dialog memuat bullet `DBP3-{runId} – Gudang Penyusutan Barat {runId}` pada kelompok `The following will be deactivated:`
22. Verifikasi kelompok `The following will be deactivated:` memuat satu bullet
23. Verifikasi dialog memuat bullet `DBB2-{runId} – Armada Pickup {runId} (still in use)` pada kelompok `The following are still in use and will be skipped:`
24. Klik `[Continue]`
25. Verifikasi toast `Success, account has been deactivated. Some items were skipped (still in use).` tampil
26. Verifikasi switch Status baris `DBP3-{runId}` Inactive
27. Verifikasi switch Status baris `DBB2-{runId}` tetap Active
