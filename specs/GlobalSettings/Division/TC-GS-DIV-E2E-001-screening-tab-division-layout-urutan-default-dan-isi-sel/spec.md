---
id: TC-GS-DIV-E2E-001-screening-tab-division-layout-urutan-default-dan-isi-sel
title: "Screening Tab Division: Layout, Urutan Default Name A-Z, Tooltip Table Tools, dan Isi Sel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-1
  - TC-GS-DIV-2
  - TC-GS-DIV-3
  - TC-GS-DIV-4
coverage:
  web: automated
---

# Screening Tab Division: Layout, Urutan Default Name A-Z, Tooltip Table Tools, dan Isi Sel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Division (data environment tetap, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Last Updated keenam Division adalah tanggal pre-setup. Spec tidak mengubah atau menghapus baris Pre-setup.
- Data Dinamis, di-seed lewat kemampuan "seeding Division lewat API" di hook `before`:
  - Population D-02 (26 Division literal `Accounting (ACC)`, `Administration (ADM)`, `Audit (AUD)`, `Business Development (BD)`, `Corporate Communication (CCM)`, `Customer Service (CSV)`, `Data Analytics (DA)`, `Engineering (ENG)`, `Facilities (FAC)`, `General Affairs (GA)`, `Information Technology (IT)`, `Internal Control (IC)`, `Logistics (LOG)`, `Marketing (MKT)`, `Procurement (PRC)`, `Product Management (PM)`, `Production (PRD)`, `Quality Assurance (QA)`, `Research and Development (RND)`, `Risk Management (RSK)`, `Sales (SLS)`, `Security (SEC)`, `Strategy (STR)`, `Supply Chain (SC)`, `Training (TRN)`, `Warehouse (WH)`). Nama literal tanpa suffix (pengecualian S-12) karena asersi urutan A-Z dan isi halaman 1 bergantung pada kumpulan nama ini. Hook `before` menghapus sisa D-03 bersuffix `-001` dari run lama; Population D-02 di-seed idempotent (dilewati bila sudah ada); cleanup di hook `after` hanya menghapus Division yang dibuat spec ini. Setelah seeding tabel berisi 32 Division (6 Pre-setup + 26 Population), halaman 1 berisi 10 baris, total 4 halaman.
  - D-03 (Division Name 120 karakter, milik spec ini): `Zzz ` + teks panjang + ` {runId}-001`, disusun sehingga panjang total tepat 120 karakter; Code `LONG120-001` (suffix nomor spec supaya tidak bentrok dengan Division D-03 pada spec lain). Berawalan `Zzz` supaya berurutan paling akhir pada sort Name A-Z dan tidak menggeser isi halaman 1 sampai 3 yang diasersi TC-GS-DIV-3. Dengan D-03 tabel berisi 33 baris (halaman 4 berisi `Treasury`, `Warehouse`, dan D-03).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus D-03 dan Division Population yang dibuat spec ini lewat API.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-division` lalu menyetelnya ke true supaya walkthrough otomatis tidak menutupi layar; hook `after` memulihkan nilai awal. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- Kemampuan teknis: hover elemen; membaca format tanggal dan jam General Settings yang berlaku (tidak diubah di spec ini).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas). Suite berjalan serial.

## Test Steps

### TC-GS-DIV-1: Screening halaman Global Settings > User > Division oleh Total Control

1. Buka Global Settings > User
2. Klik Tab Division
3. Verifikasi Header: Breadcrumb `User > Division`
4. Verifikasi Header: trigger Guided Tooltip `[?]` pada Breadcrumb
5. Verifikasi Header: Tab `User List | Position | Division | Custom Field`
6. Verifikasi Header: Tab `Division` berstatus aktif
7. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Division]`
8. Verifikasi Body: header kolom `Checkbox | Name (sortable) | Code (sortable) | Last Updated (sortable) | Actions (⋯) (unsortable)`
9. Klik header kolom Actions (⋯)
10. Verifikasi Overlay Column Visibility terbuka dengan item `Setup Column...` di dalamnya
11. Tutup Overlay Column Visibility dengan menekan Esc
12. Verifikasi Body: sedikitnya satu baris tampil di halaman 1
13. Verifikasi Body: setiap baris halaman 1 memiliki row action menu pada kolom Actions (⋯)
14. Verifikasi Footer: Pagination default 10 data per halaman

### TC-GS-DIV-2: Hover icon Table Tools menampilkan tooltip

15. Hover icon Search
16. Verifikasi tooltip `Search`
17. Hover icon Filter
18. Verifikasi tooltip `Filter`
19. Hover icon Download
20. Verifikasi tooltip `Download`
21. Hover icon Changelog
22. Verifikasi tooltip `Changelog`

### TC-GS-DIV-3: Urutan default tabel Division adalah Name A-Z (Body baris Pre-setup TC-GS-DIV-1 diverifikasi pada halaman tempat tiap baris berada)

