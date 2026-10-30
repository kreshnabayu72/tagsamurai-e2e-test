---
id: TC-GS-DIV-E2E-070-form-user-dan-non-login-user-division-dihapus-pihak-lain
title: "Form User dan Non-Login User: Division Terpilih Dihapus Pihak Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-254
  - TC-GS-DIV-255
coverage:
  web: automated
---

# Form User dan Non-Login User: Division Terpilih Dihapus Pihak Lain

## Prerequisites

- Mode: FE+BE. Spec membuat race antar-aktor (kelas multi-konteks): Admin B menghapus Division di antara pilih Division dan Submit.
- Akun yang diuji (spec memakai satu sesi UI dan satu sesi API terpisah):

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Admin A (sesi UI) | Total Control, Sari Dewi (`Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Admin B (hanya lewat API, tanpa login UI) | Total Control (admin kedua), Nadia Pratama | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | `GS_TC2_PASSWORD` |

  Akun Admin B tidak tercantum di Tabel Data Uji Pre-setup; akun ini disediakan tim FE. Login Admin A di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (`GS_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup hanya dibaca dan tidak diubah: opsi `Finance` (FIN) menjadi anchor positif pada daftar opsi dropdown Division. Population D-02 tidak dipakai.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), Division bebas relasi yang di-seed lewat API di hook `before` oleh akun Total Control (setara pembuatan lewat `[+ Division]` pada Precondition c TC):
  - `Stale Unit A {runId}-070` dengan Code `SUA` (D-22): dihapus Admin B pada TC-GS-DIV-254.
  - `Stale Unit B {runId}-070` dengan Code `SUB` (D-23): dihapus Admin B pada TC-GS-DIV-255.
  - Code `SUA` dan `SUB` literal sesuai TC (pengecualian S-12: seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite berjalan serial); hook `before` menghapus lewat API sisa Division bernama `Stale Unit A {runId lama}-070` dan `Stale Unit B {runId lama}-070` (nama berpola `Stale Unit A *-070` dan `Stale Unit B *-070`, bukan berdasarkan Code saja) yang masih memegang Code `SUA` atau `SUB`.
- Nilai field wajib lain pada dua form (diisi sebelum Submit; Submit ditolak sehingga tidak ada user yang tercipta). Fixture `fixtures/division.json` belum ada; tim FE menyediakannya:

  | Form | Field | Nilai |
  |---|---|---|
  | Create User (`[+ User]`) | First Name | `Stale` |
  | | Last Name | `User {runId}-070` |
  | | Email | `staleuser+{runId}-070@qwertysystem.net` |
  | | Access dan field wajib lain | kunci `userForm.access` dan lainnya, disediakan tim FE |
  | Create Non-Login User (`[+ Non-Login User]`) | First Name | `Stale` |
  | | Last Name | `Nonlogin {runId}-070` |
  | | Email | `stalenl+{runId}-070@qwertysystem.net` |
  | | Represented By dan field wajib lain | kunci `nonLoginForm.representedBy` dan lainnya, disediakan tim FE |

