---
id: TC-AC-SU-E2E-183-defense-in-depth-cooldown-resend-read-only-dan-payload-script
title: "Defense-in-Depth Request Langsung Ditolak untuk Group Role tanpa Assignment, Cooldown Resend, Aksi Read Only, dan Target Total Control, serta Payload Script Dirender sebagai Teks"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-620
  - TC-AC-SU-621
  - TC-AC-SU-622
  - TC-AC-SU-624
  - TC-AC-SU-665
coverage:
  web: automated
---

# Defense-in-Depth Request Langsung Ditolak untuk Group Role tanpa Assignment, Cooldown Resend, Aksi Read Only, dan Target Total Control, serta Payload Script Dirender sebagai Teks

## Prerequisites

- Mode: FE+BE.
- Akun UI aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`, login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun UI di tengah spec; hook `after` memulihkan sesi ke akun default suite.
- Sesi API tiap aktor request (login API password; token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE):

| Blok | Aktor request | Akun | Password |
|---|---|---|---|
| TC-620, TC-621 | Total Control | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-622 | Read Only | `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |
| TC-665 | Manage user and role (Update, U=true) | `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_MUR_UPDATE_PASSWORD` |

- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Data milik spec:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-183A` | `miketan+{runId}-183a@qwertysystem.net` | Activated, tanpa tier, "Manage partner" tanpa group assignment (TC-620) |
| U2 | `Sarah Lee {runId}-183B` | `sarahlee+{runId}-183b@qwertysystem.net` | Pending Activation, di luar cooldown Resend (TC-621) |
| U3 | `John Doe {runId}-183C` | `johndoe+{runId}-183c@qwertysystem.net` | Activated, Active (TC-622) |
| U4 | `Dewi Lestari {runId}-183D` | `dewilestari+{runId}-183d@qwertysystem.net` | Activated, Active, bertier Total Control (TC-665) |
| U5 | `Mike Tan {runId}-183E` | `miketan+{runId}-183e@qwertysystem.net` | Activated, Position di Global Settings bernilai `<script>alert(1)</script>` (TC-624; dipulihkan di hook `after`) |

- Kemampuan teknis (kelas a): klien HTTP yang mengirim request langsung ke server atas nama aktor tiap blok; pola request (path dan body) disediakan tim FE/BE tanpa endpoint karangan di spec; Fixture BE untuk membaca state data; mail-catcher untuk membaca jumlah email per alamat (baseline sebelum aksi, TC-621); jam server dan jam browser dibekukan pada T + 10 detik agar request kedua berada dalam jendela 60 detik (margin 60 − 10 = 50 detik), dipulihkan di hook `after`; T dibaca dari waktu terbit entri Resend pertama lewat API seeding (bukan perkiraan dari jam hook). Entri Resend ditulis asinkron: langkah "Tunggu aksi selesai" membaca kemampuan baca tiap 5 detik sampai entri terbaca, batas tunggu 30 detik. Tanpa intercept.
- State global yang diubah spec: jam server dan jam browser; suite berjalan serial (`parallel: false`).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-620: Flag aktif Group Role tanpa assignment
1. Kirim request langsung yang mengirim flag aktif untuk "Manage partner" U1 (`Mike Tan {runId}-183A`) tanpa group assignment atas nama aktor Total Control
2. Verifikasi respons server berupa penolakan hak akses (bukan 2xx)
3. Verifikasi Fixture BE: role "Manage partner" U1 tetap tidak aktif (0 group)
### TC-AC-SU-622: Aksi tulis Read Only
4. Kirim request langsung untuk menonaktifkan U3 (`John Doe {runId}-183C`) atas nama aktor Read Only
5. Verifikasi respons server berupa penolakan (bukan 2xx)
6. Verifikasi Fixture BE: U3 tetap Active
### TC-AC-SU-665: Deactivate target Total Control oleh Manage user and role
7. Kirim request langsung untuk menonaktifkan U4 (`Dewi Lestari {runId}-183D`) atas nama aktor Manage user and role (Update, U=true)
8. Verifikasi respons server berupa penolakan (bukan 2xx)
9. Verifikasi Fixture BE: U4 tetap Active
### TC-AC-SU-621: Cooldown Resend ditegakkan server
10. Catat jumlah email di mail-catcher untuk alamat `sarahlee+{runId}-183b@qwertysystem.net` sebagai baseline
11. Ketik Search `Sarah Lee {runId}-183B`, tekan Enter
12. Buka row action (⋯) baris U2, lalu klik Resend Activation Email
13. Tunggu aksi selesai: baca entri Resend U2 lewat kemampuan baca tiap 5 detik sampai entri terbaca (batas tunggu 30 detik)
14. Baca T dari waktu terbit entri Resend pertama lewat API seeding, lalu bekukan jam server dan jam browser pada T + 10 detik
15. Kirim request langsung Resend Activation Email kedua untuk U2 atas nama aktor Total Control
16. Verifikasi respons server berupa penolakan (bukan 2xx)
17. Verifikasi jumlah email untuk alamat U2 hanya bertambah 1 dari baseline (tidak ada email kedua)
18. Buka row action (⋯) baris U2
19. Verifikasi tombol Resend Activation Email baris U2 menampilkan state cooldown dengan sisa waktu
20. Pulihkan jam server dan jam browser
### TC-AC-SU-624: Payload script dirender sebagai teks
21. Klik `(←)` pada kotak Search, lalu ketik Search `<script>`, tekan Enter
22. Verifikasi sel Position baris U5 (`Mike Tan {runId}-183E`) menampilkan teks literal `<script>alert(1)</script>` dan tidak ada script yang dieksekusi (tidak ada dialog alert)
23. Verifikasi Search memperlakukan kata kunci `<script>` sebagai teks biasa dan menemukan baris U5
24. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka, lalu tutup popup
25. Klik `(←)` pada kotak Search

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-user-backend.md`; tiap TC tepat satu spec, dan BE mencatatnya pada tingkat endpoint.
- Blok request langsung (TC-620, TC-622, TC-665, TC-621) mengikuti bagian 8b butir 1: asersi hanya respons server dan state data lewat Fixture BE. Toast dan state tombol yang disebut Expected TC (TC-620 `"You don't have permission to do this."`; TC-622 `"You don't have permission to do this."`; TC-665 `"You don't have permission to edit."`, switch Disabled; TC-621 tanpa toast error) tidak diasersi pada request langsung; state cooldown tombol TC-621 diasersi karena berasal dari Resend pertama melalui UI.
- Asersi "tidak ada entri log baru" (TC-620, TC-621, TC-665) tidak ditulis di spec ini: asersi absence atas penolakan request langsung masuk spec absence (kelas g, S-05); TC-620, TC-621, dan TC-665 ada juga di `sourceTc` spec 207 yang memuat request langsung, baseline, dan asersi absence-nya (pembagian TC lintas spec, S-05: spec ini mengasersi respons server, state data, dan state tombol cooldown).
- Urutan: blok request langsung sebelum TC-621 (jam dibekukan) dan TC-624 (UI) agar jam hanya dibekukan pada blok yang membutuhkannya (S-10). Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), pembekuan dan pemulihan jam, dan pencatatan baseline email, menunggu entri Resend terbaca (polling), dan membuka row action baris U2 sebelum verifikasi state cooldown. Pada TC-624, langkah membuka Popup Changelog: User tidak punya Expected di TC dan ditutup kembali.
- Lima blok kelas a berpola sama dengan aktor berbeda lewat sesi API; 25 langkah wajar.
- Temuan untuk QA:
  - Expected TC-620, TC-622, dan TC-665 tidak menyebut status HTTP penolakan; spec mengasersi respons bukan 2xx. Kode status tepat perlu ditetapkan.
  - TC-665 menyebut aktor "Manage user and role (U=true) sebagai `Mike Tan`", memetakan nama `Mike Tan` ke akun aktor Pre-setup #4 tanpa pernyataan tegas; spec memakai akun Pre-setup #4.
  - TC-621 menyebut "tanpa toast error" dan state tombol pada request langsung; lihat bagian 8b butir 1 di atas. TC-621 tidak menyebut baseline email; spec mencatat baseline sendiri.
  - TC-624 langkah 3 membuka Popup Changelog: User tanpa Expected; TC-624 Expected butir a hanya menyebut sel Position; Search `<script>` diasumsikan mencocokkan kolom Position.
  - TC memakai nama literal (`Mike Tan`, `Sarah Lee`, `John Doe`, `Dewi Lestari`); spec memakai nama bersuffix (S-12).
