---
id: TC-AC-LCS-E2E-112-pagination-modal-changelog-reset-halaman-dan-kombinasi
title: "Pagination Modal Changelog: Reset Halaman oleh Search dan Filter, Sort, dan Kombinasi Kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-435
  - TC-AC-LCS-436
  - TC-AC-LCS-437
coverage:
  web: automated
---

# Pagination Modal Changelog: Reset Halaman oleh Search dan Filter, Sort, dan Kombinasi Kontrol

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

### TC-AC-LCS-435: Search dan Apply Filter saat di halaman 3 mereset ke halaman 1

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Pindah ke halaman 3 dengan klik next dua kali
4. Ketik Search `Edit`, tekan Enter
5. Verifikasi footer `1–10 of 27` (halaman 1)
6. Pindah ke halaman 3 dengan klik next dua kali
7. Klik icon Filter, pilih `John Doe` pada `Modified By`, klik `[Apply]`
8. Verifikasi footer `1–9 of 9` (halaman 1)

### TC-AC-LCS-436: Mengganti sort tetap di nomor halaman sekarang

9. Klik `(←)` pada kotak Search
10. Klik `[Clear Field]`, klik `[Apply]`
11. Pindah ke halaman 2 dengan klik next
12. Klik header `Date` satu kali (Oldest First)
13. Verifikasi footer tetap `11–20 of 27`
14. Verifikasi baris pada halaman 2 mengikuti urutan Oldest First dengan baris 1 bertanggal `11 May 26`
15. Klik header `Date` kedua kali
16. Klik header `Date` ketiga kali (kembali netral)

### TC-AC-LCS-437: Search, Filter, Sort, dan page size aktif bersamaan menghasilkan irisan yang benar

17. Ubah page size menjadi 25
18. Ketik Search `Edit`, tekan Enter
19. Pilih rentang `10 May 26` sampai `20 May 26` pada `Date`, klik `[Apply]`
20. Verifikasi footer `1–11 of 11`
21. Verifikasi entri bertanggal `20 May 26` sampai `10 May 26` (urutan Newest First)
22. Klik header `Date` satu kali (Oldest First)
23. Verifikasi urutan menaik `10 May 26` sampai `20 May 26`
24. Verifikasi Search `Edit` tetap aktif
25. Verifikasi filter Date `10 May 26` sampai `20 May 26` tetap aktif
26. Verifikasi page size 25 tetap aktif

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (membuka tab Client Lifecycle, karena hook `beforeEach` membuka tab Trial Settings); klik `(←)` pada kotak Search dan `[Clear Field]` lalu `[Apply]` antara TC-AC-LCS-435 dan TC-AC-LCS-436 membersihkan Search dan Filter; klik ketiga pada header Date mengembalikan sort ke netral sebelum TC-AC-LCS-437 (S-09). Panel Filter tetap terbuka sesudah `[Apply]` (TC-AC-LCS-397 mengamati panel sesudah `[Apply]`), sehingga TC-AC-LCS-437 memilih rentang Date tanpa membuka panel lagi.
- Asersi footer dan urutan memakai Dataset L hasil seeding.
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
