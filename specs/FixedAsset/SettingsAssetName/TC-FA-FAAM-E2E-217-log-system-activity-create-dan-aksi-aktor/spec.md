---
id: TC-FA-FAAM-E2E-217-log-system-activity-create-dan-aksi-aktor
title: "Log Multi-Surface: System Log Aktor dan Activity Log FAMS untuk Create dan Aksi Aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-579
  - TC-FA-FAAM-580
  - TC-FA-FAAM-734
coverage:
  web: automated
---

# Log Multi-Surface: System Log Aktor dan Activity Log FAMS untuk Create dan Aksi Aktor

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`), No. 23 (Brand `Dell`), No. 24 (UoM `Unit`, `Pcs`), No. 25 (Label).
- Data Dinamis:
  - `Log Surface Item 734 {runId}-217` (Tabel Data Uji Dinamis No. 104): dibuat lewat UI pada TC-FA-FAAM-734 dengan Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`.
  - `Log Actor Item {runId}-217`: di-seed lewat sesi API aktor Total Control di hook `before` (Create lalu Edit UoM `Unit` menjadi `Pcs`, hingga tersimpan) sebagai precondition TC-FA-FAAM-579 dan 580 ("aktor telah Create dan Edit Asset Name"); dipakai sebagai precondition TC, nilai kolomnya diasersi.
- Kemampuan teknis: membuka Detail User aktor > tab System Log dan Activity Log FAMS beserta Search di dalamnya; sesi API aktor. System Log dan Activity Log adalah audit trail permanen sehingga entri dicari lewat Search atas nama bersuffix unik (baseline nol) dan total entri tidak diasersi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Log Surface Item 734 {runId}-217` dan `Log Actor Item {runId}-217` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-579, 580, 734: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-734: Create menulis satu baris Create di System Log aktor dan Activity Log FAMS

1. Klik `[+ Asset Name]`
2. Isi Asset Name `Log Surface Item 734 {runId}-217`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Klik `[Submit]`
4. Buka Detail User aktor lalu tab System Log
5. Ketik Search `Log Surface Item 734 {runId}-217`, tekan Enter
6. Verifikasi kolom System Log `Date | Action | Object | Name | Field | Old Value | New Value` tanpa kolom Modified By
7. Verifikasi satu baris Action `Create`, Object `Asset Name`, Name `Log Surface Item 734 {runId}-217`, Field `Asset Name`, Old `—`, New `Log Surface Item 734 {runId}-217`
8. Buka Activity Log FAMS
9. Ketik Search `Log Surface Item 734 {runId}-217`, tekan Enter
10. Verifikasi kolom Activity Log sama dengan System Log ditambah `Modified By`
11. Verifikasi baris Create yang sama dengan Modified By `[First Name] [Last Initial]` aktor
12. Verifikasi pada kedua log hanya ada satu baris untuk `Log Surface Item 734 {runId}-217` (atribut konfigurasi awal lain tidak dicatat per baris)

### TC-FA-FAAM-580: Activity Log FAMS memuat aksi Asset Name

13. Ganti isi kotak search dengan `Log Actor Item {runId}-217`, tekan Enter
14. Verifikasi kolom `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`
15. Verifikasi Object `Asset Name`
16. Verifikasi Name `Log Actor Item {runId}-217` (nama sesudah kejadian)
17. Verifikasi Modified By `[First Name] [Last Initial]`

### TC-FA-FAAM-579: System Log Detail User aktor memuat aksi Asset Name

18. Buka Detail User aktor lalu tab System Log
19. Ketik Search `Log Actor Item {runId}-217`, tekan Enter
20. Verifikasi kolom `Date | Action | Object | Name | Field | Old Value | New Value` tanpa kolom Modified By
21. Verifikasi Object `Asset Name`
22. Verifikasi Name `Log Actor Item {runId}-217` (nama sesudah kejadian)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 5, 9, 13, 19 (Search nama bersuffix pada audit trail permanen; S-12, S-14).
- Urutan TC: TC-FA-FAAM-734, TC-FA-FAAM-580, lalu TC-FA-FAAM-579 agar navigasi antar surface log minimal; tidak ada ketergantungan data antar TC.
- Langkah 4 sampai 12 dan 18 sampai 22 adalah blok baca-log berpola (buka surface, cari entri, Verifikasi kolom log).
- Temuan untuk QA:
  - TC-FA-FAAM-734 tidak menyebut model untuk Brand `Dell` pada Data Uji; spec mengisi sesuai Data Uji TC apa adanya.
  - Nama dan Modified By aktor Total Control tidak tertulis di Pre-setup No. 1; langkah 11 dan 17 mengasersi format `[First Name] [Last Initial]`.
  - TC-FA-FAAM-579 dan 580 tidak menyebut cara menemukan entri aktor pada log permanen; spec memakai Search atas nama bersuffix.
  - Isi Edit pada seed `Log Actor Item` (UoM `Unit` menjadi `Pcs`) dipilih spec karena TC hanya menyebut "Create dan Edit".
