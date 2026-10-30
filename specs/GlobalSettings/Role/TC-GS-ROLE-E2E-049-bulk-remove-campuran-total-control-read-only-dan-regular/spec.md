---
id: TC-GS-ROLE-E2E-049-bulk-remove-campuran-total-control-read-only-dan-regular
title: "Bulk Remove Campuran Baris Regular, Total Control, dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-131
coverage:
  web: automated
---

# Bulk Remove Campuran Baris Regular, Total Control, dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > System > Detail `Manage master reference`.
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup): Wawan Setiawan (baris 11, kandidat tanpa access level), Siti Nurhaliza dan Rina Putri (baris 4; keduanya punya baris Manage TAG), Intan Permata (baris 19, Read Only; baris pembanding di Tab Read Only), Ahmad Fauzi (baris 1; baris pembanding di Tab Total Control).
- Given (hook `before`, lewat seeding API; dependensi TC-GS-ROLE-60): Siti Nurhaliza di-upgrade ke Total Control; Wawan Setiawan, Siti Nurhaliza, dan Rina Putri (Read Only; di-assign ulang bila sudah kehilangan Read Only, Tabel Data Uji Dinamis baris 14) punya baris Manage master reference.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus baris Manage master reference yang masih ada; kembalikan Siti Nurhaliza dan Rina Putri ke Read Only (state Pre-setup baris 4; baris Manage TAG keduanya tidak disentuh aksi spec). Last Updated Siti Nurhaliza dan Rina Putri berubah dan tidak dipulihkan.
- Kemampuan teknis: membaca isi tabel Tab Total Control, Tab Read Only, dan Detail.
- Kemampuan teknis (seeding): seeding API untuk akses level, baris role, dan data user disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-131: Bulk Remove campuran regular dan Total Control/Read Only

1. Centang baris `Wawan Setiawan`
2. Centang baris `Siti Nurhaliza` (Total Control)
3. Centang baris `Rina Putri` (Read Only)
4. Klik `Bulk Action`
5. Klik `Remove`
6. Klik `[Remove]`
7. Verifikasi toast sukses `Success, user has been removed.`
8. Verifikasi baris `Wawan Setiawan`, `Siti Nurhaliza`, dan `Rina Putri` hilang dari Detail `Manage master reference`
9. Buka Tab Total Control
10. Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control
11. Verifikasi baris `Siti Nurhaliza` tidak ada di Tab Total Control
12. Buka Tab Read Only
13. Verifikasi baris `Intan Permata` tampil di Tab Read Only
14. Verifikasi baris `Rina Putri` tidak ada di Tab Read Only
15. Buka Tab System, lalu klik role `Manage TAG` untuk membuka Detail-nya
16. Verifikasi baris Manage TAG milik `Siti Nurhaliza` tetap ada
17. Verifikasi baris Manage TAG milik `Rina Putri` tetap ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah tab dan Detail (langkah 9, 12, 15; Langkah 3 dan 4 TC-GS-ROLE-131).
- Anchor absence (bagian 8b butir 2): baris `Ahmad Fauzi` tampil di Tab Total Control dan baris `Intan Permata` tampil di Tab Read Only mendahului asersi ketiadaan `Siti Nurhaliza` dan `Rina Putri`.
- Temuan untuk QA:
  - TC-GS-ROLE-131 tidak memuat langkah dialog dan hanya satu klik `[Remove]` (Langkah 2: `Bulk Action > Remove > [Remove]`); varian dialog campuran tidak diasersi di TC ini.
  - TC-GS-ROLE-131 tidak menyebut baris pembanding untuk asersi hilangnya Siti Nurhaliza dari Tab Total Control dan Rina Putri dari Tab Read Only; spec memakai Ahmad Fauzi dan Intan Permata (Pre-setup).
  - TC-GS-ROLE-131 tidak menyebut bahwa Wawan Setiawan, Siti Nurhaliza, dan Rina Putri punya baris Manage master reference; kondisi itu disiapkan lewat seeding.
