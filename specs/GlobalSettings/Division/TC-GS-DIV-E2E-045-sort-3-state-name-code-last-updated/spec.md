---
id: TC-GS-DIV-E2E-045-sort-3-state-name-code-last-updated
title: "Sort 3-State Tabel Division: Name, Code, Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-163
  - TC-GS-DIV-164
  - TC-GS-DIV-165
coverage:
  web: automated
---

# Sort 3-State Tabel Division: Name, Code, Last Updated

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Last Updated keenam Division ini identik (Tabel Data Uji Pre-setup TC), lebih lama dari hari uji, dan tidak diubah TC mana pun, sehingga urutan antar-Division Pre-setup pada sort Last Updated tidak diasersi.
- Data Dinamis: Population D-02 (26 Division, Name (Code)): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada), sehingga tabel memuat 32 baris dan Last Updated Population = hari uji (lebih baru dari Pre-setup). Nama literal tanpa suffix karena asersi urutan A-Z dan Z-A halaman 1 bergantung pada kumpulan nama dan kode ini (pengecualian S-12 untuk Population Division: seeding idempotent, cleanup milik spec, suite serial). Cleanup di hook `after` hanya menghapus Division Population yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Urutan yang diasersi pada halaman 1 (page size 10, 32 baris):
  - Name A-Z: Accounting, Administration, Audit, Business Development, Compliance, Corporate Communication, Customer Service, Data Analytics, Engineering, Facilities.
  - Name Z-A: Warehouse, Treasury, Training, Supply Chain, Strategy, Security, Sales, Risk Management, Research and Development, Quality Assurance.
  - Code A-Z: ACC, ADM, AUD, BD, CCM, CMP, CSV, DA, ENG, FAC.
  - Code Z-A: WH, TRS, TRN, STR, SLS, SEC, SC, RSK, RND, QA.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: sort tabel kembali ke default Name A-Z di akhir tiap TC; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): tabel harus memuat tepat 32 baris (Pre-setup + Population) saat spec mulai.

## Test Steps

### TC-GS-DIV-165: Kolom checkbox dan Actions (⋯) tidak memiliki ikon sort

1. Verifikasi header kolom Checkbox tidak memiliki ikon sort
2. Verifikasi header kolom Actions (⋯) tidak memiliki ikon sort

### TC-GS-DIV-163: Sort 3-state kolom teks Name dan Code

3. Klik header Name
4. Verifikasi Name ascending A-Z pada halaman 1: `Accounting`, `Administration`, `Audit`, `Business Development`, `Compliance`, `Corporate Communication`, `Customer Service`, `Data Analytics`, `Engineering`, `Facilities`
5. Klik header Name
6. Verifikasi Name descending Z-A pada halaman 1: `Warehouse`, `Treasury`, `Training`, `Supply Chain`, `Strategy`, `Security`, `Sales`, `Risk Management`, `Research and Development`, `Quality Assurance`
7. Klik header Name
8. Verifikasi Name kembali ke default Name A-Z (urutan halaman 1 sama dengan langkah 4)
9. Klik header Code
10. Verifikasi Code ascending A-Z pada halaman 1: `ACC`, `ADM`, `AUD`, `BD`, `CCM`, `CMP`, `CSV`, `DA`, `ENG`, `FAC`
11. Klik header Code
12. Verifikasi Code descending Z-A pada halaman 1: `WH`, `TRS`, `TRN`, `STR`, `SLS`, `SEC`, `SC`, `RSK`, `RND`, `QA`
13. Klik header Code
14. Verifikasi Code kembali ke default sort tabel Name A-Z (urutan halaman 1 sama dengan langkah 4)

### TC-GS-DIV-164: Sort 3-state kolom Last Updated

15. Klik header Last Updated
16. Verifikasi Oldest First: 6 baris pertama adalah Division Pre-setup (`Compliance`, `Finance`, `Human Resources`, `Legal`, `Operations`, `Treasury`)
17. Klik header Last Updated
18. Verifikasi Newest First: 10 baris halaman 1 seluruhnya Division Population dan tidak ada Division Pre-setup
19. Klik header Last Updated
20. Verifikasi Last Updated kembali ke default sort Name A-Z (urutan halaman 1 sama dengan langkah 4)

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Dependensi TC-GS-DIV-30 (Population) dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-165 (screening tanpa aksi) ditaruh di awal (sumber 163, 164, 165) mengikuti prinsip 2 konvensi bagian 3.
- Langkah penghubung: tidak ada; tiap TC berakhir pada klik ketiga yang mengembalikan sort ke default.
- Pembagian TC lintas spec: TC-GS-DIV-155 sampai 158 (sort dalam kombinasi dengan Search dan Filter) ada di spec 043.
- Temuan untuk QA:
  - TC-GS-DIV-163: Name default sort adalah Name A-Z, sehingga klik 1 (ascending) dan klik 3 (default) menghasilkan urutan yang sama; keduanya dibedakan lewat langkah klik yang bernomor, bukan lewat urutan baris.
  - TC-GS-DIV-164: Last Updated keenam Division Pre-setup identik, sehingga urutan antar-baris Pre-setup tidak diasersi.
  - TC-GS-DIV-164: Newest First menaruh Division Population di atas; TC tidak menyatakan urutan antar-Division Population yang dibuat pada hari yang sama, sehingga hanya komposisi halaman 1 yang diasersi.
