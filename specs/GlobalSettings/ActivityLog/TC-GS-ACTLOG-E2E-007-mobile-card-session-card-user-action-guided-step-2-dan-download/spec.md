---
id: TC-GS-ACTLOG-E2E-007-mobile-card-session-card-user-action-guided-step-2-dan-download
title: "Mobile: Card Session, Card User Action, Guided Step 2, dan Download"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-24
  - TC-GS-ACTLOG-25
  - TC-GS-ACTLOG-26
  - TC-GS-ACTLOG-140
coverage:
  web: automated
---

# Mobile: Card Session, Card User Action, Guided Step 2, dan Download

## Prerequisites

- Mode: FE+BE.
- Viewport: mobile (ukuran ditetapkan tim FE, contoh 390 x 844), diset di langkah 1 dan dipulihkan ke viewport awal di langkah 32; hook `after` memulihkan viewport sebagai cadangan. Spec berjalan di browser web dengan viewport mobile, bukan di aplikasi mobile.
- Akun aktor (login di hook `before`; hook `after` mengembalikan sesi ke akun default suite):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`), pembaca Activity Log. Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
  - Admin `Hendra Pratama` (Client A): `Fixture.activityLog.adminHendra` (email ditetapkan tim FE) dengan `Spectra.env.GS_HENDRA_PASSWORD`. Melakukan aksi User Action lewat sesi API di hook `before` (Modified By `Hendra Pratama`, tampil `Hendra P`).
- Data Pre-setup: Division `Finance` (Pre-setup Division; hanya menjadi nilai tujuan perubahan Division user uji, tidak diubah atau dihapus).
- Data Dinamis:
  - Seed BE dua baris Session (alamat IP `192.0.2.10` adalah alamat contoh yang tidak dapat dihasilkan login nyata, dan nilai Employee ID `EMP001`, Position `Staff`, Division `Marketing` ditulis TC sehingga baris dibuat langsung oleh BE): baris `Login` `Success` milik `John Doe` (Employee ID `EMP001`, Position `Staff`, Division `Marketing`, IP Address `192.0.2.10`, Note `Login with password`) dan baris milik `Siti Nurbaya` (tanpa Position). Nama dan Employee ID literal karena asersi singkatan `John D`, `EMP001`, dan nilai Position `—` bergantung padanya.
  - Division `Marketing` (Population D-02, nama literal karena Expected TC-26 menyebut `Marketing`): di-seed di hook `before` secara idempotent (dilewati bila sudah ada); hook `after` menghapusnya hanya bila dibuat spec ini; suite berjalan serial.
  - User `Siti Nurbaya {runId}-007` dibuat oleh Hendra Pratama lewat sesi API dengan Division `Marketing` (aksi `Create`, Object `User`, Old Value `—`), lalu Division diubah ke `Finance` (aksi `Edit`, Field `Division`, Old Value `Marketing`, New Value `Finance`).
  - Brand `Brand Mobile {runId}-007` dibuat lalu dihapus oleh Hendra Pratama lewat sesi API (aksi `Delete`, New Value `—`).
  - Penanda waktu T0 dicatat di hook `before` sebelum seeding; cap waktu seed = waktu seeding (setelah T0), disediakan tim FE/BE; baris milik run ini adalah baris bertanggal setelah T0 dan berada di bagian teratas daftar card (sort default Date terbaru di atas).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus user uji lewat API. Baris log tidak dapat dihapus (append-only).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md); spec ini mengatur flag sendiri sesudah hook suite, yaitu menyetel `guided_tooltip_seen_gs-activity-log` ke belum `true` sebelum langkah 1; walkthrough otomatis TC-GS-ACTLOG-24 ditutup dengan `[Done]` (flag menjadi `true` untuk TC sesudahnya).
- Kemampuan teknis (disediakan tim FE/BE): seed BE baris Session seperti di atas (tanpa endpoint yang dikarang); membaca isi berkas unduhan CSV dan XLSX (nama berkas dan baris header).
- State global yang diubah: viewport browser (dipulihkan seperti di atas) dan flag Guided Tooltip (dipulihkan hook suite `after`). Spec tidak mengubah format tanggal atau jam.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-24: Guided Tooltip mobile, Step 2 menyorot tombol [⋯] yang membuka bottom sheet Filter

1. Setel viewport ke ukuran mobile
2. Buka Global Settings > Activity Log (flag belum `true`)
3. Klik `[Next]` ke Step 2
4. Verifikasi Step 2 menyorot tombol `[⋯]` di toolbar (bukan icon Filter desktop)
5. Verifikasi Step 2 Title `Narrow Down the Log`
6. Verifikasi tooltip tampil sebagai bottom sheet mini
7. Klik `[Done]`

### TC-GS-ACTLOG-25: Card Session menampilkan Position dan Division, tanpa Device / Browser

8. Buka Global Settings > Activity Log > Session
9. Amati card teratas bertanggal setelah T0 milik `John Doe` (Employee ID `EMP001`) dan card teratas bertanggal setelah T0 milik `Siti Nurbaya`
10. Verifikasi card `John Doe` baris 1: `Login` + `Success` + timestamp di kanan
11. Verifikasi card `John Doe` baris 2: `John D` · `EMP001` · `Staff` · `Marketing`
12. Verifikasi card `John Doe` baris 3: `192.0.2.10`
13. Verifikasi card `John Doe` baris 4: `Login with password`
14. Verifikasi Device / Browser tidak tampil di card
15. Verifikasi card `Siti Nurbaya`: nilai Position tampil `—`
16. Verifikasi tab Session dan tab User Action tetap tampil di atas daftar card

### TC-GS-ACTLOG-26: Card User Action

17. Buka Global Settings > Activity Log > User Action
18. Amati card `Edit` dan card `Create` dengan Name `Siti Nurbaya {runId}-007` serta card `Delete` dengan Name `Brand Mobile {runId}-007`
19. Verifikasi card `Edit` baris 1: `Edit` + `User` + `Siti Nurbaya {runId}-007` + timestamp di kanan
20. Verifikasi card `Edit` baris 2: `Division: Marketing → Finance`
21. Verifikasi card `Edit` baris 3: `by Hendra P`
22. Verifikasi card `Create`: Old Value kosong tampil `—`
23. Verifikasi card `Delete`: New Value kosong tampil `—`

### TC-GS-ACTLOG-140: Download mobile memuat kolom lengkap tab karena tidak ada Setup Column

24. Buka Global Settings > Activity Log > Session
25. Klik `[⋯]`, pilih Download, pilih `Download as CSV`, buka berkas
26. Verifikasi tab Session: nama berkas `Activity-Log-Session.csv`
27. Verifikasi tab Session: berkas memuat kesepuluh kolom: `Date`, `User`, `Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`
28. Klik tab "User Action"
29. Klik `[⋯]`, pilih Download, pilih `Download as XLSX`, buka berkas
30. Verifikasi tab User Action: nama berkas `Activity-Log-User-Action.xlsx`
31. Verifikasi tab User Action: berkas memuat kedelapan kolom: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`
32. Pulihkan viewport ke ukuran awal

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-24, 25, 26, 140). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-GS-ACTLOG-18, 19, 20, 21, 22, dan 23 (Guided Tooltip desktop) ada di spec 005 dan 006; Step 2 mobile hanya di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (viewport mobile, precondition TC-24, TC-25, TC-26, dan TC-140), 7 (`[Done]` menutup walkthrough otomatis supaya layar bersih untuk TC berikutnya), 8, 17, dan 24 (membuka tab yang dipakai TC), 28 (pindah ke tab User Action), 32 (memulihkan viewport).
- TC-24 dijalankan pertama karena mensyaratkan flag belum `true`; setelah `[Done]` flag `true` dan walkthrough tidak muncul untuk TC-25, TC-26, dan TC-140.
- Temuan untuk QA:
  - TC-24 tidak menyebut isi Step 1 versi mobile; spec hanya mengasersi Step 2 sesuai Expected.
  - TC-26 tidak menyebut format baris untuk card `Delete` selain New Value `—`; spec hanya mengasersi New Value `—`.
  - TC-26 menyebut Division `Marketing` dan `Finance` tanpa menyatakan Pre-setup; `Finance` ada di Pre-setup Division, `Marketing` di-seed spec ini (Population D-02).
  - `GS_HENDRA_PASSWORD` belum terdaftar di `.env.example`; email admin `Hendra Pratama` ditetapkan tim FE (fixture baru).
  - TC-25 dan TC-140 tidak menyebut ukuran viewport mobile; ditetapkan tim FE.
  - TC-140 Expected tidak menyebut cara membaca isi berkas; spec meminta kemampuan membaca berkas unduhan dari tim FE/BE.
