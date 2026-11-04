---
id: TC-FA-RP-E2E-063-remove-total-control-3
title: "Remove Total Control (3/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1131
  - TC-FA-RP-1133
coverage:
  web: automated
---

# Remove Total Control (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi), #18 (pohon group), #21 (Ahmad Fauzi memegang `Manage asset & TAG` Create, Read, Update di `Head Office`), #39 (Ahmad Fauzi `Manage files` Read di `Data Center`). Pada TC-FA-RP-1131 Ahmad Fauzi di-seed berstatus Total Control dengan baris pola Group Role CRUD penuh sesuai kolom berlaku pada setiap group (termasuk `Manage files` di `Data Center` dan `Helpdesk` serta `Manage asset & TAG` di `Head Office`; `FARP-LOGIC-04b`); pada TC-FA-RP-1133 Ahmad Fauzi Total Control dengan baris pola Group Role CRUD penuh pada setiap group, termasuk `Manage files` di `Data Center`.
- Navigasi lintas modul: Settings > User > Detail User > Tab Role sub-tab Group Role (TC-FA-RP-1131).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1131: Confirm Remove Total Control mengosongkan seluruh penugasan Group Role di semua group: baris hilang dari Detail Role dan kolom Users berkurang

1. Buka Tab System lalu catat kolom Users baris Group Role `Manage files` dan `Manage asset & TAG` sebagai baseline
2. Buka Tab Total Control, klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
3. Verifikasi toast sukses `Success, Total Control has been removed.`
4. Buka Tab System dan amati kolom Users baris yang sama
5. Verifikasi kolom Users baris `Manage files` dan `Manage asset & TAG` masing-masing berkurang 1 dari baseline (dihitung per user, bukan per group)
6. Buka Detail Role Group Role `Manage files`, klik `All Groups`, lalu ketik Search `Ahmad Fauzi`, tekan Enter
7. Verifikasi baris Ahmad Fauzi tidak tampil di `Data Center` maupun `Helpdesk` (empty state hasil Search)
8. Klik `(←)` pada kotak Search
9. Buka Detail Role Group Role `Manage asset & TAG`, klik `All Groups`, lalu ketik Search `Ahmad Fauzi`, tekan Enter
10. Verifikasi baris Ahmad Fauzi tidak tampil di `Head Office` (empty state hasil Search)
11. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Group Role
12. Verifikasi tidak ada baris penugasan Group Role untuk Ahmad Fauzi

### TC-FA-RP-1133: Setelah Remove Total Control, user kembali eligible di popup Assign User ke Role Group Role dan penugasan baru dimulai dari baseline Read

13. Tetapkan ulang Ahmad Fauzi sebagai Total Control dengan baris pola Group Role CRUD penuh pada setiap group, termasuk `Manage files` di `Data Center`, lewat seeding API
14. Buka Fixed Asset > Settings > Role & Permission > System lalu Detail Role Group Role `Manage files` dan klik node `Data Center` di Sidebar Group Tree
15. Klik `[+ Assign]`, ketik Search `Ahmad Fauzi`, tekan Enter
16. Verifikasi Ahmad Fauzi tidak ada di daftar (Total Control dikecualikan; empty state hasil Search)
17. Tutup popup lewat `✕`
18. Buka Tab Total Control, klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
19. Buka Detail Role Group Role `Manage files`, klik node `Data Center`, klik `[+ Assign]`, lalu ketik Search `Ahmad Fauzi`, tekan Enter
20. Verifikasi Ahmad Fauzi ada di daftar (penugasan Group Role di `Data Center` sudah dihapus)
21. Centang Ahmad Fauzi lalu klik `[Assign]`
22. Verifikasi baris Ahmad Fauzi tampil di Detail Role `Manage files` dengan badge Group `Data Center`
23. Verifikasi Read aktif dan terkunci pada baris Ahmad Fauzi (bukan nilai penugasan sebelum pencabutan)
24. Verifikasi Delete tidak aktif pada baris Ahmad Fauzi
25. Verifikasi Create dan Update menampilkan `—` pada baris Ahmad Fauzi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 25 langkah.
- Langkah penghubung (S-03): langkah 8, 17. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 13; tidak ada `Verifikasi`.
- Asersi absence pada TC-FA-RP-1131 memakai empty state hasil Search sebagai anchor positif (butir 8b.2).
- Baseline kolom Users dicatat sebagai langkah TC (langkah pertama TC-FA-RP-1131) dan asersi memakai selisih 1 terhadap baseline (S-12).
- Temuan untuk QA:
  - TC-FA-RP-1131 precondition c merujuk Pre-setup #15, #18, #21, #39; baris pola Group Role `Manage files` di `Helpdesk` untuk Ahmad Fauzi tidak ada di Pre-setup dan di-seed lewat seeding API sesuai TC.
  - TC-FA-RP-1133 Expected c memakai `Create/Update` `—` pada `Manage files` (kolom tidak berlaku); sesuai TC-FA-RP-247.
