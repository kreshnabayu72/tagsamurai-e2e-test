---
id: TC-AC-SU-E2E-161-pelepasan-group-manager-akibat-delete-group
title: "Hapus Group di Settings > Group Dicatat sebagai Remove (Group Deleted), Dicatat di Tab System Log dan Activity Log, dan Memperbarui Banner Group Manager tanpa Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-546
  - TC-AC-SU-602
  - TC-AC-SU-640
coverage:
  web: automated
---

# Hapus Group di Settings > Group Dicatat sebagai Remove (Group Deleted), Dicatat di Tab System Log dan Activity Log, dan Memperbarui Banner Group Manager tanpa Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke user target (U3) dilakukan eksplisit pada langkah 19 untuk mengamati notifikasi; password user target seeding dari `Spectra.env.AC_SU_SEEDED_PASSWORD` (nama env baru, didaftarkan pemilik repo). Hook `after` memulihkan sesi ke Default User.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Group dan user milik spec (group Pre-setup tidak dihapus; Region A dari Group Tree Pre-setup hanya menjadi group Group Manager yang tidak dihapus):

| Kode | Name / Group | Email | State awal |
|---|---|---|---|
| G1 | `Region C {runId}-161A` | - | group milik spec, tanpa user lain, lolos validasi hapus Settings > Group |
| G2 | `Region C {runId}-161B` | - | group milik spec, tanpa user lain, lolos validasi hapus |
| G3 | `Region C {runId}-161C` | - | group milik spec, tanpa user lain, lolos validasi hapus |
| U1 | `Dedi Kurnia {runId}-161A` | `dedikurnia+{runId}-161a@qwertysystem.net` | Group Manager di G1 |
| U2 | `Dedi Kurnia {runId}-161B` | `dedikurnia+{runId}-161b@qwertysystem.net` | Group Manager di G2 |
| U3 | `Dedi Kurnia {runId}-161C` | `dedikurnia+{runId}-161c@qwertysystem.net` | Group Manager di Region A dan G3, Activated, dapat login, sudah memiliki satu notifikasi lain (anchor, dipakai sebagai precondition TC, tidak diasersi selain keberadaannya) |

- Kemampuan teknis: Fixture BE (seeding group, user, Group Manager, dan satu notifikasi anchor untuk U3; pembacaan Tab System Log lewat UI). Jendela tunggu 5 detik tanpa memuat ulang halaman sebelum asersi absence notifikasi adalah pilihan spec (bukan nilai TC atau PRD). Tanpa intercept dan klien HTTP.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-546: Popup Changelog mencatat Remove (Group Deleted)
1. Klik menu Settings > Group di sidebar, lalu hapus group G1 (`Region C {runId}-161A`)
2. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
3. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
4. Ketik Search `Dedi Kurnia {runId}-161A` pada Popup Changelog: User, tekan Enter
5. Verifikasi 1 baris untuk U1: Action `Remove (Group Deleted)`, User Name `Dedi Kurnia {runId}-161A`, Field `Group Manager — Region C {runId}-161A`, Old Value `Assigned`, New Value `—`, Modified By `Default User`
6. Verifikasi tidak ada baris lain untuk U1 (pelepasan assignment Group Role di G1 tidak dicatat)
### TC-AC-SU-640: Tab System Log dan Activity Log mencatat pelepasan Group Manager
7. Tutup Popup Changelog: User, klik menu Settings > Group di sidebar, lalu hapus group G2 (`Region C {runId}-161B`)
8. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
9. Ketik Search nama tampil Default User, tekan Enter, klik Name baris Default User untuk membuka Detail, lalu klik Tab System Log
10. Ketik Search `Dedi Kurnia {runId}-161B` pada Tab System Log, tekan Enter
11. Verifikasi 1 baris: Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Dedi Kurnia {runId}-161B`, Field `Group Manager — Region C {runId}-161B`, Old Value `Assigned`, New Value `—`
12. Verifikasi tidak ada baris lain untuk `Dedi Kurnia {runId}-161B` (pelepasan assignment Group Role di G2 tidak dicatat)
13. Klik menu Admin Console > Activity Log di sidebar, lalu ketik Search `Dedi Kurnia {runId}-161B`, tekan Enter
14. Verifikasi baris Activity Log yang sama (Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Dedi Kurnia {runId}-161B`, Field `Group Manager — Region C {runId}-161B`, Old Value `Assigned`, New Value `—`) dengan Modified By `Default User`
### TC-AC-SU-602: Banner Group Manager diperbarui dan tanpa notifikasi in-app
15. Klik menu Settings > Group di sidebar, lalu hapus group G3 (`Region C {runId}-161C`)
16. Tunggu aksi selesai, lalu klik menu Settings > User di sidebar
17. Ketik Search `Dedi Kurnia {runId}-161C`, tekan Enter, klik Name baris U3 untuk membuka Detail, lalu klik Tab Role
18. Verifikasi banner `"This user is a Group Manager for: Region A."`
19. Lakukan Logout dari akun Default User
20. Login sebagai U3 (`dedikurnia+{runId}-161c@qwertysystem.net`), lalu klik lonceng notifikasi navbar
21. Verifikasi notifikasi anchor milik U3 yang sudah ada tampil di daftar
22. Tunggu 5 detik tanpa memuat ulang halaman
23. Verifikasi daftar notifikasi U3 tidak memuat notifikasi baru "You are no longer Group Manager for Region C {runId}-161C"

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar dan pembukaan Detail (langkah 9, 17), Search nama user pada Popup Changelog, Tab System Log, dan Activity Log (langkah 4, 10, 13, R-16; user bernama unik sehingga baseline entri nol), menutup popup, serta jendela tunggu 5 detik sebelum asersi absence notifikasi (bagian 6, pilihan spec).
- Urutan: ganti akun eksplisit pada langkah 19 ke user target di akhir spec karena Expected TC-602 butir b mengamati notifikasi U3 (sesi UI berurutan di browser yang sama, bukan konteks kedua bersamaan). TC-586 dan TC-601 ada di spec 199.
- Spec berisi tiga blok TC dengan aktor Default User; 23 langkah wajar untuk tiga blok yang berdiri sendiri (group dan user seeding sendiri per blok).
- Temuan untuk QA:
  - TC-546 butir b dan TC-640 butir c menyebut "tidak ada baris log untuk pelepasan assignment Group Role" tanpa menyebut surface; spec mengasersinya pada surface yang sedang diamati (Popup Changelog: User untuk TC-546; Tab System Log untuk TC-640) lewat Search nama user.
  - TC-602 butir b ("Tidak ada notifikasi in-app ke Dedi Kurnia") tidak menyebut anchor atau akun target; spec men-seed satu notifikasi anchor untuk U3 dan memakai password env baru `AC_SU_SEEDED_PASSWORD`.
  - TC memakai `Region C` dan `Dedi Kurnia` literal; Region C bukan bagian Group Tree Pre-setup, sehingga spec men-seed group bersuffix agar penghapusan tidak mengenai data Pre-setup (S-06, S-12).
  - TC-640 menyebut "Buka Settings > User > Detail milik Default User"; nama tampil akun Default User tidak tertulis di Pre-setup TC (hanya email).
  - Post Condition TC-546 butir c ("Pelepasan Group Role — Tidak dicatat di surface mana pun") tidak punya langkah observasi di semua surface; hanya surface yang disebut di atas yang diasersi.
