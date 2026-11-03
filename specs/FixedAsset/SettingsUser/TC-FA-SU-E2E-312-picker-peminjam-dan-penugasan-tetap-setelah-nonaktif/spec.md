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
6. Verifikasi picker PIC tidak memuat Gita Permata {runId}-312 (nonaktif di FAMS) maupun Rudi Hartono {runId}-312 (nonaktif di Global Settings)
7. Tutup picker dan form tanpa menyimpan, lalu buka form Borrow dan buka picker peminjam
8. Verifikasi picker peminjam memuat sedikitnya satu pengguna aktif efektif lain (pembanding)
9. Verifikasi picker peminjam tidak memuat Gita Permata {runId}-312 maupun Rudi Hartono {runId}-312
10. Tutup picker dan form tanpa menyimpan, lalu buka Fixed Asset > Settings > User dan Search `Gita Permata {runId}-312`, tekan Enter
11. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Activate]` pada dialog `Activate User`
12. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke ON), lalu buka form pendaftaran aset dan picker PIC
13. Verifikasi picker PIC memuat Gita Permata {runId}-312
14. Tutup picker dan form tanpa menyimpan, lalu buka form Borrow dan picker peminjam
15. Verifikasi picker peminjam memuat Gita Permata {runId}-312
16. Tutup picker dan form tanpa menyimpan

### TC-FA-SU-958: Penonaktifan pengguna tidak menghapus penugasan peran, grup, Transaction Role, dan Home Group

17. Buka Fixed Asset > Settings > User, Search `Gita Permata {runId}-312`, tekan Enter, klik nama Gita Permata {runId}-312, lalu buka Tab Role
18. Catat penugasan Global Role, Group Role, dan Transaction Role Gita Permata {runId}-312 serta kolom Home Group baris Gita Permata {runId}-312
19. Kembali ke User List lewat breadcrumb `User`, Search `Gita Permata {runId}-312`, tekan Enter
20. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Deactivate]` pada dialog `Deactivate User`
21. Tunggu aksi selesai, lalu klik nama Gita Permata {runId}-312 dan buka Tab Role
22. Verifikasi Tab Role Gita Permata {runId}-312 menampilkan penugasan yang sama dengan catatan
23. Kembali ke User List lewat breadcrumb `User`, Search `Gita Permata {runId}-312`, tekan Enter
24. Verifikasi kolom Home Group baris Gita Permata {runId}-312 tidak berubah dari catatan
25. Klik sakelar Active pada baris Gita Permata {runId}-312, lalu klik `[Activate]` pada dialog `Activate User`
26. Tunggu aksi selesai, lalu klik nama Gita Permata {runId}-312 dan buka Tab Role
27. Verifikasi Tab Role Gita Permata {runId}-312 menampilkan penugasan yang sama dengan catatan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 3, 4, 7, 10, 12, 14, 16, 17, 19, 21, 23, 26; langkah baseline jumlah entri (S-12): 18. Langkah 1, 10, 17, 19, dan 23 juga Search untuk menemukan baris target (R-16).
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-312` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-957 butir a menyebut tiga kategori pengguna yang tidak muncul (nonaktif di FAMS, nonaktif di Global Settings, tanpa App Access FAMS) dan tiga picker (PIC, peminjam, approver), tetapi Langkah Uji hanya menonaktifkan Gita Permata dan membuka picker PIC dan peminjam. Spec mengasersi kategori nonaktif di FAMS (Gita Permata) dan nonaktif di Global Settings (Rudi Hartono, Pre-setup #38) pada picker PIC dan peminjam; kategori tanpa App Access FAMS dan picker approver tidak diasersi karena tidak ada langkah dan data pembukanya.
  - TC-FA-SU-957 tidak menyebut jalur menu atau nama field picker pada pendaftaran aset dan Borrow; ditentukan di Page Object. TC-FA-SU-957 "ulangi" sesudah Activate ditulis sebagai pembukaan ulang kedua picker.
  - TC-FA-SU-958 tidak menyebut daftar penugasan yang dicatat; spec mencatat penugasan yang tampil di Tab Role sebelum Deactivate. Kolom Home Group dicatat dari User List.
