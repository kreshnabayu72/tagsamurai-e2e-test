---
id: TC-AC-DS-E2E-149-log-snapshot-immutability-dan-filter-identitas-sku
title: "Log Snapshot: Device Name Rename, Edit Kode Dua Kali, dan Filter All SKUs Berkunci Identitas SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-491
  - TC-AC-DS-492
  - TC-AC-DS-493
coverage:
  web: automated
---

# Log Snapshot: Device Name Rename, Edit Kode Dua Kali, dan Filter All SKUs Berkunci Identitas SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti `SFR-VEL-4P` (Device Name `4-Port Fixed Reader`; foto kedua default, entri Changelog Edit `Photo — Set as default` pada #33) dan `HHR-ARC-200` (Device Name `UHF Handheld Reader`) serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal (#27), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33) termasuk entri Edit kode `HHR-ARC-20` > `HHR-ARC-200` oleh `Budi K`, modul Device Name sebagai tempat rename (#39). Nilai dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): Device Name Pre-setup `4-Port Fixed Reader` menjadi `4-Port Fixed Reader Pro` (TC-AC-DS-491) dan SKU Pre-setup `HHR-ARC-200` (kode menjadi `HHR-ARC-201`, `HHR-ARC-202` pada TC-AC-DS-492; menjadi `HHR-ARC-201` pada TC-AC-DS-493). TC menetapkan data ini sebagai Pre-setup bersama; pemulihan ke nama `4-Port Fixed Reader` dan kode `HHR-ARC-200` dijamin fixture BE (disediakan tim FE/BE) di hook `before`, di antara TC (langkah 29), dan di hook `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri. Last Modified SKU terkait dipulihkan oleh fixture BE (A-11).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah total entri Changelog Principal lewat BE tepat sebelum aksi pemicu TC-AC-DS-492 (N1, langkah 10) untuk asersi selisih +2 pada langkah 25 dan sebelum pemicu TC-AC-DS-493 (N2, langkah 30) untuk selisih +1 pada langkah 39 (S-12, 8b butir 10); pemulihan data di atas; rename Device Name lewat modul Device Name (TC tidak menyebut jalur menu; lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-491: Entri Changelog lama tetap menampilkan Device Name saat entri ditulis walau Device Name di-rename

1. Di modul Device Name, ganti nama `4-Port Fixed Reader` menjadi `4-Port Fixed Reader Pro` hingga perubahan tersimpan
2. Buka Settings > Device > Device SKU, lalu muat ulang halaman
3. Ketik Search `SFR-VEL-4P`, tekan Enter
4. Verifikasi baris `SFR-VEL-4P` pada List menampilkan Device Name terkini `4-Port Fixed Reader Pro` (live-join)
5. Klik ikon Changelog
6. Verifikasi modal "Changelog: Device SKU" tampil
7. Ketik Search `SFR-VEL-4P` pada modal, tekan Enter
8. Verifikasi entri Edit `SFR-VEL-4P` (Photo — Set as default) pada modal Changelog tetap menampilkan SKU `4-Port Fixed Reader (SFR-VEL-4P)` sesuai nama saat entri ditulis (snapshot), tidak berubah menjadi `4-Port Fixed Reader Pro`

### Pemulihan state antar TC

9. Klik `(←)` pada kotak Search modal, tutup modal Changelog, klik `(←)` pada kotak Search List

### TC-AC-DS-492: Edit kode SKU dua kali: entri pertama tetap berisi pasangan lama

10. Catat jumlah entri Changelog Principal sebagai N1 lewat kemampuan baca BE
11. Ketik Search `HHR-ARC-200`, tekan Enter
12. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
13. Verifikasi Popup Edit SKU tampil dengan field terisi
14. Ubah SKU dari `HHR-ARC-200` menjadi `HHR-ARC-201`
15. Klik `[Save]`
16. Tunggu aksi selesai: Popup Edit SKU tertutup
17. Ganti isi kotak search dengan `HHR-ARC-201`, tekan Enter
18. Klik ⋯ pada baris `HHR-ARC-201`, pilih `Edit`
19. Verifikasi Popup Edit SKU tampil dengan field terisi
20. Ubah SKU dari `HHR-ARC-201` menjadi `HHR-ARC-202`
21. Klik `[Save]`
22. Tunggu aksi selesai: Popup Edit SKU tertutup
23. Klik ikon Changelog
24. Verifikasi modal "Changelog: Device SKU" tampil
25. Verifikasi jumlah entri Changelog Principal bertambah 2 dari N1 lewat kemampuan baca BE
26. Verifikasi dua baris teratas modal Changelog memuat entri Edit dengan Old Value `UHF Handheld Reader (HHR-ARC-201)` dan New Value `UHF Handheld Reader (HHR-ARC-202)`
27. Verifikasi dua baris teratas modal Changelog memuat entri Edit dengan Old Value `UHF Handheld Reader (HHR-ARC-200)` dan New Value `UHF Handheld Reader (HHR-ARC-201)`
28. Verifikasi kolom SKU entri Edit dengan Old Value `UHF Handheld Reader (HHR-ARC-200)` tidak ditimpa mengikuti kode terbaru (tetap `UHF Handheld Reader (HHR-ARC-201)`, bukan `HHR-ARC-202`)