23. Verifikasi 10 baris halaman 1 terurut ascending: `Accounting`, `Administration`, `Audit`, `Business Development`, `Compliance`, `Corporate Communication`, `Customer Service`, `Data Analytics`, `Engineering`, `Facilities`
24. Verifikasi ikon sort kolom Name menunjukkan ascending
25. Verifikasi ikon sort kolom Code netral
26. Verifikasi ikon sort kolom Last Updated netral
27. Verifikasi baris `Compliance` di halaman 1 menampilkan Name, Code, dan Last Updated terisi tanpa sel kosong
28. Klik halaman 2 pada Pagination
29. Verifikasi Division Pre-setup di halaman 2 tampil berurutan relatif `Finance`, `Human Resources`, `Legal`, `Operations`
30. Verifikasi baris `Finance`, `Human Resources`, `Legal`, dan `Operations` di halaman 2 menampilkan Name, Code, dan Last Updated terisi tanpa sel kosong
31. Klik halaman 4 pada Pagination
32. Verifikasi Division Pre-setup `Treasury` tampil di halaman 4, sesudah `Operations` di halaman 2
33. Verifikasi baris `Treasury` menampilkan Name, Code, dan Last Updated terisi tanpa sel kosong

### TC-GS-DIV-4: Isi sel kolom tabel Division dan nama panjang tidak terpotong

34. Temukan baris dengan Name 120 karakter (D-03, `{runId}-001`) di halaman 4
35. Verifikasi Name tampil utuh 120 karakter tanpa pemotongan `..`
36. Hover sel Name baris D-03
37. Verifikasi tidak ada tooltip pada sel Name
38. Verifikasi kolom Name melebar mengikuti isi
39. Verifikasi Code `LONG120-001` tampil terisi
40. Verifikasi Last Updated tampil memakai format tanggal dan jam General Settings, bukan `—`
41. Verifikasi tinggi baris tabel konsisten pada seluruh baris yang tampil di halaman 4

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (41 langkah) karena empat TC screening tab yang sama (satu kelas harness, screening) berjalan berurutan tanpa menutup halaman; tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna) dan hanya membaca data.
- Langkah 1 membuka layar karena membuka Global Settings > User dari menu adalah Langkah Uji TC-GS-DIV-1.
- Urutan TC sumber dipertahankan. Verifikasi Body baris Pre-setup TC-GS-DIV-1 (Name, Code, dan Last Updated terisi) dijalankan di langkah 27, 30, dan 33 pada halaman tempat tiap baris berada, bersama penelusuran halaman TC-GS-DIV-3, supaya halaman tidak ditelusuri dua kali. Dengan 32 baris atau lebih, baris Pre-setup tersebar di halaman 1 (`Compliance`), halaman 2 (`Finance`, `Human Resources`, `Legal`, `Operations`), dan halaman 4 (`Treasury`); pemetaan halaman dihitung dari urutan A-Z atas 33 nama (6 Pre-setup, 26 Population, D-03).
- TC-GS-DIV-1 langkah 9 sampai 11 dan Verifikasi langkah 13 menyatakan perilaku header Actions (⋯) dan row action menu yang tertulis di Expected Result Body TC-GS-DIV-1 (b.i). Langkah 12 (sedikitnya satu baris tampil di halaman 1) adalah anchor positif untuk asersi langkah 13 (S-03, bagian 8b butir 2); Expected TC-GS-DIV-1 tidak memuatnya.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 11 (tutup Overlay Column Visibility), 28 dan 31 (pindah halaman Pagination agar baris Pre-setup dan D-03 terlihat), 34 (menemukan baris D-03 di halaman 4), 36 (hover sel Name sebagai pemicu pengecekan tooltip, Expected TC-GS-DIV-4 a).
- Temuan untuk QA:
  - TC-GS-DIV-3 mengasumsikan tabel tepat 32 baris, sedangkan TC-GS-DIV-4 membutuhkan D-03 (120 karakter) sehingga tabel menjadi 33 baris. Spec memberi D-03 nama berawalan `Zzz` agar urutan halaman 1 sampai 3 tidak berubah; nama D-03 pada TC-GS-DIV-37 (`Divisions of Corporate Strategy ...`) berawalan `D` dan akan menggeser isi halaman 1. Code D-03 diberi suffix `-001` karena Code `LONG120` harus unik.
  - TC-GS-DIV-1 mensyaratkan hanya 6 Division Pre-setup, sedangkan Expected Result TC-GS-DIV-3 mensyaratkan 32 baris; spec memakai 32 baris (Population) untuk kedua TC.
  - TC-GS-DIV-4 Expected a ("tanpa tooltip") tidak diberi langkah hover di TC; spec menambah hover sebagai aksi pemicu (langkah 36). Expected d ("tinggi baris konsisten pada seluruh baris") tidak menyebut toleransi pengukuran; spec memeriksa baris yang tampil di halaman 4 (kolom lebar hanya muncul pada baris D-03).
  - TC-GS-DIV-4 Expected c tidak menyebut format tanggal dan jam yang berlaku; spec membaca format dari General Settings yang aktif.
  - TC-GS-DIV-2 tidak mencakup tooltip header Actions (⋯); tidak ditambahkan.
