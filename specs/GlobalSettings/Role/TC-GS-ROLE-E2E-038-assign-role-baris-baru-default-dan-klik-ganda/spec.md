---
id: TC-GS-ROLE-E2E-038-assign-role-baris-baru-default-dan-klik-ganda
title: "Assign Role: Baris Baru Default dan Klik Ganda [Assign]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-95
  - TC-GS-ROLE-98
coverage:
  web: automated
---

# Assign Role: Baris Baru Default dan Klik Ganda [Assign]

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Spec memakai satu akun; tidak ada ganti akun.
- Data Pre-setup: Wawan Setiawan (Pre-setup #11, kandidat: Active, Access Global Settings dicentang, tanpa access level, tanpa baris role).
- Data yang diubah spec: baris `Import data` dan baris `Manage hardware` untuk Wawan Setiawan. Hook `after` menghapus kedua baris itu lewat seeding API (kemampuan disediakan tim FE/BE) sehingga Wawan Setiawan kembali ke kondisi kandidat Pre-setup #11.
- Kemampuan teknis: klik ganda cepat pada `[Assign]` (dua klik berurutan tanpa jeda yang disengaja).
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-95: Assign Role Import data, baris baru Read aktif dan Create unchecked

1. Klik Role Name `Import data`
2. Klik `[+ Assign]`
3. Centang Wawan Setiawan
4. Klik `[Assign]`
5. Verifikasi toast sukses "Success, role has been assigned."
6. Verifikasi baris Wawan Setiawan tampil di Detail `Import data` dengan Create unchecked
7. Verifikasi Create baris Wawan Setiawan enabled
8. Verifikasi Read baris Wawan Setiawan checked dan disabled

### TC-GS-ROLE-98: Klik ganda [Assign] pada popup Assign Role

9. Klik segmen `System` pada breadcrumb untuk membuka Tab System
10. Tunggu toast lama hilang otomatis
11. Klik Role Name `Manage hardware`
12. Klik `[+ Assign]`
13. Centang Wawan Setiawan
14. Klik `[Assign]` dua kali cepat
15. Verifikasi satu toast sukses "Success, role has been assigned."
16. Verifikasi Detail `Manage hardware` memuat tepat 1 baris Wawan Setiawan

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Tab System lewat breadcrumb (langkah 9) dan menunggu toast TC-GS-ROLE-95 hilang (langkah 10) supaya hitungan "satu toast" pada langkah 15 tidak tercampur toast sebelumnya.
- Langkah 16 mengasersi jumlah (tepat 1 baris), bukan absence; baris Wawan Setiawan di `Manage hardware` belum ada sebelum langkah 14 sehingga jumlah itu sendiri menjadi baseline nol.
- TC-GS-ROLE-97 (Assign Role gagal 5xx) berada di spec resilience terpisah dan tidak termasuk spec ini.
- Temuan untuk QA:
  - TC-GS-ROLE-95 dan TC-GS-ROLE-98 tidak punya Post Condition; tidak ada yang diasersi tambahan.
  - TC-GS-ROLE-98 Expected a menyebut "satu toast"; TC tidak menyebut durasi toast, sehingga spec menunggu toast lama hilang sebelum klik ganda.
