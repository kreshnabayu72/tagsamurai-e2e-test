---
id: TC-GS-ACTLOG-E2E-051-realtime-baris-baru-saringan-aktif-dan-opsi-filter-bertambah
title: "Realtime: Baris Baru, Saringan Aktif, dan Opsi Filter Bertambah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-79
  - TC-GS-ACTLOG-168
  - TC-GS-ACTLOG-195
  - TC-GS-ACTLOG-196
  - TC-GS-ACTLOG-197
coverage:
  web: automated
---

# Realtime: Baris Baru, Saringan Aktif, dan Opsi Filter Bertambah

## Prerequisites

- Mode: FE+BE.
- Akun pengamat Activity Log (satu-satunya sesi UI): Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` (seedSession). Spec tidak berganti akun.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Pelaku kedua ("sesi lain" pada TC) hanya memicu perubahan state dan tidak diasersi, sehingga dijalankan lewat sesi API (login, logout, Create Brand, Create Measurement); tidak ada sesi UI kedua. Langkah pemicu diberi awalan "Pemicu API".
- Akun pemicu (user dinamis, dibuat lewat API di hook `before` dengan suffix `{runId}-051`; password dari `Spectra.env.ACTLOG_PASSWORD`):
  - `Siti Nurbaya {runId}-051` (tanpa Position, Division `Operations {runId}-051`), belum pernah login sebelum TC-GS-ACTLOG-79.
  - `Dewi Lestari {runId}-051`, admin Total Control Client A yang belum pernah memiliki entri User Action sebelum TC-GS-ACTLOG-168.
  - `John Doe {runId}-051` (Position `Staff {runId}-051`, Division `Marketing {runId}-051`).
  - Nama dinamis bersuffix karena TC tidak mengasersi singkatan nama.
- Data pembanding opsi Filter (bagian 8b butir 2): aktor pengamat sudah punya baris Session (login hook `before`) dan baris User Action (pembuatan user dinamis di hook `before`), sehingga daftar opsi User dan Modified By memuat sedikitnya satu opsi selain akun pemicu.
- Data Dinamis lain (suffix `{runId}-051`): Brand `Realtime Brand {runId}-051` (TC-GS-ACTLOG-168), Brand `Acme Corp {runId}-051` (TC-GS-ACTLOG-196), Brand `Acme Corp 2 {runId}-051` dan Measurement `Pieces {runId}-051` (TC-GS-ACTLOG-197). Dibuat lewat sesi API oleh pemicu. Cleanup di hook `after`: semua Brand, Measurement, user, Position, dan Division dinamis dihapus lewat API tanpa berasumsi langkah spec berhasil penuh. Entri log tidak dapat dihapus; seed memakai nama bersuffix run sehingga run berikutnya tidak bentrok, dan asersi tahan baris dari run lain.
- Kemampuan teknis (disediakan tim FE/BE):
  - Sesi API untuk login dan logout user dinamis serta Create Brand dan Create Measurement oleh admin; login lewat Auth API harus menulis baris Session `Login` yang sama dengan login UI (Device/Browser tidak diasersi).
  - Mengamati tabel pengamat tanpa memuat ulang halaman sampai pembaruan realtime tampil (auto-wait; TC tidak menyebut batas waktu).
  - Baseline jumlah (S-12): pengamat mencatat jumlah baris (tabel berfilter/Search yang menyempit ke nama bersuffix `{runId}-051`) sebelum aksi pemicu; baris atau opsi "baru" adalah yang jumlahnya bertambah dibanding catatan baseline, atau baris bernama bersuffix unik dengan baseline nol. Penanda waktu tidak dipakai.
- State global yang diubah dan dipulihkan: Filter Tab Session dan Tab User Action (dibersihkan di langkah 33 dan 34).
- Suite serial (`parallel: false`).
- Hook `beforeEach`: kembali ke layar Global Settings > Activity Log > Session.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-79: Opsi filter bertambah tanpa muat ulang halaman saat data log baru muncul, Tab Session

2. Klik icon Filter, buka daftar opsi field User, lalu catat opsi
3. Verifikasi daftar opsi field User memuat sedikitnya satu opsi selain `Siti Nurbaya {runId}-051`
4. Verifikasi opsi awal tidak memuat `Siti Nurbaya {runId}-051`
5. Pemicu API: login sebagai `Siti Nurbaya {runId}-051`
6. Tanpa memuat ulang halaman, tutup lalu buka lagi daftar opsi field User
7. Verifikasi opsi `Siti Nurbaya {runId}-051` muncul di daftar opsi tanpa muat ulang halaman
8. Tutup daftar opsi dan Filter Panel

### TC-GS-ACTLOG-168: Opsi Modified By bertambah tanpa muat ulang halaman saat aksi admin baru tercatat

9. Klik tab "User Action", klik icon Filter, buka daftar opsi field Modified By, lalu catat opsi
10. Verifikasi daftar opsi field Modified By memuat sedikitnya satu opsi selain `Dewi Lestari {runId}-051`
11. Verifikasi opsi awal tidak memuat `Dewi Lestari {runId}-051`
12. Pemicu API: login sebagai `Dewi Lestari {runId}-051`, lalu buat satu Brand `Realtime Brand {runId}-051`
13. Tanpa memuat ulang halaman, tutup lalu buka lagi daftar opsi field Modified By
14. Verifikasi opsi `Dewi Lestari {runId}-051` muncul di daftar opsi tanpa muat ulang halaman
15. Tutup daftar opsi dan Filter Panel

### TC-GS-ACTLOG-195: Baris Session baru muncul otomatis tanpa muat ulang

16. Klik tab "Session" (Filter dan Search kosong), lalu catat jumlah baris Login milik `Siti Nurbaya {runId}-051` sebagai baseline
17. Pemicu API: login sebagai `Siti Nurbaya {runId}-051`
18. Tanpa memuat ulang halaman, verifikasi jumlah baris Login milik `Siti Nurbaya {runId}-051` bertambah satu dari baseline langkah 16 dan baris baru muncul di tabel secara otomatis
19. Verifikasi tidak ada dialog yang tampil

### TC-GS-ACTLOG-196: Baris User Action baru muncul otomatis tanpa muat ulang

20. Klik tab "User Action" (Filter dan Search kosong)
21. Pemicu API: login sebagai `Dewi Lestari {runId}-051`, lalu buat Brand `Acme Corp {runId}-051`
22. Tanpa memuat ulang halaman, verifikasi baris `Create` `Brand` `Acme Corp {runId}-051` (nama bersuffix unik, baseline nol) muncul di tabel secara otomatis
23. Verifikasi tidak ada dialog yang tampil

### TC-GS-ACTLOG-197: Event baru mengikuti saringan aktif, kedua tab

24. Pemicu API: login sebagai `John Doe {runId}-051` (kondisi awal sesi aktif yang di-logout pada langkah 26)
25. Klik tab "Session", klik icon Filter, pilih Activity `Login`, klik [Apply], lalu catat jumlah baris Login milik `John Doe {runId}-051` pada tabel berfilter sebagai baseline
26. Pemicu API: logout sebagai `John Doe {runId}-051`, lalu login kembali sebagai `John Doe {runId}-051`
27. Tanpa memuat ulang halaman, verifikasi jumlah baris Login milik `John Doe {runId}-051` bertambah satu dari baseline langkah 25 dan baris baru tampil
28. Verifikasi baris Logout baru milik `John Doe {runId}-051` tidak tampil
29. Klik tab "User Action", klik icon Filter, pilih Object `Brand`, klik [Apply]
30. Pemicu API: login sebagai `Dewi Lestari {runId}-051`, buat Measurement `Pieces {runId}-051`, lalu buat Brand `Acme Corp 2 {runId}-051`
31. Tanpa memuat ulang halaman, verifikasi baris `Create` `Brand` `Acme Corp 2 {runId}-051` (nama bersuffix unik, baseline nol) tampil
32. Verifikasi baris `Create` `Measurement` `Pieces {runId}-051` tidak tampil

### Pemulihan state antar TC

33. Tab User Action: klik icon Filter, klik [Clear Field], lalu klik [Apply]
34. Klik tab "Session", klik icon Filter, klik [Clear Field], lalu klik [Apply]

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`. Mode: FE+BE. Kelas multi-konteks (prinsip 13c), jenis pengamat realtime dengan pelaku kedua; pelaku kedua memicu lewat sesi API dan tidak diasersi, sehingga tidak ada sesi UI kedua.
- Urutan TC dalam spec: 79, 168, 195, 196, 197 (urutan nomor sumber). Ketergantungan TC-GS-ACTLOG-197 pada TC-GS-ACTLOG-195 dan TC-GS-ACTLOG-196 dipenuhi oleh TC-GS-ACTLOG-195 dan 196 yang berjalan lebih dulu di spec yang sama.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 8 dan 15 (menutup daftar opsi dan Filter Panel); langkah 24 (login `John Doe {runId}-051` sebagai kondisi awal sesi aktif yang di-logout pada langkah 26); langkah 33 dan 34 (membersihkan Filter kedua tab, hook `after` sebagai cadangan).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 dan 10 (daftar opsi memuat opsi pembanding) sebagai anchor sebelum asersi opsi awal tidak memuat nama pemicu pada langkah 4 dan 11 (bagian 8b butir 2).
- Tab User Action pada TC-GS-ACTLOG-197 memakai Brand `Acme Corp 2 {runId}-051` karena Brand `Acme Corp {runId}-051` dari TC-GS-ACTLOG-196 masih ada dan nama Brand harus unik.
- Asersi absence pada langkah 28 dan 32 didahului anchor positif di surface yang sama (langkah 27 dan 31) dan memakai baseline jumlah entri dan nama bersuffix unik (S-12).
- Pembagian TC lintas spec: tidak ada TC yang terbelah.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 29, 33, dan 34 mengikuti TC-GS-ACTLOG-197 (dan pola pemulihan state).
  - TC-GS-ACTLOG-79 dan 168: TC menyebut opsi `Siti Nurbaya` dan `Dewi Lestari` tanpa menyatakan apakah opsi filter memakai nama lengkap atau singkatan (`Siti N`, `Dewi L`); spec mengikuti TC (nama lengkap).
  - TC-GS-ACTLOG-195, 196, 197: TC tidak menyebut batas waktu munculnya pembaruan realtime; spec memakai auto-wait.
  - TC-GS-ACTLOG-196 dan 197: TC memakai Brand `Acme Corp` di dua TC tanpa menghapusnya di antara keduanya (Tabel Data Uji Dinamis mencatat penghapusan baru di TC-GS-ACTLOG-143); spec memakai nama berbeda di TC-GS-ACTLOG-197.
  - TC-GS-ACTLOG-197: TC tidak menyebut field wajib Measurement `Pieces` dan tidak menyebut akun pembuat Brand; spec memakai `Dewi Lestari {runId}-051` dan field wajib mengikuti PRD Measurement.
  - TC-GS-ACTLOG-197: TC tidak menyebut bahwa `John Doe` sudah login sebelum Logout; spec menambah login pembuka (langkah 24).
  - TC-GS-ACTLOG-79, 168, 195, 196, 197: akun `Siti Nurbaya`, `Dewi Lestari`, `John Doe` adalah user dinamis bersuffix yang disediakan tim FE.
  - TC-GS-ACTLOG-79, 195, 197: login pemicu lewat sesi API mengandalkan Auth API menulis baris Session `Login` yang sama dengan login UI; TC tidak menyebut cara memicunya.
