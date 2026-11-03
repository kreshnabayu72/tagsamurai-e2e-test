---
id: TC-AC-SU-E2E-201-role-matrix-tab-role-aktor-total-control-dan-read-only
title: "Role Matrix: Tab Role, Aktor Total Control dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-63
  - TC-AC-SU-64
coverage:
  web: automated
---

# Role Matrix: Tab Role, Aktor Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor: Read Only (Pre-setup #3) `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Ganti akun ke Read Only dilakukan eksplisit pada langkah 16. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-63 | Total Control | Pre-setup #2 |
| TC-AC-SU-64 | Read Only | Pre-setup #3 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-64 | `Region A` | `Region A {runId}-201` | - | Group |
| TC-AC-SU-64 | `Rudi Hartono` | `Rudi Hartono {runId}-201` | `rudihartono+{runId}-201@qwertysystem.net` | tanpa tingkat akses (kosong); Group Role `Manage allocation` aktif di `Region A {runId}-201` |
| TC-AC-SU-63 | `Dewi Lestari` | `Dewi Lestari {runId}-201` | `dewilestari+{runId}-201@qwertysystem.net` | Total Control |
| TC-AC-SU-63 | `Andi Wijaya` | `Andi Wijaya {runId}-201` | `andiwijaya+{runId}-201@qwertysystem.net` | Read Only |

- Baris aktor sendiri dicari lewat Search atas email akun; tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-63: Tab Role Global Role, aktor Total Control per target

1. Ketik Search `Dewi Lestari {runId}-201`, tekan Enter
2. Klik Name `Dewi Lestari {runId}-201`
3. Verifikasi `Dewi Lestari {runId}-201`: switch dan C/U/D enabled
4. Verifikasi banner Total Control tampil
5. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
6. Ganti isi kotak search dengan `Andi Wijaya {runId}-201`, tekan Enter
7. Klik Name `Andi Wijaya {runId}-201`
8. Verifikasi `Andi Wijaya {runId}-201`: switch dan C/U/D enabled
9. Verifikasi banner `This user has Read Only access.`
10. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
11. Ganti isi kotak search dengan `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
12. Klik Name baris aktor sendiri
13. Hover switch dan checkbox C/U/D baris `Manage group` pada sub-tab Global Role
14. Verifikasi aktor sendiri: switch dan C/U/D tampil namun disabled dengan tooltip `You can't manage your own account from here.`
15. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-64: Tab Role, aktor Read Only seluruh kontrol tulis

16. Logout dari akun aktor saat ini
17. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
18. Ketik Search `Rudi Hartono {runId}-201`, tekan Enter
19. Klik Name `Rudi Hartono {runId}-201`
20. Hover switch dan checkbox C/U/D baris `Manage group` pada sub-tab Global Role
21. Verifikasi switch dan C/U/D Global Role tampil namun disabled dengan tooltip `Read Only access cannot modify data.`
22. Klik sub-tab Group Role
23. Amati kolom Actions baris `Manage allocation`
24. Verifikasi kolom Actions: `[Detail]` tampil enabled
25. Verifikasi sub-tab Group Role tidak punya switch
26. Verifikasi kolom Actions: `[Assign Group]` tidak dirender
27. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; berlaku untuk semua Search di spec ini), semua langkah kembali ke daftar lewat Breadcrumb, langkah 28 (reset Search). Layar awal dibuka hook `beforeEach` suite; sub-tab Global Role aktif secara default pada Tab Role.
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit dan langkah tiap role berbeda target.
- Pembagian TC Role Matrix Tab Role: TC-AC-SU-62 di spec 021, TC-AC-SU-63 dan 64 di spec ini, TC-AC-SU-65 di spec 202.
- Temuan untuk QA:
  - TC-AC-SU-63 dan 64 memakai nama aktor `Andi Wijaya`, `Fajar Nugroho` yang tidak dipetakan ke Pre-setup; spec memakai akun Pre-setup #2 dan #3.
  - TC-AC-SU-63: baris yang dihover adalah `Manage group` (TC menyebut baris `Manage group` hanya pada langkah 2); target diasumsikan memiliki baris itu pada sub-tab Global Role.
  - TC-AC-SU-64 mensyaratkan `Rudi Hartono` punya Group Role `Manage allocation` aktif di `Region A`; spec men-seed record itu.
  - Nama user TC (`Region A`, `Rudi Hartono`, `Dewi Lestari`, `Andi Wijaya`) dipakai sebagai nama bersuffix `{runId}-201` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
