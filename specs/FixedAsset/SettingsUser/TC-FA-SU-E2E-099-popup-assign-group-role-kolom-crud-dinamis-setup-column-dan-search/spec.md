---
id: TC-FA-SU-E2E-099-popup-assign-group-role-kolom-crud-dinamis-setup-column-dan-search
title: "Popup Assign Group Role: Kolom CRUD Dinamis, Setup Column, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-895
  - TC-FA-SU-896
  - TC-FA-SU-897
coverage:
  web: automated
---

# Popup Assign Group Role: Kolom CRUD Dinamis, Setup Column, dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Wawan Setiawan (Pre-setup #23: Manage files pada IT Infrastructure dan Branch Surabaya; Manage purchase pada General Affairs dan Logistics Warehouse; Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan. Setup Column pada popup tidak disimpan (tanpa `[Save]`), sehingga tidak ada preferensi kolom yang perlu dipulihkan.

## Test Steps

### TC-FA-SU-895: Kolom C/R/U/D mengikuti kapabilitas role

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
3. Klik `[Assign Group]` pada baris Manage group
4. Verifikasi popup Assign Group Role Manage group menampilkan kolom Create, Read, Update, dan Delete
5. Tutup popup Assign Group Role
6. Klik `[Assign Group]` pada baris Manage files
7. Verifikasi popup Assign Group Role Manage files hanya menampilkan kolom Read dan Delete
8. Verifikasi checkbox Read selalu tercentang dan terkunci (FI-01)

### TC-FA-SU-896: Setup Column popup Assign Group Role

9. Klik header kolom Actions (⋯) pada tabel popup
10. Verifikasi kolom Group tercantum Hideable (tercentang, Enabled) pada Column Visibility
11. Verifikasi kolom C/R/U/D tidak tercantum di Column Visibility dan selalu tampil
12. Verifikasi urutan baris default Group A-Z (Branch Surabaya lalu IT Infrastructure)

### TC-FA-SU-897: Search di popup Assign Group Role

13. Ketik Search `Branch`, tekan Enter
14. Verifikasi baris Branch Surabaya tampil
15. Verifikasi baris IT Infrastructure tidak tampil
16. Ganti isi kotak Search dengan `zzz`, tekan Enter
17. Verifikasi empty state `No results found` dengan `Try adjusting your search or filter.` tampil
18. Klik ikon ×
19. Verifikasi kotak Search kosong
20. Verifikasi seluruh baris (Branch Surabaya dan IT Infrastructure) kembali tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16, butir 8b.13) dan menutup popup Assign Group Role. TC-FA-SU-896 dan TC-FA-SU-897 memakai popup Manage files yang masih terbuka dari akhir TC-FA-SU-895 (tanpa pembukaan ulang).
- Temuan untuk QA (S-15): (1) TC-FA-SU-896 dan TC-FA-SU-897 menyebut popup Manage files; TC-FA-SU-895 langkah 2 menyebut popup Manage group. (2) Keyword tanpa hasil pada TC-FA-SU-897 ditulis `zzz` sesuai data uji. (3) Urutan A-Z default memakai dua baris Manage files (Branch Surabaya, IT Infrastructure); S-11 mensyaratkan dua nilai distinct, terpenuhi.