### Pemulihan state antar TC

29. Tutup modal Changelog; pulihkan kode `HHR-ARC-202` menjadi `HHR-ARC-200` lewat fixture BE; muat ulang halaman

### TC-AC-DS-493: Filter All SKUs Changelog berkunci identitas SKU sehingga riwayat mengikuti saat kode berubah

30. Catat jumlah entri Changelog Principal sebagai N2 lewat kemampuan baca BE
31. Ketik Search `HHR-ARC-200`, tekan Enter
32. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
33. Verifikasi Popup Edit SKU tampil dengan field terisi
34. Ubah SKU dari `HHR-ARC-200` menjadi `HHR-ARC-201`
35. Klik `[Save]`
36. Tunggu aksi selesai: Popup Edit SKU tertutup
37. Klik ikon Changelog
38. Verifikasi modal "Changelog: Device SKU" tampil
39. Verifikasi jumlah entri Changelog Principal bertambah 1 dari N2 lewat kemampuan baca BE
40. Klik ikon Filter modal, buka dropdown SKU
41. Verifikasi opsi SKU berlabel `Device Name (kode SKU)` terkini `UHF Handheld Reader (HHR-ARC-201)` tampil
42. Verifikasi tidak ada opsi terpisah berlabel `UHF Handheld Reader (HHR-ARC-200)`
43. Pilih opsi `UHF Handheld Reader (HHR-ARC-201)`
44. Klik `[Apply]` pada Filter Panel modal
45. Verifikasi hasil filter memuat entri lama (Edit kode `HHR-ARC-20` > `HHR-ARC-200`)
46. Verifikasi hasil filter memuat entri baru (Edit `HHR-ARC-200` > `HHR-ARC-201`) karena keduanya milik identitas SKU yang sama

### Pemulihan state akhir

47. Klik ikon Filter, hapus chip SKU dari field, klik `[Apply]`; tutup modal Changelog; pulihkan kode `HHR-ARC-201` menjadi `HHR-ARC-200` lewat fixture BE

## Notes

- Spec berisi 47 langkah nominal, melewati sekitar 35 langkah. Alasan: tiga TC satu kelas (snapshot dan identitas pada Changelog) dan berdiri sendiri; dua TC menulis kode dua kali sehingga memerlukan langkah Edit berulang yang bukan blok baca-log. Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 3, 7, 11, 17, 31 (Search untuk menemukan baris atau entri target, R-16), langkah 10 dan 30 (mencatat baseline N1 dan N2 sebelum aksi pemicu, S-12), langkah 9, 29, dan 47 (S-03, S-09).
- Expected 491 butir a dan b langkah 4 dan 8; 492 butir b, a, c langkah 26, 27, 28 (kedua entri diidentifikasi lewat pasangan Old Value dan New Value, bukan posisi baris; selisih jumlah +2 dari baseline N1 pada langkah 25); 493 butir a dipecah langkah 41 dan 42 dan butir b langkah 45 dan 46 (anchor positif: opsi baru pada langkah 41 sebelum absence langkah 42); entri baru TC-493 dipastikan lewat selisih +1 dari baseline N2 (langkah 30 dan 39).
- Temuan untuk QA:
  - S-13: TC 491 langkah 2 hanya menyebut "pada modul Device Name rename"; jalur menu tidak disebut, sehingga ditulis sebagai langkah di modul Device Name.
  - S-14: TC 491 langkah 6 ("cari entri Edit SKU `SFR-VEL-4P`") tidak menyebut cara mencari; spec memakai Search modal. TC 492 Expected mengidentifikasi entri lewat pasangan Old dan New Value; dua entri Edit itu berselang kurang dari satu menit (kolom Date berketelitian menit), sehingga urutan di antara keduanya tidak diandalkan: spec mengasersi selisih jumlah +2 dari baseline N1 (langkah 10 dan 25, S-12) dan membaca dua baris teratas urutan default Date terbaru sebagai himpunan (S-14).
  - S-12: nilai literal Pre-setup (`SFR-VEL-4P`, `HHR-ARC-200`) mengikuti TC tanpa suffix sesuai pengecualian S-12 A-11 (`suite.md`).
  - S-06: TC mengubah baris Pre-setup bersama; pemulihan dijamin fixture BE pemulih yang dinyatakan di `suite.md` (disediakan tim FE/BE, belum terverifikasi ada di environment).
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; `Fixture.settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
