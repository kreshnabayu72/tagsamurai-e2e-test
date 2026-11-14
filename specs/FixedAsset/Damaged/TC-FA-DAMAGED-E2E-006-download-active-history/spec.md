---
id: TC-FA-DAMAGED-E2E-006-download-active-history
title: "Download sub-tab Active dan History menghasilkan berkas Damaged-Active / Damaged-History mengikuti saringan dan kolom tampil"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, T-DMG-02, "§5#r6", EB-DL-1@tabel-active, EB-DL-2@tabel-active, EB-DL-3@tabel-active, EB-FB-2@download, EB-DL-4]
smoke: [EB-DL-4]
dependsOn: []
trace:
  T-DMG-01: [6, 8, 17, 24, 31, 32, 37, 40]
  T-DMG-02: [46, 47]
  "§5#r6": [3, 5, 11, 45]
  EB-DL-1@tabel-active: [6, 17, 24, 31, 32, 40, 46]
  EB-DL-2@tabel-active: [7, 48]
  EB-DL-3@tabel-active: [5, 11, 45]
  EB-FB-2@download: [7, 48]
  EB-DL-4: [8]
anchor: []
coverage:
  web: automated
---

# Download sub-tab Active dan History menghasilkan berkas Damaged-Active / Damaged-History mengikuti saringan dan kolom tampil

## Prerequisites
- Aktor: Total Control, user `Admin T`, pada entitas khusus `Entitas Download {runId}` yang tidak dipakai spec lain.
- Layar awal: halaman Assets.
- Data:
  - DU-006-1: entitas khusus `Entitas Download {runId}`.
  - DU-006-2: `4` record `Waiting for Confirmation`, Name `Unduh Waiting {runId} - {n}`, Asset ID `UNW-{n}-{runId}`, Group `Head Office {runId}`, Source `Reported by holder`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 2 hari, pukul 10:00`.
  - DU-006-3: `8` record `Damaged`, Name `Unduh Damaged {runId} - {n}`, Asset ID `UND-{n}-{runId}`, Group `Head Office {runId}`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 4 hari, pukul 10:00`.
  - DU-006-4: record `Repaired` di sub-tab History, Name `Unduh Selesai {runId} - 1`, Asset ID `UNS-1-{runId}`, Reported By `Agus P`, Resolved By `Rina W`.
  - DU-006-5: record `Rejected` di sub-tab History, Name `Unduh Selesai {runId} - 2`, Asset ID `UNS-2-{runId}`, Reported By `Agus P`, Resolved By `Rina W`.
  - DU-006-6: record `Canceled` di sub-tab History, Name `Unduh Selesai {runId} - 3`, Asset ID `UNS-3-{runId}`, Reported By `Agus P`, Resolved By `Dewi A`.
  - DU-006-7: kata kunci Search `Tidak Ada Hasil {runId}` yang tidak cocok dengan record mana pun.
  - Entitas itu berisi `12` record berjalan dan `3` record selesai; ukuran halaman bawaan `10`, sehingga sub-tab Active menempati dua halaman. User `Agus P`, `Rina W`, dan `Dewi A` adalah user ber-runId.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Download Active tanpa saringan memuat semua baris
1. Buka tab `Damaged` pada halaman Assets
2. Klik ikon `Download`
3. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
4. Klik `Download as CSV`
5. Verifikasi berkas `Damaged-Active.csv` terunduh
6. Verifikasi berkas `Damaged-Active.csv` memuat `12` baris data walau tabel menampilkan `10` baris per halaman
7. Verifikasi tidak ada toast sukses sesudah berkas terunduh
8. Verifikasi baris `Unduh Damaged {runId} - 1` pada berkas memuat Status `Damaged` dan Last Holder `-` untuk nilai kosong
9. Klik ikon `Download`
10. Klik `Download as XLSX`
11. Verifikasi berkas `Damaged-Active.xlsx` terunduh

### Download Active mengikuti saringan
12. Klik ikon `Filter`
13. Pilih opsi `Waiting for Confirmation` pada field `Status`
14. Klik `[Apply]`
15. Klik ikon `Download`
16. Klik `Download as CSV`
17. Verifikasi berkas `Damaged-Active.csv` memuat `4` baris data, yaitu record `Unduh Waiting {runId} - 1` sampai `Unduh Waiting {runId} - 4`
18. Klik `[Clear Field]`
19. Klik `[Apply]`
20. Klik ikon `Filter` untuk menutup Filter Panel

### Download Active mengikuti sort aktif
21. Klik ikon sort pada header kolom `Name`
22. Klik ikon `Download`
23. Klik `Download as CSV`
24. Verifikasi baris data pertama pada berkas adalah `Unduh Damaged {runId} - 1` dan baris data terakhir adalah `Unduh Waiting {runId} - 4`
25. Klik ikon sort pada header kolom `Name`
26. Klik ikon sort pada header kolom `Name`

### Download Active tanpa kolom yang disembunyikan
27. Klik header kolom Actions `⋯`
28. Hapus centang `Source`
29. Klik ikon `Download`
30. Klik `Download as CSV`
31. Verifikasi header berkas `Damaged-Active.csv` memuat `Name`, `Asset ID`, `Group`, `Status`, `Last Holder`, `Reported By`, `Reported Date`, dan `Days Damaged`
32. Verifikasi header berkas tidak memuat `Source`
33. Klik header kolom Actions `⋯`
34. Centang `Source`

### Download Active tanpa hasil memuat header saja
35. Klik ikon `Search`
36. Ketik Search `Tidak Ada Hasil {runId}`, tekan Enter
37. Verifikasi tabel menampilkan `No results found`
38. Klik ikon `Download`
39. Klik `Download as CSV`
40. Verifikasi berkas `Damaged-Active.csv` terunduh dengan header kolom saja tanpa baris data
41. Klik `(←)` pada kotak Search

### Download History memakai nama berkas dan kolom History
42. Klik sub-tab `History`
43. Klik ikon `Download`
44. Klik `Download as CSV`
45. Verifikasi berkas `Damaged-History.csv` terunduh
46. Verifikasi berkas `Damaged-History.csv` memuat `3` baris data milik sub-tab History tanpa record sub-tab Active
47. Verifikasi header berkas memuat `Resolved By`, `Resolved Date`, dan `Duration`
48. Verifikasi tidak ada toast sukses sesudah berkas terunduh
