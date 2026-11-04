---
id: TC-AC-SU-E2E-165-resend-dan-bulk-resend-entri-log-changelog
title: "Resend Activation Email Menulis Entri Changelog di Background dan Bulk Resend Hanya Mencatat Baris yang Diproses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-575
  - TC-AC-SU-578
coverage:
  web: automated
---

# Resend Activation Email Menulis Entri Changelog di Background dan Bulk Resend Hanya Mencatat Baris yang Diproses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Data Dinamis:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Sarah Lee {runId}-165A` | `sarahlee+{runId}-165a@qwertysystem.net` | Pending Activation, di luar cooldown Resend (blok TC-578) |
| U2 | `Sarah Lee {runId}-165B` | `sarahlee+{runId}-165b@qwertysystem.net` | Pending Activation, di luar cooldown Resend (blok TC-575) |
| U3 | `Mike Tan {runId}-165C` | `miketan+{runId}-165c@qwertysystem.net` | Pending Activation, masih dalam cooldown Resend (blok TC-575) |

- Kemampuan teknis: Fixture BE (seeding user dan cooldown Resend U3: Resend terakhir U3 dibuat pada waktu T oleh seeding, dibaca dari Fixture BE). Untuk menjaga U3 tetap dalam cooldown 60 detik selama blok TC-575, jam server dan jam browser dibekukan pada T + 10 detik (T dicatat pada langkah 6, jam dibekukan pada langkah 7) dan dipulihkan di hook `after` (bagian 6 konvensi); blok TC-578 berjalan sebelum jam dibekukan. Baseline jumlah entri Changelog nol karena nama unik. Polling Popup Changelog: User tiap 5 detik dengan batas tunggu 30 detik mengikuti TC-578. Tanpa intercept dan klien HTTP.
- State global yang diubah spec: jam server dan jam browser (dibekukan lalu dipulihkan di hook `after`); suite serial (`parallel: false`).

## Test Steps

### TC-AC-SU-578: Entri Resend ditulis di background
1. Ketik Search `Sarah Lee {runId}-165A`, tekan Enter
2. Buka row action (⋯) baris U1, lalu klik Resend Activation Email
3. Verifikasi toast `"Success, email has been sent."` tampil tanpa menunggu entri log
4. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka, lalu ketik Search `Sarah Lee {runId}-165A`, tekan Enter; tutup dan buka ulang popup tiap 5 detik sampai entri muncul (batas tunggu 30 detik)
5. Verifikasi entri Action `Resend Activation Email` untuk U1 muncul dalam jendela tunggu
### TC-AC-SU-575: Bulk Resend partial
6. Tutup popup, catat T dari waktu Resend terakhir U3 lewat Fixture BE
7. Bekukan jam server dan jam browser pada T + 10 detik
8. Ganti isi kotak Search dengan `{runId}-165`, tekan Enter
9. Centang checkbox baris U2 (`Sarah Lee {runId}-165B`) dan baris U3 (`Mike Tan {runId}-165C`)
10. Klik `[Bulk Action]`, lalu pilih Resend Activation Email
11. Verifikasi toast partial `"Success, email has been sent. Some items were skipped."`
12. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka, lalu ketik Search `{runId}-165`, tekan Enter; tutup dan buka ulang popup tiap 5 detik sampai entri U2 muncul (batas tunggu 30 detik)
13. Verifikasi entri Action `Resend Activation Email` untuk U2 muncul (anchor)
14. Verifikasi Changelog hanya berisi 1 baris Resend Activation Email untuk U2
15. Verifikasi tidak ada entri untuk U3 (`Mike Tan {runId}-165C`)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search untuk menemukan baris target (R-16), menutup popup, polling Popup Changelog: User, pencatatan T (langkah 6), dan pembekuan jam (langkah 7).
- Urutan: TC-578 sebelum TC-575 agar jam dibekukan hanya pada blok yang membutuhkannya (S-10).
- P-1: asersi tidak adanya entri untuk U3 pada TC-575 butir c bergantung pada state berat yang dibangun di spec ini (U3 dalam cooldown lewat seeding Resend dan jam dibekukan) dan didahului anchor positif (entri U2 pada surface yang sama, bagian 8b butir 2), sehingga tetap di spec ini dan tidak dipindah ke spec absence.
- Kelas d: yang diuji adalah penulisan entri log di background (eventual) setelah email terkirim; email tidak diasersi karena tidak ada di Expected TC.
- Temuan untuk QA:
  - Post Condition TC-575 (Activity Log dan System Log aktor dicatat hanya untuk Sarah Lee) dan TC-578 (Changelog, System Log, Activity Log dicatat eventual) tanpa langkah observasi di TC tidak diasersi kecuali Changelog (Expected TC-578 butir b).
  - TC-575 tidak menyatakan cara membuat Mike Tan masih dalam cooldown; spec memakai seeding Resend terakhir dan jam dibekukan (kemampuan disediakan tim FE/BE).
  - TC memakai nama literal `Sarah Lee` dan `Mike Tan`; spec memakai nama bersuffix (S-12).
