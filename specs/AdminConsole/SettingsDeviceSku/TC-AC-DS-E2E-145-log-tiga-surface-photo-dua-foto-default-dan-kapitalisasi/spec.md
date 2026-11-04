---
id: TC-AC-DS-E2E-145-log-tiga-surface-photo-dua-foto-default-dan-kapitalisasi
title: "Log Tiga Surface: Photo Dua Foto, Set as Default, dan Perubahan Kapitalisasi Model/Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-476
  - TC-AC-DS-477
  - TC-AC-DS-483
coverage:
  web: automated
---

# Log Tiga Surface: Photo Dua Foto, Set as Default, dan Perubahan Kapitalisasi Model/Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti `HHR-ARC-100` (2 foto, foto kedua default), `HHR-ARC-200` (Model/Type `H200`) serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal (#27), file foto uji `foto-a.jpg`, `foto-b.png` (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-100` (dua foto diganti pada TC-AC-DS-476; foto pertama dijadikan default pada TC-AC-DS-477) dan `HHR-ARC-200` (Model/Type `H200` menjadi `h200` pada TC-AC-DS-483). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke dua foto semula dengan foto kedua default dan Model/Type `H200` dijamin fixture BE (disediakan tim FE/BE) di hook `before`, di antara TC (langkah 15), dan di hook `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri. Efek: Last Modified kedua SKU berubah.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (audit trail permanen; 8b butir 10); jam server dan jam browser sinkron untuk asersi Date.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-476: Log Edit Photo mengganti dua foto dalam satu Save tetap menghasilkan satu entri Photo

1. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
2. Ketik Search `HHR-ARC-100`, tekan Enter
3. Klik ⋯ pada baris `HHR-ARC-100`, pilih `Edit`
4. Verifikasi Popup Edit SKU tampil dengan field terisi
5. Ganti foto pertama dengan `foto-a.jpg` dan foto kedua dengan `foto-b.png`
6. Klik `[Save]`
7. Tunggu aksi selesai: Popup Edit SKU tertutup
8. Klik ikon Changelog
9. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Field `Photo`, Old Value `—`, New Value `—`, Modified By `Jane S` di baris pertama
10. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline langkah 1 (satu entri Photo, bukan dua)
11. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
12. Verifikasi System Log aktor `Jane Setiawan` memuat satu entri Photo untuk `HHR-ARC-100` (jumlah entri bertambah tepat 1 dari baseline langkah 1)
13. Buka Activity Log, buka tab User Action
14. Verifikasi Activity Log tab User Action memuat satu entri Photo untuk `UHF Handheld Reader (HHR-ARC-100)` (jumlah entri bertambah tepat 1 dari baseline langkah 1)

### Pemulihan state antar TC

15. Pulihkan foto `HHR-ARC-100` ke dua foto semula dengan foto kedua default lewat fixture BE; buka Settings > Device > Device SKU

### TC-AC-DS-477: Log Edit Photo — Set as default memakai nilai slot Photo 1 dan Photo 2

16. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
17. Ketik Search `HHR-ARC-100`, tekan Enter
18. Klik ⋯ pada baris `HHR-ARC-100`, pilih `Edit`
19. Verifikasi Popup Edit SKU tampil dengan field terisi
20. Tandai foto pertama sebagai default (sebelumnya foto kedua)
21. Klik `[Save]`
22. Tunggu aksi selesai: Popup Edit SKU tertutup
23. Catat waktu aksi
24. Klik ikon Changelog
25. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `UHF Handheld Reader (HHR-ARC-100)`, Field `Photo — Set as default`, Old Value `Photo 2`, New Value `Photo 1`, Modified By `Jane S` di baris pertama
26. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
27. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
28. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `HHR-ARC-100`, Field `Photo — Set as default`, Old Value `Photo 2`, New Value `Photo 1`
29. Buka Activity Log, buka tab User Action
30. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `UHF Handheld Reader (HHR-ARC-100)`, Field `Photo — Set as default`, Old Value `Photo 2`, New Value `Photo 1`, Modified By `Jane S`
31. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 16 (tidak ada entri log ganda)

### Pemulihan state antar TC

32. Pulihkan default `HHR-ARC-100` ke foto kedua lewat fixture BE; buka Settings > Device > Device SKU

### TC-AC-DS-483: Perubahan kapitalisasi Model/Type dicatat sebagai Edit nyata

33. Catat baseline jumlah entri Changelog Principal
34. Ketik Search `HHR-ARC-200`, tekan Enter
35. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
36. Verifikasi Popup Edit SKU tampil dengan field terisi
37. Ubah Model/Type dari `H200` menjadi `h200`
38. Klik `[Save]`
39. Verifikasi tidak ada toast "No changes to save."
40. Klik ikon Changelog
41. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline langkah 33
42. Verifikasi modal "Changelog: Device SKU" tampil dengan entri Edit baru Field `Model/Type`, Old Value `H200`, New Value `h200` di baris pertama

### Pemulihan state akhir

43. Tutup modal Changelog; pulihkan Model/Type `HHR-ARC-200` menjadi `H200` lewat fixture BE

## Notes

- Spec berisi 43 langkah nominal, melewati sekitar 35 langkah. Alasan: tiga TC satu kelas (pencatatan log) dan berdiri sendiri; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log; langkah 8 sampai 14 dan 24 sampai 31) yang menurut bagian 3 prinsip 13 tidak dihitung sebagai langkah smell. Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Urutan TC dalam spec: 476, 477, 483; pemulihan foto di langkah 15 dan 32 menjaga keadaan awal TC-AC-DS-477 (foto kedua default).
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 16, dan 33 (baseline, S-12), langkah 2, 17, 34 (Search untuk menemukan baris target, R-16), langkah 23 (mencatat waktu aksi), langkah 15, 32, 43 (S-03, S-09).
- Absence toast "No changes to save." (langkah 39) diletakkan segera setelah pemicu `[Save]` dan sebelum asersi entri Changelog (8b butir 11); selisih +1 entri (langkah 41) dan entri Edit baru pada langkah 42 adalah anchor positif. Entri baru pada TC-AC-DS-483 diidentifikasi lewat selisih jumlah terhadap baseline (langkah 33), lalu dibaca di baris pertama.
- Expected 476 butir a dipecah menjadi langkah 9 dan 10; butir b menjadi langkah 12 dan 14. Post Condition TC-AC-DS-483 ("tidak ada entri log ganda") tanpa langkah observasi di TC (hanya Changelog yang dibuka): tidak diasersi.
- Temuan untuk QA:
  - S-12: nilai literal Pre-setup (`HHR-ARC-100`, `HHR-ARC-200`, `H200`) mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-06: TC mengubah baris Pre-setup bersama; pemulihan bergantung fixture BE yang belum ada.
  - S-15: TC 476 langkah 6 ("Hitung entri Field Photo yang baru") tidak menyebut cara menghitung; spec memakai selisih jumlah terhadap baseline.
  - S-14: TC 476 tidak menyebut apakah tanda default berubah setelah kedua foto diganti; pemulihan fixture BE di langkah 15 menjaga keadaan awal TC 477.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
