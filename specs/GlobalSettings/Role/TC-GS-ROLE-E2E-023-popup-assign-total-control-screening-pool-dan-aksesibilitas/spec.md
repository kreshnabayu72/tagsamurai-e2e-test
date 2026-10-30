---
id: TC-GS-ROLE-E2E-023-popup-assign-total-control-screening-pool-dan-aksesibilitas
title: "Popup Assign Total Control: Screening, Pool Kandidat, dan Aksesibilitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-51
  - TC-GS-ROLE-52
  - TC-GS-ROLE-53
  - TC-GS-ROLE-77
coverage:
  web: automated
---

# Popup Assign Total Control: Screening, Pool Kandidat, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; popup hanya dibuka, diamati, dan ditutup dengan Esc.
- Akun: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Login dan navigasi dilakukan sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): kandidat picker Pre-setup #11 (Ahmad Fauzan `ahmad.fz@client.com` IT Staff IT; Ahmad Fauzan `ahmad.fauzan@client.com` Warehouse Staff Logistics; Sari Wulandari Active; Maya Anggraini Staff IT Inactive; Rudi Hartono Pending Activation; Rahmat Hidayat; Wawan Setiawan; Nina Kartika), Pre-setup #1 sampai #12 (Ahmad Fauzi, Budi Santoso, Dewi Lestari sudah Total Control; Siti Nurhaliza Read Only, Hendra Wijaya, dan Doni Pratama tanpa Total Control; Tono Wibowo tanpa Access Global Settings). Pool picker kurang dari 100 user dan lebih dari 10 user (Pre-setup #11 dan #18) sehingga page size 100 menampilkan seluruh pool dalam satu halaman dan page size default 10 membuat pagination tampil. Kondisi Pre-setup dipulihkan oleh spec lain yang mengubahnya (lihat `suite.md`).

Pool Popup Assign Total Control (TC-GS-ROLE-52):

| User | Hasil di picker |
|---|---|
| Sari Wulandari (Active) | tampil |
| Maya Anggraini (Inactive) | tampil |
| Rudi Hartono (Pending Activation) | tampil |
| Siti Nurhaliza (Read Only) | tampil |
| Hendra Wijaya | tampil |
| Doni Pratama | tampil |

- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: menekan Tab dan Esc; membaca elemen yang sedang fokus; membaca atribut sortable pada header kolom.

## Test Steps

### TC-GS-ROLE-51: Screening Popup Assign Total Control

1. Klik `[+ Assign]`
2. Verifikasi Header: Title `Assign Total Control`
3. Verifikasi Toolbar memuat `Search` dan `Filter`
4. Verifikasi placeholder Search `Search...`
5. Verifikasi Body: kolom berurutan `Checkbox`, `Name`, `Email`, `Position`, `Division`, `Status`
6. Verifikasi checkbox pada header tabel tampil
7. Verifikasi kolom `Name`, `Email`, `Position`, `Division`, dan `Status` sortable
8. Verifikasi baris terurut Name A-Z
9. Verifikasi kolom `Status` menampilkan badge `Active` atau `Inactive` pada setiap baris
10. Verifikasi Footer: pagination picker tampil
11. Verifikasi Footer: tombol `[Cancel]` (text, contrast)
12. Verifikasi Footer: tombol `[Assign]` (filled, primary, enabled walau 0 terpilih)

### TC-GS-ROLE-52: Pool Popup Assign Total Control

13. Ubah page size ke 100
14. Untuk setiap user pada tabel Prerequisites "Pool Popup Assign Total Control" (langkah 14): Verifikasi baris user tersebut tampil di picker
15. Verifikasi Ahmad Fauzi, Budi Santoso, dan Dewi Lestari tidak tampil di picker
16. Verifikasi Tono Wibowo tidak tampil di picker

### TC-GS-ROLE-53: Picker menampilkan dua user bernama sama yang dibedakan Email dan Position

17. Verifikasi baris Ahmad Fauzan dengan Email `ahmad.fz@client.com`, Position `IT Staff`, Division `IT` tampil
18. Verifikasi baris Ahmad Fauzan dengan Email `ahmad.fauzan@client.com`, Position `Warehouse Staff`, Division `Logistics` tampil

### TC-GS-ROLE-77: Accessibility Popup Assign: focus trapped dan Esc menutup

19. Tekan Tab berulang sampai fokus melewati elemen terakhir popup
20. Verifikasi fokus berputar di dalam popup dan tidak keluar dari popup
21. Tekan Esc
22. Verifikasi popup tertutup
23. Verifikasi tidak ada toast

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (51, 52, 53, 77) dipertahankan: screening di awal, pengamatan pool pada popup yang sama, lalu aksesibilitas yang menutup popup (satu pembukaan, satu penutupan).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): langkah 13 mengubah page size ke 100 supaya pool diamati pada satu halaman ("semua halaman" pada TC-GS-ROLE-52 langkah 2). Langkah 14 diulang per baris tabel Prerequisites (6 iterasi; parameter di tabel); jumlah langkah dengan ekspansi 28.
- Langkah 15 dan 16 adalah asersi absence yang didahului anchor positif langkah 14 (baris pembanding pada surface yang sama).
- Langkah 23 (tidak ada toast) dan langkah 22 menjadi bukti "tanpa assign" untuk TC-GS-ROLE-77 Expected b; TC tidak memberi langkah observasi daftar Tab Total Control.
- Pembagian TC lintas spec: TC-GS-ROLE-54 sampai 57 (seleksi, counter, validasi kosong, Cancel) ada di spec 024; TC-GS-ROLE-69 sampai 72 (Search) ada di spec 025; TC-GS-ROLE-73, 74 (Filter) ada di spec 026; TC-GS-ROLE-75, 76, 293 (pagination, Column Visibility, sort) ada di spec 027.
- Temuan untuk QA:
  - TC-GS-ROLE-52 langkah 2 ("semua halaman") tidak menyebut cara melihat semua halaman; spec memakai page size 100 dengan asumsi pool kurang dari 100 user.
  - TC-GS-ROLE-51 Expected b menyebut placeholder Search `Search...` tanpa menyatakan apakah input Search sudah terbuka saat popup dibuka; spec memverifikasi placeholder tanpa klik icon Search.
  - TC-GS-ROLE-51 Expected c.i menyebut "header = select all halaman"; perilaku Select All header diasersi di spec 024 (TC-GS-ROLE-56), sehingga di sini hanya keberadaan checkbox header yang diverifikasi.
  - TC-GS-ROLE-77 Post Condition ("tanpa assign") tidak punya langkah observasi di TC; hanya tidak ada toast yang diasersi.
