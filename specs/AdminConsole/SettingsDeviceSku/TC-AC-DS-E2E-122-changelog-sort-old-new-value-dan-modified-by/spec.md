---
id: TC-AC-DS-E2E-122-changelog-sort-old-new-value-dan-modified-by
title: "Sort Changelog: Old/New Value Angka Sebelum Teks dan Modified By Memakai Nama Lengkap"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-410
  - TC-AC-DS-411
coverage:
  web: automated
---

# Sort Changelog: Old/New Value Angka Sebelum Teks dan Modified By Memakai Nama Lengkap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) berupa seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (total pada modal dapat lebih besar karena entri yang ditulis spec lain, sehingga urutan seed diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26`; pelaku `Jane S` dan `Budi K` yang nama lengkapnya `Jane Setiawan` dan `Budi Kurniawan`), Port `SFR-ZERO-01` bernilai `9090`, General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): SKU Pre-setup `SFR-ZERO-01` (Port `9090` menjadi `9100`) pada TC-AC-DS-410. Efek: Last Modified SKU itu berubah dan satu entri Edit Port `SFR-ZERO-01` `9090` > `9100` oleh `Jane S` ditambahkan ke Changelog (N + 1 entri selama TC itu, dengan N dicatat pada langkah 11 dari info pagination). SKU ini milik Pre-setup bersama karena TC menetapkannya; pemulihannya (Port kembali `9090`, entri Edit Port dihapus sehingga Changelog kembali N entri) dijamin fixture BE yang disediakan tim FE/BE, dijalankan di hook `before` dan `after`. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas, termasuk penghapusan entri Changelog yang dibuat spec (audit trail permanen tidak dapat dihapus lewat UI).
- State global: tidak ada selain yang disebut di atas. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-411: Sort Modified By memakai nama lengkap dan bukan format singkat

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik ikon Filter pada modal, pada field Date pilih rentang `01/09/26` sampai `03/10/26`, lalu klik `[Apply]` pada Filter Panel modal
4. Klik header kolom Modified By sekali
5. Verifikasi Ascending: baris pertama bernilai `Budi K` (nama lengkap `Budi Kurniawan` mendahului `Jane Setiawan`)
6. Klik header kolom Modified By sekali lagi
7. Verifikasi Descending: baris pertama bernilai `Jane S`
8. Klik header kolom Modified By sekali lagi (kembali ke Date Newest First)

### Pemulihan state antar TC

9. Tutup modal Changelog

### TC-AC-DS-410: Sort Old Value dan New Value meletakkan angka sebelum teks dan nilai kosong di akhir saat ascending

10. Klik ikon Changelog
11. Catat jumlah entri total pada info pagination modal sebagai N, lalu tutup modal Changelog
12. Ketik Search `SFR-ZERO-01` pada List, tekan Enter
13. Verifikasi baris SKU `SFR-ZERO-01` tampil pada List
14. Klik ⋯ pada baris `SFR-ZERO-01`, pilih `Edit`
15. Ubah Port dari `9090` menjadi `9100`
16. Klik [Save]
17. Tunggu aksi selesai: Popup Edit SKU tertutup
18. Klik `(←)` pada kotak Search List
19. Klik ikon Changelog
20. Verifikasi modal "Changelog: Device SKU" tampil
21. Verifikasi jumlah entri total pada info pagination sama dengan N + 1: satu entri Edit Port `SFR-ZERO-01` `9090` > `9100` oleh `Jane S` ditambahkan pada langkah 16
22. Verifikasi baris pertama pada urutan default Newest First adalah entri Edit Port `SFR-ZERO-01` `9090` > `9100` oleh `Jane S`
23. Klik ikon Filter pada modal, pada field Date pilih rentang `01/09/26` sampai `03/10/26`, lalu klik `[Apply]` pada Filter Panel modal
24. Klik header kolom Old Value sekali, lalu pindah ke halaman terakhir
25. Verifikasi Old Value Ascending: baris terakhir pada halaman terakhir bernilai `—` (entri Create `BLE-KIN-GW1`)
26. Klik header kolom Old Value sekali lagi
27. Verifikasi Old Value Descending: halaman 1 dimulai baris bernilai `—`
28. Klik header kolom New Value sekali, lalu pindah ke halaman terakhir
29. Verifikasi New Value Ascending: baris terakhir pada halaman terakhir bernilai `—` (entri Delete `HHR-ARC-300`)
30. Klik ikon Filter pada modal, klik `[Clear Field]`, lalu klik `[Apply]`
31. Klik header kolom Old Value sekali, lalu telusuri halaman sampai baris `9090` ditemukan
32. Verifikasi Old Value Ascending: `9090` berada sebelum semua baris bernilai teks (angka lebih dulu daripada teks)
33. Verifikasi Old Value Ascending: baris bernilai `—` berada sesudahnya
34. Klik header kolom Old Value sekali lagi, lalu telusuri halaman sampai baris `9090` ditemukan
35. Verifikasi Old Value Descending: `9090` berada setelah semua baris bernilai teks
36. Klik header kolom New Value sekali, lalu telusuri halaman sampai baris `9100` ditemukan
37. Verifikasi New Value Ascending: `9100` berada sebelum semua baris bernilai teks (angka lebih dulu daripada teks)
38. Verifikasi New Value Ascending: baris bernilai `—` berada sesudahnya

