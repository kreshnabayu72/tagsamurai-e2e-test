---
id: TC-AC-DS-E2E-142-log-tiga-surface-create-dan-edit-kode-device-name
title: "Log Tiga Surface: Create SKU serta Edit Kode SKU dan Device Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-467
  - TC-AC-DS-468
  - TC-AC-DS-469
coverage:
  web: automated
---

# Log Tiga Surface: Create SKU serta Edit Kode SKU dan Device Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal (#27), file foto uji `foto-a.jpg` (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: SKU `LOG-NEW-01` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-LG1`, foto `foto-a.jpg`) dibuat pada TC-AC-DS-467 (kode literal sesuai TC, bukan bersuffix; lihat Temuan untuk QA). Hook `before` menghapus `LOG-NEW-01` bila ada, hook `after` menghapusnya.
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-200` (kode menjadi `HHR-ARC-201` pada TC-AC-DS-468; Device Name menjadi `UHF Handheld Reader Pro` pada TC-AC-DS-469). TC menetapkan baris ini, sehingga menjadi Pre-setup bersama yang diubah; pemulihan ke kode `HHR-ARC-200` dan Device Name `UHF Handheld Reader` dijamin fixture BE (disediakan tim FE/BE) di hook `before`, di antara TC (langkah 32), dan di hook `after`. Efek: Last Modified `HHR-ARC-200` berubah dan Changelog, System Log, serta Activity Log bertambah entri permanen.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (audit trail permanen, jumlah tidak dapat diturunkan dari seeding; 8b butir 10); jam server dan jam browser sinkron untuk asersi Date.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-467: Log Create SKU: satu entri Field SKU pada tiga surface

1. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
2. Klik `[+ SKU]`
3. Isi form: Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-LG1`, SKU `LOG-NEW-01`, foto `foto-a.jpg`
4. Klik `[Submit]`
5. Tunggu aksi selesai: popup Register SKU tertutup
6. Catat waktu aksi
7. Klik ikon Changelog
8. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Create`, SKU `Asset TAG (LOG-NEW-01)`, Field `SKU`, Old Value `—`, New Value `Asset TAG (LOG-NEW-01)`, Modified By `Jane S` di baris pertama
9. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
10. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
11. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Create`, Object `Device SKU`, Name `LOG-NEW-01`, Field `SKU`, Old Value `—`, New Value `Asset TAG (LOG-NEW-01)`
12. Buka Activity Log, buka tab User Action
13. Verifikasi Activity Log tab User Action memuat entri Action `Create`, Object `Device SKU`, Name `Asset TAG (LOG-NEW-01)`, Field `SKU`, Old Value `—`, New Value `Asset TAG (LOG-NEW-01)`, Modified By `Jane S`
14. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 1 (satu entri Create, bukan satu entri per field)

### Pemulihan state antar TC

15. Buka Settings > Device > Device SKU

### TC-AC-DS-468: Log Edit kode SKU: Old dan New berformat Device Name dan kode

16. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
17. Ketik Search `HHR-ARC-200`, tekan Enter
18. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
19. Verifikasi Popup Edit SKU tampil dengan field terisi
20. Ubah SKU dari `HHR-ARC-200` menjadi `HHR-ARC-201`
21. Klik `[Save]`
22. Tunggu aksi selesai: Popup Edit SKU tertutup
23. Catat waktu aksi
24. Klik ikon Changelog
25. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `UHF Handheld Reader (HHR-ARC-201)`, Field `SKU`, Old Value `UHF Handheld Reader (HHR-ARC-200)`, New Value `UHF Handheld Reader (HHR-ARC-201)`, Modified By `Jane S` di baris pertama
26. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
27. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
28. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `HHR-ARC-201`, Field `SKU`, Old Value `UHF Handheld Reader (HHR-ARC-200)`, New Value `UHF Handheld Reader (HHR-ARC-201)`
29. Buka Activity Log, buka tab User Action
30. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `UHF Handheld Reader (HHR-ARC-201)`, Field `SKU`, Old Value `UHF Handheld Reader (HHR-ARC-200)`, New Value `UHF Handheld Reader (HHR-ARC-201)`, Modified By `Jane S`
31. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 16

### Pemulihan state antar TC

32. Pulihkan kode SKU `HHR-ARC-201` menjadi `HHR-ARC-200` lewat fixture BE; buka Settings > Device > Device SKU

### TC-AC-DS-469: Log Edit Device Name

33. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
34. Ketik Search `HHR-ARC-200`, tekan Enter
35. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
36. Verifikasi Popup Edit SKU tampil dengan field terisi
37. Ubah Device Name dari `UHF Handheld Reader` menjadi `UHF Handheld Reader Pro`
38. Klik `[Save]`
39. Tunggu aksi selesai: Popup Edit SKU tertutup
40. Catat waktu aksi
41. Klik ikon Changelog
42. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `UHF Handheld Reader Pro (HHR-ARC-200)`, Field `Device Name`, Old Value `UHF Handheld Reader`, New Value `UHF Handheld Reader Pro`, Modified By `Jane S` di baris pertama
43. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
44. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
45. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `HHR-ARC-200`, Field `Device Name`, Old Value `UHF Handheld Reader`, New Value `UHF Handheld Reader Pro`
46. Buka Activity Log, buka tab User Action
47. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `UHF Handheld Reader Pro (HHR-ARC-200)`, Field `Device Name`, Old Value `UHF Handheld Reader`, New Value `UHF Handheld Reader Pro`, Modified By `Jane S`
48. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 33

### Pemulihan state akhir

49. Pulihkan Device Name `HHR-ARC-200` menjadi `UHF Handheld Reader` lewat fixture BE; buka Settings > Device > Device SKU

## Notes

- Spec berisi sekitar 49 langkah nominal, melewati sekitar 35 langkah. Alasan: tiga TC satu kelas (pencatatan log tiga surface) dan masing-masing berdiri sendiri; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log; langkah 7 sampai 14, 24 sampai 31, 41 sampai 48) yang menurut bagian 3 prinsip 13 tidak dihitung sebagai langkah smell. Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 16, 33 (baseline, S-12), langkah 6, 23, 40 (mencatat waktu aksi), langkah 15, 32, 49 (kembali ke List dan memulihkan data, S-03, S-09), dan langkah 17 serta 34 (Search untuk menemukan baris target, R-16).
- Expected 467 butir a dipecah: kolom entri Changelog dalam satu `Verifikasi` (satu entri, langkah 8) dan Date terpisah (langkah 9); butir b langkah 11; butir c langkah 13; butir d langkah 14 dan Post Condition "tidak ada entri log ganda" ditutup oleh langkah 14 (selisih baseline). Pola sama untuk TC 468 dan 469.
- Pelaku aksi adalah aktor yang sama dengan pembaca log; tidak ada pelaku kedua.
- Temuan untuk QA:
  - S-12: kode literal `LOG-NEW-01`, `HHR-ARC-200`, dan nilai Pre-setup lain mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan: seeding idempotent, serial, pemulihan fixture BE).
  - S-06: TC 468 dan 469 mengubah baris Pre-setup `HHR-ARC-200` karena nilai Expected bergantung pada kodenya; pemulihannya bergantung fixture BE yang belum ada.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
