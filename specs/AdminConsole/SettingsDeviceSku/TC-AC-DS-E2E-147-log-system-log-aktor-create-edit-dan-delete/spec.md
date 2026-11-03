---
id: TC-AC-DS-E2E-147-log-system-log-aktor-create-edit-dan-delete
title: "System Log Aktor: Create, Edit per Field, dan Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-485
  - TC-AC-DS-486
  - TC-AC-DS-487
coverage:
  web: automated
---

# System Log Aktor: Create, Edit per Field, dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun kedua: Total Control Principal PT Arunika Prima (Budi Kurniawan, Modified By `Budi K`) `totalControlSku2_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC2_PASSWORD` (Pre-setup #2), dipakai pada langkah 30 (ganti akun eksplisit) untuk membaca System Log miliknya.
- Data Pre-setup: SKU inti `HHR-ARC-200` (Model/Type `H200`, Brand `Arcturus`) dan `TAG-ARC-OBJ` serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal `Arcturus`, `Veltrix` (#27), file foto uji `foto-a.jpg` (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: SKU `LOG-SYS-01` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-LS1`, foto `foto-a.jpg`) dibuat pada TC-AC-DS-485 (kode literal sesuai TC; lihat Temuan untuk QA). Hook `before` menghapus `LOG-SYS-01` bila ada, hook `after` menghapusnya.
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-200` (Model/Type `H210`, Brand `Veltrix` pada TC-AC-DS-486) dan `TAG-ARC-OBJ` (dihapus pada TC-AC-DS-487). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke `H200`, `Arcturus`, dan mendaftarkan kembali `TAG-ARC-OBJ` dijamin fixture BE (disediakan tim FE/BE) di hook `before`, di antara TC (langkah 13), dan di hook `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) System Log aktor `Jane Setiawan` dan `Budi Kurniawan` sebelum aksi (audit trail permanen; 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-486: System Log aktor mencatat satu baris per field untuk Edit

1. Catat baseline jumlah entri System Log aktor `Jane Setiawan`
2. Ketik Search `HHR-ARC-200`, tekan Enter
3. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
4. Verifikasi Popup Edit SKU tampil dengan field terisi
5. Ubah Model/Type menjadi `H210` dan Brand menjadi `Veltrix`
6. Klik `[Save]`
7. Tunggu aksi selesai: Popup Edit SKU tertutup
8. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
9. Verifikasi System Log memuat dua baris Edit terpisah: Field `Model/Type` (`H200` > `H210`) dan Field `Brand` (`Arcturus` > `Veltrix`) (jumlah entri bertambah tepat 2 dari baseline langkah 1)
10. Verifikasi kedua baris bernama `HHR-ARC-200` pada kolom Name dan Object `Device SKU`

### Pemulihan state antar TC

11. Buka Settings > Device > Device SKU
12. Pulihkan `HHR-ARC-200` (Model/Type `H200`, Brand `Arcturus`) lewat fixture BE
13. Muat ulang halaman

### TC-AC-DS-487: System Log aktor mencatat Delete

14. Catat baseline jumlah entri System Log aktor `Jane Setiawan`
15. Ketik Search `TAG-ARC-OBJ`, tekan Enter
16. Klik ⋯ pada baris `TAG-ARC-OBJ`, pilih `Delete`
17. Verifikasi dialog Delete tampil
18. Klik `[Delete]`
19. Tunggu aksi selesai: dialog tertutup
20. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
21. Verifikasi System Log memuat entri Action `Delete`, Object `Device SKU`, Name `TAG-ARC-OBJ`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—` (jumlah entri bertambah tepat 1 dari baseline langkah 14)

### Pemulihan state antar TC

22. Buka Settings > Device > Device SKU

### TC-AC-DS-485: System Log aktor mencatat Create dengan Name berisi kode SKU

23. Catat baseline jumlah entri System Log aktor `Jane Setiawan` dan `Budi Kurniawan`
24. Klik `[+ SKU]`
25. Isi form: Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-LS1`, SKU `LOG-SYS-01`, foto `foto-a.jpg`
26. Klik `[Submit]`
27. Tunggu aksi selesai: popup Register SKU tertutup
28. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
29. Verifikasi System Log `Jane Setiawan` memuat entri Action `Create`, Object `Device SKU`, Name `LOG-SYS-01` (kode SKU saja), Field `SKU`, Old Value `—`, New Value `Asset TAG (LOG-SYS-01)` (jumlah entri bertambah tepat 1 dari baseline langkah 23)
30. Logout, lalu login sebagai Total Control Principal kedua `totalControlSku2_automated_{namaCompany}@qwertysystem.net`
31. Buka Settings > User, cari user `totalControlSku2_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
32. Verifikasi tabel System Log `Budi Kurniawan` tampil
33. Verifikasi System Log `Budi Kurniawan` tidak memuat entri `LOG-SYS-01` (jumlah entri sama dengan baseline langkah 23)

### Pemulihan state akhir

34. Logout, lalu login sebagai akun default suite (Total Control Principal `totalControlSku_automated_{namaCompany}@qwertysystem.net`)

## Notes

- Urutan TC dalam spec: 486, 487, 485 (bukan urutan nomor). TC-AC-DS-485 terakhir karena langkah 30 mengganti akun ke akun kedua (S-07, S-10); TC yang menghapus data ada sebelum ganti akun.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 14, 23 (baseline, S-12), langkah 2 dan 15 (Search untuk menemukan baris target, R-16), langkah 11 sampai 13, 22, dan 34 (S-03, S-09). Langkah 30 adalah ganti akun eksplisit (S-07).
- Expected 485 butir b dicatat sebagai asersi kepemilikan log (bagian 3 prinsip 13 butir g: pengecekan isolasi log per aktor bukan kelas g), dengan anchor positif tabel System Log `Budi Kurniawan` tampil (langkah 32) dan selisih jumlah entri terhadap baseline (langkah 33). Bagian "hanya memuat aksi yang dilakukan `Jane Setiawan`" ditutup oleh langkah 29 dan 33.
- Temuan untuk QA:
  - S-15: TC 485 langkah 5 berbunyi "Login ... (sesi kedua) lalu buka Detail user `Jane Setiawan` > System Log", sedangkan Expected b menyebut System Log `Budi Kurniawan`. Spec mengikuti Expected: sesi kedua adalah `Budi Kurniawan` (Pre-setup #2) yang membuka System Log miliknya. Perlu penjelasan QA.
  - S-12: kode literal `LOG-SYS-01`, `HHR-ARC-200`, `TAG-ARC-OBJ` mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-06: TC mengubah dan menghapus baris Pre-setup bersama; pemulihan bergantung fixture BE yang belum ada.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`, `AC_DS_TC2_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
