---
id: TC-GS-DIV-E2E-042-filter-panel-last-updated-clear-field-dan-reset-halaman
title: "Filter Panel Tabel Division: Screening, Last Updated, Clear Field, dan Reset Halaman"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-149
  - TC-GS-DIV-150
  - TC-GS-DIV-152
  - TC-GS-DIV-169
coverage:
  web: automated
---

# Filter Panel Tabel Division: Screening, Last Updated, Clear Field, dan Reset Halaman

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Last Updated keenam Division ini identik, lebih lama dari hari uji, dan tidak diubah TC mana pun (Tabel Data Uji Pre-setup TC).
- Tanggal pre-setup (`{tanggal pre-setup}`): teks tanggal pada sel Last Updated baris Pre-setup `Compliance` (urutan ke-5 pada sort default Name A-Z, sehingga ada di halaman 1 tabel 32 baris; Last Updated keenam Division Pre-setup identik; format mengikuti Date Format General Settings), dibaca sekali di hook `before` dan dipakai untuk memilih rentang tanggal di Filter Panel.
- Data Dinamis: Population D-02 (26 Division, Name (Code)): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada), sehingga tabel memuat 32 baris dan Last Updated Population = hari uji. Nama literal tanpa suffix karena asersi jumlah 32 baris dan pemisahan Pre-setup terhadap Population bergantung pada kumpulan nama ini (bagian 5 konvensi, S-12). Cleanup di hook `after` hanya menghapus Division Population yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: Filter Last Updated dikosongkan dan halaman dikembalikan ke halaman 1 di akhir spec; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): tabel harus memuat tepat 32 baris saat spec mulai.
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel; membaca teks sel Last Updated.

## Test Steps

### TC-GS-DIV-149: Screening Filter Panel Tabel Division

1. Verifikasi Filter Panel tersembunyi sebelum icon Filter diklik
2. Klik icon Filter
3. Verifikasi Filter Panel terbuka
4. Verifikasi satu-satunya field pada Filter Panel adalah `Last Updated`
5. Verifikasi field `Last Updated` bertipe date range picker
6. Verifikasi placeholder field `Last Updated` `Select date`
7. Verifikasi aksi `[Clear Field]`
8. Verifikasi aksi `[Apply]`
9. Verifikasi tidak ada field `Modified By`, `Division Name`, `Field`, atau `Action`

### TC-GS-DIV-150: Filter Last Updated menyaring baris dalam rentang tanggal

10. Pilih rentang tanggal `{tanggal pre-setup}` sampai `{tanggal pre-setup}` pada field `Last Updated` di Filter Panel yang masih terbuka
11. Klik `[Apply]`
12. Verifikasi tabel hanya menampilkan 6 Division Pre-setup: Compliance, Finance, Human Resources, Legal, Operations, Treasury
13. Verifikasi Division Population (hari uji) tidak tampil, mis. `Accounting`, `Facilities`, `Sales`
14. Verifikasi tabel berada di halaman 1

### TC-GS-DIV-152: Clear Field pada Filter Panel dan Apply mengembalikan seluruh data

15. Klik icon Filter
16. Klik `[Clear Field]`
17. Verifikasi field `Last Updated` kosong
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan seluruh 32 Division (halaman 1 berisi 10 baris, total 4 halaman)

### TC-GS-DIV-169: Apply Filter dari halaman lebih dari 1 mereset ke halaman 1

20. Pindah ke halaman 3 tabel
21. Klik icon Filter
22. Pilih rentang tanggal `{tanggal pre-setup}` sampai `{tanggal pre-setup}` pada field `Last Updated`
23. Klik `[Apply]`
24. Verifikasi tabel kembali ke halaman 1
25. Verifikasi tabel menampilkan hasil filter (hanya 6 Division Pre-setup)
26. Klik icon Filter
27. Klik `[Clear Field]`
28. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Dependensi TC-GS-DIV-30 (Population) dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (149, 150, 152, 169) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 26 sampai 28 mengosongkan Filter di akhir spec. Langkah 10 memakai Filter Panel yang masih terbuka dari TC-GS-DIV-149 (langkah 1 TC-GS-DIV-150 "Klik icon Filter" dipenuhi langkah 2). Langkah 1 TC-GS-DIV-152 (Filter rentang pre-setup lalu Apply) dipenuhi state akhir TC-GS-DIV-150.
- Penyimpangan urutan Expected TC-GS-DIV-152: `Verifikasi` field `Last Updated` kosong (langkah 17) ditaruh sebelum `[Apply]` karena field tersebut diamati langsung setelah `[Clear Field]`, selagi Filter Panel masih terbuka.
- Pembagian TC lintas spec: TC-GS-DIV-151 (teks tanggal pada input Date filter mengikuti Date Format General Settings) ada di spec 052; TC-GS-DIV-153 sampai 159 (kombinasi Search, Filter, Sort, Pagination) ada di spec 043.
- Asersi tambahan (konkretisasi Expected): langkah 19 ("seluruh data" TC-GS-DIV-152 ditulis 32 Division, halaman 1 berisi 10 baris, total 4 halaman) dan langkah 25 ("hasil filter" TC-GS-DIV-169 ditulis hanya 6 Division Pre-setup), keduanya turunan dari Population D-02 (26 Division) dan 6 Pre-setup.
- Temuan untuk QA:
  - TC-GS-DIV-150, 152, 169: tanggal pre-setup tidak disebut konkret di TC; spec membacanya dari sel Last Updated baris `Compliance` halaman 1 (Last Updated keenam Division Pre-setup identik menurut Tabel Data Uji Pre-setup TC).
  - TC-GS-DIV-150 Expected c ("Halaman kembali ke halaman 1") bermakna hanya bila tabel berada di halaman lain sebelum Apply; TC tidak menyatakannya, sehingga perilaku itu diasersi di TC-GS-DIV-169 (langkah 20 sampai 24) dan langkah 14 hanya mengamati halaman 1.
