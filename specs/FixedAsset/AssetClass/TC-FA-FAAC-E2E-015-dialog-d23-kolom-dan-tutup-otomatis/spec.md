---
id: TC-FA-FAAC-E2E-015-dialog-d23-kolom-dan-tutup-otomatis
title: "Dialog Asset Names Without Asset Class: Sembunyikan dan Tampilkan Kolom, serta Menutup Sendiri Saat Jumlah Menjadi 0"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-278
  - TC-FA-FAAC-279
coverage:
  web: automated
---

# Dialog Asset Names Without Asset Class: Sembunyikan dan Tampilkan Kolom, serta Menutup Sendiri Saat Jumlah Menjadi 0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state global, keanggotaan Asset Name tanpa Asset Class): hook `before` mengatur lewat fixture BE tepat tiga Asset Name tanpa Asset Class: Forklift 3T (Machinery > Warehouse; 6 aset aktif), Laptop Standard (IT > Devices; 120 aset aktif), Crane Rental Unit (Machinery > Rented; 0 aset aktif) (TC-FA-FAAC-278). Untuk TC-FA-FAAC-279 spec mengatur lewat fixture BE tepat satu Asset Name tanpa Asset Class: `Crane Rental Unit`; Asset Class tujuan assign adalah `Machinery` (Class Code MACHINERY, Pre-setup). Hook `after` memulihkan keanggotaan Asset Name ke keadaan awal run. Seed disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: sesi API aktor sebagai pelaku kedua yang hanya memicu perubahan state (TC-FA-FAAC-279; akun dengan hak Update, dinyatakan di `suite.md`), serta fixture BE untuk mengatur dan memulihkan keanggotaan Asset Name; disediakan tim FE/BE.
- Jeda "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 19) adalah pilihan spec sebagai jendela perambatan perubahan antar-sesi, bukan nilai TC atau PRD.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah keanggotaan Asset Name tanpa Asset Class yang dipakai bersama.

## Test Steps

### TC-FA-FAAC-278: Menyembunyikan dan menampilkan kolom pada tabel dialog D-23

1. Klik link `[View asset names]` pada banner
2. Klik ikon ⋯ pada header kolom Actions
3. Hilangkan centang `Category`
4. Verifikasi kolom Category hilang dari tabel
5. Hilangkan centang `Assets`
6. Verifikasi kolom Assets hilang dari tabel
7. Hilangkan centang `Asset Name` (kolom terakhir yang visible)
8. Verifikasi centang `Asset Name` tidak dapat dihilangkan
9. Verifikasi tooltip `At least one column must remain visible.`
10. Centang kembali `Category` dan `Assets`
11. Verifikasi kolom Category dan Assets tampil lagi
12. Klik `[Close]` untuk menutup dialog

### TC-FA-FAAC-279: Dialog menutup sendiri saat jumlah Asset Name tanpa Asset Class menjadi 0

13. Atur Asset Name tanpa Asset Class menjadi tepat satu (`Crane Rental Unit`) lewat fixture BE hingga tersimpan
14. Refresh halaman
15. Klik tab Asset Class
16. Klik link `[View asset names]` pada banner
17. Verifikasi dialog `Asset Names Without Asset Class` terbuka dengan baris `Crane Rental Unit`
18. Assign `Crane Rental Unit` ke Asset Class `Machinery` lewat sesi API aktor hingga assign tersimpan
19. Tunggu 5 detik tanpa memuat ulang halaman
20. Verifikasi dialog D-23 menutup sendiri
21. Verifikasi tidak ada toast
22. Verifikasi banner Asset Name tanpa Asset Class Hidden

## Notes

- Langkah penghubung (S-03): langkah 12 (menutup dialog), langkah 13 sampai 15 (mengatur keanggotaan Asset Name lewat fixture BE sebagai precondition TC-FA-FAAC-279 dan memuat ulang tab), langkah 19 (jendela perambatan perubahan antar-sesi).
- Langkah 18 memicu perubahan state lewat sesi API aktor (R-20; rujukan butir "Sesi API aktor" di `suite.md`). Pelaku kedua tidak membuka sesi UI karena hasil di sesi itu tidak diasersi.
- Assign `Crane Rental Unit` ke Asset Class Pre-setup `Machinery` mengubah keanggotaan Asset Name tetapi tidak mengubah data Asset Class; pemulihannya dijamin fixture BE di hook `after` (S-06).
- Urutan TC dalam spec: 278, 279. TC-FA-FAAC-279 di akhir karena mengubah keanggotaan.
- Anchor absence: langkah 20 (dialog menutup) mendahului absence toast pada langkah 21 dan banner pada langkah 22 (8b butir 2 dan 11); langkah 17 membuktikan dialog sempat tampil (8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-279 menyebut "tunggu pembaruan" tanpa mekanisme (SSE, polling) maupun durasi; spec memakai jendela 5 detik tanpa memuat ulang halaman.
  - TC-FA-FAAC-279 precondition menyebut "sesi kedua memiliki hak Update" tanpa akun; spec menulisnya sebagai sesi API aktor yang disediakan tim FE/BE (S-13).
  - TC-FA-FAAC-278 langkah 3 ("Hilangkan centang Asset Name (kolom terakhir yang visible)") berbunyi sama dengan Expected; spec memisahkan aksi (langkah 7) dari asersinya (langkah 8 dan 9).
