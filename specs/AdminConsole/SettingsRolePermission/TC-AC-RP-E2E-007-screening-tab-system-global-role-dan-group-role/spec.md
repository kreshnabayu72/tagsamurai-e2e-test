---
id: TC-AC-RP-E2E-007-screening-tab-system-global-role-dan-group-role
title: "Screening Tab System: Dua Section, Urutan Katalog dan Jumlah Users, serta Link Role Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-27
  - TC-AC-RP-28
  - TC-AC-RP-29
  - TC-AC-RP-30
coverage:
  web: automated
---

# Screening Tab System: Dua Section, Urutan Katalog dan Jumlah Users, serta Link Role Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #13 (pemegang tingkat akses), #14 (penugasan GM), dan #15 (penugasan individual per Global Role dan Group Role). Jumlah Users yang diasersi pada TC-AC-RP-28 dan TC-AC-RP-29 dihitung dari #13 sampai #15 sesuai aturan kolom Users (per user, assignment aktif) dan ditulis sebagai nilai tetap TC. Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-27: Screening Tab System dua section

1. Klik tab `System`
2. Susuri toolbar dan kedua section
3. Verifikasi Toolbar hanya berisi ikon Search, Download, Changelog
4. Verifikasi tidak ada Filter dan tidak ada "+ Assign" pada Toolbar
5. Verifikasi section "Global Role" tampil dengan description statis "This role applies globally, regardless of the group assigned to the user."
6. Verifikasi section "Group Role" tampil dengan description statis "This role only applies within the groups assigned to the user. Data outside the assigned group is not visible."
7. Verifikasi masing-masing tabel berkolom Role Name, Users, Actions `⋯`
8. Verifikasi tidak ada tombol tambah, edit nama, atau hapus role, dan description tidak memiliki tombol copy
9. Verifikasi tidak ada Pagination di bawah kedua tabel

### TC-AC-RP-28: Daftar Global Role Principal berurutan katalog A-Z beserta jumlah Users

10. Verifikasi tabel Global Role menampilkan 10 baris berurutan beserta Users: `Manage device master data` 13, `Manage group` 8, `Manage hardware stock` 9, `Manage language` 9, `Manage plans & licensing` 8, `Manage preload` 8, `Manage presetup` 8, `Manage privacy policy` 8, `Manage TAG stock` 8, `Manage user and role` 10

### TC-AC-RP-29: Daftar Group Role Principal berurutan katalog A-Z beserta jumlah Users

11. Verifikasi tabel Group Role menampilkan 6 baris berurutan beserta Users: `Manage active client` 10, `Manage allocation` 12, `Manage archived client` 10, `Manage distributor` 12, `Manage partner` 10, `Manage wallet & pricing` 11
12. Verifikasi `Manage partner` bernilai Users 10 karena `Sarah Kimura` memegang peran aktif tanpa penugasan group dan tidak dihitung
13. Verifikasi Users dihitung per user, bukan per baris user × group

### TC-AC-RP-30: Role Name Tab System adalah link ke Role Detail dengan row action Detail sebagai jalur kedua

14. Klik link `Manage language`
15. Verifikasi halaman Role Detail `Manage language` terbuka
16. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
17. Klik `⋯` pada baris `Manage language`
18. Verifikasi overlay `⋯` memuat `Detail` (ikon `FileInfoLine`, severity dark)
19. Tutup overlay row action

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 2 (susur toolbar dan kedua section sebagai prasyarat asersi), langkah 16 (kembali ke Tab System lewat Breadcrumb, mengikuti "Kembali ke Tab System" pada Langkah Uji TC-AC-RP-30), dan langkah 19 (menutup overlay).
- Jumlah Users pada TC-AC-RP-28 dan TC-AC-RP-29 adalah nilai tetap hasil hitung TC dari Data Uji #13 sampai #15, bukan total audit trail; tidak ada angka absolut Changelog, System Log, atau Activity Log yang diasersi (S-12).
- Temuan untuk QA:
  - TC-AC-RP-28 dan TC-AC-RP-29 menggantungkan jumlah Users pada penjumlahan Data Uji #13 sampai #15 yang tidak ditulis rincinya; perubahan data Pre-setup (mis. penugasan baru) membuat angka berubah, dan pemulihan baseline automation tidak didefinisikan di TC (mekanismenya "disediakan tim FE/BE").
  - TC-AC-RP-29 Expected memuat tiga klausa (urutan dan jumlah, pengecualian `Sarah Kimura`, dan aturan hitung per user) dalam satu butir; spec memecahnya menjadi tiga Verifikasi (S-01).
