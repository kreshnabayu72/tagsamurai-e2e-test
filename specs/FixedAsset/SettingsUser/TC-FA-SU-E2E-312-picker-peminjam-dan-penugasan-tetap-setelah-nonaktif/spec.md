---
id: TC-FA-SU-E2E-312-picker-peminjam-dan-penugasan-tetap-setelah-nonaktif
title: "Picker PIC dan Peminjam serta Penugasan Tetap Setelah Nonaktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-957
  - TC-FA-SU-958
coverage:
  web: automated
---

# Picker PIC dan Peminjam serta Penugasan Tetap Setelah Nonaktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Global Settings (#38). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Gita Permata {runId}-312`, email `gita.permata+{runId}-312@qwertysystem.net`: Active; Global Role Import Data dan Manage accounting; Group Role Manage group pada Finance & Accounting; Home Group Finance & Accounting; tanpa Transaction Role.
  - `Rudi Hartono {runId}-312`, email `rudi.hartono+{runId}-312@qwertysystem.net`: sakelar FAMS ON dan nonaktif di Global Settings (Inactive efektif).
- Kemampuan membuka picker PIC pada form pendaftaran aset dan picker peminjam pada form Borrow (modul Asset Registration dan Borrow), tanpa menyimpan form; jalur menu dan nama field picker tidak ditentukan TC (lihat Temuan untuk QA).
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-957: Picker PIC dan peminjam di modul transaksi hanya menampilkan pengguna dengan status aktif efektif

1. Ketik Search `Gita Permata {runId}-312`, tekan Enter
2. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Deactivate]` pada dialog `Deactivate User`
3. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke OFF)
4. Buka form pendaftaran aset lalu buka picker PIC
5. Verifikasi picker PIC memuat sedikitnya satu pengguna aktif efektif lain (pembanding)
6. Ketik Search `Gita Permata {runId}-312` pada picker PIC, tekan Enter
7. Verifikasi picker PIC tidak memuat Gita Permata {runId}-312 (nonaktif di FAMS)
8. Ganti isi kotak search picker PIC dengan `Rudi Hartono {runId}-312`, tekan Enter
9. Verifikasi picker PIC tidak memuat Rudi Hartono {runId}-312 (nonaktif di Global Settings)
10. Tutup picker dan form tanpa menyimpan, lalu buka form Borrow dan buka picker peminjam
11. Verifikasi picker peminjam memuat sedikitnya satu pengguna aktif efektif lain (pembanding)
12. Ketik Search `Gita Permata {runId}-312` pada picker peminjam, tekan Enter
13. Verifikasi picker peminjam tidak memuat Gita Permata {runId}-312
14. Ganti isi kotak search picker peminjam dengan `Rudi Hartono {runId}-312`, tekan Enter
15. Verifikasi picker peminjam tidak memuat Rudi Hartono {runId}-312
16. Tutup picker dan form tanpa menyimpan, lalu buka Fixed Asset > Settings > User dan Search `Gita Permata {runId}-312`, tekan Enter
17. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Activate]` pada dialog `Activate User`
18. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke ON), lalu buka form pendaftaran aset dan picker PIC
19. Ketik Search `Gita Permata {runId}-312` pada picker PIC, tekan Enter
20. Verifikasi picker PIC memuat Gita Permata {runId}-312
21. Tutup picker dan form tanpa menyimpan, lalu buka form Borrow dan picker peminjam
22. Ketik Search `Gita Permata {runId}-312` pada picker peminjam, tekan Enter
23. Verifikasi picker peminjam memuat Gita Permata {runId}-312
24. Tutup picker dan form tanpa menyimpan

### TC-FA-SU-958: Penonaktifan pengguna tidak menghapus penugasan peran, grup, Transaction Role, dan Home Group

25. Buka Fixed Asset > Settings > User, Search `Gita Permata {runId}-312`, tekan Enter, klik nama Gita Permata {runId}-312, lalu buka Tab Role
26. Catat penugasan Global Role, Group Role, dan Transaction Role Gita Permata {runId}-312 serta kolom Home Group baris Gita Permata {runId}-312
27. Kembali ke User List lewat breadcrumb `User`, Search `Gita Permata {runId}-312`, tekan Enter
28. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Deactivate]` pada dialog `Deactivate User`
29. Tunggu aksi selesai, lalu klik nama Gita Permata {runId}-312 dan buka Tab Role
30. Verifikasi Tab Role Gita Permata {runId}-312 menampilkan penugasan yang sama dengan catatan
31. Kembali ke User List lewat breadcrumb `User`, Search `Gita Permata {runId}-312`, tekan Enter
32. Verifikasi kolom Home Group baris Gita Permata {runId}-312 tidak berubah dari catatan
33. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Activate]` pada dialog `Activate User`
34. Tunggu aksi selesai, lalu klik nama Gita Permata {runId}-312 dan buka Tab Role
35. Verifikasi Tab Role Gita Permata {runId}-312 menampilkan penugasan yang sama dengan catatan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 19, 21, 22, 24, 25, 27, 29, 31, 34; langkah baseline jumlah entri (S-12): 26. Langkah 1, 16, 25, 27, dan 31 juga Search untuk menemukan baris target (R-16).
- Presence dan absence di picker PIC dan peminjam (Table User Picker berpaginasi) ditemukan lewat Search nama bersuffix pada kotak search picker (langkah 6, 8, 12, 14, 19, 22; R-22), sehingga asersi tidak bergantung pada halaman pertama picker; pembanding aktif efektif pada langkah 5 dan 11 mendahului asersi absence, dan Search Gita Permata {runId}-312 yang sama menemukan baris pada langkah 19 dan 22 sesudah Activate.
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-312` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-957 butir a menyebut tiga kategori pengguna yang tidak muncul (nonaktif di FAMS, nonaktif di Global Settings, tanpa App Access FAMS) dan tiga picker (PIC, peminjam, approver), tetapi Langkah Uji hanya menonaktifkan Gita Permata dan membuka picker PIC dan peminjam. Spec mengasersi kategori nonaktif di FAMS (Gita Permata) dan nonaktif di Global Settings (Rudi Hartono, Pre-setup #38) pada picker PIC dan peminjam; kategori tanpa App Access FAMS dan picker approver tidak diasersi karena tidak ada langkah dan data pembukanya.
  - TC-FA-SU-957 tidak menyebut jalur menu atau nama field picker pada pendaftaran aset dan Borrow; ditentukan di Page Object. TC-FA-SU-957 "ulangi" sesudah Activate ditulis sebagai pembukaan ulang kedua picker.
  - TC-FA-SU-958 tidak menyebut daftar penugasan yang dicatat; spec mencatat penugasan yang tampil di Tab Role sebelum Deactivate. Kolom Home Group dicatat dari User List.
