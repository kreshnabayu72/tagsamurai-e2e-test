---
id: TC-FA-SU-E2E-110-bulk-actions-bar-user-list-screening-empat-elemen-ikon-severity-dan-label-select-all
title: "Bulk Actions Bar User List: Screening Empat Elemen, Ikon Severity, dan Label Select All"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1041
  - TC-FA-SU-1042
  - TC-FA-SU-1043
coverage:
  web: automated
---

# Bulk Actions Bar User List: Screening Empat Elemen, Ikon Severity, dan Label Select All

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Pengguna Pre-setup yang dicentang atau diamati (tanpa aksi tulis): Hana Kusuma (Pending Activation, Active), Kartika Sari (Pending Activation, Inactive), dan Indra Wijaya (Pending Email Confirmation). Ketiganya berada di halaman 1 pada default sort Name ascending.
- N pada `Select All ([N] records)` = 23 (25 pengguna dikurangi Default User dan akun sendiri, sesuai TC-FA-SU-1043).

## Test Steps

### TC-FA-SU-1041: Screening Bulk Actions Bar

1. Centang baris Hana Kusuma
2. Centang baris Kartika Sari
3. Verifikasi Bulk Actions Bar muncul dengan empat elemen berurutan dari kiri ke kanan: dropdown `Bulk Action`, counter `2 Users selected`, `Select All (23 records)`, dan ikon `(×)`
4. Klik `Bulk Action`
5. Verifikasi overlay `Bulk Action` memuat empat aksi: `Activate`, `Deactivate`, `Edit Home Group`, `Resend Activation Email`
6. Tutup overlay `Bulk Action` dengan Esc
7. Klik ikon `(×)` pada Bulk Actions Bar
8. Verifikasi Bulk Actions Bar tertutup
9. Verifikasi seleksi baris Hana Kusuma dan Kartika Sari dikosongkan

### TC-FA-SU-1042: Ikon dan severity row action serta aksi Bulk Actions Bar

10. Klik ⋯ pada baris Hana Kusuma
11. Verifikasi row action `Detail` berikon `FileInfoLine`, `Edit Home Group` berikon `Edit2Line`, dan `Resend Activation Email` berikon `MailSendLine`, seluruhnya severity dark
12. Tutup menu row action dengan Esc
13. Klik ⋯ pada baris Indra Wijaya
14. Verifikasi row action `Resend Confirmation Email` berikon `MailSendLine` dengan severity dark
15. Tutup menu row action dengan Esc
16. Centang baris Hana Kusuma dan Kartika Sari
17. Klik `Bulk Action`
18. Verifikasi aksi overlay: `Activate` berikon `CheckLine`, `Deactivate` berikon `CloseLine`, `Edit Home Group` berikon `Edit2Line`, `Resend Activation Email` berikon `MailSendLine`, seluruhnya severity dark
19. Tutup overlay dengan Esc, lalu klik ikon `(×)` pada Bulk Actions Bar

### TC-FA-SU-1043: Label Select All singular dan plural

20. Klik icon Search, ketik `Hana`, tekan Enter
21. Centang satu-satunya baris hasil
22. Verifikasi tombol `Select All (1 record)` tampil
23. Klik ikon `(×)` pada Bulk Actions Bar
24. Klik `(←)` pada kotak Search
25. Centang baris pertama pada tabel
26. Verifikasi tombol `Select All (23 records)` tampil
27. Verifikasi counter `1 User selected` tampil
28. Klik ikon `(×)` pada Bulk Actions Bar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 6, 12, 15, 19 (menutup overlay dan menu), 16 (mencentang kembali baris untuk langkah 3 TC-FA-SU-1042), 23 dan 28 (membersihkan seleksi, S-09), dan 24 (menutup Search).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1043 langkah 4 ("Hapus Search lalu centang satu baris") tidak menyebut nasib seleksi Hana Kusuma; Expected b menyebut counter `1 User selected`, sehingga spec membersihkan seleksi sebelum mencentang baris berikutnya (langkah 23). (2) TC-FA-SU-1041 memakai `Select All ([N] records)` tanpa nilai N; N = 23 diambil dari Expected TC-FA-SU-1043.
