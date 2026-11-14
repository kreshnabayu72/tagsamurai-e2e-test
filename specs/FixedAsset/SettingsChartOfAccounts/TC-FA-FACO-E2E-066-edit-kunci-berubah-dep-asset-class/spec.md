---
id: TC-FA-FACO-E2E-066-edit-kunci-berubah-dep-asset-class
title: "Save Edit saat akun mulai dipakai Asset Class sesudah form dibuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [D-16, "§[F-FACO-02] Edit Account#r4", "§[F-FACO-02] Edit Account#r11", "§[F-FACO-02] Edit Account#r12", "§[F-FACO-02] Edit Account#r13", "§[F-FACO-02] Edit Account#r14", "§9.4.2#r8"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  D-16: [12, 13]
  "§[F-FACO-02] Edit Account#r4": [12, 33]
  "§[F-FACO-02] Edit Account#r11": [12, 14]
  "§[F-FACO-02] Edit Account#r12": [16, 17, 19, 20]
  "§[F-FACO-02] Edit Account#r13": [22, 23, 26]
  "§[F-FACO-02] Edit Account#r14": [34, 35, 36, 39, 40]
  "§9.4.2#r8": [12, 16, 17, 22, 23, 26, 33]
anchor: []
coverage:
  web: automated
---

# Save Edit saat akun mulai dipakai Asset Class sesudah form dibuka

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-066-1: Account Code `EDA-{runId}`, Account Name `Mesin Gerinda {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat form Edit dibuka.
  - DU-066-2: Account Code `EDB-{runId}`, Account Name `Mesin Frais {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, belum dipakai Asset Class saat form Edit dibuka.
  - DU-066-3: Asset Class `Armada Produksi {runId}`, belum memakai `EDA-{runId}` maupun `EDB-{runId}`.
  - Account Label yang diharapkan untuk DU-066-1 adalah `EDA-{runId} – Mesin Gerinda {runId}`, dari Account Code dan Account Name.
  - Nilai yang dicoba disimpan pada `EDA-{runId}` adalah Account Name `Mesin Gerinda Baru {runId}` dan Account Function `Asset Cost` (DU-066-4).
  - Nilai yang disimpan pada `EDB-{runId}` adalah Account Name `Mesin Frais Baru {runId}` (DU-066-5).

## Test Steps

### Save Edit ditolak saat Account Function terkunci sesudah form dibuka
1. Klik ikon Changelog
2. Ketik Search `{runId}` pada Changelog, tekan Enter
3. Catat jumlah entri Changelog yang tampil
4. Klik `✕` pada Changelog
5. Ketik Search `{runId}`, tekan Enter
6. Klik `⋯` pada baris `EDA-{runId}`
7. Klik `Edit`
8. Asset Class `Armada Produksi {runId}` memakai akun `EDA-{runId}` pada field Depreciation Expense
9. Pilih Account Function `Asset Cost`
10. Ganti isi Account Name menjadi `Mesin Gerinda Baru {runId}`
11. Klik `[Save]`
12. Verifikasi dialog `Cannot Save Account` tampil
13. Verifikasi dialog memuat bullet `EDA-{runId} – Mesin Gerinda {runId}`
14. Verifikasi tidak ada toast yang tampil
15. Klik `[OK]`
16. Verifikasi field Account Function Disabled
17. Verifikasi field Account Function kembali ke nilai tersimpan `Depreciation Expense`
18. Arahkan kursor ke field Account Function
19. Verifikasi alasan `Account Function can't be changed because this account is used by 1 Asset Class.` tersampaikan pada field Account Function yang Disabled
20. Verifikasi isi Account Name tetap `Mesin Gerinda Baru {runId}`
21. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
22. Verifikasi baris `EDA-{runId}` menampilkan Account Name `Mesin Gerinda {runId}`
23. Verifikasi baris `EDA-{runId}` menampilkan Account Function `Depreciation Expense`
24. Klik ikon Changelog
25. Ketik Search `{runId}` pada Changelog, tekan Enter
26. Verifikasi jumlah entri Changelog sama dengan jumlah yang dicatat
27. Klik `✕` pada Changelog

### Save Edit berhasil saat status kunci berubah tetapi field terkunci tidak diubah
28. Klik `⋯` pada baris `EDB-{runId}`
29. Klik `Edit`
30. Asset Class `Armada Produksi {runId}` memakai akun `EDB-{runId}` pada field Accumulated Depreciation
31. Ganti isi Account Name menjadi `Mesin Frais Baru {runId}`
32. Klik `[Save]`
33. Verifikasi toast `Success, account has been updated.` tampil
34. Verifikasi form Edit Account tertutup
35. Verifikasi baris `EDB-{runId}` menampilkan Account Name `Mesin Frais Baru {runId}`
36. Verifikasi Used By baris `EDB-{runId}` bernilai `1`
37. Klik ikon Changelog
38. Ketik Search `EDB-{runId}` pada Changelog, tekan Enter
39. Verifikasi Changelog memuat entri Action `Edit` untuk Field `Account Name` dengan Old Value `Mesin Frais {runId}` dan New Value `Mesin Frais Baru {runId}`
40. Verifikasi Changelog tidak memuat entri untuk Field `Account Function` pada `EDB-{runId}`
41. Klik `✕` pada Changelog
