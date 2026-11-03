---
id: TC-AC-DS-E2E-148-log-activity-log-principal-distributor-dan-edit
title: "Activity Log: Aksi SKU Principal sebagai Objek Non-entitas, Distributor Entity-bound, dan Edit per Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-488
  - TC-AC-DS-489
  - TC-AC-DS-490
coverage:
  web: automated
---

# Activity Log: Aksi SKU Principal sebagai Objek Non-entitas, Distributor Entity-bound, dan Edit per Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Principal di atas).
- Akun kedua: Total Control Distributor PT Cakra Distribusi (Dewi Lestari, Modified By `Dewi L`, Local Registration aktif) `totalControlDist_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10), dipakai pada langkah 20 dan seterusnya (ganti akun eksplisit).
- Data Pre-setup: SKU inti `HHR-ARC-200` (Model/Type `H200`) dan `TAG-ARC-OBJ` serta seed (#29, #30); SKU lokal Distributor `LOC-NOR-01` dan Activity Log Distributor dengan entri Create `Rugged Handheld Reader (LOC-NOR-01)` oleh `Dewi L` (#31, #34); pohon Category (#25), Device Name (#26), Brand Principal (#27), Brand Distributor `Nordik` (#28); file foto uji `foto-a.jpg` (#37); General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35); riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: SKU Distributor `DIS-LOG-01` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Nordik`, Model/Type `T-DL1`, foto `foto-a.jpg`) dibuat pada TC-AC-DS-489 (kode literal sesuai TC; lihat Temuan untuk QA). Hook `before` menghapus `DIS-LOG-01` bila ada, hook `after` menghapusnya.
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-200` (Model/Type `H211` pada TC-AC-DS-490) dan `TAG-ARC-OBJ` (dihapus pada TC-AC-DS-488). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke `H200` dan mendaftarkan kembali `TAG-ARC-OBJ` dijamin fixture BE (disediakan tim FE/BE) di hook `before` dan `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Activity Log tab User Action untuk Principal dan Distributor sebelum aksi (audit trail permanen; 8b butir 10); jam server dan jam browser sinkron untuk asersi Date.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-490: Activity Log mencatat Edit per field dengan Modified By aktor

1. Catat baseline jumlah entri Activity Log tab User Action Principal
2. Ketik Search `HHR-ARC-200`, tekan Enter
3. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
4. Verifikasi Popup Edit SKU tampil dengan field terisi
5. Ubah Model/Type menjadi `H211`
6. Klik `[Save]`
7. Tunggu aksi selesai: Popup Edit SKU tertutup
8. Catat waktu aksi
9. Buka Activity Log, buka tab User Action
10. Verifikasi Activity Log memuat entri baru Action `Edit`, Object `Device SKU`, Field `Model/Type`, Old Value `H200`, New Value `H211`, Modified By `Jane S` (jumlah entri bertambah tepat 1 dari baseline langkah 1)
11. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)

### Pemulihan state antar TC

12. Buka Settings > Device > Device SKU

### TC-AC-DS-488: Activity Log mencatat aksi SKU Principal sebagai objek non-entitas

13. Catat baseline jumlah entri Activity Log tab User Action Principal dan Distributor PT Cakra Distribusi
14. Ketik Search `TAG-ARC-OBJ`, tekan Enter
15. Klik ⋯ pada baris `TAG-ARC-OBJ`, pilih `Delete`
16. Verifikasi dialog Delete tampil
17. Klik `[Delete]`
18. Tunggu aksi selesai: dialog tertutup
19. Buka Activity Log, buka tab User Action
20. Verifikasi Activity Log Principal memuat entri baru Action `Delete`, Object `Device SKU`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`, Modified By `Jane S`
21. Logout, lalu login sebagai Total Control Distributor PT Cakra Distribusi `totalControlDist_automated_{namaCompany}@qwertysystem.net`
22. Buka Activity Log, buka tab User Action
23. Verifikasi Activity Log Distributor memuat entri Create miliknya sendiri `Rugged Handheld Reader (LOC-NOR-01)` oleh `Dewi L`
24. Verifikasi Activity Log Distributor PT Cakra Distribusi tidak memuat entri Delete `TAG-ARC-OBJ` karena SKU Principal bersifat non-entitas (jumlah entri sama dengan baseline langkah 13)

### TC-AC-DS-489: Activity Log mencatat aksi SKU Distributor sebagai entity-bound

25. Buka Settings > Device > Device SKU
26. Catat baseline jumlah entri Activity Log tab User Action Distributor PT Cakra Distribusi dan Principal
27. Klik `[+ SKU]`
28. Isi form: Category `Asset TAG`, Device Name `Asset TAG`, Brand `Nordik`, Model/Type `T-DL1`, SKU `DIS-LOG-01`, foto `foto-a.jpg`
29. Klik `[Submit]`
30. Tunggu aksi selesai: popup Register SKU tertutup
31. Buka Activity Log, buka tab User Action
32. Verifikasi Activity Log Distributor memuat entri baru Action `Create`, Object `Device SKU`, Field `SKU`, Old Value `—`, New Value `Asset TAG (DIS-LOG-01)`, Modified By `Dewi L` (jumlah entri bertambah tepat 1 dari baseline langkah 26)
33. Logout, lalu login sebagai Total Control Principal `totalControlSku_automated_{namaCompany}@qwertysystem.net`
34. Buka Activity Log, buka tab User Action
35. Verifikasi Activity Log Principal juga memuat entri yang sama karena entitas target adalah Distributor pemilik SKU (jumlah entri bertambah tepat 1 dari baseline langkah 26)

## Notes

- Urutan TC dalam spec: 490, 488, 489 (bukan urutan nomor). Alur akun: Principal (490, 488), ganti akun ke Distributor (langkah 21, akhir 488 dan seluruh 489), lalu kembali ke Principal (langkah 33) yang juga akun default suite (S-07). Pemulihan sesi tidak diperlukan sesudah langkah 35; hook `after` memulihkan data.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 13, 26 (baseline, S-12), langkah 2 dan 14 (Search untuk menemukan baris target, R-16), langkah 8 (mencatat waktu aksi), langkah 12 dan 25 (S-03, S-09). Langkah 21 dan 33 adalah ganti akun eksplisit.
- Expected 488 butir b (ketiadaan entri Delete `TAG-ARC-OBJ` pada Activity Log Distributor) ditulis sebagai asersi jumlah berbaseline dan didahului anchor positif (langkah 23: entri Create milik Distributor sendiri) sesuai Expected butir c; urutan butir c ditaruh sebelum butir b (8b butir 2). Ini asersi kepemilikan/scope log, bukan asersi absence kelas g.
- Temuan untuk QA:
  - S-14: TC 488, 489, 490 tidak menyebut urutan baris pada Activity Log; entri baru dicari dengan selisih jumlah terhadap baseline, bukan posisi "teratas".
  - S-12: kode literal `HHR-ARC-200`, `TAG-ARC-OBJ`, `DIS-LOG-01` mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-06: TC mengubah dan menghapus baris Pre-setup bersama; pemulihan bergantung fixture BE yang belum ada.
  - Fixture rancangan Pre-setup #34 (Activity Log seed Distributor) belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`, `AC_DS_DIST_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
