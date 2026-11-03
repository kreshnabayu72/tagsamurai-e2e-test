---
id: TC-AC-LCS-E2E-108-sort-modal-changelog-nilai-modified-by-dan-perpindahan
title: "Sort Modal Changelog: Old Value, New Value, Modified By, dan Perpindahan Kolom Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-403
  - TC-AC-LCS-404
  - TC-AC-LCS-405
  - TC-AC-LCS-406
coverage:
  web: automated
---

# Sort Modal Changelog: Old Value, New Value, Modified By, dan Perpindahan Kolom Sort

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

### TC-AC-LCS-403: Sort kolom Old Value numerik menaik lalu menurun

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Klik header `Old Value` satu kali
4. Verifikasi menaik baris 1 bernilai Old Value `5` (entri 1 May 26)
5. Klik header `Old Value` kedua kali
6. Verifikasi menurun baris 1 bernilai Old Value `135` (entri 27 May 26)
7. Klik header `Old Value` ketiga kali (kembali netral)

### TC-AC-LCS-404: Sort kolom New Value numerik menaik lalu menurun

8. Klik header `New Value` satu kali
9. Verifikasi menaik baris 1 bernilai New Value `8` (entri 1 May 26)
10. Klik header `New Value` kedua kali
11. Verifikasi menurun baris 1 bernilai New Value `138` (entri 27 May 26)
12. Klik header `New Value` ketiga kali (kembali netral)

### TC-AC-LCS-405: Sort kolom Modified By berdasarkan nama lengkap bukan format singkat

13. Klik header `Modified By` satu kali
14. Verifikasi A–Z nama lengkap baris 1 bernilai Modified By `Budi S`
15. Klik header `Modified By` kedua kali
16. Verifikasi Z–A nama lengkap baris 1 bernilai Modified By `Sarah T`
17. Klik header `Modified By` ketiga kali (kembali netral)

### TC-AC-LCS-406: Berpindah kolom sort mereset kolom sebelumnya dan memulai dari klik pertama; sort tidak mereset Search

18. Ketik Search `Edit`, tekan Enter
19. Klik header `Date` satu kali (Oldest First)
20. Klik header `Field` satu kali
21. Verifikasi indikator sort `Date` non-aktif
22. Verifikasi indikator sort `Field` aktif menaik (A–Z)
23. Verifikasi kata kunci Search `Edit` tetap aktif
24. Verifikasi footer tetap `1–10 of 27`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (membuka tab Client Lifecycle, karena hook `beforeEach` membuka tab Trial Settings); klik ketiga pada header kembali ke netral sebelum TC berikutnya (S-09).
- Asersi sort memakai Dataset L yang punya banyak nilai distinct pada tiap kolom (S-11).
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
