---
id: TC-FA-CAID-E2E-088-transfer-group-update-segmen-dan-log-cascade
title: "Transfer Group: Update Segmen Group Code, Dilewati, dan Log Cascade"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-273
  - TC-FA-CAID-274
  - TC-FA-CAID-275
  - TC-FA-CAID-253
coverage:
  web: automated
---

# Transfer Group: Update Segmen Group Code, Dilewati, dan Log Cascade

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Transactions > Transfer, jadi langkah kedua membuka halaman itu (langkah pertama hanya mencatat baseline).
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite; tiket Transfer XFR-1 untuk aset A1 dari Group `Jakarta Office` ke Group `Warehouse` (Code `WH`) berstatus In Transit (No 25), di-seed oleh hook `before`; General Settings Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (No 27). Seed antar TC lewat seed API: B6 (Group Code tidak tercentang) dengan A1 `LAP/T490/0926/1` dan XFR-1 In Transit (TC-FA-CAID-274); B1 dengan Master Switch OFF, A1 `1`, dan XFR-1 In Transit (TC-FA-CAID-275).
- Fixture: nilai data Pre-setup di atas (baseline konfigurasi, Asset ID aset A1, Code Group) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE).
- Data Dinamis: Group aset A1 menjadi `Warehouse` (Dinamis No 9); dibersihkan oleh seed reset Company sebelum TC berikutnya.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan baca jumlah entri Changelog Asset A1, System Log Sarah Johnson, Activity Log, dan Modal Changelog: Custom Asset ID sebelum aksi (disediakan tim FE/BE). Kolom Changed At diasersi dengan toleransi satu menit terhadap waktu aksi yang dicatat sesudah klik `[Confirm Receipt]`; jam server dan jam browser sinkron.
- State global: konfigurasi Company Alpha dan aset diubah; hook `after` memulihkan Company Alpha ke baseline B1, aset A1 sampai A5, dan tiket XFR-1 ke seed awal. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-273: Transfer Group: segmen Group Code di-update, riwayat Transfer dicatat, dan banner tampil

1. Catat baseline jumlah entri Changelog Asset A1, System Log Sarah Johnson, Activity Log tab User Action, dan jumlah baris Modal Changelog: Custom Asset ID
2. Buka Fixed Asset > Transactions > Transfer
3. Buka tab Incoming lalu klik `[Arrival Scan]` pada XFR-1
4. Lakukan verifikasi unit A1 pada arrival scan lalu klik `[Confirm Receipt]`, lalu catat waktu aksi
5. Verifikasi toast sukses `Success, assets received and transfer completed.` tampil
6. Buka Fixed Asset > Assets > All Assets > Detail A1
7. Verifikasi Asset ID A1 menjadi `WH/LAP/T490/0926/1`: hanya segmen Group Code yang berubah dan segmen lain serta Increment `1` tetap
8. Buka tab `Histori Aset`
9. Verifikasi entri teratas memuat Old Asset ID `JKT/LAP/T490/0926/1`, New Asset ID `WH/LAP/T490/0926/1`, Reason `Transfer`, Changed At berisi tanggal dan jam aksi dalam format General Settings (dd/MM/yy, 24 jam, toleransi satu menit), dan Changed By `Sarah J`
10. Verifikasi banner info di Asset Detail berbunyi `Asset ID has been updated due to group transfer. Previous ID: JKT/LAP/T490/0926/1. Please reprint asset label if applicable.`

### TC-FA-CAID-253: Log cascade Transfer: entri per aset di Changelog aset, System Log, dan Activity Log

11. Buka Modal Changelog Asset pada Detail A1
12. Verifikasi jumlah entri Changelog aset bertambah satu dibanding baseline
13. Verifikasi baris baru Changelog aset memuat Action `Edit`, Field `Asset ID`, Old Value `JKT/LAP/T490/0926/1`, New Value `WH/LAP/T490/0926/1`, dan Modified By `Sarah J`
14. Tutup Modal Changelog Asset
15. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
16. Verifikasi System Log aktor bertambah satu entri dibanding baseline dengan Field `Asset ID`, Old Value `JKT/LAP/T490/0926/1`, dan New Value `WH/LAP/T490/0926/1`
17. Buka Fixed Asset > Activity Log > tab User Action
18. Verifikasi Activity Log bertambah satu entri dibanding baseline dengan Field `Asset ID`, Old Value `JKT/LAP/T490/0926/1`, dan New Value `WH/LAP/T490/0926/1`
19. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu buka Modal Changelog: Custom Asset ID dan dropdown filter `Field`
20. Verifikasi Modal Changelog: Custom Asset ID memuat sedikitnya satu baris
21. Verifikasi jumlah baris Modal Changelog: Custom Asset ID sama dengan baseline (tidak bertambah)
22. Verifikasi opsi filter `Field` tetap `Segments Formula`, `Separator`, `Status`

