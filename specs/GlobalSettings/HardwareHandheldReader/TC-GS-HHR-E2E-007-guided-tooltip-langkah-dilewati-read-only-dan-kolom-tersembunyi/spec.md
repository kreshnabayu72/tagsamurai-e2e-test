---
id: TC-GS-HHR-E2E-007-guided-tooltip-langkah-dilewati-read-only-dan-kolom-tersembunyi
title: "Guided Tooltip Halaman Handheld Reader: Step 3 Dilewati saat Kolom Device Name Disembunyikan dan Step 2 Dilewati untuk Read Only"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-31
  - TC-GS-HHR-32
coverage:
  web: automated
---

# Guided Tooltip Halaman Handheld Reader: Step 3 Dilewati saat Kolom Device Name Disembunyikan dan Step 2 Dilewati untuk Read Only

## Prerequisites

- Mode: FE+BE (backend nyata). Suite `parallel: false`.
- Akun aktor:
  - Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A) untuk TC-GS-HHR-32. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Read Only (Maya Putri) `readOnly_automated_qaTeam1@qwertysystem.net` (Pre-setup 2, Client A) untuk TC-GS-HHR-31: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_RO_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Hardware > Handheld Reader untuk akun Total Control dengan flag Guided Tooltip akun itu bernilai seen (lihat bawah) sehingga walkthrough tidak menutupi Overlay Column Visibility dan Setup Column pada langkah 1 sampai 4. Kunjungan yang memicu auto-open (langkah 7 dan 18) ditulis di `## Test Steps`.
- Guided Tooltip (page_key `gs-handheld-reader`): spec ini menguji flag `guided_tooltip_seen_gs-handheld-reader` sendiri sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`) untuk TC-GS-HHR-31 dan 32 sendiri. Hook `before` mencatat nilai awal flag akun Total Control dan akun Read Only, menyetel flag akun Total Control ke true (agar langkah 1 sampai 4 berjalan tanpa walkthrough), dan mereset flag akun Read Only ke belum ada (precondition "flag belum diset" TC-GS-HHR-31). Flag akun Total Control di-reset ke belum ada pada langkah 6 (precondition TC-GS-HHR-32). Hook `after` memulihkan nilai awal kedua flag. Mekanisme baca, reset, penyetelan, dan pemulihan flag disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Data Pre-setup (Client A, plan Growth, General Settings `dd/MM/yy` 24-hour): Seed Reader A (DD-01 s.d. DD-10) dipulihkan fixture backend (disediakan tim FE) sebelum spec berjalan; spec tidak membaca atau mengubah isi baris. Data Dinamis: tidak ada.
- Kemampuan teknis: Overlay Column Visibility dan Setup Column (modal dengan `[Reset to Default]` dan `[Save]`); pembacaan spotlight dan tombol tooltip; ganti akun (logout lalu login).
- State global yang diubah: visibilitas kolom `Device Name` tabel daftar reader akun Total Control (disembunyikan lewat Setup Column di langkah 3 dan 4, dipulihkan di langkah 14 dan 15; hook `after` memulihkannya sebagai cadangan), flag Guided Tooltip kedua akun (dipulihkan seperti di atas), dan sesi akun (dipulihkan hook `after`).

## Test Steps

### TC-GS-HHR-32: Step 3 dilewati saat kolom Device Name disembunyikan lewat Setup Column

1. Klik header kolom `Actions (⋯)` untuk membuka Overlay Column Visibility
2. Klik item `Setup Column...`
3. Hapus centang `Device Name`
4. Klik `[Save]`
5. Tunggu aksi selesai (popup Setup Column tertutup)
6. Reset flag `guided_tooltip_seen_gs-handheld-reader` akun Total Control ke belum ada
7. Buka Global Settings > Hardware > Handheld Reader lewat address bar
8. Klik `[Next]` pada Step 1
9. Verifikasi tombol pada Step 2 berupa `[Done]`
10. Verifikasi tombol pada Step 2 bukan `[Next]`
11. Klik `[Done]` pada Step 2
12. Verifikasi Step 3 tidak tampil
13. Verifikasi walkthrough selesai setelah Step 2
14. Klik header kolom `Actions (⋯)` untuk membuka Overlay Column Visibility, lalu klik item `Setup Column...`
15. Centang `Device Name`, lalu klik `[Save]`

### TC-GS-HHR-31: Step 2 dilewati untuk Read Only karena tombol Activate Hidden

16. Ganti akun: logout dari akun Total Control
17. Login sebagai Read Only dengan `Spectra.env.GS_RO_PASSWORD`
18. Buka Global Settings > Hardware > Handheld Reader lewat address bar
19. Verifikasi Step 1 tampil dengan judul `License Counter`
20. Klik `[Next]` pada Step 1
21. Verifikasi walkthrough berpindah langsung ke Step 3 dengan judul `Reader Detail`
22. Verifikasi Step `Add Hardware` tidak tampil
23. Klik `[Done]` untuk menutup walkthrough

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 32, 31. TC-GS-HHR-32 memakai akun Total Control (akun default suite) dan mengubah visibilitas kolom, lalu memulihkannya sebelum ganti akun; TC-GS-HHR-31 ditaruh terakhir karena butuh ganti akun ke Read Only (langkah 16 dan 17). Urutan ini menyimpang dari urutan TC sumber (31, 32) demi satu sesi akun sebelum ganti akun. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras, karena hook `before` mereset flag akun Read Only sendiri dan Read Only tidak bergantung pada visibilitas kolom akun Total Control.
- TC-GS-HHR-32 precondition d menyembunyikan kolom `Device Name` sebelum kunjungan yang memicu auto-open; urutan langkah 1 sampai 7 memenuhinya: kolom disembunyikan saat flag seen true (tanpa walkthrough), lalu flag di-reset (langkah 6), lalu halaman dibuka lewat address bar (langkah 7). Tidak ada `Verifikasi` untuk kolom `Device Name` hilang karena itu precondition, bukan Expected TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (menyembunyikan `Device Name` lewat Setup Column), langkah 5 (Tunggu aksi selesai, `[Save]` Setup Column adalah aksi sisi klien), langkah 6 (reset flag), langkah 7 dan 18 (membuka halaman lewat address bar sebagai pemicu auto-open), langkah 14 dan 15 (memulihkan visibilitas `Device Name`), langkah 16 dan 17 (ganti akun), dan langkah 23 (tutup walkthrough).
- Langkah 12 (absence Step 3) didahului langkah 9 dan 10 (Step 2 tampil dengan `[Done]`) dan langkah 22 (absence Step `Add Hardware`) didahului langkah 19 dan 21 (Step 1 dan Step 3 tampil) sebagai anchor positif absence (konvensi bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-HHR-32 tidak menyebut cara menyembunyikan kolom `Device Name` selain "lewat Setup Column"; spec memakai item `Setup Column...` pada Overlay Column Visibility, hapus centang `Device Name`, lalu `[Save]` (TC-GS-HHR-278).
  - TC-GS-HHR-31 dan 32 mensyaratkan flag belum diset tanpa menyebut cara mereset; mekanismenya disediakan tim FE/BE.
  - TC-GS-HHR-32 Expected a tidak menyebut Step 1 dan 2; spec tidak mengasersi judul Step 1 dan Step 2 pada TC-GS-HHR-32.
