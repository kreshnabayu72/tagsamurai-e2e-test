---
id: TC-FA-RP-E2E-087-volume-data-company-volume-seleksi-bulk-selection-limit-dan-1
title: "Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (1/4)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-286
  - TC-FA-RP-287
  - TC-FA-RP-288
coverage:
  web: automated
---

# Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (1/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control `Company Volume` (Pre-setup #23, `Total Control Volume`), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_VOLUME_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_VOLUME_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #23 `Company Volume`: 120 pengguna Active Activated (`Bulk User 1` sampai `Bulk User 120`), Total Control `Total Control Volume`, dan 120 penugasan Global Role `Import data` (seeding volume besar disediakan tim FE/BE). Selection Limit pada nilai default (tidak diubah spec ini).
- State yang diubah spec ini: tidak ada (hanya seleksi sisi klien; tidak ada Remove yang dikonfirmasi).

## Test Steps

### TC-FA-RP-286: Bulk Action Bar muncul saat baris dicentang dengan counter dan satu aksi Remove

1. Klik Tab `System`, klik Role Name `Import data` pada section Global Role
2. Centang satu baris
3. Verifikasi bar menampilkan `Bulk Action`, `1 User selected`, dan `Select All (120 records)`, serta `(✕)` paling kanan
4. Centang baris kedua
5. Verifikasi counter `2 Users selected`
6. Klik `Bulk Action`
7. Verifikasi menu hanya memuat satu aksi `Remove` (severity danger)
8. Tutup menu `Bulk Action` dengan `Esc`
9. Hapus centang satu baris
10. Verifikasi counter `1 User selected`
11. Klik ikon `(✕)` pada bar
12. Verifikasi seluruh seleksi dibatalkan
13. Verifikasi bar tertutup

### TC-FA-RP-287: Checkbox header: pilih halaman, hapus pilihan, dan status indeterminate

14. Centang satu baris
15. Verifikasi checkbox header berstatus indeterminate
16. Verifikasi counter `1 User selected`
17. Klik checkbox header
18. Verifikasi seluruh baris halaman aktif tercentang
19. Verifikasi counter `10 Users selected`
20. Klik checkbox header lagi
21. Verifikasi seluruh baris tidak tercentang
22. Verifikasi bar hilang

### TC-FA-RP-288: Select All (N records) memilih lintas halaman lalu berubah menjadi Unselect All

23. Centang satu baris, lalu klik `Select All (120 records)`
24. Verifikasi counter menunjukkan total 120
25. Verifikasi tombol berubah menjadi `Unselect All`
26. Pindah ke halaman 2
27. Verifikasi baris halaman 2 tercentang
28. Klik `Unselect All`
29. Verifikasi seluruh seleksi lintas halaman dibatalkan
30. Verifikasi bar tertutup
31. Centang satu baris, klik `Select All (120 records)`, lalu hapus centang satu baris
32. Verifikasi bar tetap tampil
33. Verifikasi tombol kembali `Select All (119 records)`
34. Klik ikon `(✕)` pada bar untuk membatalkan seluruh seleksi

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-286, TC-FA-RP-287, TC-FA-RP-288).
- Kelas e (volume data, bagian 3 prinsip 13e): ambang 120 baris. Seluruh data milik Pre-setup #23 hanya dibaca.
- Langkah penghubung (S-03): membuka Tab System dan Detail Role; menutup menu `Bulk Action` dengan `Esc` (langkah 8, antara klik `Bulk Action` dan hapus centang); membatalkan seleksi (langkah 34) sebagai pembersih state (S-09).
- Temuan untuk QA:
  - TC-FA-RP-286, TC-FA-RP-287, dan TC-FA-RP-288 tidak menyebut Detail Role yang diuji selain `Import data` pada Company Volume; Select All (120 records) memakai penugasan Pre-setup #23.
  - Akun Total Control `Company Volume` tidak tertulis di Pre-setup TC (hanya "Total Control Volume"); dicatat "disediakan tim FE" (S-11).
