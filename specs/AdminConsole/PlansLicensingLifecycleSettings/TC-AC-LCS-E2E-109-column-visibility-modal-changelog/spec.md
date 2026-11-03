---
id: TC-AC-LCS-E2E-109-column-visibility-modal-changelog
title: "Column Visibility Modal Changelog: Screening Overlay, Perubahan Langsung, dan Guard Kolom Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-407
  - TC-AC-LCS-408
  - TC-AC-LCS-409
coverage:
  web: automated
---

# Column Visibility Modal Changelog: Screening Overlay, Perubahan Langsung, dan Guard Kolom Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Preferensi kolom modal Changelog (Column Visibility dan Setup Column) yang tersimpan di browser dihapus di hook `after` (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-407: Screening overlay Column Visibility modal Changelog

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Hover header kolom `(⋯)`
3. Verifikasi tooltip "Column Visibility" tampil
4. Klik header `(⋯)`
5. Susuri overlay Column Visibility
6. Verifikasi overlay berisi daftar berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
7. Verifikasi checkbox seluruh item dalam daftar tercentang
8. Verifikasi checkbox seluruh item dalam daftar enabled
9. Verifikasi seluruh item dalam daftar memiliki drag handle
10. Verifikasi item "Setup Column..." tampil di bagian bawah overlay

### TC-AC-LCS-408: Perubahan di overlay Column Visibility langsung diterapkan tanpa tombol Save

11. Uncheck `Old Value`
12. Verifikasi kolom `Old Value` hilang dari tabel seketika
13. Tarik `Modified By` ke posisi paling atas daftar
14. Verifikasi kolom `Modified By` menjadi kolom pertama tabel
15. Verifikasi tidak ada tombol Save pada overlay
16. Hapus preferensi kolom modal Changelog di browser
17. Tutup modal dengan `[✕]`
18. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle

### TC-AC-LCS-409: Guard kolom visible terakhir: checkbox tidak dapat di-uncheck saat tersisa satu kolom

19. Klik header `(⋯)`
20. Uncheck `Date`, `Action`, `Field`, `Old Value`, `New Value`
21. Hover checkbox `Modified By`
22. Verifikasi checkbox `Modified By` disabled
23. Verifikasi tooltip "At least one column must remain visible." tampil
24. Coba uncheck `Modified By`
25. Verifikasi checkbox `Modified By` tetap tercentang
26. Verifikasi kolom `Modified By` tetap tampil

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 'Hapus preferensi kolom', menutup modal, dan membuka modal kembali antara TC-AC-LCS-408 dan TC-AC-LCS-409 mengembalikan konfigurasi kolom ke default sebelum TC berikutnya (S-09); hook `after` menghapus preferensi kolom sebagai cadangan.
- Konfigurasi kolom hasil TC-AC-LCS-408 tersimpan di cache browser (Post Condition TC).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-408 ("Konfigurasi kolom tersimpan di cache browser") tidak punya langkah observasi di TC dan tidak diasersi; Expected TC hanya menyebut perubahan langsung pada tabel.
  - Post Condition TC-AC-LCS-407 dan TC-AC-LCS-409 ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
