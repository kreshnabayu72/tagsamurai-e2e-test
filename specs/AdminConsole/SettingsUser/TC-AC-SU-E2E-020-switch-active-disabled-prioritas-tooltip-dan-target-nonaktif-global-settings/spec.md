---
id: TC-AC-SU-E2E-020-switch-active-disabled-prioritas-tooltip-dan-target-nonaktif-global-settings
title: "Switch Active Disabled: Tooltip Self pada Detail, Baris Default User, dan Target Nonaktif di Global Settings"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-77
  - TC-AC-SU-98
  - TC-AC-SU-100
  - TC-AC-SU-101
coverage:
  web: automated
---

# Switch Active Disabled: Tooltip Self pada Detail, Baris Default User, dan Target Nonaktif di Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-100 | `Rudi Hartono` | `Rudi Hartono {runId}-020` | `rudihartono+{runId}-020@qwertysystem.net` | switch per-produk ON lalu dinonaktifkan di Global Settings |
| TC-AC-SU-101 | `Rudi Hartono` | `Rudi Hartono T101 {runId}-020` | `rudihartono+{runId}-020-T101@qwertysystem.net` | switch per-produk OFF, nonaktif di Global Settings (diaktifkan kembali di Global Settings oleh spec) |

- Baris Default User (Pre-setup #1) dan baris aktor sendiri dicari lewat Search atas email akun masing-masing; keduanya tidak diubah. Mengaktifkan kembali user di Global Settings (TC-AC-SU-101) dijalankan lewat Fixture BE (disediakan tim FE/BE).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-77: Prioritas tooltip self di atas tier pada target diri sendiri

1. Ketik Search `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
2. Klik Name baris aktor sendiri
3. Klik Tab Role
4. Hover switch Global Role
5. Verifikasi tooltip tunggal `You can't manage your own account from here.`
6. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-98: Switch Active baris Default User Disabled dengan tooltip

7. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
8. Hover switch Active baris Default User
9. Verifikasi switch tampil ON, tetap visible namun disabled (muted, cursor default)
10. Verifikasi tooltip `Default User cannot be modified.`
11. Klik switch tersebut
12. Verifikasi tidak ada dialog

### TC-AC-SU-100: Switch Active target nonaktif di Global Settings, Disabled, posisi terakhir dipertahankan

13. Ganti isi kotak search dengan `Rudi Hartono {runId}-020`, tekan Enter
14. Lihat switch baris `Rudi Hartono {runId}-020`
15. Verifikasi switch tetap tampil ON (posisi terakhir) namun disabled/muted
16. Hover switch
17. Verifikasi tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
18. Klik switch
19. Verifikasi tidak ada dialog

### TC-AC-SU-101: Target diaktifkan kembali di Global Settings, switch interaktif di posisi yang sama

20. Aktifkan kembali `Rudi Hartono T101 {runId}-020` di Global Settings lewat Fixture BE
21. Muat ulang halaman Settings > User dengan F5
22. Ganti isi kotak search dengan `Rudi Hartono T101 {runId}-020`, tekan Enter
23. Amati switch baris `Rudi Hartono T101 {runId}-020`
24. Verifikasi switch kembali enabled di posisi OFF (tidak di-reset ke ON)
25. Klik switch
26. Verifikasi dialog `Activate User` terbuka
27. Klik `[Cancel]` pada dialog `Activate User`
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), langkah 6 (kembali ke daftar), langkah 27 (tutup dialog tanpa mengubah status, S-09), langkah 28 (reset Search).
- Temuan untuk QA:
  - TC-AC-SU-77 memakai aktor `Dewi Lestari`; spec memakai akun Total Control Pre-setup #2 dan baris self dicari lewat emailnya.
  - TC-AC-SU-100 Post Condition "Status per-produk tidak berubah" dan TC-AC-SU-101 langkah 1 ("Aktifkan kembali di Global Settings > User") tidak punya langkah observasi/mekanisme di TC; Post Condition tidak diasersi (S-01) dan pengaktifan kembali memakai Fixture BE.
  - TC-AC-SU-101 memakai user dengan state berbeda dari TC-AC-SU-100 (per-produk OFF); spec membuat dua record terpisah (penanda `T101` pada nama, ditaruh sebelum `{runId}-020` agar nama seed tidak saling mengandung).
  - Nama user TC (`Rudi Hartono`) dipakai sebagai nama bersuffix `{runId}-020` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
