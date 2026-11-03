---
id: TC-AC-LCS-E2E-111-pagination-modal-changelog-default-dan-navigasi
title: "Pagination Modal Changelog: Ukuran Halaman Default, Navigasi, dan Penggantian Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-432
  - TC-AC-LCS-433
  - TC-AC-LCS-434
coverage:
  web: automated
---

# Pagination Modal Changelog: Ukuran Halaman Default, Navigasi, dan Penggantian Page Size

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Pengecualian A-15: Fixture BE menyediakan kemampuan overwrite dan clear riwayat Changelog per tab (disediakan tim FE/BE, idempotent); total absolut Changelog (footer `1-N of N`, jumlah baris, empty state) diasersi pada riwayat yang dibentuk di hook `before` spec ini dan dikembalikan di hook `after` suite; suite berjalan serial (`parallel: false`).
- Data uji mengacu ke berkas `fixtures/lifecycle-settings.json` (`Fixture.lifecycleSettings`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-432: Default 10 baris per halaman dan pilihan page size 10, 25, 50, 100

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Verifikasi footer `1–10 of 27`
4. Verifikasi tabel menampilkan 10 baris
5. Buka pilihan page size
6. Verifikasi pilihan page size: 10, 25, 50, 100
7. Verifikasi tidak ada opsi "All"
8. Tutup pilihan page size dengan memilih `10`

### TC-AC-LCS-433: Navigasi halaman next, previous, dan input nomor halaman; input tidak valid diabaikan

9. Klik next
10. Verifikasi footer `11–20 of 27`
11. Klik next lagi
12. Verifikasi footer `21–27 of 27`
13. Verifikasi tabel menampilkan 7 baris
14. Klik previous
15. Verifikasi footer `11–20 of 27`
16. Ketik `3` pada input nomor halaman, tekan Enter
17. Verifikasi footer `21–27 of 27`
18. Ketik `0` pada input nomor halaman, tekan Enter
19. Verifikasi input `0` diabaikan dan tabel tetap di halaman 3 (`21–27 of 27`)
20. Ketik `4` pada input nomor halaman, tekan Enter
21. Verifikasi input `4` diabaikan dan tabel tetap di halaman 3 (`21–27 of 27`)
22. Ketik `abc` pada input nomor halaman, tekan Enter
23. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 3 (`21–27 of 27`)

### TC-AC-LCS-434: Mengganti page size ke 25 kembali ke halaman 1 dengan 25 baris

24. Ketik `1` pada input nomor halaman, tekan Enter
25. Klik next ke halaman 2
26. Ubah page size menjadi 25
27. Verifikasi footer `1–25 of 27`
28. Verifikasi tabel menampilkan 25 baris di halaman 1

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (membuka tab Client Lifecycle, karena hook `beforeEach` membuka tab Trial Settings); menutup pilihan page size dengan memilih `10` (nilai default tidak berubah) dan mengetik `1` pada input nomor halaman (kembali ke halaman 1 sebelum TC-AC-LCS-434, S-09).
- Asersi footer dan jumlah baris memakai Dataset L hasil seeding.
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
