---
id: TC-GS-NLU-E2E-023-create-dropdown-searchable-dan-represented-by-login-user-pending
title: "Create: dropdown searchable dan Represented By Login User pending"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-83
  - TC-GS-NLU-460
coverage:
  web: automated
---

# Create: dropdown searchable dan Represented By Login User pending

## Prerequisites

- Mode: FE+BE (backend nyata; opsi dropdown dan pool Represented By dibaca dari backend nyata, dan record hasil Create dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9, 10, dan 13, hanya dibaca): Position `Driver`, Division `Logistics`, Login User `Rina Putri` (Activated, email pending `rinaputri.baru@qwertysystem.net`, badge `Pending Email Confirmation`).
- Data Dinamis milik spec: Non-Login User `Pending Email {runId}-023` (First Name `Pending`, Last Name `Email {runId}-023`), Email `pendingemail+{runId}-023@qwertysystem.net`, Division `Logistics`, Represented By `Rina Putri`. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-023` lewat API (mekanisme disediakan tim FE/BE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-83: Dropdown Position dan Division searchable

1. Klik `[+ Non-Login User]`
2. Verifikasi placeholder Position `Select position` dan placeholder Division `Select division`
3. Klik dropdown Position
4. Verifikasi kotak pencarian Position berisi placeholder `Search position...`
5. Ketik `driv` pada kotak pencarian Position
6. Verifikasi daftar Position menyempit ke `Driver`
7. Pilih opsi `Driver`
8. Klik dropdown Division
9. Verifikasi kotak pencarian Division berisi placeholder `Search division...`
10. Ketik `logi` pada kotak pencarian Division
11. Verifikasi daftar Division menyempit ke `Logistics`
12. Pilih opsi `Logistics`
13. Klik `[Clear Field]`

### TC-GS-NLU-460: Login User Activated dengan email pending dapat dipilih sebagai Represented By

14. Isi First Name `Pending`, Last Name `Email {runId}-023`, dan Email `pendingemail+{runId}-023@qwertysystem.net`
15. Pilih Division `Logistics`
16. Klik `[+ Select User]`
17. Verifikasi baris `Rina Putri` tampil di popup Select User
18. Klik baris `Rina Putri`, klik `[Select]`
19. Verifikasi Represented By menampilkan `Rina Putri`
20. Klik `[Submit]`
21. Verifikasi toast sukses `Success, non-login user has been created.`
22. Ketik Search `Pending Email {runId}-023`, tekan Enter
23. Verifikasi sel Represented By pada baris `Pending Email {runId}-023` berisi `Rina P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 dan 12 (memilih opsi untuk menutup daftar dropdown), langkah 13 (`[Clear Field]` mengosongkan pilihan TC-GS-NLU-83 sebelum TC-GS-NLU-460), langkah 22 (Search untuk menemukan baris target; R-16).
- Temuan untuk QA:
  - TC-GS-NLU-460 Expected a ("dapat dipilih") tidak menyebut tampilan sesudah memilih; spec mengasersi Represented By terisi `Rina Putri` di langkah 19 sebagai tanda baris terpilih.
  - TC-GS-NLU-460 tidak menyebut cara menemukan baris yang baru dibuat; spec mencari lewat Name bersuffix di langkah 22 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
  - TC-GS-NLU-460 tidak menyebut cara menemukan baris `Rina Putri` di popup Select User (tanpa Search); spec mengikuti TC dan mengklik baris langsung. Badge `Pending Email Confirmation` pada Precondition tidak disebut di Expected sehingga tidak diasersi.
