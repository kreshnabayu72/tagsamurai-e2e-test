---
id: TC-GS-ROLE-E2E-029-assign-total-control-upgrade-read-only-dan-user-pending-email-confirmation
title: "Assign Total Control: Upgrade User Read Only dan User Pending Email Confirmation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-307
  - TC-GS-ROLE-60
coverage:
  web: automated
---

# Assign Total Control: Upgrade User Read Only dan User Pending Email Confirmation

## Prerequisites

- Mode: FE+BE.
- Akun aktor (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Akun kedua (langkah ganti akun di akhir spec): Siti Nurhaliza (Read Only; Pre-setup #4), email disediakan tim FE, password `Spectra.env.GS_RO_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`), termasuk akun Siti Nurhaliza.
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-029`; diubah dan dipulihkan sesuai catatan "Reset Pre-setup per TC" di `tc-role.md`):
  - Bagas Prasetyo (Pre-setup #18, Pending Email Confirmation, belum konfirmasi email, Access Global Settings dicentang, tanpa access level, tanpa baris role) (TC-GS-ROLE-307).
  - Siti Nurhaliza (Pre-setup #4, Finance Staff, Finance, Active) sebagai Read Only dengan baris role Manage TAG (TC-GS-ROLE-60).
- Pemulihan di hook `after`: Bagas Prasetyo kembali tanpa access level dan tanpa baris role; Siti Nurhaliza kembali ke Read Only dengan baris Manage TAG seperti Pre-setup #4 (termasuk Modified By dan Last Updated sejauh dapat dipulihkan).
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): mengatur access level dan baris role user Pre-setup lewat API untuk Given dan pemulihan; login UI sebagai Siti Nurhaliza di sesi yang sama setelah logout aktor; Overlay Notifikasi dapat dibuka dari akun Siti Nurhaliza.

## Test Steps

### TC-GS-ROLE-307: Pool dan Assign Total Control untuk user Pending Email Confirmation

1. Klik `[+ Assign]`
2. Verifikasi Bagas Prasetyo tampil di picker (semua halaman)
3. Verifikasi Bagas Prasetyo memiliki badge `Pending Email Confirmation` di sebelah Name
4. Centang Bagas Prasetyo
5. Klik `[Assign]`
6. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
7. Verifikasi baris Bagas Prasetyo muncul di Tab Total Control

### TC-GS-ROLE-60: Assign Total Control langsung ke user Read Only (upgrade)

8. Klik `[+ Assign]`
9. Centang Siti Nurhaliza
10. Klik `[Assign]`
11. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
12. Verifikasi baris Siti Nurhaliza tampil di Tab Total Control
13. Buka Tab Read Only
14. Ketik Search `Siti Nurhaliza`, tekan Enter
15. Verifikasi `No results found` tampil (Siti Nurhaliza tidak lagi di Tab Read Only)
16. Klik `(←)` pada kotak Search
17. Buka Tab System
18. Buka Detail "Manage user and role"
19. Verifikasi baris Siti Nurhaliza: Create, Read, Update, dan Delete checked
20. Logout, lalu login sebagai Siti Nurhaliza
21. Buka Overlay Notifikasi
22. Verifikasi Overlay Notifikasi tampil
23. Verifikasi notifikasi `Your Read Only access was removed` tidak ada di Overlay Notifikasi

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-ROLE-307 dijalankan pertama agar tidak ada ganti akun di tengah; TC-GS-ROLE-60 terakhir karena berakhir dengan login sebagai Siti Nurhaliza (langkah 20), lalu hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik `(←)` pada kotak Search (langkah 16) untuk mengosongkan Search sebelum pindah tab, membuka Tab Read Only dan Tab System (langkah 13 dan 17).
- Langkah 14 sampai 15 mewujudkan Expected TC-GS-ROLE-60 b ("tidak lagi di Tab Read Only") lewat Search; empty state `No results found` menjadi anchor positif absence (bagian 8b butir 2).
- Langkah 22 (Overlay Notifikasi tampil) menjadi anchor positif bagi asersi absence notifikasi pada langkah 23. TC-GS-ROLE-60 tidak menyebut notifikasi pembanding atau empty state Overlay Notifikasi.
- Temuan untuk QA:
  - TC-GS-ROLE-307 dan TC-GS-ROLE-60 menyebut "Centang <nama>" dan "Klik Detail" tanpa cara menemukan baris bila picker atau Detail lebih dari satu halaman; spec mengikuti TC dan mekanisme menemukan baris diputuskan di tahap script.
  - TC-GS-ROLE-60 Expected d tidak menyebut data pembanding untuk membuktikan Overlay Notifikasi sudah dimuat; spec memakai tampilnya Overlay Notifikasi sebagai anchor.
  - Pre-setup #18 TC-GS-ROLE-307 tidak menyebut pemulihan Bagas Prasetyo (Tabel Dinamis #17 menyatakan menjadi Total Control); spec memulihkannya di hook `after` agar dapat diulang.
