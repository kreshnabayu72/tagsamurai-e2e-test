---
id: TC-FA-FAAC-E2E-016-aksesibilitas-keyboard-dan-fokus
title: "Aksesibilitas Tab Asset Class: Navigasi Keyboard, Esc Menutup Modal, Fokus Terkunci di Modal Changelog, dan Tab Detail dengan Tombol Panah"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-36
  - TC-FA-FAAC-37
  - TC-FA-FAAC-38
  - TC-FA-FAAC-39
coverage:
  web: automated
---

# Aksesibilitas Tab Asset Class: Navigasi Keyboard, Esc Menutup Modal, Fokus Terkunci di Modal Changelog, dan Tab Detail dengan Tombol Panah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Seed disediakan tim FE/BE (lihat `suite.md`).
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Spec ini tidak menyimpan perubahan: seleksi baris dibatalkan, modal Setup Column ditutup tanpa Save, dan tidak ada field Detail yang diubah.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-36: Navigasi keyboard Tab, Enter, dan Space pada tabel Asset Class

1. Tekan Tab berulang kali dari awal halaman hingga fokus mencapai tab bar, toolbar, checkbox baris, dan Class Code
2. Verifikasi fokus berpindah antar elemen interaktif mengikuti urutan Tab (tab bar, toolbar, checkbox baris, Class Code)
3. Ketik Search `HEAVY-EQ`, tekan Enter
4. Fokuskan checkbox baris HEAVY-EQ dengan Tab, lalu tekan Space
5. Verifikasi Space mencentang checkbox baris HEAVY-EQ
6. Tekan Space sekali lagi pada checkbox baris HEAVY-EQ untuk membatalkan centang
7. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
8. Fokuskan icon Search dengan Tab, lalu tekan Enter
9. Verifikasi Enter pada icon Search membuka kotak Search
10. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
11. Fokuskan tab Chart of Accounts dengan Tab, lalu tekan Enter
12. Verifikasi Enter pada tab membuka tab `Chart of Accounts`
13. Klik tab Asset Class

### TC-FA-FAAC-37: Esc menutup modal Changelog dan modal Setup Column

14. Klik icon Changelog
15. Verifikasi modal `Changelog: Asset Class` tampil
16. Tekan Esc
17. Verifikasi modal `Changelog: Asset Class` tertutup
18. Klik ikon ⋯ pada header kolom Actions
19. Klik `Setup Column...`
20. Verifikasi modal `Setup Column` tampil
21. Tekan Esc
22. Verifikasi modal `Setup Column` tertutup tanpa menyimpan perubahan (kolom tabel tidak berubah)

### TC-FA-FAAC-38: Fokus terkunci di dalam modal Changelog

23. Klik icon Changelog
24. Verifikasi modal `Changelog: Asset Class` tampil
25. Tekan Tab berulang kali melebihi jumlah elemen interaktif di modal
26. Verifikasi fokus hanya berputar di antara elemen dalam modal `Changelog: Asset Class` dan tidak keluar ke halaman di belakangnya
27. Tekan Shift+Tab berulang kali
28. Verifikasi fokus tetap berputar di antara elemen dalam modal dan tidak keluar ke halaman di belakangnya
29. Tekan Esc untuk menutup modal

### TC-FA-FAAC-39: Tab Detail dapat dioperasikan dengan tombol panah

30. Ketik Search `HEAVY-EQ`, tekan Enter
31. Klik link Class Code `HEAVY-EQ` untuk membuka Detail
32. Fokuskan tab General
33. Tekan panah kanan
34. Verifikasi fokus pindah ke tab `Depreciation`
35. Tekan panah kiri
36. Verifikasi fokus kembali ke tab `General`
37. Klik breadcrumb `Asset Class`
38. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Spec melewati sekitar 35 langkah (38 langkah): keempat blok adalah satu kelas (aksesibilitas keyboard dan fokus) pada layar dan dataset Pre-setup yang sama tanpa mengubah data, tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login dan hook.
- Langkah penghubung (S-03): langkah 3 dan 30 (Search untuk menemukan baris target karena HEAVY-EQ tidak dijamin berada di halaman 1; R-16), langkah 6 (membatalkan centang agar seleksi tidak terbawa, S-09), langkah 7, 10, dan 38 (mengosongkan Search; R-16), langkah 13 (kembali ke tab Asset Class), langkah 29 (menutup modal), langkah 37 (kembali ke daftar).
- Asersi atas state sementara (fokus, tooltip) ditulis segera sesudah aksi pemicunya (8b butir 5).
- Temuan untuk QA:
  - TC-FA-FAAC-37 butir b ("tanpa menyimpan perubahan") tidak menyebut perubahan yang dibuat sebelum Esc; spec tidak mengubah kolom sebelum Esc dan mengasersi kolom tabel tidak berubah.
  - TC-FA-FAAC-36 langkah 2 mengandaikan checkbox baris HEAVY-EQ sudah difokuskan; spec memfokuskannya dengan Tab pada langkah 4. TC-FA-FAAC-36 tidak memuat langkah Search; spec menambahkannya (langkah 3).
