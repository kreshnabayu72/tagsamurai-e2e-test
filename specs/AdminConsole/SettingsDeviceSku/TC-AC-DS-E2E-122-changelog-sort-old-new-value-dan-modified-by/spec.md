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
- Data Pre-setup: SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) dalam keadaan awal 35 entri (4 halaman pada 10 baris per halaman; pelaku `Jane S` dan `Budi K` yang nama lengkapnya `Jane Setiawan` dan `Budi Kurniawan`), Port `SFR-ZERO-01` bernilai `9090`, General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): SKU Pre-setup `SFR-ZERO-01` (Port `9090` menjadi `9100`) pada TC-AC-DS-410. Efek: Last Modified SKU itu berubah dan satu entri Edit Port `SFR-ZERO-01` `9090` > `9100` oleh `Jane S` ditambahkan ke Changelog (36 entri selama TC itu). SKU ini milik Pre-setup bersama karena TC menetapkannya; pemulihannya (Port kembali `9090`, entri Edit Port dihapus sehingga Changelog kembali 35 entri) dijamin fixture BE yang disediakan tim FE/BE, dijalankan di hook `before` dan `after`. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas, termasuk penghapusan entri Changelog yang dibuat spec (audit trail permanen tidak dapat dihapus lewat UI).
- State global: tidak ada selain yang disebut di atas. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-411: Sort Modified By memakai nama lengkap dan bukan format singkat

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik header kolom Modified By sekali
4. Verifikasi Ascending: baris pertama bernilai `Budi K` (nama lengkap `Budi Kurniawan` mendahului `Jane Setiawan`)
5. Klik header kolom Modified By sekali lagi
6. Verifikasi Descending: baris pertama bernilai `Jane S`
7. Klik header kolom Modified By sekali lagi (kembali ke Date Newest First)

### Pemulihan state antar TC

8. Tutup modal Changelog

### TC-AC-DS-410: Sort Old Value dan New Value meletakkan angka sebelum teks dan nilai kosong di akhir saat ascending

9. Ketik Search `SFR-ZERO-01` pada List, tekan Enter
10. Verifikasi baris SKU `SFR-ZERO-01` tampil pada List
11. Klik ⋯ pada baris `SFR-ZERO-01`, pilih `Edit`
12. Verifikasi Popup Edit SKU tampil dengan field terisi
13. Ubah Port dari `9090` menjadi `9100`
14. Klik [Save]
15. Tunggu aksi selesai: Popup Edit SKU tertutup
16. Klik `(←)` pada kotak Search List
17. Klik ikon Changelog
18. Verifikasi modal "Changelog: Device SKU" tampil
19. Verifikasi Changelog memuat 36 entri (4 halaman) selama TC ini
20. Verifikasi baris pertama pada urutan default Newest First adalah entri Edit Port `SFR-ZERO-01` `9090` > `9100` oleh `Jane S` yang ditambahkan pada langkah 14
21. Klik header kolom Old Value sekali
22. Verifikasi Old Value Ascending: halaman 1 dimulai `9090` (angka lebih dulu daripada teks)
23. Pindah ke halaman terakhir (halaman 4)
24. Verifikasi baris terakhir halaman 4 bernilai `—` (entri Create `BLE-KIN-GW1`)
25. Klik header kolom Old Value sekali lagi
26. Verifikasi Old Value Descending: halaman 1 dimulai baris bernilai `—`
27. Pindah ke halaman terakhir (halaman 4)
28. Verifikasi baris terakhir halaman 4 bernilai `9090` (angka setelah teks)
29. Klik header kolom New Value sekali
30. Verifikasi New Value Ascending: halaman 1 dimulai `9100` (angka lebih dulu daripada teks)
31. Pindah ke halaman terakhir (halaman 4)
32. Verifikasi baris terakhir halaman 4 bernilai `—` (entri Delete `HHR-ARC-300`)

### Pemulihan state akhir

33. Klik header kolom New Value dua kali (kembali ke Date Newest First), lalu tutup modal Changelog

## Notes

- Urutan TC dalam spec: TC-AC-DS-411 dikerjakan lebih dulu karena membaca 35 entri awal tanpa mengubah data; TC-AC-DS-410 menulis data (Edit Port) sehingga ditaruh di akhir (S-10). Urutan berbeda dari nomor TC; tiap TC tetap berdiri sendiri.
- Langkah penghubung tanpa `Verifikasi`: langkah 7, 8, 16, 33; langkah 9 (Search untuk menemukan baris target, R-16) dan langkah 15 (menunggu aksi selesai, 8b butir 8).
- Expected 410 butir a dipecah: langkah 19 (36 entri, 4 halaman) dan langkah 20 (entri Edit Port ditambahkan). Butir b dipecah di langkah 22 dan 24; butir c di langkah 26 dan 28; butir d di langkah 30 dan 32.
- Post Condition TC 410 (pemulihan Port dan entri oleh automation baseline) tanpa langkah observasi di TC: tidak diasersi; dilakukan fixture BE di `after`.
- Temuan untuk QA:
  - S-12: TC menetapkan jumlah absolut (35 dan 36 entri) pada audit trail permanen; spec mengikuti TC dan bergantung pada keadaan awal yang dijamin fixture BE. Pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-14: langkah 20 mengandalkan bahwa entri baru berada di baris pertama urutan default Newest First; TC tidak menyatakannya secara eksplisit.
  - TC 410 langkah 5, 7, 9 menyebut "perhatikan halaman 1" setelah sort tanpa menyatakan apakah sort mereset halaman; spec mengikuti TC.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
