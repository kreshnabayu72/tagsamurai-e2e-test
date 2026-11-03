---
id: TC-FA-SU-E2E-100-popup-select-group-screening-node-ter-assign-disabled-dan-search
title: "Popup Select Group: Screening, Node Ter-assign Disabled, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-898
  - TC-FA-SU-899
  - TC-FA-SU-900
coverage:
  web: automated
---

# Popup Select Group: Screening, Node Ter-assign Disabled, dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Wawan Setiawan (Pre-setup #23: Manage files pada IT Infrastructure dan Branch Surabaya; Manage purchase pada General Affairs dan Logistics Warehouse; Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse). Role Manage files sudah ter-assign pada IT Infrastructure dan Branch Surabaya. Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-898: Screening popup Select Group

1. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role
2. Klik `[Assign Group]` pada baris Manage files
3. Klik `[+ Assign Group]`
4. Verifikasi header `Select Group` dengan close `[✕]` tampil
5. Verifikasi kolom pencarian dengan placeholder `Search groups...` tampil
6. Verifikasi pohon grup entitas dengan checkbox per node
7. Verifikasi node yang sudah ter-assign ke role ini tampil Disabled
8. Verifikasi footer menampilkan `[Cancel]` (Text, Contrast) dan `[Select]`
9. Verifikasi `[Select]` Disabled sampai node dicentang
10. Centang node General Affairs
11. Verifikasi `[Select]` Enabled
12. Hapus centang node General Affairs

### TC-FA-SU-899: Node ter-assign Disabled dengan tooltip

13. Verifikasi node IT Infrastructure dan Branch Surabaya (sudah ter-assign ke Manage files) tampil Disabled
14. Hover node IT Infrastructure
15. Verifikasi tooltip "This group is already assigned to this role." tampil

### TC-FA-SU-900: Search di popup Select Group

16. Ketik Search `Surabaya`, tekan Enter
17. Verifikasi node Branch Surabaya (Disabled) tampil tetapi tidak dapat dipilih
18. Verifikasi parent node Branch Surabaya tampil
19. Ganti isi kotak Search dengan `zzz`, tekan Enter
20. Verifikasi empty state `No results found` dengan `Try adjusting your search or filter.` tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): mencentang node General Affairs dan menghapus centangnya (untuk mengamati `[Select]` Enabled lalu mengembalikan state, S-09). TC-FA-SU-899 dan TC-FA-SU-900 memakai popup Select Group yang masih terbuka dari TC-FA-SU-898 (tanpa pembukaan ulang).
- Temuan untuk QA (S-15): (1) Expected c TC-FA-SU-900 ("node di luar scope aktor tidak pernah muncul") tidak teramati dengan akun Total Control yang melihat seluruh pohon; scope aktor diamati pada TC-FA-SU-907 dan tidak diasersi di spec ini. (2) Keyword tanpa hasil pada TC-FA-SU-900 ditulis `zzz` sesuai data uji. (3) TC-FA-SU-898 Expected c menyebut `[Select]` Disabled "sampai ≥1 node dicentang" tanpa langkah mencentang; spec menambah langkah mencentang node General Affairs untuk mengamati transisi tersebut.
