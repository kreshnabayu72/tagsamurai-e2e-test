---
id: TC-GS-ROLE-E2E-003-screening-detail-role-kolom-crud-dinamis-dan-deskripsi-enam-role
title: "Screening Detail Role: Kolom CRUD Dinamis, Deskripsi Enam Role, dan Posisi Checkbox"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-4
  - TC-GS-ROLE-5
  - TC-GS-ROLE-281
coverage:
  web: automated
---

# Screening Detail Role: Kolom CRUD Dinamis, Deskripsi Enam Role, dan Posisi Checkbox

## Prerequisites

- Mode: FE+BE.
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission > Tab System.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`).
- Spec hanya membaca data; tidak ada data yang dibuat, diubah, atau dihapus, sehingga tidak ada pemulihan Pre-setup.
- Data Pre-setup untuk Detail "Manage user and role": Hendra Wijaya (Pre-setup #5, Manage user and role C/R/U/D) dan Doni Pratama (Pre-setup #10, Manage user and role R) tampil di halaman 1 Detail, serta Budi Santoso (Default User, Pre-setup #2) dengan Position "—" dan Division "—".
- Tabel role yang diuji pada TC-GS-ROLE-5 (Data Uji TC; hasil yang diharapkan sama persis dengan Expected TC):

| Role Name | Kolom CRUD yang dirender | Deskripsi |
|---|---|---|
| `Import data` | `Create`, `Read` | This role allows the user to import external data into the system through the Import menu. |
| `Manage files` | `Read`, `Delete` | This role allows the user to manage uploaded files and attachments through the File Manager menu. |
| `Manage hardware` | `Create`, `Read`, `Update`, `Delete` | This role allows the user to manage handheld reader devices through the Hardware menu. |
| `Manage master reference` | `Create`, `Read`, `Update`, `Delete` | This role allows the user to manage brand and measurement master data through the Brand and Measurement menus. |
| `Manage TAG` | `Read`, `Update` | This role allows the user to manage, audit, and combine or separate TAGs through the TAG menu. |
| `Manage user and role` | `Create`, `Read`, `Update`, `Delete` | This role allows the user to manage user accounts and role permissions through the User and Role & Permission menus. |

- Kemampuan teknis: pembacaan posisi horizontal checkbox terhadap sel (untuk asersi rata tengah) dan pembacaan atribut checked/disabled.

## Test Steps

### TC-GS-ROLE-4: Screening halaman Detail role "Manage user and role"

1. Klik Role Name `Manage user and role`
2. Verifikasi breadcrumb "Role & Permission > System > Detail" tampil
3. Verifikasi segmen "System" pada breadcrumb clickable
4. Verifikasi Title "Manage user and role" tampil
5. Verifikasi teks di bawah Title "This role allows the user to manage user accounts and role permissions through the User and Role & Permission menus."
6. Verifikasi Table Tools memuat `Search | Filter | Download | Changelog | [+ Assign]`
7. Verifikasi kolom tabel berurutan `Checkbox | Name | Position | Division | Create | Read | Update | Delete | Actions (⋯)` dengan Checkbox pinned kiri
8. Verifikasi kolom Name, Position, dan Division sortable
9. Verifikasi kolom Create, Read, Update, Delete, dan Actions (⋯) unsortable
10. Klik header kolom Actions (⋯)
11. Verifikasi overlay Column Visibility terbuka
12. Tutup overlay Column Visibility dengan Esc
13. Klik `⋯` pada baris `Doni Pratama`
14. Verifikasi row action `Remove` tampil
15. Tutup row action menu dengan Esc
16. Verifikasi kolom Read di semua baris checked
17. Verifikasi kolom Read di semua baris disabled
18. Verifikasi tidak ada kolom Status (Active/Inactive)
19. Verifikasi kolom Position baris `Budi Santoso` (Default User) bernilai "—"
20. Verifikasi kolom Division baris `Budi Santoso` (Default User) bernilai "—"
21. Verifikasi Pagination default 10 baris/halaman

### TC-GS-ROLE-281: Detail checkbox CRUD rata tengah di sel

22. Verifikasi checkbox Create, Read, Update, dan Delete berada di tengah sel (centered) di semua baris
23. Klik segmen "System" pada breadcrumb

### TC-GS-ROLE-5: Detail kolom CRUD dinamis dan deskripsi per role untuk 6 role

24. Untuk setiap baris tabel "Role Name" (langkah 24 sampai 28): klik Role Name `{Role Name}`
25. Untuk setiap baris tabel "Role Name" (langkah 24 sampai 28): Verifikasi kolom CRUD `{Kolom CRUD yang dirender}` tampil di tabel Detail
26. Untuk setiap baris tabel "Role Name" (langkah 24 sampai 28): Verifikasi deskripsi `{Deskripsi}` tampil di bawah Title
27. Untuk setiap baris tabel "Role Name" (langkah 24 sampai 28): Verifikasi tidak ada kolom CRUD lain selain `{Kolom CRUD yang dirender}` (kolom yang tidak berlaku tidak dirender sama sekali, bukan kolom berisi "—")
28. Untuk setiap baris tabel "Role Name" (langkah 24 sampai 28): klik segmen "System" pada breadcrumb

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-GS-ROLE-4 dan TC-GS-ROLE-281 dijalankan dahulu pada Detail "Manage user and role" yang sama (satu pembukaan Detail); TC-GS-ROLE-5 menyusul sebagai perulangan karena berpindah antar Detail.
- Langkah 24 sampai 28 diulang enam kali (satu kali per baris tabel Prerequisites); parameter tiap iterasi ada di tabel dan tidak ada langkah bersyarat. Verifikasi "tidak ada kolom CRUD lain" ditulis sebagai satu pernyataan tunggal untuk keenam role: pada role dengan empat kolom CRUD pernyataan itu terpenuhi trivial, pada role lain menjalankan Expected g TC-GS-ROLE-5. Ekspansi: 21 + 2 + 30 = 53 langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): klik header Actions dan Esc (langkah 10 dan 12, menjalankan klausa "header = overlay Column Visibility" Expected TC-GS-ROLE-4), membuka dan menutup row action menu (langkah 13 dan 15, menjalankan klausa "body = row action Remove"), klik breadcrumb "System" (langkah 23 dan 28).
- Spec melewati sekitar 35 langkah (53 dengan ekspansi). Alasan: seluruh blok berkelas sama (screening Detail tanpa aksi tulis, satu akun, satu dataset); sekitar 30 langkah berasal dari perulangan enam role yang parameternya ada di tabel Prerequisites, dan sisanya dari aturan S-01 (satu `Verifikasi` per klausa Expected TC-GS-ROLE-4). Blok TC-GS-ROLE-5 berdiri sendiri (dimulai dari Tab System) sehingga tetap bermakna walau blok TC-GS-ROLE-4 gagal.
- TC-GS-ROLE-5 langkah 2 ("screening Title, deskripsi, dan kolom CRUD") menyebut Title, tetapi Expected hanya memuat kolom CRUD dan deskripsi; spec mengasersi hanya yang ada di Expected (S-02).
- Temuan untuk QA:
  - TC-GS-ROLE-4 tidak menyebut baris yang dipakai untuk memeriksa row action Remove; spec memakai `Doni Pratama` (Pre-setup #10) di halaman 1.
  - TC-GS-ROLE-4 Expected b.i memuat "Actions (⋯) ... body per baris = row action Remove" tanpa kondisi disabled; spec hanya mengasersi `Remove` tampil.
  - TC-GS-ROLE-5 Expected g tidak menyebut cara mengamati "tidak dirender sama sekali"; spec mengasersi tidak ada kolom CRUD lain di luar tabel Prerequisites.