### Pemulihan state akhir

39. Klik header kolom New Value dua kali (kembali ke Date Newest First), lalu tutup modal Changelog

## Notes

- Urutan TC dalam spec: TC-AC-DS-411 dikerjakan lebih dulu karena membaca entri seed tanpa mengubah data; TC-AC-DS-410 menulis data (Edit Port) sehingga ditaruh di akhir (S-10). Urutan berbeda dari nomor TC; tiap TC tetap berdiri sendiri.
- Langkah penghubung tanpa `Verifikasi`: langkah 3 dan 23 (Filter Date seed `01/09/26` sampai `03/10/26` sesuai langkah TC), langkah 8, 9, 11 (mencatat N), 18, 24, 26, 28, 30, 31, 34, 36, dan 39; langkah 12 (Search untuk menemukan baris target, R-16) dan langkah 17 (menunggu aksi selesai, 8b butir 8).
- Expected 410: butir a di langkah 21 (N + 1) dan langkah 22 (isi entri Edit Port ditambahkan); butir b di langkah 25; butir c di langkah 27; butir d di langkah 29; butir e (posisi entri Edit Port relatif setelah Filter Date dilepas, tanpa posisi halaman absolut) dipecah per klausa di langkah 32 dan 33 (Old Value Ascending), langkah 35 (Old Value Descending), serta langkah 37 dan 38 (New Value Ascending).
- Ukuran spec (di atas sekitar 35 langkah): dua TC sort Changelog yang memakai modal yang sama; TC-AC-DS-410 sendiri memuat 16 langkah TC dan lima butir Expected dengan 9 `Verifikasi` yang tidak dapat digabung, dan TC-AC-DS-411 dibuka lebih dulu karena hanya membaca (S-10).
- Post Condition TC 410 (pemulihan Port dan entri oleh automation baseline) tanpa langkah observasi di TC: tidak diasersi; dilakukan fixture BE di `after`.
- Temuan untuk QA:
  - S-12: jumlah entri memakai N dari info pagination (N + 1 sesudah Edit Port) dan urutan seed diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26`; nilai literal Pre-setup #29 dan #33 memakai pengecualian S-12 A-11 (`suite.md`).
  - S-14: langkah 22 mengandalkan bahwa entri baru berada di baris pertama urutan default Newest First, dibaca sesudah selisih N + 1 dibuktikan pada langkah 21 (S-14 2026-11-03); TC tidak menyatakannya secara eksplisit.
  - TC 410 langkah 7, 9, 11 menyebut "perhatikan halaman 1" setelah sort tanpa menyatakan apakah sort mereset halaman; spec mengikuti TC.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
