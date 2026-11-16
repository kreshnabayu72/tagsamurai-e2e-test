---
id: TC-FA-FACO-E2E-061-deactivate-diblokir-dep-asset-class
title: "Deactivate akun yang dipakai Asset Class ditolak dengan dialog blok"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [C-02, D-04, FACO-LOGIC-02c, FACO-LOGIC-02d, "§3.8#r3", "§[F-FACO-04] Deactivate Account#r1", "§[F-FACO-04] Deactivate Account#r5", "§9.4.2#r11", "§9.4.2#r15", "EB-FB-2@guard-blok"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  C-02: [9, 13, 27, 28]
  D-04: [4, 5, 6, 11, 22, 23, 24]
  FACO-LOGIC-02c: [9, 13, 27, 28]
  FACO-LOGIC-02d: [4, 22]
  "§3.8#r3": [2, 4, 9]
  "§[F-FACO-04] Deactivate Account#r1": [4, 9]
  "§[F-FACO-04] Deactivate Account#r5": [22, 27, 28, 31]
  "§9.4.2#r11": [4, 9]
  "§9.4.2#r15": [22, 31]
  "EB-FB-2@guard-blok": [7, 25]
anchor: []
coverage:
  web: automated
---

# Deactivate akun yang dipakai Asset Class ditolak dengan dialog blok

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-061-1: Account Code `DAX-{runId}`, Account Name `Mesin Bubut {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, dipakai 1 Asset Class (DU-061-3).
  - DU-061-2: Account Code `DAY-{runId}`, Account Name `Mesin Press {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, dipakai 2 Asset Class (DU-061-3, DU-061-4).
  - DU-061-3: Asset Class `Heavy Equipment {runId}`; Asset Cost `DAX-{runId}`, Accumulated Depreciation `DAY-{runId}`.
  - DU-061-4: Asset Class `Office Equipment {runId}`; Accumulated Depreciation `DAY-{runId}`.
  - Account Label yang diharapkan untuk DU-061-1 adalah `DAX-{runId} – Mesin Bubut {runId}`, dari Account Code dan Account Name.
  - Account Label yang diharapkan untuk DU-061-2 adalah `DAY-{runId} – Mesin Press {runId}`, dari Account Code dan Account Name.
  - Bullet beranotasi yang diharapkan untuk DU-061-1 adalah `DAX-{runId} – Mesin Bubut {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.
  - Bullet beranotasi yang diharapkan untuk DU-061-2 adalah `DAY-{runId} – Mesin Press {runId} (still in use)`, dari Account Label dan anotasi untuk akun yang dipakai Asset Class.

## Test Steps

### Deactivate akun yang dipakai 1 Asset Class ditolak
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi switch Status baris `DAX-{runId}` Enabled
3. Klik switch Status baris `DAX-{runId}`
4. Verifikasi dialog `Cannot Deactivate Account` tampil
5. Verifikasi dialog memuat bullet `DAX-{runId} – Mesin Bubut {runId}`
6. Verifikasi dialog memuat kalimat `This account is used by 1 Asset Class and cannot be deactivated.`
7. Verifikasi tidak ada toast yang tampil
8. Klik `[OK]`
9. Verifikasi switch Status baris `DAX-{runId}` tetap Active

### Deactivate akun yang dipakai 2 Asset Class ditolak
10. Klik switch Status baris `DAY-{runId}`
11. Verifikasi dialog memuat kalimat `This account is used by 2 Asset Classes and cannot be deactivated.`
12. Klik `[OK]`
13. Verifikasi switch Status baris `DAY-{runId}` tetap Active

### Bulk Deactivate seluruh akun yang dipakai ditolak
14. Klik ikon Changelog
15. Ketik Search `{runId}` pada Changelog, tekan Enter
16. Catat jumlah entri Changelog yang tampil
17. Klik `✕` pada Changelog
18. Centang baris `DAX-{runId}`
19. Centang baris `DAY-{runId}`
20. Klik `Bulk Action`
21. Pilih `Deactivate`
22. Verifikasi dialog `Cannot Deactivate Accounts` tampil
23. Verifikasi dialog memuat bullet `DAX-{runId} – Mesin Bubut {runId} (still in use)`
24. Verifikasi dialog memuat bullet `DAY-{runId} – Mesin Press {runId} (still in use)`
25. Verifikasi tidak ada toast yang tampil
26. Klik `[OK]`
27. Verifikasi switch Status baris `DAX-{runId}` tetap Active
28. Verifikasi switch Status baris `DAY-{runId}` tetap Active
29. Klik ikon Changelog
30. Ketik Search `{runId}` pada Changelog, tekan Enter
31. Verifikasi jumlah entri Changelog sama dengan jumlah yang dicatat
32. Klik `✕` pada Changelog
33. Klik `×` pada Bulk Action bar
