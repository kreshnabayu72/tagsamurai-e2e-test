---
id: TC-AC-SU-E2E-199-hapus-group-tanpa-notifikasi-dan-assignment-group-role-terakhir
title: "Hapus Group Tidak Mengirim Notifikasi ke Group Manager yang Dilepas dan Menonaktifkan Group Role pada Assignment Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-586
  - TC-AC-SU-601
coverage:
  web: automated
---

# Hapus Group Tidak Mengirim Notifikasi ke Group Manager yang Dilepas dan Menonaktifkan Group Role pada Assignment Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor blok TC-586: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Akun aktor blok TC-601: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login Default User di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke user target (langkah 2) dan ke Total Control (langkah 7) dilakukan eksplisit; password user target seeding dari `Spectra.env.AC_SU_SEEDED_PASSWORD` (nama env baru, didaftarkan pemilik repo). Hook `after` memulihkan sesi ke Default User.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Group dan user milik spec (group Pre-setup tidak dihapus):

| Kode | Name / Group | Email | State awal |
|---|---|---|---|
| G1 | `Region C {runId}-199A` | - | group milik spec, tanpa user lain, lolos validasi hapus Settings > Group |
| G2 | `Region B {runId}-199B` | - | group milik spec, lolos validasi hapus |
| U1 | `Dedi Kurnia {runId}-199A` | `dedikurnia+{runId}-199a@qwertysystem.net` | Activated, dapat login, Group Manager di G1, sudah memiliki satu notifikasi lain (anchor, dipakai sebagai precondition TC, tidak diasersi selain keberadaannya) |
| U2 | `Mike Tan {runId}-199B` | `miketan+{runId}-199b@qwertysystem.net` | Activated, "Manage partner" aktif hanya di G2 |
| - | Role Count awal U2 | - | dibaca dari User List sebelum group dihapus |

- Kemampuan teknis: Fixture BE (seeding group, user, Group Manager, role, dan satu notifikasi anchor untuk U1). Jendela tunggu 5 detik tanpa memuat ulang halaman sebelum asersi absence notifikasi adalah pilihan spec (bukan nilai TC atau PRD). Tanpa intercept dan klien HTTP.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-586: Tidak ada notifikasi saat Group Manager dilepas akibat hapus group
1. Klik menu Settings > Group di sidebar, lalu hapus group G1 (`Region C {runId}-199A`)
2. Tunggu aksi selesai, lalu lakukan Logout dari akun Default User
3. Login sebagai U1 (`dedikurnia+{runId}-199a@qwertysystem.net`), lalu klik lonceng notifikasi navbar
4. Verifikasi notifikasi anchor milik U1 yang sudah ada tampil di daftar
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Verifikasi daftar notifikasi U1 tidak memuat notifikasi baru "You are no longer Group Manager for Region C {runId}-199A"
### TC-AC-SU-601: Group Role tidak aktif saat assignment terakhir dihapus
7. Lakukan Logout dari akun U1
8. Login sebagai Total Control, lalu klik menu Settings > User di sidebar
9. Ketik Search `Mike Tan {runId}-199B`, tekan Enter, lalu catat Role Count pada baris U2
10. Klik menu Settings > Group di sidebar, lalu hapus group G2 (`Region B {runId}-199B`)
11. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
12. Ketik Search `Mike Tan {runId}-199B`, tekan Enter, klik Name baris U2 untuk membuka Detail, klik Tab Role, lalu sub-tab Group Role
13. Verifikasi role "Manage partner" tidak aktif
14. Verifikasi kolom Group pada baris "Manage partner" bernilai `—`
15. Klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-199B`, tekan Enter
16. Verifikasi Role Count pada baris U2 berkurang 1 dari nilai yang dicatat pada langkah 9
17. Klik Name baris U2 untuk membuka Detail, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog toolbar sehingga Modal Changelog: User > Group Role terbuka
18. Verifikasi modal tidak memuat baris log untuk pelepasan Group Role akibat hapus group

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search untuk menemukan baris target (langkah 9, 12, R-16), pencatatan Role Count awal, dan jendela tunggu 5 detik sebelum asersi absence notifikasi (bagian 6).
- Ganti akun eksplisit pada langkah 2 (TC-586 mengamati notifikasi U1) dan 7 (TC-601 mensyaratkan Total Control); sesi UI berurutan, bukan konteks kedua bersamaan. TC-546, TC-602, dan TC-640 ada di spec 161.
- Asersi absence TC-601 butir d didahului Verifikasi butir a sampai c yang membuktikan Detail dan User List sudah memuat hasil hapus group (anchor). Pengecekan Role Count dilakukan lewat pembacaan User List sebelum dan sesudah hapus.
- Temuan untuk QA:
  - TC-586 tidak menyebut anchor atau akun target dengan notifikasi lama; spec men-seed satu notifikasi anchor untuk U1 dan memakai password env baru `AC_SU_SEEDED_PASSWORD`.
  - TC-601 memakai Region B Pre-setup sebagai group yang dihapus; spec memakai group milik spec bersuffix agar Pre-setup tidak dihapus (S-06).
  - TC-601 butir d ("Tidak ada entri log untuk pelepasan Group Role") tidak menyebut surface; spec mengasersi di Modal Changelog: User > Group Role sesuai langkah 3 TC.
  - TC-586 dan TC-601 memakai nama literal (`Dedi Kurnia`, `Mike Tan`, `Region C`, `Region B`); spec memakai nama bersuffix (S-12).
