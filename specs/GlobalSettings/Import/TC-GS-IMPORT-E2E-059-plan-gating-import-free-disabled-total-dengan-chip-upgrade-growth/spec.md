---
id: TC-GS-IMPORT-E2E-059-plan-gating-import-free-disabled-total-dengan-chip-upgrade-growth
title: "Plan Gating Import: Free Disabled Total dengan Chip Upgrade; Growth, Professional, dan Enterprise Aktif Penuh"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-45
  - TC-GS-IMPORT-46
  - TC-GS-IMPORT-608
  - TC-GS-IMPORT-609
coverage:
  web: automated
---

# Plan Gating Import: Free Disabled Total dengan Chip Upgrade; Growth, Professional, dan Enterprise Aktif Penuh

## Prerequisites

- Mode: FE+BE (backend nyata). Verifikasi baca per plan tier; spec tidak mengubah plan. Suite serial (`parallel: false`); lihat `suite.md`.
- Akun, password lewat env (tiap akun pada client dengan plan berbeda):
  - Total Control Client Free (Dewi Lestari) `totalControl_automated_qaTeam8@qwertysystem.net`, `Spectra.env.GS_CLIENTFREE_TC_PASSWORD` (plan Free; login di hook `before`).
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD` (plan Growth).
  - Total Control Client Professional (Surya Kencana) `totalControl_automated_qaTeam12@qwertysystem.net`, `Spectra.env.GS_CLIENTPRO_TC_PASSWORD` (plan Professional).
  - Total Control Client Enterprise (Tari Wulandari) `totalControl_automated_qaTeam13@qwertysystem.net`, `Spectra.env.GS_CLIENTENT_TC_PASSWORD` (plan Enterprise).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite.
- Tabel "Client yang diuji" untuk langkah ulang (TC-GS-IMPORT-46, 608, 609):

| Client | Akun | Plan | TC |
|---|---|---|---|
| Client A | Total Control Client A | Growth | TC-GS-IMPORT-46 |
| Client Professional | Total Control Client Professional | Professional | TC-GS-IMPORT-608 |
| Client Enterprise | Total Control Client Enterprise | Enterprise | TC-GS-IMPORT-609 |

- Data: Client Free punya draft Brand tersimpan yang disiapkan lewat langkah penyiapan fixture sebelum plan diturunkan ke Free (tidak diubah spec ini). Plan tiap client disediakan tim FE/BE lewat fixture Admin Console.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk akun aktor. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk tiap akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

### TC-GS-IMPORT-45: Plan Free

1. Buka menu Import dari sidebar
2. Verifikasi halaman Import tampil Disabled 🔒 total
3. Verifikasi chip "Upgrade" tampil
4. Klik Sub-Tab Measurement
5. Verifikasi Sub-Tab Measurement tidak menjadi aktif
6. Klik [Upload File]
7. Verifikasi file picker tidak terbuka
8. Verifikasi Modal Column Mapping tidak terbuka
9. Verifikasi draft Brand tersimpan tidak dapat diakses: tidak ada baris staging yang dapat dibuka

### TC-GS-IMPORT-46, 608, 609: Plan Growth, Professional, dan Enterprise

Untuk setiap baris tabel "Client yang diuji" (langkah 10 sampai 13):

10. Ganti akun: login sebagai akun pada baris tabel, lalu buka menu Import dari sidebar
11. Verifikasi halaman Import aktif penuh: Sub-Tab, `[Upload File]`, dan `[Download Template]` Enabled
12. Verifikasi chip "Upgrade" tidak tampil
13. Logout

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: state tenant (kelas h, prinsip 13h; plan gating). Spec membaca tampilan per tier dan tidak mengubah tier.
- Langkah 10 sampai 13 diulang tiga kali (TC-GS-IMPORT-46, 608, 609) sehingga ekspansinya 12 langkah; total spec sekitar 21 langkah dan di bawah smell 35 langkah. Langkah identik, hanya akun dan plan yang berbeda (tabel Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 (logout sebelum akun berikutnya).
- Langkah 12 (absence chip "Upgrade") memakai Sub-Tab dan tombol Enabled langkah 11 sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-45 tidak mengatur plan Client Free selama spec; plan Free disediakan fixture sebelum spec.
  - TC-GS-IMPORT-45 Expected d ("draft tersimpan tidak dapat diakses") tidak menyebut cara membuktikan ketiadaan akses selain tidak ada baris staging yang dapat dibuka.