### TC-FA-CAID-274: Transfer saat formula tanpa segmen Group Code dilewati tanpa perubahan Asset ID

23. Tutup dropdown filter dan Modal Changelog: Custom Asset ID
24. Pulihkan Company Alpha ke baseline B6 (Group Code tidak tercentang), A1 ber-Asset ID `LAP/T490/0926/1`, dan tiket XFR-1 In Transit (seed API)
25. Buka Fixed Asset > Transactions > Transfer
26. Buka tab Incoming lalu klik `[Arrival Scan]` pada XFR-1
27. Lakukan verifikasi unit A1 pada arrival scan lalu klik `[Confirm Receipt]`
28. Verifikasi toast sukses `Success, assets received and transfer completed.` tampil
29. Buka Fixed Asset > Assets > All Assets > Detail A1 > tab `Histori Aset`
30. Verifikasi Group A1 menjadi `Warehouse`
31. Verifikasi Asset ID A1 tetap `LAP/T490/0926/1`
32. Verifikasi tidak ada entri riwayat Asset ID baru dan tidak ada banner info

### TC-FA-CAID-275: Transfer saat Master Switch OFF dilewati tanpa mutasi Asset ID

33. Pulihkan Company Alpha ke baseline B1 dengan Master Switch OFF, A1 ber-Asset ID `1`, dan tiket XFR-1 In Transit (seed API)
34. Buka Fixed Asset > Transactions > Transfer
35. Buka tab Incoming lalu klik `[Arrival Scan]` pada XFR-1
36. Lakukan verifikasi unit A1 pada arrival scan lalu klik `[Confirm Receipt]`
37. Tunggu aksi selesai
38. Buka Fixed Asset > Assets > All Assets > Detail A1 > tab `Histori Aset`
39. Verifikasi Transfer selesai: Group A1 menjadi `Warehouse`
40. Verifikasi Asset ID A1 tetap `1`
41. Verifikasi tidak ada entri riwayat dan tidak ada banner info

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 41 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik (cascade Asset ID akibat Transfer Group beserta log-nya), semua kelas fungsional cascade, dan tiap blok TC di-seed ulang sendiri sehingga berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC-FA-CAID-253 sesudah TC-FA-CAID-273: precondition TC-FA-CAID-253 adalah Transfer TC-FA-CAID-273, sehingga log dibaca pada aksi yang sama. Asersi "tidak bertambah" pada langkah 21 memakai baseline jumlah (bukan kelas g) dan langkah 20 menjadi anchor positif.
- Langkah penghubung: langkah 2, 25, 34 (buka halaman), 1 (baseline, S-12), 4 (catat waktu aksi), 14 dan 23 (menutup modal dan dropdown), 24 dan 33 (pemulihan Company Alpha antar TC lewat seed), 37 (tunggu aksi selesai: hasil `[Confirm Receipt]` pada langkah 36 tidak diasersi langsung dan langkah 38 membuka tab `Histori Aset`, yang dihitung berpindah surface, bagian 8b butir 8).
- Anchor asersi absence riwayat dan banner pada langkah 32 dan 41: `Verifikasi` Group dan Asset ID A1 pada Detail A1 (langkah 30 dan 31, serta 39 dan 40) mendahuluinya pada halaman yang sama (bagian 8b butir 2); tidak ada asersi absence setelah F5.
- Frasa "Verifikasi unit A1" pada langkah TC adalah aksi pemindaian di arrival scan, ditulis "Lakukan verifikasi unit" agar tidak terbaca sebagai asersi.
- Temuan untuk QA:
  - Expected TC-FA-CAID-275 "Transfer selesai" tidak menyebut bentuk observasinya (toast atau status tiket); diasersi lewat Group A1 menjadi `Warehouse`.
  - TC-FA-CAID-274 menyebut A1 `LAP/T490/0926/1` pada B6 dan tidak menyebut cara menyiapkannya; disiapkan lewat seed.
  - TC-FA-CAID-253 tidak menyebut baseline jumlah entri; baseline dicatat sebelum aksi (S-12).
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
