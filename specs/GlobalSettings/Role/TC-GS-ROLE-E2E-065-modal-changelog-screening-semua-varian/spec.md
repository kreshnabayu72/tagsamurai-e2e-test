---
id: TC-GS-ROLE-E2E-065-modal-changelog-screening-semua-varian
title: "Modal Changelog: Screening Varian Tab Total Control, Read Only, System, dan Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-196
  - TC-GS-ROLE-197
coverage:
  web: automated
---

# Modal Changelog: Screening Varian Tab Total Control, Read Only, System, dan Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > Total Control.
- Seeding precondition TC (lewat API oleh akun Ahmad Fauzi di hook `before`, dipakai sebagai precondition TC, tidak diasersi; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level`, POST/PATCH/DELETE `/v2/iam/products/{product}/roles/capabilities/users`; asumsi seeding lewat API mencatat entri Changelog sama seperti aksi UI):
  - Fikri Ramadhan (Pre-setup #18): Assign Total Control lalu Remove Total Control, lalu Assign Read Only lalu Remove Read Only, sehingga Changelog Tab Total Control dan Tab Read Only masing-masing memuat entri Assign dan Remove (TC-GS-ROLE-196).
  - Citra Dewanti (Pre-setup #18): Assign Role Manage TAG, Edit CRUD Update, lalu Remove baris Manage TAG, sehingga Changelog Tab System dan Detail "Manage TAG" memuat entri Edit, Assign, dan Remove (TC-GS-ROLE-197).
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Fikri Ramadhan dan Citra Dewanti dikembalikan ke kondisi kandidat Pre-setup #18 (Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) lewat API; Modal Changelog ditutup. Entri Changelog tidak bisa dihapus.
- Tabel Tab Changelog (parameter perulangan TC-GS-ROLE-196):

| Tab | Title Modal Changelog |
|---|---|
| Total Control | `Changelog: Role & Permission > Total Control` |
| Read Only | `Changelog: Role & Permission > Read Only` |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-196: Screening Modal Changelog Tab Total Control dan Tab Read Only

1. Untuk setiap baris tabel Tab Changelog (langkah 1 sampai 13): klik Tab sesuai kolom "Tab"
2. Klik icon Changelog di Table Tools
3. Verifikasi Title Modal Changelog sesuai kolom "Title Modal Changelog" pada tabel
4. Verifikasi toolbar `Search | Filter | Download`
5. Klik icon Search
6. Verifikasi placeholder Search `Search action, user, or value...`
7. Klik `(←)` pada kotak Search
8. Verifikasi kolom `Date (sortable) | Action (sortable) | User Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯)`
9. Verifikasi header kolom `Actions (⋯)` berfungsi sebagai Column Visibility
10. Verifikasi baris tabel tidak memiliki row action
11. Verifikasi baris terurut Date terbaru dulu
12. Verifikasi pagination default 10 baris per halaman
13. Tutup Modal Changelog lewat `[✕]`

### TC-GS-ROLE-197: Screening Modal Changelog Tab System dan Detail

14. Klik Tab `System`
15. Klik icon Changelog di Table Tools
16. Verifikasi Title Modal Changelog `Changelog: Role & Permission > System`
17. Klik icon Search
18. Verifikasi placeholder Search `Search action, role, user, or value...`
19. Klik `(←)` pada kotak Search
20. Verifikasi kolom `Date | Action | Role — User | Field | Old Value | New Value | Modified By | Actions (⋯)`
21. Verifikasi semua kolom data tersebut sortable
22. Verifikasi baris terurut Date terbaru dulu
23. Tutup Modal Changelog lewat `[✕]`
24. Klik Role Name `Manage TAG`
25. Klik icon Changelog di Table Tools
26. Verifikasi Title Modal Changelog `Changelog: Role & Permission > Manage TAG`
27. Klik icon Search
28. Verifikasi placeholder Search `Search action, user, or value...`
29. Klik `(←)` pada kotak Search
30. Verifikasi kolom `Date | Action | Role — User | Field | Old Value | New Value | Modified By | Actions (⋯)`
31. Verifikasi semua kolom data tersebut sortable
32. Verifikasi baris terurut Date terbaru dulu
33. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (196, 197) dipertahankan; kedua TC adalah screening tanpa aksi tulis.
- Langkah 1 sampai 13 diulang untuk Tab Total Control lalu Tab Read Only (Langkah Uji 3 TC-GS-ROLE-196 "Ulangi di Tab Read Only"; Expected d "struktur identik"); parameter di tabel Tab Changelog. Klik Tab `Total Control` pada iterasi pertama tidak mengubah tab aktif dari hook `beforeEach`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 7, 17 dan 19, 27 dan 29 (membuka dan menutup kotak Search hanya untuk membaca placeholder; Search tidak dijalankan), langkah 13, 23, dan 33 (menutup Modal Changelog), langkah 24 (membuka Detail "Manage TAG" lewat Role Name di Tab System).
- Spec melewati sekitar 35 langkah (33 langkah nominal, 46 dengan ekspansi satu blok ulang) karena tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01) dan screening dilakukan pada empat varian modal. Semuanya satu kelas harness (screening Modal Changelog), satu akun, dan data baca saja; kegagalan satu varian tidak membuat varian lain kehilangan makna.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-196 dan 197 menyebut "Ada entry Assign/Remove" dan "Ada entry Edit/Assign/Remove" tanpa menyebut cara menyediakannya; spec men-seed entri lewat API (Prerequisites) dan tidak mengasersi isi entri.
  - TC-GS-ROLE-196 Expected c dan TC-GS-ROLE-197 Expected d ("Default sort Date terbaru dulu"): kolom Date berketelitian menit, sehingga entri seeding spec ini dapat bernilai Date sama; urutan descending hanya teramati pada entri dengan Date berbeda yang sudah ada di environment.
  - TC-GS-ROLE-196 tidak menyebut apakah placeholder Search dibaca setelah klik icon Search; spec membuka kotak Search lalu menutupnya (langkah 5 dan 7).
