---
id: TC-AC-RP-E2E-079-tab-system-search-sort-setup-column
title: "Tab System: Search, kolom tidak sortable, Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-272
  - TC-AC-RP-273
  - TC-AC-RP-274
coverage:
  web: automated
---

# Tab System: Search, kolom tidak sortable, Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Katalog Tab System (Pre-setup #15): Global Role `Manage plans & licensing`, `Manage preload`, `Manage presetup`, `Manage privacy policy`, dan seterusnya; Group Role termasuk `Manage partner`, `Manage allocation` (Users 12), `Manage distributor` (Users 12).
- Pemulihan Setup Column: preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Kemampuan teknis: penghapusan preferensi kolom di browser (disediakan tim FE).

## Test Steps

### TC-AC-RP-272: Search Tab System mencakup Role Name dan Users

1. Klik tab `System`
2. Klik ikon Search
3. Verifikasi placeholder kotak Search "Search role..."
4. Ketik Search `manage p`, tekan Enter
5. Verifikasi Global Role `Manage plans & licensing`, `Manage preload`, `Manage presetup`, dan `Manage privacy policy` tampil
6. Verifikasi Group Role `Manage partner` tampil
7. Ganti isi kotak search dengan `12`, tekan Enter
8. Verifikasi baris `Manage allocation` dan `Manage distributor` (keduanya Users 12) tampil

### TC-AC-RP-273: Kolom Tab System tidak sortable

9. Klik `(←)` pada kotak Search
10. Klik header Role Name
11. Klik header Users
12. Verifikasi urutan baris tetap urutan katalog A-Z
13. Verifikasi tidak ada ikon sort pada header Role Name dan Users

### TC-AC-RP-274: Setup Column Tab System

14. Buka Column Visibility
15. Verifikasi daftar hanya memuat Role Name dan Users (tanpa kolom curated)
16. Sembunyikan kolom Users
17. Verifikasi kolom Users tidak tampil pada section Global Role dan Group Role

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 9 mengosongkan Search sebelum TC-AC-RP-273 (S-09).
- Placeholder Search diasersi saat kotak baru dibuka dan masih kosong (S-14), sebelum mengetik; Verifikasi urutan katalog pada TC-AC-RP-273 ditulis lebih dulu sebagai anchor positif bagi asersi absence ikon sort.
- Temuan untuk QA: Column Visibility pada TC-AC-RP-274 tidak menyebut `[Save]`; spec mengikuti TC.