- Kemampuan teknis: Admin B sebagai sesi API terpisah (login lewat API dengan `Spectra.env.GS_TC2_PASSWORD`) untuk menghapus Division di antara pilih Division dan Submit; seeding dan penghapusan Division lewat API; membaca seluruh opsi dropdown Division form Create User dengan menggulir daftar tanpa mengetik pencarian (disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedua Division bersuffix `{runId}-070` bila masih ada.
- Tidak ada state global yang diubah.
- TC-GS-DIV-254 dan 255: login sebagai Total Control (Admin A) dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-254: Form User dengan Division terpilih yang dihapus pihak lain

1. Buka Global Settings > User > Tab User List, klik tombol `[+ User]` (Create User)
2. Buka field dropdown Division
3. Gulir daftar opsi dropdown Division hingga opsi `Stale Unit A {runId}-070` terlihat, lalu pilih opsi `Stale Unit A {runId}-070`
4. Admin B (sesi API atas akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`) menghapus Division `Stale Unit A {runId}-070`
5. Admin A mengisi field wajib lain form Create User dengan nilai dari fixture `userForm`
6. Klik [Submit]
7. Verifikasi error level field Division: `This division no longer exists. Please select another.`
8. Verifikasi field Division dikosongkan otomatis
9. Buka field dropdown Division
10. Gulir daftar opsi dropdown Division hingga opsi `Finance` terlihat
11. Verifikasi opsi `Finance` tampil pada daftar opsi Division
12. Verifikasi daftar opsi Division di-refresh: opsi `Stale Unit A {runId}-070` tidak ada
13. Verifikasi field lain form Create User tidak ter-reset: First Name, Last Name, dan Email tetap sesuai nilai yang diisi
14. Klik `✕` di header form Create User
15. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
16. Klik [Leave]

### TC-GS-DIV-255: Form Non-Login User dengan Division terpilih yang dihapus pihak lain

17. Buka Sub-tab Non-Login User, klik tombol `[+ Non-Login User]` (Create Non-Login User)
18. Buka field dropdown Division
19. Ketik `Stale Unit B {runId}-070` pada pencarian dropdown, pilih opsi `Stale Unit B {runId}-070`
20. Admin B (sesi API atas akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`) menghapus Division `Stale Unit B {runId}-070`
21. Admin A mengisi field wajib lain form Create Non-Login User dengan nilai dari fixture `nonLoginForm`
22. Klik [Submit]
23. Verifikasi error level field Division: `This division no longer exists. Please select another.`
24. Verifikasi field Division dikosongkan otomatis
25. Buka field dropdown Division, ketik `Finance` pada pencarian dropdown
26. Verifikasi opsi `Finance` tampil pada daftar opsi Division
27. Ganti isi pencarian dropdown dengan `Stale Unit B {runId}-070`
28. Verifikasi daftar opsi Division di-refresh: opsi `Stale Unit B {runId}-070` tidak ada
29. Verifikasi field lain form Create Non-Login User tidak ter-reset: First Name, Last Name, Email, dan Represented By tetap sesuai nilai yang diisi
30. Klik `✕` di header form Create Non-Login User
31. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
32. Klik [Leave]

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Urutan TC di spec: 254 lalu 255 (sesuai urutan sumber); keduanya mengikuti pola yang sama dan menghapus Division milik masing-masing oleh Admin B.
- Admin B bertindak lewat sesi API terpisah (bukan sesi browser kedua) dan hanya berfungsi sebagai pemicu penghapusan; asersi hanya pada sesi UI Admin A, tidak ada asersi di sesi B (P-2). TC sumber menyebut "Admin B menghapus" tanpa mekanisme; spec memakai sesi API.
- Dropdown Division form Create User (TC-GS-DIV-254) diamati dengan menggulir daftar tanpa mengetik pencarian, karena PRD User mendefinisikan field Division form Create User hanya sebagai `Select division`. Pencarian di dalam dropdown dipakai hanya pada form Create Non-Login User (`Search division...`, `non-login-user.md` `FLD-05`; langkah 19, 25, dan 27).
- Asersi absence opsi (langkah 12 dan 28) didahului anchor positif opsi `Finance` pada daftar yang sama (langkah 11 dan 26; bagian 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 3, 9, 10, 18, 19, 25, dan 27 (membuka dropdown, menggulir atau mengetik pencarian supaya opsi dapat dipilih dan ada-tidaknya opsi dapat diperiksa), langkah 14 sampai 16 dan 30 sampai 32 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`; Verifikasi dialog pada langkah 15 dan 31 adalah asersi tambahan agar penutupan deterministik, S-08).
- Division di-seed lewat API karena pembuatannya bukan objek uji; TC sumber menyebut "dibuat lewat `[+ Division]`". Dependensi tidak bergantung pada spec lain.
- Langkah 1 membuka Tab User List (layar modul User, bukan layar awal Division) karena form Create User adalah objek uji; layar awal hook `beforeEach` adalah Tab Division.
- Nama tombol `[+ User]` dan `[+ Non-Login User]` mengikuti PRD User (tooltip `Create User`); TC sumber menulis "form Create User" dan "form Create Non-Login User".
- Temuan untuk QA:
  - PRD User tidak mendefinisikan pencarian di dropdown Division form Create User, sedangkan PRD Non-Login User mendefinisikannya (`non-login-user.md` `FLD-05`); TC-GS-DIV-254 tidak menyebut cara memilih Division pada form, sehingga spec menggulir daftar opsi.
  - TC-GS-DIV-254 dan 255 Langkah Uji 3 ("mengisi field wajib lain") tidak merinci field dan nilainya; spec menuliskan kebutuhan fixture di Prerequisites.
  - TC-GS-DIV-254 dan 255 tidak menyebut bagaimana Admin B menghapus Division (UI atau API) dan akun Admin B; spec memakai sesi API atas akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`.
  - TC-GS-DIV-254 dan 255 Expected Result b ("tanpa mereset field lain") tidak menyebut field mana; spec memverifikasi field identitas yang diisi pada langkah 5 dan 21.
